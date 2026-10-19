# Phase-1 intake format and API

Implementation contract for this PR, proposed for review. It selects the narrow
intake portion of DEC-002 without settling phase-2 domain/graph semantics.
The merged plan authorizes intake; the earlier conversation did not prescribe
this exact syntax. No owner adoption of these syntax details is claimed.

## Source selection

`inspect_sources([Path(...)])` reads explicit local UTF-8 Markdown files. A UTF-8
BOM and CRLF are accepted; newlines are normalized on read while physical line
numbers are retained. No directory traversal/discovery, linked-document fetching,
model execution or graph evaluation occurs. Paths are deduplicated and sorted
lexically, without resolving symlink/path aliases. Select one lexical path for
each physical file. An empty selection is invalid.

Each file must begin with YAML frontmatter delimited by `---` lines:

```yaml
schema_version: 1
model_id: example-pipeline
```

Version is an integer, not a quoted string or Boolean. Every selected document
must use the same nonblank model ID. Additional metadata is retained without
being treated as domain-validated. Unclosed frontmatter prevents indexing that
document; malformed metadata otherwise permits partial body inspection.

## Tagged definitions

Only top-level fenced blocks with the exact info string
`yaml pipeline-definition` are model definitions. Ordinary prose, headings, and
untagged YAML examples are not promoted into model facts. Use one mapping per
block. See [the executable fixture](../../tests/fixtures/minimal.md).

~~~~text
```yaml pipeline-definition
kind: processor
id: P01
consumes: [DS-01]
produces: [DS-02]
provides_capabilities: [segmentation]
```
~~~~

Allowed kinds are processor, artifact, capability, constraint, assumption and
dependency. `id` starts with an ASCII letter and contains letters, digits,
underscores, dots or hyphens. IDs and aliases are case-sensitive and globally
unique across all selected files. `aliases` is an optional list of nonblank
strings; references resolve exact strings without implicit normalization.

Reference fields are lists of nonblank strings: consumes/produces target artifact
records; requires_capabilities/provides_capabilities target capability records;
constraints targets constraint records; references can target any kind. IDs and
aliases share a namespace. Collisions remain ambiguous; intake never selects the
first provider. Dependencies currently use explicit references, without inferred
edge semantics. Duplicate alias entries are also collisions.

Other fields, including implementation state, schema references and expressions,
are preserved as YAML values for later canonical validation. They are not checked
for semantic completeness, executed or used to claim capability feasibility.
YAML duplicate keys, aliases, nonmapping roots, unsafe object tags, malformed
syntax and unterminated definition fences yield diagnostics. YAML anchors without
alias use are inert; YAML merge keys are unsupported. Literal expression strings
remain data. No arbitrary expression interpreter is included.

## Result and error behavior

`IntakeResult` retains documents, indexes (metadata/headings/raw definition blocks),
validated definition envelopes, successful resolved references, and diagnostics.
`valid` means only that intake has no diagnostics, not that the model is feasible
or even canonically complete. Collections are tuples; nested extra YAML values
remain ordinary Python values and must not be treated as deeply immutable.

Each diagnostic has a stable code, message and 1-based inclusive source line
span. YAML parser errors identify the physical error line; schema and reference
diagnostics locate the complete frontmatter or definition block. Related spans
locate colliding or resolved definitions. No claim of field-level columns is made.
Diagnostics sort by source, line, code and message. Successful records remain
available when unrelated files or blocks fail. Source read/encoding failures are
diagnostics; unexpected programmer errors propagate instead of becoming success.

Codes: no_sources, source_read_error, missing_frontmatter, unclosed_frontmatter,
invalid_frontmatter, invalid_yaml, unclosed_definition, invalid_definition,
duplicate_identifier, missing_reference, ambiguous_reference,
reference_kind_mismatch, model_id_mismatch.

## Deferred work

Canonical build-stage records and full semantic validation belong to phase 2.
Target/inventory and expected feasibility outcomes belong to the phase-3 fixture
design. Capability inference, bootstrap analysis, report serialization, a CLI,
solver execution and operational proof are absent. No source size/performance
guarantee is made without representative specifications.
