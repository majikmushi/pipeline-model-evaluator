# Risks and open questions

| ID | Risk / evidence | Mitigation | State |
| --- | --- | --- | --- |
| R-001 | Earlier plan previously inaccessible | Attachment recovered; source-reconciliation.md corrects baseline | resolved |
| R-002 | Exact extraction/schema/compatibility details remain unspecified | P1-01 example and DEC-002/003 | open |
| R-003 | Conceptual capabilities mistaken for operational proof | Separate lifecycle evidence, derivation and result classes | open |
| R-004 | Python minimum not runtime-tested | QA-01 supported-version checks | open |
| R-005 | No behavioral tests or evaluator exist | Keep readiness separate from prepared docs | tracked |
| R-006 | Connector cannot inspect detailed branch protection | Use existing draft PR, preserve settings | tracked |
| R-007 | No representative input sizes | Define limits after examples | open |
| R-008 | Ordinary path reachability ignores multi-input requirements | AND/OR composition fixtures and explicit inference | open |
| R-009 | Circular declarations self-justify feasibility | Bootstrap/independent-path cases; provenance-aware inference | open |

Domain-detail owner is the project owner; implementation roles remain unassigned.
