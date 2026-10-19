# Continuation checkpoint

Updated 2026-10-20 (Australia/Perth).
Repository: https://github.com/majikmushi/pipeline-model-evaluator
Branch: docs/land-workbench-alignment
Base branch: main after PR #2 merged

Preparation PR #1 and phase-1 PR #2 were verified merged. The repository has the initial phase-1
intake library: explicit local Markdown, frontmatter, tagged YAML definitions,
heading/block line evidence, typed ID/alias reference resolution and diagnostics.
Documents, indexes, blocks and definition/reference records are retained on
partial failures. See ../design/intake-format.md for the concrete proposed format.

P1-02/P1-03 are merged and tested for this intake scope. P1-01 remains in progress:
canonical contracts, representative inventory/target and expected feasibility
outcomes still need design work. The exact intake syntax was merged for its scoped library API;
merely coding it does not imply owner adoption of every contract.

Verification: 27 tests pass on Python 3.12.14; wheel/source distribution build
passes. Other final checks are recorded in work-log.md. Phase-2 canonical graphs
and phase-3 composition are not implemented; intake valid does not mean feasible.

Resume: ../README.md -> ../design/intake-format.md -> ../planning/decisions.md
-> work-items.json. Next bounded work is completing P1-01 and reviewing the
canonical model contracts for P2-03. Do not run real processors or add solvers.
No external issues, automation or independent reviewer is claimed. This
documentation branch proposes carrying the workbench mapping onto main.

## Broader reference mapping

The supplied workbench v0.11 is mapped in ../requirements/workbench-alignment.md
with source sections and a SHA-256 fingerprint. WB-MAP-01 was merged into the phase-1 branch after PR #2 had merged into main;
this branch carries it onto main. Three design
items and four deferred extensions are tracked separately; phase-1 behavior and
its existing evidence are unchanged. DEC-008 remains open for concrete contract
adoption. WB-DES-01 has a separate proposed contract document alongside current
P1-01/P2-03 planning, with no new implementation claimed.

## Contract proposal after mapping

Draft PR #4 targets main to land the workbench mapping. A subsequent design
proposal for WB-DES-01 is in ../design/workbench-contract-boundaries.md. It
illustrates identity/revision/context/extension records, separates graph kinds
and cycle policies, and names effects on DEC-002/003/008. It is not an adopted
schema or tested implementation. Review the branch dependency and examples
before taking P2-03/P2-01 implementation work; WB-DES-02 remains the next
fixture-design task.
