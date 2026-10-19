# Proposed phases 1–3

Status: design proposal. Reconcile with the original plan before implementation.

## Phase 1: Model definition and validation

Agree what a pipeline model describes, its schema version, node and edge fields,
identifier constraints, reference resolution, and allowed graph shapes.
Use Pydantic for boundary validation after those decisions are approved.
Deliver a schema, accepted/rejected fixtures, and structured error contracts.
Completion: reviewers approve semantics and every validation rule has examples.

## Phase 2: Structural evaluation

Use NetworkX internally to inspect a validated model. Candidate checks are
unresolved references, reachability, and cycles; whether each is an error depends
on the approved domain policy. Define enabled checks and deterministic diagnostic
ordering. Do not invent scores, thresholds, or assume every pipeline is a DAG.
Completion: approved checks have positive, negative, and boundary test cases;
evaluation does not mutate input and produces repeatable results.

## Phase 3: Reporting and integration

Define a versioned JSON report and an invocation surface. Decide whether a CLI
is needed, its input format, error output, and exit codes before adding it.
Deliver reviewed report fixtures, usage documentation, and integration checks.
Completion: reproducible reports and documented handling of invalid input,
evaluation findings, and internal failures.

## Deferred

Executing pipelines, arbitrary code loading, remote resource fetching, GUI work,
plugins, performance optimization, and numeric quality scoring are outside this
preparation. No phase is claimed complete by this scaffolding.
