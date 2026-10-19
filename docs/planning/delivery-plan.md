# Delivery plan

Scope follows the recovered plan. Status is in ../tracking/work-items.json.
Dates and individual assignees are not agreed.

| Milestone | Work | Dependencies | Exit |
| --- | --- | --- | --- |
| M0 Preparation | PREP-01, PLAN-01, RECON-01 | None | Scaffold and source-aligned planning in PR |
| M1 Intake/validation | P1-01, P1-02, P1-03 | M0; DEC-002/003 as applicable | Indexed/extracted spec with source diagnostics |
| M2 Canonical model/graph | P2-03, P2-01, P2-02 | M1 | Typed model, validity checks and queryable graph |
| M3 Composition/dependencies | P3-03, P3-04, P3-05, P3-06, QA-01 | M2; DEC-004 | Evidence-backed target feasibility and gap result |
| Later | P3-01, P3-02 | Separately scoped | Phase-5 reporting/invocation integration |

## Bounded assignments

P1-01: turn recovered concepts into a small representative tagged source fixture,
inventory, target and expected outcomes; settle extraction/schema/graph decisions.
P1-02: source loader, Markdown index, frontmatter, spans and retained stage outputs.
P1-03: tagged-definition extraction and stable ID/alias/reference diagnostics.
P2-03: canonical domain records, lifecycle evidence, assumptions, selection profile
and extensible constraint contract. Unsupported constraints remain explicit.
P2-01: typed internal graph with all inputs and alternative providers preserved.
P2-02: structural/type checks, policy selection and deterministic finding order.
P3-03: forward fixed-point inference with explicit inventory and AND input gating.
P3-04: backward prerequisite analysis retaining OR provider alternatives.
P3-05: unsupported cycles, bootstrap/external path checks and unreachable outputs.
P3-06: combine analyses into basic feasibility/gap results with evidence,
derivations, assumptions, result class and contradictions; no operational claims.
QA-01: verify the first-version questions and every applicable requirement.

P3-01 and P3-02 retain historical IDs but are deferred; they no longer define
phase 3. Do not interpret old ID names as current phase membership.

Done requires reviewed affected design, implementation where applicable,
meaningful executed checks, evidence and updated checkpoint. Prepared documents
do not complete feature work or imply PR merge.
