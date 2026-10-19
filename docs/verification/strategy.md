# Verification strategy

Current phase-1 evidence: 27 intake tests passed on Python 3.12.14 and 3.14.8;
locked sync and wheel/source build passed. The initial scaffold's zero-test
collection was superseded by that intake suite. Planning changes require
reference/link and register validation, not repeated runtime checks for
unchanged source.

## First-version acceptance cases

| Requirements | Required cases |
| --- | --- |
| SRC-001/002/003, MOD-002 | Markdown headings/frontmatter, tagged YAML, source spans, malformed blocks, duplicate/missing/ambiguous IDs, inspect retained stages |
| MOD-001/003, SEL-001 | Typed domain records, schema versions, artifact/contract compatibility, inventory and assumptions, selection profile, unsupported constraint |
| EVA-001/002/003, QUA-001 | Graph fidelity/nonmutation, enabled rules, stable order and domain-only public API |
| CMP-001 | Satisfied/unsatisfied multi-input processors; declared but unavailable artifacts; missing required capabilities |
| CMP-002 | Target prerequisites, alternative providers, one viable and one blocked branch |
| CMP-003 | No-bootstrap cycle, explicit bootstrap, independent provider path, unreachable output |
| RES-001/002, REP-002 | Proven-from-model, conditional, unresolved and contradiction cases; conceptual does not imply operational; internal failures distinct |
| SEC-001 | Model expressions/strings remain data; no execution or remote retrieval |
| QUA-002 | Every applicable requirement mapped to actual tests and run evidence |

The minimum combined fixture should include explicit inventory, a target,
multi-input processing, alternative providers, a missing definition, assumptions
and a cycle pair with/without bootstrap. Split into focused cases where useful.
Review exact expected results before claiming implementation done.
Broad REP-001 golden report compatibility is deferred to phase 5.

Before delivery verify all seven first-version questions in design/phases.md.
Keep source locations and derivations in expected outputs, not just Boolean
reachability. Introduce CI and optional parsers in their scoped implementation PRs.

## Workbench alignment verification

WB-001–014 acceptance evidence is in the requirement alignment matrix. These
checks are planned, not executed runtime tests. Prioritize revision identity,
context/source separation, graph-kind cycle distinctions and feasibility versus
provider availability when the respective contracts are selected. Retaining
extra YAML fields does not satisfy extension round-trip or semantic validation.
The [WB-DES-02 scenario matrix](../design/evaluation-scenarios.md) proposes
specific inputs, conclusions and provenance assertions. It is design evidence,
not an executed test suite; turn it into runtime fixtures after DEC-002/003/004/008
and the inventory completeness contract are selected.
The [WB-DES-03 concern contracts](../design/module-boundaries.md) assign a
verification obligation to each current or proposed stage. Intake checks are
executable now; canonical, graph, evaluation and result obligations remain
planned until those modules and their public contracts exist.

For this documentation change: validate work/requirement/decision references,
acyclic dependencies, local links and source section/version/hash metadata.
Runtime tests need not be rerun for unchanged source/dependencies.
