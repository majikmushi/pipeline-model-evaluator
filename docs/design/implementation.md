# Implementation details

The recovered design organizes work into concerns. Phase-1 source intake now
exists in `sources/intake.py` and `sources/records.py`; the other entries below
are proposed boundaries, not empty stubs to create now. See the
[module concern proposal](module-boundaries.md) for ownership and dependency
direction.

| Package | Responsibilities |
| --- | --- |
| sources/intake.py, records.py (implemented) | Read selected Markdown, frontmatter, headings, tagged YAML and source spans; resolve intake IDs/aliases and references |
| Canonical resolution (proposed) | Resolve canonical identity, revisions and contextual bindings beyond intake aliases |
| models/definitions.py, artifacts.py, capabilities.py, findings.py | Pydantic canonical records and evidence/results |
| validation/schemas.py, contracts.py | Serialized structure, references and type/contract compatibility |
| graphs/builder.py, queries.py | Internal typed NetworkX relationships |
| evaluation/structural.py, dependencies.py | Structural findings, gaps and cycle support |
| evaluation/capabilities.py, composition.py | Forward/backward reasoning, alternative providers and multi-input requirements |
| evaluation/coverage.py | Coverage of required definitions/contracts/evidence; scope after composition |
| output/markdown.py, json.py | Basic phase-3 result projection; broad serializers in phase 5 |
| cli.py | Optional invocation adapter after contract agreement |

## Nine retained stages

Load -> index -> extract -> resolve -> build -> validate -> graph -> evaluate
-> project. Carry source identity and span through each stage. Retain intermediate
records in a run result so a failing stage can be inspected without a full rerun.
Do not silently extract arbitrary prose as authoritative machine definitions.

## Inference design

Use an artifact/processor relationship representation that retains AND
requirements for a processor's multiple inputs and OR alternatives across
providers. A bipartite typed graph remains an implementation candidate;
DEC-003 accepts the semantics but leaves the concrete projection open.
Forward evaluation uses a deterministic worklist/fixed point over finite declared
artifacts/capabilities. Record derivation dependencies for every addition.
Backward evaluation explores providers and prerequisite sets with visited-state
tracking; preserve alternatives rather than stopping at the first provider.
These algorithm details are proposals to verify against agreed fixtures.

Analyze strongly connected components to locate cycles, then test whether
explicit inventory or an independent provider enables progress. A declared cycle
alone neither proves feasibility nor invalidity. Keep conditional and unresolved
paths distinct from supported derivations and contradictions.

## Evidence and extensions

Record conceptual/validated/simulated/operational evidence independently from
declared determinism. A feasible conceptual composition is not operational proof.
Selection profiles include targets, input inventory, uncertainty, cost and methods.
Cost optimization and actual LLM selection are deferred.
Start explicit constraint checks as Python rules; define an adapter boundary and
report unsupported expressions. Add clingo/Z3 only in a later scoped change.

## Dependencies and verification

Existing stack: uv, Pydantic, NetworkX, pytest, markdown-it-py and PyYAML.
The Markdown/YAML parsers were selected for the phase-1 intake implementation.
Do not add solvers, RDF, planning frameworks or GUI dependencies now.
Verify source-span fidelity, malformed tagged data, ambiguous references,
multi-input gating, alternative providers, bootstrap/no-bootstrap cycles,
explicit inventory, missing definitions, result classes and repeatable evidence.
