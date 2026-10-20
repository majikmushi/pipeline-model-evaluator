# Decision register

Updated after recovery of the plan; see source-reconciliation.md.
Recovered direction is source-supported context. The user accepted the core
DEC-002/003 directions on 2026-10-20; exact wire and compatibility choices
remain open. No independent review is claimed.

| ID | State | Decision / question | Affected work |
| --- | --- | --- | --- |
| DEC-001 | resolved from source | Design-time artifact-processing model; phases 1 intake, 2 canonical graph, 3 composition | RECON-01 |
| DEC-002 | core accepted; details open | Keep the merged phase-1 intake contract; canonical definitions have stable identity, immutable revision/source references, separate contextual interpretation and versioned preserved extensions. Revision-ID generation, aliases, wire encoding and migration remain open | P1-01/P1-02/P1-03/P2-03 |
| DEC-003 | core accepted; details open | Preserve typed graph kinds, n-ary roles, AND prerequisites, OR providers and bootstrap-aware provider cycles; graph representation and compatibility rules still need fixtures | P1-01/P2-01/P2-02 |
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

The broader canonical schema was not selected by the phase-1 merge. The later
user acceptance of DEC-002/003 core boundaries is recorded below; it does not
retroactively make intake a graph or inference implementation. Python 3.12
runtime results are recorded in the work log.

## 2026-10-20: DEC-002 and DEC-003 core direction accepted

The user answered “2 yes 3 yes” to the explicit DEC-002/DEC-003 decision list
in this chat. This accepts the core boundaries proposed in
../design/workbench-contract-boundaries.md while leaving choices the proposal
did not settle open.

- **DEC-002 accepted:** stable definition identity is independent of labels and
  source lines; revisions and source snapshots identify exact inputs without
  rewriting earlier evidence; contextual interpretations link to, rather than
  replace, source definitions; unsupported extension payloads retain their
  vocabulary/version and are not reported as semantically validated. The merged
  phase-1 intake syntax remains the current executable input contract.
- **DEC-003 accepted:** distinct semantic, connector, provider-dependency and
  derivation projections preserve relationship roles; processor prerequisites
  remain conjunctive and alternative providers remain separate. Semantic cycles
  are not categorically invalid, provider cycles cannot prove themselves
  without an external seed/path, and proof derivations are acyclic. NetworkX
  remains an internal adapter, not the public domain model.

Still to choose for DEC-002: assigned versus content-derived revision IDs,
canonicalization, alias/rename behavior, exact context and extension wire
encoding, version compatibility and migration. Still to choose for DEC-003:
concrete graph query/edge representation, artifact/capability compatibility
rules, connector semantics and executable cycle fixtures. These details remain
blockers for the affected implementation work; DEC-004 and DEC-008 are not
accepted by this reply.

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

The WB-DES-01 [contract boundary document](../design/workbench-contract-boundaries.md)
provides the accepted core directions and illustrative records. Public revision
identifiers, canonicalization, context binding and compatibility still need
selection and acceptance fixtures before implementation.

The WB-DES-02 [acceptance scenarios](../design/evaluation-scenarios.md) make
DEC-004/008 reviewable without selecting a result encoding. Inventory
completeness, unsupported-constraint classification and rule disabling remain
open details; executable fixtures must follow the adopted choices.

The WB-DES-03 [module concern proposal](../design/module-boundaries.md) assigns
data and error ownership across intake, canonicalization, validation, graphs,
evaluation and result assembly. It does not resolve public API shapes, remaining
DEC-002/003 details, or DEC-004/008 choices.

## 2026-10-20: remaining choices recommended for review

The user requested best-fit proposals that account for reengineering. The
[decision recommendations](../design/reengineering-decision-proposals.md)
compare alternatives and propose source/content fingerprints, canonical
snapshot manifests, conservative exact-match compatibility, derived graph
queries, a run/evidence envelope, open-world inventory and a staged WB scope.
These recommendations do **not** extend the accepted core DEC-002/003 direction
or resolve DEC-004/008. Review the listed decision gates and fixtures before
moving those entries to resolved or unblocking implementation.
