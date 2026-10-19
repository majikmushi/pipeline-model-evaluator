# Proposed revision, context, extension and graph contracts

Status: core identity/context/extension and graph-kind boundaries accepted for
DEC-002/003 by the user on 2026-10-20. The examples remain illustrative input
to unresolved wire details and DEC-008; they are not an implemented API. The
phase-1 `inspect_sources` format remains the current executable intake boundary.

## Contract boundaries

| Concept | Proposed invariant | Why it matters |
| --- | --- | --- |
| Definition identity | A stable, opaque ID denotes a definition within a model namespace; display name and source line are attributes, never identity | Renaming or moving text must not merge distinct definitions |
| Definition revision | An immutable revision identifies one normalized definition payload plus its source reference; a new payload has a new revision | Old evaluation evidence remains traceable after edits |
| Source snapshot | A collection of selected document revisions and intake-format version identifies the exact source set used for a build | A run can be repeated against the same input set |
| Contextual interpretation | A context ID and interpretation revision link to a definition ID/revision; they do not replace the source definition | One source can have different meanings in different contexts |
| Evaluation run | A run ID links the model snapshot, policy revision, target, inventory and evaluator version | Later changes cannot silently rewrite earlier conclusions |
| Extension | Retain raw extension data with vocabulary ID/version and source span; unsupported semantics remain explicitly unvalidated | Unknown fields can be preserved without claiming their meaning |

The existing phase-1 `model_id`, `kind`, `id` and aliases establish intake names,
but do not yet provide content-addressed revisions, immutable storage, contextual
interpretations or run identity. Revision identifiers could be hashes or assigned
IDs; that choice is open. Any hash scheme would need canonicalization rules for
mapping order, scalar types and normalization before use as a public contract.
The proposal below uses illustrative IDs, not mandated serialization.

## Worked identity and context example

```yaml
source_snapshot:
  snapshot_id: snap-17
  intake_format_version: 1
  documents:
    - path: model.md
      content_revision: doc-r4
definition:
  model_id: example-pipeline
  id: P01
  kind: processor
  revision: def-r2
  source: {document_revision: doc-r4, lines: [12, 18]}
  display_name: Segmenter
interpretations:
  - {context_id: batch, revision: ctx-r1, definition_id: P01,
     definition_revision: def-r2, role: offline-transform}
  - {context_id: interactive, revision: ctx-r3, definition_id: P01,
     definition_revision: def-r2, role: interactive-service}
```

An edit to P01 creates `def-r3` while retaining P01 as its identity. A previous
result that cites `def-r2` and `snap-17` still denotes its original input. The
two interpretations may coexist without mutating `def-r2`. Two distinct IDs
with the display name “Segmenter” remain distinct. A missing or conflicting
context binding is an explicit unresolved/invalid finding, not a first-match
selection. How aliases survive renames or namespace changes remains DEC-002.

## Extension preservation example

```yaml
extension:
  owner_definition_id: P01
  vocabulary: example.vendor/resource-profile
  vocabulary_version: "2"
  source: {document_revision: doc-r4, lines: [16, 18]}
  payload: {accelerator: optional, vendor_mode: fast}
  semantic_status: unsupported
```

The payload is data to retain, not a rule to evaluate. A supported representation
round trip should reproduce the vocabulary/version and payload without dropping
unknown keys; byte-for-byte YAML spelling is not guaranteed. If an adapter
cannot preserve it, it reports loss before writing. `semantic_status` is not a
validation success flag. The current intake library preserves extra parsed YAML
fields only; it does not implement this extension envelope or round-trip API.

## Graph kinds and cycle policy

| Graph kind | Nodes and relationship representation | Cycle rule |
| --- | --- | --- |
| Semantic relationship | Definition IDs; relationship record has its own ID, type and named participant roles (two or more) | Cycles may be meaningful; validate roles/type, not acyclicity |
| Connector | Port/interface endpoints plus direction and compatibility facts | A cycle is not automatically invalid; check the selected connector semantics |
| Provider dependency | Required artifact/capability and candidate provider records; conjunctive prerequisites stay grouped, alternatives stay separate | Reject a feasibility proof that depends solely on itself; seek an external seed/bootstrap path |
| Derivation/provenance | Finding/result nodes linked to input revisions, rules and assumptions | A proof derivation must be acyclic and trace to base evidence |
| Runtime interaction | Execution instances and events, if later selected | Outside the current design-time evaluator scope |

For example, a semantic relation `mutually-refines(A, B)` may form a valid
cycle. A provider chain `A requires B; B requires A` cannot establish either
output from an empty inventory. If B is explicitly available in the selected
inventory, a separate, evidence-linked feasibility conclusion may be possible.
The graph adapter must keep a three-participant relation such as
`transfer(source=A, artifact=X, destination=B)` as one relationship with roles;
projecting it to pairwise edges must not discard the original record.

These are distinct typed projections from canonical records, not a requirement
to use one mutable graph object as the domain model. A NetworkX adapter may
implement graph checks, but public records and result evidence must remain
independent of NetworkX objects.

## Accepted direction and remaining work

- **DEC-002 / P2-03:** define identity namespace, revision creation, source
  snapshot, context binding, extension envelope and conversion from phase-1
  envelopes. Decide whether revisions are hashes or assigned IDs and specify
  compatibility/version migration before freezing a wire format.
- **DEC-003 / P2-01–02:** define typed relationship records and graph projections;
  retain n-ary roles and full AND/OR prerequisites; give provider and derivation
  graphs different cycle checks. No blanket DAG rule should apply to semantic
  relationships or connectors.
- **DEC-008 / P3-06:** carry snapshot, policy, inventory, target and evaluator
  identities into findings/results. WB-DES-02 will supply expected result
  classes and concrete fixtures before any runtime adoption.

Reviewable acceptance examples: (1) P01 is revised without changing its stable
identity or an earlier result's cited revision; (2) batch and interactive
contexts bind the same definition differently; (3) equal labels do not merge
IDs; (4) an unknown extension survives a supported representation round trip
and remains unvalidated; (5) a semantic cycle is allowed while an unseeded
provider cycle is not proof; (6) a three-role relation preserves every role.
These are design expectations, not passing executable tests.
