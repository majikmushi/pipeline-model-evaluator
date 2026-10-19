# Planning and tracking process

## Continue a chat

Read ../tracking/checkpoint.md, ../README.md, requirements, decisions, and the
selected work item. Inspect current branch/PR before edits. Treat prior chat
summaries as context; verify repository state. Preserve unrelated work.

## Track changes

Use ../tracking/work-items.json as the status source. Status values:
planned, in_progress, blocked, done, deferred. Update status, evidence and
blocked_by together. An implementation item cannot start while its required
decisions remain open. Planning/doc work can continue independently.

For each item: record scope and requirement IDs, dependencies, responsible role,
acceptance evidence, and a bounded next step. Use work-log.md for dated events.
Before ending work, refresh checkpoint.md with completed work, checks, gaps,
next item and next entrypoint. Do not mark behavior done based on documentation.

## Change control

Work on branches and PRs; follow any subsequently introduced governance.
Keep main untouched until normal merge. Preserve IDs when superseding scope.
Link new requirements to their source, decisions, work items and verification.
Do not create external issues or notifications automatically; the repository
register is sufficient for current tracking. Optional future issues should link
to work IDs and keep the register synchronized.

## Definition of ready / done

Ready: bounded scope, adopted affected requirements, resolved blocking decisions,
inputs available, and meaningful acceptance checks.
Done: change is reviewable, checks actually executed and recorded, acceptance
evidence linked, risks disclosed, and tracker/checkpoint updated. PR merge state
is distinct from item completion and must not be implied.

## Reusable work-log entry

Date; work IDs; change/PR; result; checks with environment and outcome; unresolved
issues; next action. Never store secrets or access tokens in planning records.
