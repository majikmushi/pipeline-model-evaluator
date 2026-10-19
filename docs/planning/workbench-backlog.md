# Workbench-derived evaluator backlog

Source: [alignment and traceability](../requirements/workbench-alignment.md).
These items capture selected design work and later ideas; they are not additional
mandatory dependencies for the first evaluator release. JSON work-item status is
authoritative. No external issue board or notifications are created.

## Planned design work

| Work ID | Scope and output | Ready when | Done evidence |
| --- | --- | --- | --- |
| WB-DES-01 | Revision/context/extension and graph-kind contracts; impact assessment for P2-03 and P2-01 | Mapping available; current intake shape inspected | Reviewed schema examples for revisions, contexts, preserved extensions and relationship roles; explicit proposed changes to DEC-002/003 |
| WB-DES-02 | Feasibility/evidence/provider distinction and small acceptance scenarios | WB-DES-01 examples available | Expected results for conceptual feasibility vs provider availability, alternative providers, unknown evidence and source derivation; inputs linked to P3-06 and QA-01 |
| WB-DES-03 | Module concern contracts, dependency direction and diagnostic/evidence correlation | Current module boundaries and result proposal available | Purpose/state/invariants/API/errors/exclusions/test matrix per affected module; declared logging/evidence owners |

WB-DES-01 now has a [reviewable boundary proposal](../design/workbench-contract-boundaries.md).
Its schema examples and acceptance cases are proposed; DEC-002/003/008 and the
final canonical wire/compatibility contract remain open.
WB-DES-02 has [proposed expected scenarios](../design/evaluation-scenarios.md)
for abstract feasibility, provider availability, alternatives, uncertainty,
contradiction, bootstrap and rerun provenance. Exact executable oracles depend
on the open result, inventory and revision decisions.

DEC-008 records adoption questions. Design work may proceed to make them concrete;
runtime implementation of these additions requires resolution of the affected
contract choices. No owner approval or engineering design is inferred from an
imported document's imperative language.

## Deferred extensions

| Work ID | Captured scope | Selection criterion |
| --- | --- | --- |
| WB-EXT-01 | Dimension-specific preservation assessments | A concrete transformation/task with expected preservation results exists |
| WB-EXT-02 | Durable, version-compatible checkpoint save/restore | A real resumption need beyond inspecting in-memory stages is selected |
| WB-EXT-03 | Workbench/protocol adapters and shared application services | A client/integration is selected with explicit supported operations and effects |
| WB-EXT-04 | Impact/dependency health, scenario comparison and experiment notebook | Owner selects an idea, outcome, fixtures and a bounded release scope |

GUI construction, database engines, backup scheduling, simulator/DAP implementation
and full standard support are broader-workbench work, not hidden evaluator tasks.
Promotion of a deferred item should name its own requirements, acceptance tests,
dependencies and affected baseline rather than silently expanding phases 1–3.
