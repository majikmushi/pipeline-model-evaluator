# Project brief

Updated: 2026-10-20 (Australia/Perth).

## Confirmed task context

Prepare https://github.com/majikmushi/pipeline-model-evaluator as a Python
pipeline model evaluator with uv, Pydantic, NetworkX, and pytest. Cover phases
1–3, interfaces, contracts, requirements, implementation planning, and tracking.
Preserve existing content and use a branch/PR. Substantial feature implementation
is outside the current authorization.

## Intended outcome

Proposed: a static tool that accepts an explicit pipeline model, validates its
shape and references, evaluates approved structural rules, and emits a repeatable
report. Model authors and reviewers should be able to locate findings in input
and understand which policy produced them.

The exact source model, node/edge meanings, graph validity rules, and scoring
meaning have not been recovered. These are open design questions, not implicit
requirements. This project does not evaluate machine-learning predictions unless
the owner later defines that as the intended domain.

## Sources and limits

- Current chat: repository selection, requested stack, design-only preparation,
  and request for planning/tracking and implementation detail documentation.
- Referenced chat: Organizational Concepts in Programming,
  conversation ID 390fc28f-65c4-47c0-b943-87d0060c2c8c.
  Its assistant planning answers were returned as unresolved content references.
- Initial repository: main at 8f4f3923d4ff4c98dca2e8a1d64f1a6ce1171de7,
  containing only README.md.
- Initial preparation: commit d230af169888f481822da81cd17638e5ba8e88fe
  in draft PR #1.

No missing chat answer is treated as recovered evidence. There is no configured
external project definition or role policy in the inspected repository.

## Scope

Now: reviewable preparation and project records.
Later, after design decisions: schema, structural analysis, reporting, and
possibly a CLI. Deferred: pipeline execution, remote fetching, plugins, GUI,
deployment, numeric scoring, and performance targets without representative data.
