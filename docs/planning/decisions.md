# Decision register

Updated after recovery of the plan; see source-reconciliation.md.
Recovered direction is source-supported context. Exact wire choices remain open.
No independent approval is claimed.

| ID | State | Decision / question | Affected work |
| --- | --- | --- | --- |
| DEC-001 | resolved from source | Design-time artifact-processing model; phases 1 intake, 2 canonical graph, 3 composition | RECON-01 |
| DEC-002 | open | Exact tagged YAML marker/frontmatter/schema versions, ID and alias rules, strictness | P1-01/P1-02/P1-03/P2-03 |
| DEC-003 | open details | AND processor inputs, OR providers and bootstrap-aware cycles are required; graph representation and compatibility rules need fixtures | P1-01/P2-01/P2-02 |
| DEC-004 | open details | Proven/conditional/unresolved plus contradictions required; exact encoding, severity, identity, ordering and failure containers | P3-06 |
| DEC-005 | deferred | Library/CLI integration and broad report formats/platform policy | P3-01/P3-02 |
| DEC-006 | proposed | Python >=3.12; intake tests now run on 3.12.14 and 3.14.8 | QA-01 |
| DEC-007 | source direction | Explicit inventory/assumptions, lifecycle evidence, retained stages; no capability declaration promoted to operational proof | P2-03/P3-06 |

When adopting implementation details, record owner/date/source, alternatives,
rationale, consequences and affected IDs. Preserve superseded choices in the work
log. DEC-001 no longer blocks work merely because the earlier plan was missing.

## 2026-10-20: DEC-002 intake implementation proposal

The phase-1 PR proposes schema_version 1 and model_id frontmatter, exact
`yaml pipeline-definition` fences, generic kind/id envelopes, a shared
case-sensitive ID/alias namespace, and explicit typed reference fields.
See ../design/intake-format.md and tests/fixtures/minimal.md for the concrete
contract and evidence. This is an explicit implementation choice for PR review,
not a claim that the earlier plan prescribed this syntax or the owner approved it.
Ordinary prose/YAML stays unextracted; unsupported YAML and aliases produce
errors rather than silently losing content. Pydantic preserves extra domain
fields for phase 2 without validating their semantics.

The broader DEC-002 canonical schema and DEC-003/004 remain open. Intake work
proceeds against the documented proposal; no graph or inference choices are
adopted as a side effect. Python 3.12 runtime results are recorded in the work log.

## DEC-008: workbench-derived contract adoption (open)

The user authorized mapping the supplied workbench v0.11 document into evaluator
requirements and backlog on 2026-10-20. The mapping records proposed WB-001–014,
not approval of every source proposal or authorization for full-workbench runtime
implementation. Source version/hash and CR-WB-001 are recorded in
../requirements/workbench-alignment.md.

Resolve exact revision/snapshot identity, context and extension representation,
graph-kind boundaries, run/evidence provenance and module ownership through
WB-DES-01/02/03. Link accepted choices to DEC-002/003/004 and their fixtures.
Deferred integrations and ideas require their own selected scope. Preserve
historical phase-1 evidence; no claim of conformance to KerML, SysML, LSP or MCP
is made by retaining a reference to those systems.
