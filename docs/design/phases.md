# Implementation phases from the recovered plan

Source: [reconciliation](../planning/source-reconciliation.md).
Phase-1 intake is implemented for the documented scoped format. Its broader
P1-01 representative fixtures remain in progress; phases 2 and 3 are not
implemented.

## Phase 1: Specification intake and structural validation

Load Markdown/YAML, preserve source locations, index headings and stable IDs,
extract tagged machine-readable definitions, validate frontmatter and report
missing/duplicated references. Keep intermediate document/index/definition
records for inspection. Deliver parsed specification and source-linked diagnostics.

## Phase 2: Canonical model and graph construction

Define processor, artifact type, capability, dependency, constraint, assumption,
evidence and finding contracts. Resolve aliases and references; validate types
and relationships; build a typed queryable graph. Deliver a canonical model
with validity checks, without silently interpreting unknown definitions as false.

## Phase 3: Capability composition and dependency evaluation

Forward-chain from explicitly available inputs/capabilities. Backward-chain from
requested target artifacts to prerequisites and alternative providers. Honor all
inputs of multi-input processors. Identify missing prerequisites, unsupported
cycles, unreachable outputs and incompatible contracts. Cycles may be supported
by bootstrap inputs or independent paths; do not ban them categorically.
Deliver feasibility/gap results with evidence, derivations, assumptions, and
proven/conditional/unresolved classifications plus explicit contradictions.

## Later phases

Phase 4: constraint solver adapters and optimization (clingo/Z3 only when needed).
Phase 5: broad JSON/Markdown reporting, diagrams, abstract simulation, external
adapters and extensibility. Design selection profiles and a constraint interface
now; defer actual solvers, LLM integration and real processor execution.

## First-version acceptance questions

Which stages/datasets exist? Who consumes/produces each artifact? Which required
capabilities are declared/provided/missing? Can the target be derived from the
available inventory? What prerequisites, assumptions or contracts block it?
Which conclusions follow from the model, remain conditional, or are unresolved?
Where are their supporting definitions?
