# Model and interface contracts

Scope recovered from the earlier plan; exact wire schema remains a design task.
[Source reconciliation](../planning/source-reconciliation.md).

## Canonical records

| Record | Required design content |
| --- | --- |
| Model | model ID/version, typed collections, source revision |
| Processor | stable ID, consumes/produces artifact types, requires/provides capabilities, constraints, lifecycle state, determinism |
| ArtifactType | stable ID, schema reference and compatibility information |
| Capability | stable ID and declared meaning |
| Dependency | typed endpoints and relationship meaning |
| Constraint | stable ID, expression/rule reference; unsupported expressions remain unresolved |
| Assumption | stable ID, status, explicit acceptance and evidence |
| Evidence | source reference, stable definition ID, source location |
| Finding | ID/code, severity, result classification, evidence and derivation |
| SelectionProfile | target output, available inputs, acceptable uncertainty, target cost, allowed methods |

Availability is an explicit inventory, not inferred from artifact declarations.
Lifecycle evidence distinguishes conceptual, validated, simulated and
operationally demonstrated claims. Inference cannot upgrade a declaration into
operational proof. Stable IDs identify definitions; line spans aid navigation.

## Pipeline boundaries (design signatures)

```python
load_sources(paths: Sequence[Path]) -> SourceBundle
index_sources(sources: SourceBundle) -> StructuralIndex
extract_definitions(sources: SourceBundle, index: StructuralIndex) -> DefinitionSet
resolve_definitions(definitions: DefinitionSet) -> ResolutionResult
build_model(resolved: ResolutionResult) -> ModelBuildResult
validate_model(model: Model) -> tuple[Diagnostic, ...]
build_graph(model: Model) -> EvaluationGraph
evaluate(model: Model, profile: SelectionProfile, policy: EvaluationPolicy) -> EvaluationResult
project_results(result: EvaluationResult) -> ResultArtifact
```

These signatures supersede the generic mapping-only parser proposal. Define
result/error containers and partial-data rules before coding. Retain intermediate
representations; findings preserve provenance through transformations.

## Evaluation contract

Forward inference adds outputs only after all required inputs and capabilities
are satisfied under the explicit assumption policy. Backward reasoning retains
alternative providers and full prerequisite sets. A simple graph path is
insufficient proof of multi-input feasibility.

Result classes: proven (within validated model and accepted assumptions),
conditional (explicit unsatisfied assumptions/contracts), unresolved (insufficient
knowledge). Contradictions/invalid compositions must be flagged separately.
Operational correctness is outside design-time proof. Prevent circular
self-justification; verify bootstrap availability and external enabling paths.

Order findings deterministically; record selected rules, inventory, target,
model/policy identity, derivation and supporting definition locations.
Severity and epistemic result class are separate fields. Do not infer a numeric
score. Public domain records must not expose mutable NetworkX graph objects.

## Error and extension boundaries

Separate malformed source/frontmatter, unresolved definitions, model findings,
unsupported constraints and internal failures. Unknown is not false.
Read only selected source files; do not execute model code or fetch remote refs.
Specify a constraint adapter interface returning findings and unsupported cases;
phase 1–3 does not implement a solver. Exact schema, tagged-block marker,
alias rules, canonical identity and output encoding remain open decisions.

## Implemented phase-1 boundary

The concrete `inspect_sources` facade and retained intake records are specified
in [intake format](intake-format.md). The signatures above remain intended
phase boundaries, not a claim that every stage is a separate public function.
