---
id: SD-README
title: Semantic Display — subproject index
status: proposed
version: 0.1.0
updated: 2026-11-05
---

# Semantic Display

Python-first, Qt-based **interactive semantic modelling workbench** for designing concepts, software architectures, and engineering systems. It is a separate subproject within pipeline-model-evaluator; no application code has been implemented here yet.

## Documentation index

| Document | Purpose |
| --- | --- |
| [Requirements](docs/requirements.md) | Scope, functional requirements and measurable acceptance |
| [Architecture](docs/architecture.md) | Subsystem boundaries and information flow |
| [Low-level design](docs/lld.md) | Data structures, APIs, interactions, storage and semantics |
| [Delivery plan](docs/implementation-plan.md) | File-by-file implementation order and checkpoints |
| [Verification](docs/verification.md) | Test cases and completion gates |
| [Decisions and open questions](docs/decisions.md) | Adopted design direction and unresolved choices |

## What we are building

An interactive canvas where the user can create and connect concepts, systems and components; split the workspace into independently configurable views; select structural, dependency and semantic representations; and see model changes reflected in every relevant view. Later increments add graph-defined types/predicates, LLM proposals via MCP, and evaluator findings.

**One model; multiple synchronized projections.** Diagram positions and layout are view state, not system semantics.

## Initial technology direction

Python 3.12+, PySide6/Qt 6, QGraphicsScene/QGraphicsView, Python dataclasses, SQLite, pytest/pytest-qt. NetworkX is optional for algorithms; it is not the authoritative store. Layout engines and the MCP SDK are deferred until their milestones.

## Scope and repository boundary

- This directory owns the planned desktop application, model editing operations, view projection and workspace state.
- The parent pipeline-model-evaluator owns document intake, canonical pipeline evaluation, capability/dependency inference and evidence-aware findings.
- Integration will use explicit versioned contracts, not imports of evaluator internals.
- The parent repository's Python package, lockfile, evaluator documentation and tests are unchanged by this documentation scaffold.
- This is a **docs-only starting point**. The implementation plan describes when to add an independent pyproject.toml, source tree and tests.

## First concrete target

Create a small graph (Computer → contains → CPU/RAM), display it in Qt, edit it, save it, reload it and preserve stable identities. Then show it in two split panes using different projections.

**Next action:** implement milestone M1 in [Delivery plan](docs/implementation-plan.md); use [Verification](docs/verification.md) as the acceptance gate.
