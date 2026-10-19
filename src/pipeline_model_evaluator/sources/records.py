"""Phase-1 records; these are not the phase-2 canonical domain model."""

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator


class Record(BaseModel):
    model_config = ConfigDict(frozen=True)


class SourceLocation(Record):
    source: str
    start_line: int
    end_line: int


class Diagnostic(Record):
    code: str
    message: str
    location: SourceLocation
    related: tuple[SourceLocation, ...] = ()


class Frontmatter(Record):
    model_config = ConfigDict(frozen=True, extra="allow")
    schema_version: StrictInt
    model_id: StrictStr = Field(min_length=1)

    @field_validator("schema_version")
    @classmethod
    def supported_version(cls, value: int) -> int:
        if value != 1:
            raise ValueError("only schema_version 1 is supported")
        return value

    @field_validator("model_id")
    @classmethod
    def nonblank_model_id(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("model_id cannot be blank")
        return value


class Definition(Record):
    # Unknown domain fields are retained for phase 2, never treated as validated.
    model_config = ConfigDict(frozen=True, extra="allow")
    kind: Literal["processor", "artifact", "capability", "constraint", "assumption", "dependency"]
    id: StrictStr = Field(pattern=r"^[A-Za-z][A-Za-z0-9_.-]*$")
    aliases: tuple[StrictStr, ...] = ()
    references: tuple[StrictStr, ...] = ()
    consumes: tuple[StrictStr, ...] = ()
    produces: tuple[StrictStr, ...] = ()
    requires_capabilities: tuple[StrictStr, ...] = ()
    provides_capabilities: tuple[StrictStr, ...] = ()
    constraints: tuple[StrictStr, ...] = ()

    @field_validator("aliases", "references", "consumes", "produces", "requires_capabilities",
                     "provides_capabilities", "constraints", mode="before")
    @classmethod
    def identifier_sequence(cls, value: Any) -> Any:
        if not isinstance(value, (list, tuple)) or any(
            not isinstance(item, str) or not item.strip() for item in value
        ):
            raise ValueError("expected a sequence of nonblank identifier strings")
        return value


class SourceDocument(Record):
    source: str
    text: str


class Heading(Record):
    level: int
    title: str
    location: SourceLocation


class DefinitionBlock(Record):
    content: str
    location: SourceLocation
    content_start_line: int


class DocumentIndex(Record):
    source: str
    frontmatter: Frontmatter | None = None
    headings: tuple[Heading, ...] = ()
    blocks: tuple[DefinitionBlock, ...] = ()


class DefinitionRecord(Record):
    definition: Definition
    location: SourceLocation


class ResolvedReference(Record):
    owner_id: str
    field: str
    requested_id: str
    target_id: str
    location: SourceLocation
    target_location: SourceLocation


class IntakeResult(Record):
    documents: tuple[SourceDocument, ...]
    indexes: tuple[DocumentIndex, ...]
    definitions: tuple[DefinitionRecord, ...]
    references: tuple[ResolvedReference, ...]
    diagnostics: tuple[Diagnostic, ...]

    @property
    def valid(self) -> bool:
        """Intake validity only, not canonical or semantic model validity."""
        return not self.diagnostics
