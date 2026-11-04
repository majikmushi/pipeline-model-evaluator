---
id: SD-VERIFY
title: Semantic Display — verification strategy
status: proposed
version: 0.1.0
updated: 2026-11-05
---

# Verification Strategy

## 1. Test levels

| Level | Tool | Scope |
| --- | --- | --- |
| Unit | pytest | Core graph, semantic resolver, projection selection |
| Repository | pytest + temporary SQLite | Integrity, rollback, save/load, migrations |
| GUI | pytest-qt | Canvas rendering, commands, pane state |
| Integration | pytest + test MCP client | Proposal validation and approval boundary |
| Contract | pytest | Evaluator snapshot/finding schema compatibility |

Tests should use deterministic IDs and small model fixtures. Headless Qt CI may use an offscreen platform where supported; an actual interactive smoke test is still required before claiming UX readiness.

## 2. Acceptance scenarios

| ID | Milestone | Test | Expected result |
| --- | --- | --- | --- |
| V-01 | M1 | Create Computer, CPU and RAM | Three retrievable stable IDs |
| V-02 | M1 | Create two contains connections | Two distinct connection IDs and correct endpoints |
| V-03 | M1 | Reuse an existing ID | Duplicate rejected; original unchanged |
| V-04 | M1 | Connect to missing endpoint | Rejected; no dangling connection |
| V-05 | M1 | Add same node to two graphs | Both memberships valid; no duplicate node |
| V-06 | M2 | Fail second operation in a transaction | Entire transaction rolled back; no event emitted |
| V-07 | M2 | Save/reload graph | IDs, relationships and memberships preserved |
| V-08 | M2 | Commit with stale revision | Conflict; model unchanged |
| V-09 | M3 | Drag node on canvas | Only view position changes |
| V-10 | M4 | Create and connect via UI | Controller and repository reflect edits |
| V-11 | M4 | Undo then redo an edit | Model restored correctly |
| V-12 | M5 | Open two different projections | Both map to same canonical IDs |
| V-13 | M5 | Rename shared node in pane A | Pane B updates if in scope |
| V-14 | M5 | Move node in pane A | Pane B position unchanged |
| V-15 | M5 | Save/reload workspace | Split layout and representation choices preserved |
| V-16 | M6 | Define Sensor subtype of Component | Resolver recognizes new type without code change |
| V-17 | M6 | Introduce invalid subtype cycle | Deterministic diagnostic, no infinite recursion |
| V-18 | M7 | Reject LLM proposal | No canonical model change |
| V-19 | M7 | Approve valid LLM proposal | Exactly one atomic commit |
| V-20 | M7 | Approve stale proposal | Conflict and revalidation required |
| V-21 | M8 | Return evaluator finding | Correct semantic ID overlay and classification |
| V-22 | M8 | Unsupported evaluator rule | Explicit unresolved/unsupported, not a false proof |

## 3. Gate policy

A milestone is complete only if its tests pass, its public interfaces are documented, and its demo can be reproduced. A planned feature is not marked implemented merely because the design describes it.

## 4. Quality risks to test early

- Node deletion with incoming/outgoing references.
- Mixed node/connection membership in graphs.
- Event publication after failed transactions.
- Qt UI thread access from background workers.
- Multiple pane refresh without recursive edit loops.
- User-created type definitions with missing references.
- LLM proposals that reference stale or unauthorized IDs.
- Persistence migration across schema versions.
