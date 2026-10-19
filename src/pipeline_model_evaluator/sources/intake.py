"""Deterministic intake of explicit Markdown/YAML sources; never executes models."""

from collections import defaultdict
from pathlib import Path
from typing import Any

from markdown_it import MarkdownIt
from pydantic import ValidationError
import yaml

from .records import (
    Definition, DefinitionBlock, DefinitionRecord, Diagnostic, DocumentIndex,
    Frontmatter, Heading, IntakeResult, ResolvedReference, SourceDocument, SourceLocation,
)


class _UniqueSafeLoader(yaml.SafeLoader):
    """Reject aliases and duplicate keys rather than silently replacing values."""

    def compose_node(self, parent: Any, index: Any) -> Any:
        if self.check_event(yaml.AliasEvent):
            event = self.peek_event()
            raise yaml.MarkedYAMLError(problem="YAML aliases are unsupported", problem_mark=event.start_mark)
        return super().compose_node(parent, index)

    def construct_mapping(self, node: Any, deep: bool = False) -> dict:
        keys = set()
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=deep)
            try:
                if key in keys:
                    raise yaml.MarkedYAMLError(problem="duplicate YAML key", problem_mark=key_node.start_mark)
                keys.add(key)
            except TypeError as exc:
                raise yaml.MarkedYAMLError(problem="mapping keys must be scalar", problem_mark=key_node.start_mark) from exc
        return super().construct_mapping(node, deep=deep)


def _location(source: str, start: int, end: int | None = None) -> SourceLocation:
    return SourceLocation(source=source, start_line=start, end_line=end or start)


def _yaml_mapping(content: str, location: SourceLocation, content_start: int,
                  diagnostics: list[Diagnostic]) -> dict | None:
    try:
        value = yaml.load(content, Loader=_UniqueSafeLoader)
        if not isinstance(value, dict):
            raise ValueError("expected one YAML mapping")
        return value
    except (yaml.YAMLError, ValueError, RecursionError) as exc:
        mark = getattr(exc, "problem_mark", None)
        line = content_start + mark.line if mark is not None else location.start_line
        diagnostics.append(Diagnostic(code="invalid_yaml", message=str(exc),
                                      location=_location(location.source, line)))
        return None


def _index(document: SourceDocument, diagnostics: list[Diagnostic]) -> DocumentIndex:
    lines = document.text.splitlines(keepends=True)
    frontmatter = None
    body_start = 0
    if lines and lines[0].strip() == "---":
        close = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        if close is None:
            diagnostics.append(Diagnostic(code="unclosed_frontmatter", message="frontmatter needs a closing ---",
                                          location=_location(document.source, 1, max(1, len(lines)))))
            return DocumentIndex(source=document.source)
        body_start = close + 1
        loc = _location(document.source, 1, close + 1)
        value = _yaml_mapping("".join(lines[1:close]), loc, 2, diagnostics)
        if value is not None:
            try:
                frontmatter = Frontmatter.model_validate(value)
            except ValidationError as exc:
                diagnostics.append(Diagnostic(code="invalid_frontmatter", message=str(exc), location=loc))
    else:
        diagnostics.append(Diagnostic(code="missing_frontmatter", message="expected model_id and schema_version frontmatter",
                                      location=_location(document.source, 1)))
    # Blank out frontmatter while retaining physical line numbers.
    body = "\n" * body_start + "".join(lines[body_start:])
    tokens = MarkdownIt("commonmark").parse(body)
    headings, blocks = [], []
    for i, token in enumerate(tokens):
        if token.type == "heading_open" and token.map:
            headings.append(Heading(level=int(token.tag[1:]), title=tokens[i + 1].content,
                                    location=_location(document.source, token.map[0] + 1, token.map[1])))
        if token.type != "fence" or token.info.strip() != "yaml pipeline-definition" or not token.map:
            continue
        start, end = token.map
        loc = _location(document.source, start + 1, end)
        # CommonMark accepts an unterminated fence; the model format does not.
        closing = lines[end - 1].strip() if end else ""
        if (len(closing) < len(token.markup) or set(closing) != {token.markup[0]}
                or end - start < 2):
            diagnostics.append(Diagnostic(code="unclosed_definition", message="definition fence needs a closing delimiter", location=loc))
            continue
        blocks.append(DefinitionBlock(content=token.content, location=loc, content_start_line=start + 2))
    return DocumentIndex(source=document.source, frontmatter=frontmatter,
                         headings=tuple(headings), blocks=tuple(blocks))


def _resolve(records: list[DefinitionRecord], diagnostics: list[Diagnostic]) -> list[ResolvedReference]:
    names: dict[str, list[DefinitionRecord]] = defaultdict(list)
    for record in records:
        for name in (record.definition.id, *record.definition.aliases):
            names[name].append(record)
    for name, candidates in sorted(names.items()):
        if len(candidates) > 1:
            diagnostics.append(Diagnostic(code="duplicate_identifier", message=f"identifier or alias {name!r} is not unique",
                                          location=candidates[0].location,
                                          related=tuple(c.location for c in candidates[1:])))
    expected = {"references": None, "consumes": "artifact", "produces": "artifact",
                "requires_capabilities": "capability", "provides_capabilities": "capability",
                "constraints": "constraint"}
    resolved = []
    for record in records:
        for field, kind in expected.items():
            for name in getattr(record.definition, field):
                candidates = names.get(name, [])
                code = "missing_reference" if not candidates else "ambiguous_reference" if len(candidates) > 1 else None
                if code:
                    diagnostics.append(Diagnostic(code=code, message=f"{record.definition.id}.{field}: {name!r}",
                                                  location=record.location,
                                                  related=tuple(c.location for c in candidates)))
                elif kind and candidates[0].definition.kind != kind:
                    diagnostics.append(Diagnostic(code="reference_kind_mismatch", message=f"{field} requires {kind}: {name!r}",
                                                  location=record.location, related=(candidates[0].location,)))
                else:
                    target = candidates[0]
                    resolved.append(ResolvedReference(owner_id=record.definition.id, field=field, requested_id=name,
                                                      target_id=target.definition.id, location=record.location,
                                                      target_location=target.location))
    return resolved


def inspect_sources(paths: list[Path] | tuple[Path, ...]) -> IntakeResult:
    """Inspect explicit local UTF-8 files in stable path order, retaining partial results.

    Invalid source/model input yields diagnostics. Unexpected programmer failures
    are not converted to successful intake. No paths are discovered or fetched.
    """
    documents, indexes, records, diagnostics = [], [], [], []
    if not paths:
        diagnostics.append(Diagnostic(code="no_sources", message="select at least one source file",
                                      location=_location("<input>", 1)))
    for path in sorted(set(map(Path, paths)), key=str):
        try:
            document = SourceDocument(source=str(path), text=path.read_text(encoding="utf-8-sig"))
        except (OSError, UnicodeError) as exc:
            diagnostics.append(Diagnostic(code="source_read_error", message=str(exc), location=_location(str(path), 1)))
            continue
        documents.append(document)
        index = _index(document, diagnostics)
        indexes.append(index)
        for block in index.blocks:
            value = _yaml_mapping(block.content, block.location, block.content_start_line, diagnostics)
            if value is None:
                continue
            try:
                definition = Definition.model_validate(value)
            except ValidationError as exc:
                diagnostics.append(Diagnostic(code="invalid_definition", message=str(exc), location=block.location))
                continue
            records.append(DefinitionRecord(definition=definition, location=block.location))
    identities = {i.frontmatter.model_id for i in indexes if i.frontmatter is not None}
    if len(identities) > 1:
        diagnostics.append(Diagnostic(code="model_id_mismatch", message="all source documents must describe the same model_id",
                                      location=_location(indexes[0].source, 1)))
    references = _resolve(records, diagnostics)
    return IntakeResult(documents=tuple(documents), indexes=tuple(indexes), definitions=tuple(records),
                        references=tuple(references), diagnostics=tuple(sorted(diagnostics, key=lambda d: (
                            d.location.source, d.location.start_line, d.code, d.message))))
