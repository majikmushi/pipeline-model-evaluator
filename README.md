# pipeline-model-evaluator-
pipeline-model-evaluator/

## Python project preparation

Design-stage static pipeline model evaluator.
No evaluator, CLI, scoring algorithm, or pipeline execution is implemented.

## Development

Python 3.12 or later and uv are required.

```sh
uv sync --locked
uv run python -c "import pipeline_model_evaluator"
uv run pytest
uv build
```

The pytest suite is intentionally empty at this stage; see tests/README.md.
Commit changes to dependency declarations together with a regenerated uv.lock.

## Design

- [Phases 1–3](docs/design/phases.md)
- [Interfaces and contracts](docs/design/contracts.md)
- [Repository preparation and decisions](docs/design/preparation.md)

The original plan has now been recovered from the attached conversation export.
See [source reconciliation](docs/planning/source-reconciliation.md). Initial scope
is specification intake, canonical model/graph construction, and capability
composition/dependency evaluation. Exact schemas and examples remain design work.

## Planning and continuation

Start with the [project documentation index](docs/README.md) and
[continuation checkpoint](docs/tracking/checkpoint.md). Requirements, work items,
decisions, risks, implementation details and verification are tracked there.
