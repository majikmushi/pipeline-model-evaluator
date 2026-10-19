# Implementation details: proposed design

This is an implementation specification for future bounded changes, not source
code or evidence that those changes exist. Follow approved requirements and
[contracts](contracts.md); unresolved details stay behind their decision gates.

## Intended modules

| Module under src/pipeline_model_evaluator | Responsibility | Main boundary |
| --- | --- | --- |
| models.py | Pydantic input schema and domain values | PipelineModel |
| parsing.py | Convert decoded input to schema; map validation errors | parse_model |
| diagnostics.py | Immutable diagnostic values and stable ordering | Diagnostic |
| validation.py | Cross-record IDs/references and approved constraints | validate_structure |
| graph.py | Convert validated records to internal NetworkX graph | Internal only |
| policy.py | Enabled rules and approved settings | EvaluationPolicy |
| evaluation.py | Orchestrate validation/rules without side effects | evaluate |
| reporting.py | Report model and deterministic JSON serialization | EvaluationReport, serialize_report |
| cli.py | Optional thin adapter after DEC-005 | Process boundary |

Only __init__.py exists now. Do not create empty executable stubs for every module.

## Data flow and failures

Decoded mapping -> Pydantic validation -> cross-record validation -> internal
graph -> enabled rules -> ordered diagnostics -> report -> JSON.
No graph is built when references are invalid unless an adopted policy explicitly
defines a safe partial graph. Preserve original locations for diagnostics.
Catch anticipated boundary errors narrowly; do not catch every exception and
label it a model finding. Application adapters may format internal errors, but
must signal failure distinctly.

## Schema and graph decisions

Pydantic configuration, strictness/coercion, extra fields, ID types, and schema
version dispatch depend on DEC-001/002. Do not infer them from sample spelling.
Graph vs DiGraph vs MultiDiGraph depends on DEC-003: edge direction, parallel
edges, and self-loops. Assign stable identifiers before any reordering.
Avoid exposing live graphs or relying on insertion order in public output.

## Evaluation and reporting

Each approved rule has a stable code, documented preconditions, policy setting,
and input/output fixture. Share a single diagnostic ordering function.
Evaluate must define whether it runs validation itself and how blocking findings
affect later rules before callers rely on it (DEC-004).
Report identity must specify canonicalization and policy version. Keep volatile
timestamps out of deterministic fixtures or isolate them under an explicit
contract. Do not add score fields until their interpretation is approved.

## Implementation sequence

Implement one work item per reviewable change with its requirement IDs and
meaningful checks. Start with examples and contracts, then parser, cross-record
validation, graph adapter, rules, reports, and conditional invocation adapter.
Dependencies and exit gates are in ../planning/delivery-plan.md.
