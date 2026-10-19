# Proposed interfaces and contracts

These are design signatures, not executable stubs or approved public APIs.

```python
parse_model(document: Mapping[str, object]) -> PipelineModel
validate_structure(model: PipelineModel) -> tuple[Diagnostic, ...]
evaluate(model: PipelineModel, policy: EvaluationPolicy) -> EvaluationReport
serialize_report(report: EvaluationReport) -> str
```

## Boundaries

- PipelineModel: versioned Pydantic schema with explicit node identifiers and
  edge references. Required fields, extra-field policy, and graph restrictions
  remain open decisions.
- Diagnostic: stable code, severity, human-readable message, and location or
  model reference. Define and test a stable sort key.
- EvaluationPolicy: explicit enabled checks and approved severity/threshold
  choices. Defaults must not imply an unapproved meaning of correctness.
- EvaluationReport: schema version, model identity, policy identity, and ordered
  findings. Define identity and provenance before serializing reports.

Parsing rejects malformed documents with structured validation errors.
Structural validation reports issues in otherwise schema-valid input.
Specify which diagnostic severities prevent evaluation, and how evaluate uses
validation, before implementation. Internal failures must remain distinguishable
from model findings; never silently convert them into success.

Keep NetworkX graphs internal. Public models and reports must not expose mutable
graph instances. Evaluation must not mutate caller-owned input.
Serialization should produce stable JSON; decide numeric and timestamp handling.
The evaluator must not execute input code or the pipeline it describes.

## Decisions needed before implementation

1. Authoritative source model and representative examples.
2. Input format, schema version policy, and unknown-field behavior.
3. Edge semantics, disconnected components, and cycle validity.
4. Rule catalogue, diagnostic severities, and stop/continue policy.
5. Report identity, deterministic ordering, invocation, and exit-code contract.
