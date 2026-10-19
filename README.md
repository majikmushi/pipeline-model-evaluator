# pipeline-model-evaluator-
pipeline-model-evaluator/

## Python project preparation

Design-time pipeline model evaluator. Phase-1 specification intake is implemented;
canonical graph construction and capability evaluation remain planned.
No CLI, scoring algorithm, or pipeline execution is implemented.

## Development

Python 3.12 or later and uv are required.

```sh
uv sync --locked
uv run python -c "import pipeline_model_evaluator"
uv run pytest
uv build
```

The intake tests cover parsing, source evidence and reference diagnostics; see tests/README.md.
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

## Specification intake

```python
from pathlib import Path
from pipeline_model_evaluator.sources import inspect_sources

result = inspect_sources([Path("tests/fixtures/minimal.md")])
for diagnostic in result.diagnostics:
    print(diagnostic.code, diagnostic.location, diagnostic.message)
```

See the [intake format and API](docs/design/intake-format.md). Intake validity
does not establish canonical completeness or target feasibility.
