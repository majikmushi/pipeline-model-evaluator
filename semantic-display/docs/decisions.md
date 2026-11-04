---
id: SD-DECISIONS
title: Semantic Display — decisions and open questions
status: proposed
version: 0.1.0
updated: 2026-11-05
---

# Design Decisions

These are the working design directions inferred from the project discussion. They are not evidence of implemented behavior.

| ID | Decision | Rationale | Status |
| --- | --- | --- | --- |
| SD-ADR-001 | Use Python 3.12+ initially | Rapid iteration and evaluator ecosystem | Proposed |
| SD-ADR-002 | Use PySide6/Qt 6 first; keep GTK replaceable | Mature desktop canvas and workspace primitives | Proposed |
| SD-ADR-003 | One canonical semantic graph | Prevent contradictory copies across views | Proposed |
| SD-ADR-004 | Use stable opaque IDs for all model objects | Rename/layout independence and traceability | Proposed |
| SD-ADR-005 | Keep presentation state separate | Same object can appear in several layouts | Proposed |
| SD-ADR-006 | All semantic edits go through ModelController | Uniform validation, undo, LLM access | Proposed |
| SD-ADR-007 | Start with binary connections with IDs | Fast MVP, future n-ary migration path | Proposed |
| SD-ADR-008 | Use SQLite first | Local transactional persistence | Proposed |
| SD-ADR-009 | Use a small trusted semantic bootstrap | Self-describing metamodel without infinite regress | Proposed |
| SD-ADR-010 | MCP proposals require explicit approval | Prevent unreviewed LLM changes | Proposed |
| SD-ADR-011 | Keep evaluator a separate bounded context | Avoid UI dependencies and premature coupling | Proposed |
| SD-ADR-012 | Maintain independent subproject packaging | Avoid modifying evaluator runtime dependencies | Proposed |

## Open decisions

| ID | Question | Default for first implementation |
| --- | --- | --- |
| SD-OPEN-001 | Is the first release desktop-only? | Yes; local single-user Qt application |
| SD-OPEN-002 | How are graph elements stored in SQLite? | Shared elements registry + typed tables |
| SD-OPEN-003 | Should relation roles be generalized immediately? | No; preserve IDs and migrate after MVP |
| SD-OPEN-004 | What does graph composition mean? | Defer semantics; implement membership only |
| SD-OPEN-005 | Should model types be enforced before editor MVP? | No; structural integrity first |
| SD-OPEN-006 | How much UML/SysML fidelity is required? | No formal conformance claim initially |
| SD-OPEN-007 | How is MCP connected to desktop app? | Evaluate local process/IPC when M7 begins |
| SD-OPEN-008 | What is the evaluator interchange schema? | Define at M8 with actual evaluator contracts |
| SD-OPEN-009 | Should workbench and evaluator share a Python distribution? | No initially; explicit integration boundary |

## Revision protocol

When a decision is accepted, update its status, date, impact on contracts, implementation plan and tests. Do not silently change the interpretation of an existing predicate or persisted model version.
