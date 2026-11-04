---
id: SD-REQ
title: Semantic Display — requirements
status: proposed
version: 0.1.0
updated: 2026-11-05
---

# Requirements

## 1. Purpose and scope

Build a desktop environment for designing concepts and systems interactively. The initial product is a graph editor, not a full SysML/UML implementation, runtime telemetry tool, or autonomous design agent. Formal semantics and evaluation are added incrementally.

Priority: **P0** required for the initial MVP; **P1** next functional release; **P2** later extension.

## 2. Functional requirements

| ID | Priority | Requirement | Acceptance evidence |
| --- | --- | --- | --- |
| SD-FR-001 | P0 | Create, rename and delete nodes with stable IDs | UI operation and core test |
| SD-FR-002 | P0 | Create and delete directed, named connections with stable IDs | Core and UI tests |
| SD-FR-003 | P0 | Reject duplicate IDs and dangling connection references | Negative core tests |
| SD-FR-004 | P0 | Create graphs and assign graph membership | Core tests |
| SD-FR-005 | P0 | Display nodes and connections in an interactive Qt canvas | GUI smoke test |
| SD-FR-006 | P0 | Select, drag, zoom, pan and edit model objects | GUI interaction test |
| SD-FR-007 | P0 | Save/reload semantic model and view positions independently | Round-trip test |
| SD-FR-008 | P0 | Route all semantic edits through a framework-independent controller | Unit and integration tests |
| SD-FR-009 | P1 | Split canvas recursively and choose a representation per pane | Workspace test |
| SD-FR-010 | P1 | Show at least structural, dependency and semantic projections | Projection tests |
| SD-FR-011 | P1 | Synchronize model changes across affected panes; optionally link selection | Cross-pane test |
| SD-FR-012 | P1 | Persist and restore pane layouts, filters and view state | Workspace round-trip |
| SD-FR-013 | P1 | Define user-created types and predicates as graph objects | Create Sensor type without code change |
| SD-FR-014 | P1 | Resolve instance-of and subtype-of semantics with explicit bootstrap rules | Resolver tests |
| SD-FR-015 | P1 | Validate model edits and expose structured diagnostics | Invalid command rejected |
| SD-FR-016 | P2 | Expose read-only model context through MCP | Connected client test |
| SD-FR-017 | P2 | Preview, validate and explicitly approve LLM-proposed changes | Approval-gated test |
| SD-FR-018 | P2 | Display evaluator findings as view overlays | Adapter integration test |
| SD-FR-019 | P2 | Support graph-to-graph references and composition semantics | Composition tests |
| SD-FR-020 | P2 | Support generalized n-ary relations with participant roles | Hyper-relation test |

## 3. Nonfunctional requirements

| ID | Requirement |
| --- | --- |
| SD-NFR-001 | Semantic core must not import Qt or GUI classes. |
| SD-NFR-002 | IDs must not change when names, layouts or representations change. |
| SD-NFR-003 | Committed changes must be atomic; failed changes leave no partial state. |
| SD-NFR-004 | Model events are emitted only after successful commit. |
| SD-NFR-005 | Presentation changes must not trigger semantic evaluation. |
| SD-NFR-006 | Saved data must include a schema version and support migration. |
| SD-NFR-007 | Unrecognized semantic definitions must remain unresolved, not silently treated as valid or false. |
| SD-NFR-008 | LLM input/output is untrusted; tools must enforce scope and approval. |
| SD-NFR-009 | UI must remain responsive while layout or evaluation runs; background results must be marshalled to the Qt UI thread. |
| SD-NFR-010 | A single process and single writer are sufficient for MVP; concurrent collaborative editing is out of scope. |

## 4. User workflows

### WF-01: Create a system
Create graph ComputerSystem → add Computer, CPU and RAM → connect Computer to CPU and RAM using contains → save → reopen → inspect unchanged IDs and relationships.

### WF-02: Compare representations
Open Structural and Dependency panes → select CPU in one → optionally highlight CPU in the other → edit CPU name → both panes update if CPU is in their scope.

### WF-03: Extend vocabulary
Create a Type definition Sensor → declare Sensor a subtype of Component → create a sensor instance → resolver recognizes the new type without a new Python class.

### WF-04: LLM-assisted design (later)
Select subsystem → request decomposition → LLM returns candidate operations → validate → show diff/preview → user approves → commit → refresh projections. Rejecting the candidate changes nothing.

## 5. Explicit exclusions from MVP

Full SysML v2 compliance; complete UML notation coverage; collaborative network editing; runtime execution visualization; graph database; arbitrary executable user rules; automated architecture synthesis; inference-based correctness claims; and unrestricted LLM write access.

## 6. Traceability

Requirements map to implementation milestones in [Delivery plan](implementation-plan.md) and executable scenarios in [Verification](verification.md). A design document is not evidence that a requirement has been implemented.
