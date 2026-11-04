---
id: SD-PLAN
title: Semantic Display — implementation plan
status: proposed
version: 0.1.0
updated: 2026-11-05
---

# Implementation Plan

## 1. Build strategy

Use vertical slices. Each milestone must run and pass tests before the next begins. Do not scaffold the full target package with empty files.

The parent repository already has a Python evaluator package. Keep this subproject independently installable when implementation begins; do not change the parent evaluator's dependencies or lockfile just to add Qt.

## 2. Proposed source layout (introduced incrementally)

~~~text
semantic-display/
├── README.md
├── docs/
│   ├── requirements.md
│   ├── architecture.md
│   ├── lld.md
│   ├── implementation-plan.md
│   ├── verification.md
│   └── decisions.md
├── pyproject.toml                    # add in M1
├── src/semantic_display/
│   ├── __init__.py
│   ├── core/
│   │   ├── records.py
│   │   ├── graph.py
│   │   └── errors.py
│   ├── application/
│   │   ├── commands.py
│   │   ├── controller.py
│   │   └── events.py
│   ├── persistence/
│   │   └── sqlite_repository.py
│   ├── projections/
│   │   ├── contracts.py
│   │   └── providers.py
│   ├── semantics/
│   │   ├── bootstrap.py
│   │   └── resolver.py
│   ├── gui/
│   │   ├── main_window.py
│   │   ├── canvas.py
│   │   └── workspace.py
│   └── integrations/
│       ├── mcp.py
│       └── evaluator.py
└── tests/
    ├── test_graph.py
    ├── test_controller.py
    ├── test_sqlite.py
    ├── test_projections.py
    ├── test_semantics.py
    └── test_gui.py
~~~

Only create modules when their milestone requires them.

## 3. Milestones

| Milestone | Deliverable | Acceptance gate |
| --- | --- | --- |
| M0 | Design documentation and scope | Documents reviewed; no code claimed |
| M1 | Python graph core | Nodes, connections, graphs, integrity tests pass |
| M2 | Commands and SQLite persistence | Atomic edits and save/load round-trip |
| M3 | Qt viewer | Graph renders; pan/zoom/drag works |
| M4 | Interactive editor | Create/connect/edit/delete through UI |
| M5 | Split views and projections | Two panes, independent representations, synchronized model |
| M6 | Graph-defined semantics | Create Sensor type without Python source change |
| M7 | MCP/LLM proposals | Read model, preview proposal, approve/deny |
| M8 | Evaluator adapter | Findings mapped to model IDs and shown as overlays |

### M1 — Graph core (first implementation task)

1. Add semantic-display/pyproject.toml with Python >=3.12, a src-layout package and pytest dev dependency. Qt is not required yet.
2. Create core/records.py: immutable Node, Connection, Graph records with stable IDs.
3. Create core/graph.py: create/get/list/update/delete and membership operations.
4. Create core/errors.py: duplicate ID and invalid reference exceptions.
5. Create tests/test_graph.py: construction, duplicate rejection, missing endpoints, deletion policy, graph membership.
6. Add a tiny example in a test: Computer contains CPU and RAM.
7. Run tests from the subproject directory; commit only when green.

**Done when:** no GUI dependency is needed to construct and inspect the example graph.

### M2 — Model controller and persistence

1. Add typed command records and ModelController.
2. Implement one-command atomic commit, revision increment and post-commit event.
3. Create SQLite schema with a shared elements registry (or equivalent rigorously tested reference enforcement).
4. Implement save/load of nodes, connections and graph membership.
5. Add tests for rollback, stale revision, deletion, persistence and restart.
6. Add separate tables for view state when needed in M3.

**Done when:** the same IDs and relations survive restart; failed edits change nothing.

### M3 — Qt graph viewer

1. Add PySide6 and pytest-qt to the subproject dependency set and regenerate its own lockfile.
2. Create MainWindow, CanvasView, CanvasScene, NodeItem and EdgeItem.
3. Render a saved graph using canonical IDs.
4. Add selection, zoom, pan and drag.
5. Persist dragged positions separately from semantic data.
6. Add a GUI smoke test.

**Done when:** Computer/CPU/RAM can be displayed and repositioned without changing semantic relations.

### M4 — Interactive editing

1. Add create-node action and property editor.
2. Add connection-creation gesture and predicate selection.
3. Add rename/delete actions.
4. Route all edits through ModelController.
5. Implement undo/redo and visible validation errors.
6. Test create → save → restart → edit → save.

**Done when:** a user can build and save the example without modifying Python source.

### M5 — Multiple representations

1. Define DiagramModel and ViewDefinition.
2. Add Structural and Dependency projection providers; add Semantic provider once definitions exist.
3. Add QSplitter and representation dropdown per pane.
4. Keep each pane's zoom, filters and positions independent.
5. Add model revision change events and cross-pane refresh.
6. Save/restore split tree and view configuration.

**Done when:** editing a shared element in pane A updates its representation in pane B without copying canonical data.

### M6 — Self-describing semantics

1. Add trusted bootstrap definitions: Type, Predicate, instance_of, subtype_of.
2. Store user type and predicate definitions as ordinary graph elements.
3. Add semantic resolver with cycle detection and explicit unresolved result.
4. Add type/predicate selectors to property editor.
5. Add tests creating Sensor subtype of Component without new Python classes.

**Done when:** new modelling vocabulary is authored as model data.

### M7 — LLM via MCP

1. Expose scoped read-only inspect/search tools.
2. Add candidate change set creation and structural validation.
3. Show candidate diff/preview in the UI.
4. Add explicit approval and stale-revision checks.
5. Add integration tests for rejected/approved proposals and unauthorized operations.

**Done when:** LLM cannot silently commit edits and approved proposals update the graph.

### M8 — Evaluation

1. Define public snapshot and finding contracts.
2. Implement evaluator adapter to pipeline-model-evaluator.
3. Distinguish unsupported, unresolved and invalid outcomes.
4. Map findings to canonical IDs and draw overlays.
5. Add deterministic scenario tests.

**Done when:** a relevant evaluator finding is visible in a pane and traceable to a model element.

## 4. Execution rules

- No Qt imports in core, semantics or persistence.
- No model mutation from QGraphicsItem.
- No direct LLM database access.
- One authoritative logical model and versioned storage schema.
- No new dependency unless the milestone uses it.
- Update requirement/test traceability as features are implemented.
- Each milestone ends with a demo and a test gate, not only documentation.

## 5. First work package

**WP-SD-001: Build the Python graph core.**

Inputs: [LLD §2](lld.md), [Requirements](requirements.md).  
Outputs: installable minimal Python subproject, Node/Connection/Graph records, Graph operations, tests.  
Acceptance: [Verification scenarios V-01 through V-05](verification.md).

Do not start with MCP, SysML, an ontology engine or a complex Qt editor. Start with a tested, inspectable graph.
