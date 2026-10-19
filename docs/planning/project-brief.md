# Project brief

Updated 2026-10-20 (Australia/Perth).
Repository: https://github.com/majikmushi/pipeline-model-evaluator.
Current scope: design-stage preparation and planning in draft PR #1.

## Purpose

Evaluate artifact-processing pipeline designs without executing their processors.
Read the indexed Markdown/YAML specification, reconstruct its canonical model,
validate it and determine whether requested outputs can be composed from explicitly
available inputs and capabilities. Return evidence-backed feasibility and gaps.

The recovered plan is documented in [source reconciliation](source-reconciliation.md).
Its final repository confirmation selects phases 1–3 with uv, Pydantic, NetworkX
and pytest. Initial generic repository planning is superseded where it conflicts.

## Delivery boundary

Phase 1: specification intake and structural validation.
Phase 2: canonical model and graph construction.
Phase 3: capability composition and dependency evaluation.
Design selection profiles and an extensible constraint interface now.
Later: solvers/optimization (phase 4), broad reporting/simulation/adapters (phase 5),
LLM integration and operational processing.

## Confirmed preparation constraints

Preserve existing content, use branch/PR workflow and do not implement substantial
features during preparation. Add requirements, implementation details and durable
tracking/continuation records. No schedule or individual assignment is implied.

## Remaining specificity

The plan is recovered; the exact tagged YAML grammar, full serialized schema,
representative acceptance model, alias behavior, compatibility rules and result
encoding still need a reviewed design. These are bounded design tasks, not a
request to reconstruct the entire earlier conversation again.
