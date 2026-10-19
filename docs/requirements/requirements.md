# Requirements and acceptance criteria

Source baseline: [recovered plan](../planning/source-reconciliation.md).
Confirmed preparation constraints are directly requested. Plan-derived behaviors
come from the recovered design, but exact formats remain open decisions.
Work status lives in ../tracking/work-items.json.

| ID | Basis | Requirement | Acceptance evidence | Work |
| --- | --- | --- | --- | --- |
| PRE-001 | confirmed | uv/Pydantic/NetworkX/pytest setup | Locked sync, imports and build | PREP-01 |
| PRE-002 | confirmed | Preserve files; branch/PR workflow | Original README retained, main unchanged | PREP-01 |
| PRE-003 | confirmed | Planning, requirements and tracking | Linked records and validation | PLAN-01 |
| PRE-004 | confirmed | No substantial features in preparation | Source docstring only | PREP-01 |
| SRC-001 | plan-derived | Load/index Markdown/YAML and validate frontmatter | Parsed headings/frontmatter with exact source spans | P1-02 |
| SRC-002 | plan-derived | Extract tagged definitions; detect duplicate/missing refs | Good/malformed/duplicate/missing fixtures with source diagnostics | P1-03 |
| SRC-003 | plan-derived | Retain intermediate representations | Inspect load/index/extract/resolve/build results on failure | P1-02 |
| MOD-001 | plan-derived | Versioned canonical processor/artifact/capability/dependency/constraint/assumption model | Typed records and invalid-version/field cases | P2-03 |
| MOD-002 | plan-derived | Resolve stable IDs and references, with evidence | Unique IDs and source-linked missing/ambiguous cases | P1-03 |
| MOD-003 | plan-derived | Define explicit graph/contract compatibility policy | Reviewed edge/type/cycle semantics and fixtures | P1-01 |
| EVA-001 | plan-derived | Evaluate selected checks under explicit policy | Enabled/disabled rule cases | P2-02 |
| EVA-002 | plan-derived | Query typed internal graph without mutating input | Relationship fidelity and nonmutation cases | P2-01 |
| EVA-003 | plan-derived | Repeatable findings and evidence order | Repeat/reorder fixtures | P2-02 |
| CMP-001 | plan-derived | Forward infer from explicit inventory, honoring every input/capability | Multi-input and unavailable-artifact fixtures | P3-03 |
| CMP-002 | plan-derived | Backward reason from target across alternative providers | Alternative prerequisite sets and missing-input results | P3-04 |
| CMP-003 | plan-derived | Detect unsupported cycles and unreachable outputs | Bootstrap/independent-path/no-bootstrap fixtures | P3-05 |
| RES-001 | plan-derived | Proven/conditional/unresolved results plus explicit contradictions | Expected classification, evidence and derivation per fixture | P3-06 |
| RES-002 | plan-derived | Declared capability is not operational proof; unknown is not false | Conceptual/missing-definition cases retain uncertainty | P3-06 |
| SEL-001 | plan-derived | Selection-profile and constraint extension contracts | Targets/inventory/uncertainty/cost/method fields; unsupported constraint behavior | P2-03 |
| REP-001 | deferred phase 5 | Broad versioned JSON reporting | Golden/compatibility tests after format agreement | P3-01 |
| REP-002 | plan-derived | Distinguish malformed input, findings and internal failure | Separate result/error cases in basic feasibility output | P3-06 |
| SEC-001 | preparation boundary | No model execution or remote retrieval | Inspection and hostile-data cases | P1-02 |
| QUA-001 | design constraint | Keep NetworkX internal to analysis | Domain-only public records | P2-01 |
| QUA-002 | quality proposal | Map adopted behavior to meaningful checks | Executed requirement-to-test matrix | QA-01 |

No numeric score or performance threshold is specified. Concrete serialization,
tag markers and compatibility rules require DEC-002/003/004. Basic phase-3
feasibility results are required even though broad reporting is phase 5.

## Broader workbench reference

The [workbench alignment matrix](workbench-alignment.md) adds WB-001–014 as
traceable evaluator proposals and deferred ideas from the supplied v0.11 document.
It records source sections, acceptance evidence, existing requirement links and
work IDs. These additions do not retroactively change the phase-1 contract or
claim that the workbench is implemented. Review CR-WB-001 and DEC-008 before
adopting concrete schema/runtime changes.
