# Risks and open questions

| ID | Risk / evidence | Mitigation | State |
| --- | --- | --- | --- |
| R-001 | Earlier plan previously inaccessible | Attachment recovered; source-reconciliation.md corrects baseline | resolved |
| R-002 | Canonical schema, revision and compatibility details remain unspecified | Review [decision recommendations](../design/reengineering-decision-proposals.md) with P1-01 fixtures and DEC-002/003 | open |
| R-003 | Conceptual capabilities mistaken for operational proof | Separate lifecycle evidence, derivation and result classes | open |
| R-004 | Python minimum not runtime-tested | Phase-1 intake tests passed on Python 3.12.14 and 3.14.8 | resolved for intake |
| R-005 | No canonical evaluator or phase-2/3 behavioral tests exist | Keep phase-1 intake evidence separate from evaluation readiness | tracked |
| R-006 | Connector cannot inspect detailed branch protection | Use existing draft PR, preserve settings | tracked |
| R-007 | No representative input sizes | Define limits after examples | open |
| R-008 | Ordinary path reachability ignores multi-input requirements | AND/OR composition fixtures and explicit inference | open |
| R-009 | Circular declarations self-justify feasibility | Bootstrap/independent-path cases; provenance-aware inference | open |

Domain-detail owner is the project owner; implementation roles remain unassigned.
