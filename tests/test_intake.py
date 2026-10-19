from pathlib import Path

import pytest

from pipeline_model_evaluator.sources import inspect_sources


HEADER = "---\nschema_version: 1\nmodel_id: example\n---\n"


def source(tmp_path, text, name="model.md"):
    path = tmp_path / name
    path.write_text(text, encoding="utf-8")
    return path


def block(body):
    return f"```yaml pipeline-definition\n{body}\n```\n"


def codes(result):
    return [d.code for d in result.diagnostics]


def test_empty_source_selection_is_not_a_valid_model():
    assert codes(inspect_sources([])) == ["no_sources"]


def test_extracts_definitions_aliases_and_exact_source_lines():
    path = Path(__file__).parent / "fixtures/minimal.md"
    result = inspect_sources([path])
    assert result.valid
    assert [h.title for h in result.indexes[0].headings] == ["Example pipeline", "Segmenter"]
    assert result.indexes[0].headings[0].location.start_line == 5
    assert result.definitions[0].location.start_line == 7
    assert result.definitions[0].location.end_line == 12
    alias = next(r for r in result.references if r.requested_id == "raw_text")
    assert alias.target_id == "DS-01"
    assert alias.target_location == result.definitions[0].location
    assert result.definitions[-1].definition.model_extra["implementation"]["state"] == "conceptual"
    assert result.documents[0].text == path.read_text()


@pytest.mark.parametrize("metadata,expected", [
    ("", "missing_frontmatter"),
    ("---\nmodel_id: example\n", "unclosed_frontmatter"),
    ("---\nschema_version: 2\nmodel_id: example\n---\n", "invalid_frontmatter"),
    ("---\nschema_version: true\nmodel_id: example\n---\n", "invalid_frontmatter"),
    ("---\nschema_version: 1\nmodel_id: ' '\n---\n", "invalid_frontmatter"),
    ("---\n- a\n---\n", "invalid_yaml"),
])
def test_frontmatter_failures_are_diagnostics(tmp_path, metadata, expected):
    result = inspect_sources([source(tmp_path, metadata + "# Heading\n")])
    assert expected in codes(result)
    assert len(result.documents) == 1
    assert len(result.indexes) == 1
    assert not result.valid


@pytest.mark.parametrize("body,expected", [
    ("kind: artifact\nid: DS-01\nid: DS-02", "invalid_yaml"),
    ("kind: artifact\nid: [", "invalid_yaml"),
    ("- list", "invalid_yaml"),
    ("kind: unknown\nid: X", "invalid_definition"),
    ("kind: artifact\nid: 123", "invalid_definition"),
    ("kind: processor\nid: P\nconsumes: X", "invalid_definition"),
    ("kind: processor\nid: P\nconsumes: ['']", "invalid_definition"),
    ("kind: artifact\nid: &id A\nreferences: [*id]", "invalid_yaml"),
    ("kind: artifact\nid: A\nmetadata: !!python/object/apply:os.system ['echo unsafe']", "invalid_yaml"),
])
def test_bad_yaml_or_envelopes_do_not_discard_other_blocks(tmp_path, body, expected):
    text = HEADER + block(body) + block("kind: artifact\nid: GOOD")
    result = inspect_sources([source(tmp_path, text)])
    assert expected in codes(result)
    assert [d.definition.id for d in result.definitions] == ["GOOD"]
    assert len(result.indexes[0].blocks) == 2


def test_yaml_error_uses_physical_line_number(tmp_path):
    result = inspect_sources([source(tmp_path, HEADER + block("kind: artifact\nid: A\nid: B"))])
    assert result.diagnostics[0].location.start_line == 8


def test_untagged_code_and_prose_are_not_definitions(tmp_path):
    text = HEADER + "# P01\n```yaml\nkind: artifact\nid: A\n```\n"
    result = inspect_sources([source(tmp_path, text)])
    assert result.valid
    assert not result.definitions


def test_unclosed_definition_is_not_silently_accepted(tmp_path):
    result = inspect_sources([source(tmp_path, HEADER + "```yaml pipeline-definition\nkind: artifact\nid: A\n")])
    assert codes(result) == ["unclosed_definition"]
    assert not result.definitions


def test_cross_file_resolution_and_input_order_are_stable(tmp_path):
    a = source(tmp_path, HEADER + block("kind: artifact\nid: A"), "a.md")
    b = source(tmp_path, HEADER + block("kind: processor\nid: P\nconsumes: [A, MISSING]"), "b.md")
    first = inspect_sources([b, a])
    assert first == inspect_sources([a, b, a])
    assert codes(first) == ["missing_reference"]
    assert first.references[0].target_location.source == str(a)
    assert first.diagnostics[0].location.source == str(b)


def test_collisions_stay_ambiguous_instead_of_selecting_first(tmp_path):
    text = HEADER + block("kind: artifact\nid: A\naliases: [shared]")
    text += block("kind: artifact\nid: B\naliases: [shared]")
    text += block("kind: processor\nid: P\nconsumes: [shared]")
    result = inspect_sources([source(tmp_path, text)])
    assert set(codes(result)) == {"duplicate_identifier", "ambiguous_reference"}
    assert not result.references
    assert len(next(d for d in result.diagnostics if d.code == "ambiguous_reference").related) == 2


def test_duplicate_id_and_wrong_reference_kind(tmp_path):
    text = HEADER + block("kind: capability\nid: C") * 2
    text += block("kind: processor\nid: P\nconsumes: [P]\nrequires_capabilities: [C]")
    result = inspect_sources([source(tmp_path, text)])
    assert set(codes(result)) == {"duplicate_identifier", "reference_kind_mismatch", "ambiguous_reference"}


def test_models_cannot_be_accidentally_combined(tmp_path):
    a = source(tmp_path, HEADER, "a.md")
    b = source(tmp_path, HEADER.replace("example", "other"), "b.md")
    assert "model_id_mismatch" in codes(inspect_sources([a, b]))


def test_read_failures_preserve_valid_documents(tmp_path):
    good = source(tmp_path, HEADER)
    bad = tmp_path / "bad.md"
    bad.write_bytes(b"\xff")
    result = inspect_sources([good, bad, tmp_path / "missing.md"])
    assert codes(result) == ["source_read_error", "source_read_error"]
    assert len(result.documents) == len(result.indexes) == 1


def test_bom_crlf_and_setext_heading_locations(tmp_path):
    path = tmp_path / "windows.md"
    text = HEADER + "Title\n=====\n" + block("kind: artifact\nid: A")
    path.write_bytes(b"\xef\xbb\xbf" + text.replace("\n", "\r\n").encode())
    result = inspect_sources([path])
    assert result.valid
    assert result.indexes[0].headings[0].location.start_line == 5
    assert result.indexes[0].headings[0].location.end_line == 6


def test_plain_strings_are_not_executed(tmp_path):
    marker = tmp_path / "must-not-exist"
    payload = f"__import__('pathlib').Path('{marker}').touch()"
    result = inspect_sources([source(tmp_path, HEADER + block(f"kind: constraint\nid: C\nexpression: {payload}"))])
    assert result.valid
    assert not marker.exists()
