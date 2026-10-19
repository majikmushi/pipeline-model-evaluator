# Delivery plan

No delivery dates or individual assignees have been agreed. Roles below describe
responsibilities, not an observed assignment. Status lives in the JSON register.

| Milestone | Work items | Dependencies | Exit gate |
| --- | --- | --- | --- |
| M0 Preparation | PREP-01, PLAN-01 | None | Reviewable scaffold, planning records and honest check evidence |
| M1 Model contract | P1-01, P1-02, P1-03 | M0; DEC-001/002/003 | Approved schema and fixtures, structured validation errors |
| M2 Structural evaluation | P2-01, P2-02 | M1; DEC-003/004 | Approved rules, deterministic findings, nonmutation checks |
| M3 Reporting/integration | P3-01, P3-02, QA-01 | M2; DEC-004/005 | Stable report, documented invocation if adopted, mapped checks |

## Work breakdown

- P1-01: owner supplies source model and expected results; analyst reconciles
  recovered plan, proposes schema and records decisions. Do not invent semantics.
- P1-02: implement schema/parser after approval; include invalid version, malformed
  fields and hostile data cases. SEC-001 applies.
- P1-03: implement cross-record validation; cover duplicate IDs, missing endpoints,
  and approved empty/disconnected graph behavior.
- P2-01: implement private graph conversion; verify graph fidelity and unchanged
  caller input, including parallel edges if adopted.
- P2-02: implement only approved rules and policy selection; verify positive,
  negative, boundary, disabled-rule, and deterministic-order behavior.
- P3-01: implement versioned report and serializer with canonical identity rules;
  review golden fixtures and compatibility behavior.
- P3-02: implement an invocation adapter only if adopted; document input/errors,
  stdout/stderr and exit behavior. Otherwise document library invocation.
- QA-01: reconcile all adopted requirement IDs to tests, execute supported Python
  checks and package checks, and record actual evidence and remaining limits.

## Completion rule

Each implementation item needs adopted requirements, reviewed decisions, linked
change, executed checks, and a work-log entry before done. Review is performed
through normal PR review; this chat does not constitute independent review.
