---
id: SD-ARCH
title: Semantic Display — architecture
status: proposed
version: 0.1.0
updated: 2026-11-05
---

# Architecture

## 1. System boundary

Semantic Display is a Python desktop subproject inside the pipeline-model-evaluator repository. It owns the modelling workbench. The existing evaluator remains a separate bounded context and may later be called through an adapter.

~~~text
+--------------------------------------------------------------+
| Qt Workbench                                                  |
| Model explorer | Properties | Split Canvas | Future LLM chat  |
+---------------------------+----------------------------------+
                            |
                            v
+--------------------------------------------------------------+
| Workspace + Model Controller                                 |
| commands | selection | change routing | candidate previews   |
+-------------+---------------------------+--------------------+
              |                           |
              v                           v
+--------------------------+  +-------------------------------+
| Semantic Model Services  |  | View Projection Engine        |
| types | predicates       |  | representation | layout       |
| definitions | validation |  | diagram-to-model ID mapping   |
+-------------+------------+  +-------------------------------+
              |
              v
+--------------------------------------------------------------+
| Graph Kernel + Repository                                    |
| identities | nodes | connections | graphs | atomic updates   |
+---------------------------+----------------------------------+
                            |
                            v
                       SQLite files

External LLM client -- MCP adapter --> Model Controller
Pipeline evaluator <--- evaluation adapter ---> Model Controller
~~~

## 2. Data ownership

| Information | Owner | Examples |
| --- | --- | --- |
| Canonical model | Graph repository | Nodes, relations, definitions, graph membership |
| Semantic interpretation | Semantic services | Type resolution, predicate compatibility |
| Editing workflow | Model controller | Commands, transactions, undo/redo |
| View projection | Projection engine | Visible nodes/edges, semantic ID mapping |
| View state | Workspace repository | Pane layout, zoom, node positions, filters |
| Graphics | Qt scene | Rendered shapes, handles, edge paths |
| Evaluation findings | Evaluator/adapter | Diagnostics, assumptions, evidence |
| Candidate proposals | Proposal store/controller | Uncommitted LLM or user changes |

A canvas item never becomes the source of truth for a semantic object.

## 3. Model, projection and presentation

Three distinct objects are required:

1. **Canonical model:** what exists and how objects are related.
2. **Diagram projection:** which canonical objects and relations appear in a particular representation, and how they map to diagram elements.
3. **Presentation state:** where diagram elements appear, styling, zoom and pane layout.

A projection may omit elements or derive diagram annotations, but must not silently mutate the canonical model. A model operation must be explicit.

## 4. Change propagation

~~~text
UI edit / LLM-approved operation
  → ModelCommand
  → validate structure and policy
  → repository transaction
  → committed ChangeSet(model_revision, affected_ids)
  → event dispatcher
  → affected projection rebuild/delta
  → affected Qt scene update
  → optional asynchronous evaluation
  → findings overlay refresh
~~~

A node drag changes only presentation state. Renaming a node changes the canonical model and can affect several panes.

## 5. Pane architecture

The workspace is a recursive split tree. Internal nodes specify horizontal/vertical split and proportions. Leaf nodes hold a tab group or a representation pane.

Each pane owns a ViewDefinition: representation ID, source graph, root/focus, filters, depth, overlay flags, layout strategy and independent navigation state. The same canonical element can be visible in several panes.

Start with QSplitter and QTabWidget. Detachable docking and more advanced layouts are later enhancements.

## 6. Representation strategy

Use a registry of projection providers. Initial providers:

- **Structural:** selected nodes and containment-like explicit relationships.
- **Dependency:** explicit prerequisite/dependency relationships.
- **Semantic:** types, predicates, instance-of and subtype-of definitions.

Do not claim UML or SysML conformance merely because a diagram resembles a notation. Add notation-specific mappings and validation only when implemented.

## 7. Subproject dependency direction

~~~text
semantic-display GUI → application controller → core/repository
semantic-display projections → core query interfaces
semantic-display MCP adapter → application controller
semantic-display evaluator adapter → public evaluator contracts
pipeline-model-evaluator core -X→ semantic-display GUI
~~~

The parent evaluator must not depend on Qt or this workbench's presentation classes. Avoid circular imports between projects.

## 8. Planned development boundaries

MVP: single-process, local SQLite, one writer, simple scene refresh, explicit predicates and binary connections.

Later: semantic interpreter, incremental projections, generalized relations, graph composition, external LLM agents, solver adapters and evidence overlays.

See [LLD](lld.md) for contracts and [Delivery plan](implementation-plan.md) for order.
