# Proposed module concern contracts

Status: WB-DES-03 design proposal, 2026-10-20. This defines ownership and
dependency direction for the existing phase-1 intake and possible phase-2/3
modules. It does not create those later modules or select the remaining canonical
schema, graph representation or result encoding details in DEC-002/003/004/008.
The user has accepted the core DEC-002/003 boundaries; this concern proposal
remains review material.

## Direction of dependencies

```text
selected files -> intake records -> canonical model -> graph projections
                                  -> evaluation -> result projection
```

The current `sources/intake.py` and `sources/records.py` implement the first
boundary only. Later stages consume domain records and return new records;
they do not mutate intake evidence. A client, CLI, database, GUI or live provider
would call an application boundary around these stages. The domain model must
not import those adapters, a NetworkX graph object or a concrete storage engine.
The evaluator may depend on graph query interfaces, but a graph adapter must
not own canonical identity or result evidence.

## Concern contracts

| Concern and present state | Owned data and purpose | Invariants and interface | Errors and exclusions | Verification obligation |
| --- | --- | --- | --- | --- |
| Source intake (implemented) | Selected UTF-8 Markdown, frontmatter, headings, tagged YAML blocks, definition envelopes, resolved references and source spans | `inspect_sources(paths) -> IntakeResult`; deterministic path/diagnostic order; partial records survive unrelated source errors; `valid` covers intake only | Source/encoding, YAML, envelope and reference failures become source-linked diagnostics; no directory discovery, remote fetch, model execution or feasibility claim | Existing phase-1 fixtures cover malformed and partial input, spans, aliases, reference kinds and stable ordering |
| Canonical model builder (proposed P2-03) | Versioned processor, artifact, capability, dependency, constraint, assumption and evidence records; links to source and revision identity | Accepts resolved intake data; returns a build result with accepted records, rejected records and diagnostics; a record is canonical only after its own domain validation | Do not silently treat preserved extra YAML fields as validated semantics; unsupported versions, bindings and extensions remain explicit; no provider availability inference | Fixtures for valid/invalid versions and fields, identity/context collisions, preserved extensions and source-to-canonical traceability |
| Structural/contract validation (proposed P2-02) | Selected rule results for types, contracts and relationships | Rules receive a canonical snapshot plus explicit policy revision and return findings without changing model records | Unsupported constraints are reported as unsupported or unresolved; unexpected programmer failures remain internal errors; no arbitrary expression execution | Rule enabled/disabled cases, conflicting contracts, stable finding order and source/rule evidence |
| Graph projection/query (proposed P2-01) | Typed semantic, connector, provider-dependency and derivation projections | Builds/query graphs from canonical records; preserves n-ary relationship roles and full AND/OR prerequisites; returns domain values, not mutable NetworkX objects | Graph construction errors identify invalid model records; no global DAG rule, identity rewriting or UI graph state | Role fidelity, graph-specific cycle policy, nonmutation and adapter-independent public results |
| Composition evaluation (proposed P3-03/04/05) | Forward/backward derivations, alternatives, missing prerequisites and bootstrap analysis | Takes model snapshot, graph queries, target, explicit inventory and policy; records each derivation and all prerequisite branches | An empty or unknown inventory is not operational availability; cycles cannot justify themselves; no live processor/provider execution | F-01/02/05 and multi-input/alternative fixtures in `evaluation-scenarios.md` |
| Result assembly/projection (proposed P3-06) | Claim classes, findings, derivations, assumptions and correlation references | Takes stage outputs and creates a run-scoped result citing source snapshot, rule/policy, inventory, target and evaluator version; projection is a separate step | Contradictions remain separate from uncertainty; projection failures must not rewrite evaluation evidence; no broad report format commitment | F-03/04/06, deterministic ordering, distinct internal failure and model-finding cases |
| External adapters (deferred) | Invocation, persistence, GUI, provider discovery and protocol integration | Depend on application/domain contracts; declare supported subset and effects | Do not make a design-time conclusion into operational proof or mutate historical runs | Contract tests only after a concrete adapter is selected |

These are concern boundaries, not a required one-file-per-row layout. The
existing intake code's Pydantic `frozen=True` models contain extra YAML values
that may be mutable; deep immutability is not claimed. The canonical builder
must decide how to copy or freeze such values before promising immutable
revisions. `build_model`, `validate_model`, `build_graph`, `evaluate` and
`project_results` remain design signatures in [contracts](contracts.md).

## Diagnostic, evidence and history ownership

| Record | Purpose and owner | Retention/correlation rule |
| --- | --- | --- |
| Source diagnostic | Intake or canonical/validation stage explains malformed or unsupported input with source span and related spans | May exist before any run; stable code and stage identity allow filtering; it is not itself a feasibility conclusion |
| Evaluation finding and derivation | Evaluator/result assembly records a claim, rule, assumptions, inputs and source references | Part of the run result; later reruns create new result identity rather than editing the old evidence |
| Diagnostic log event | Application/runtime boundary records an operational fault, timing or internal exception | Correlate by run/stage ID when present; retention can differ from result evidence and cannot erase it |
| Project/change history | Project workflow records baseline, requirement change, decision and PR evidence | Separate from evaluator output; links to run or source revision when applicable but does not rewrite it |

Illustrative correlation: a source diagnostic cites `source=model.md:12-18`
and `stage=resolve`. A later run finding cites the accepted definition revision,
`run=R7`, `rule=contract-r2` and its derivation. If projection of R7 fails, a
log event cites `run=R7`, `stage=project` and an internal error code; the R7
evaluation evidence remains inspectable. This is a contract example, not a
logging format or durable checkpoint implementation.

An expected invalid model produces diagnostics or findings, not a success
boolean with lost detail. A read/encoding failure remains a source diagnostic.
An unexpected bug is an internal failure that the application boundary may log
and return distinctly; the core must not convert it into an ordinary model
finding. Error containers and public serialization remain DEC-004.

## Review and handoff

This proposal affects P2-03, P2-01/02 and P3-06. Before implementation, review
the remaining revision-ID and wire choices, partial build results, inventory
completeness, graph query shapes and result/error containers alongside
DEC-002/003/004/008. QA-01 should turn each row's obligations into meaningful
checks when the relevant module exists. Existing intake tests validate only
the implemented first row; no graph, composition, evidence store or external
adapter is claimed to exist.
