# Intake tests

Run `uv run pytest` from the repository root. Phase-1 coverage includes Markdown
headings/frontmatter, explicit YAML blocks, locations, aliases/references,
malformed input, duplicate IDs, cross-file resolution, unsafe tags, read failures
and deterministic ordering. `fixtures/minimal.md` is the initial input contract.

Canonical model validation, graph behavior, target feasibility and result classes
remain phase-2/3 work. These tests do not claim those behaviors exist.
