# Recommended phase-2/3 decisions with an evolution path

Status: recommendation for review, 2026-10-20. The user accepted the core
DEC-002/003 direction; the choices below fill in remaining details and propose
DEC-004/008 policy. They are **not adopted decisions or implemented behavior**.
“Reengineering” here means evolving source formats, model semantics and storage
without silently changing the meaning of earlier evaluations.

## Why this fit

The evaluator currently has a small, working `inspect_sources` API that reads
explicit Markdown/YAML and retains source-linked diagnostics. It has no
canonical model, graph adapter, evaluation result or persistence layer. The
broader workbench v0.11 reference (sections 4, 13 and 16) calls for stable
identity, pinned revisions, append-only results and derived graph views. The
evaluator can honor those boundaries with in-memory records and versioned
manifests first; it does not need to adopt the workbench database or GUI.

| Choice | Recommend | Why this fits better than the main alternative |
| --- | --- | --- |
| Stable identity | `(model_id, id)` is the canonical key; `kind` cannot change under that key. Display names and file locations are attributes. | Using labels/paths as identity would make renames and file moves change meaning. Random IDs would require an allocator absent from the current source workflow. |
| Alias and reengineering | Aliases resolve input references only and never become stored identity. Changing an ID creates a new identity with an explicit `supersedes` link; old snapshots retain the old key. | Silently rewriting an old ID would invalidate historical references. |
| Source revision | A version-tagged SHA-256 digest of the selected definition block's UTF-8 content after newline normalization, combined with its canonical key and kind. This is a **source revision**, not a claim that semantically equivalent YAML hashes alike. | An assigned revision counter needs mutable coordination; semantic YAML canonicalization would be fragile before the domain schema is fixed. Harmless formatting changes may create a new source revision, which is safe over-versioning. |
| Source snapshot | A sorted manifest of caller-supplied logical source keys, document digests and intake-format version; fingerprint the manifest. Keep physical path/line spans as provenance, not as the snapshot's identity. Reject duplicate logical keys. | Absolute paths vary by machine. A manifest permits replay and comparison while preserving source navigation. |
| Canonical snapshot | Versioned Pydantic domain records built from a pinned source snapshot. Record canonical schema and builder version, selected definition revisions and context revisions; fingerprint this manifest separately from source revision. | A source edit and a changed interpretation rule have different causes and should not share one revision field. |
| Unknown extensions | Retain vocabulary ID/version, source span and original definition block; expose parsed JSON-compatible data only when lossless. Mark semantics unsupported until an adapter claims support. | Dropping extra fields loses source meaning; treating arbitrary parsed YAML as validated or deeply immutable is false for the current intake records. |
| Storage | Keep phase-2 records in memory and emit a versioned manifest/result artifact when selected. Add a store port later; SQLite remains an adapter choice for a real persistence need. | A database now would couple the canonical schema to untested editing and migration behavior. |

The fingerprint is an integrity and reproducibility key, not a security claim.
Specify an algorithm tag such as `source-block-v1:sha256:…` in persisted
references. Do not hash a Python object representation, absolute path or mutable
`model_extra` dictionary. The canonical builder must copy or freeze accepted
values before promising immutable revisions. Serialize the snapshot manifest
as UTF-8 JSON with sorted object keys and source entries sorted by logical key;
reject non-JSON values there. This rule applies to the manifest, not arbitrary
YAML extension data.

## DEC-002: proposed record boundary

```text
DefinitionKey(model_id, id) + immutable kind
SourceRef(logical_source_key, document_digest, line_span)
DefinitionRevision(key, source_block_digest, source_ref)
SourceSnapshot(intake_format_version, sorted source manifest)
CanonicalSnapshot(schema_version, builder_version, source_snapshot,
                  sorted definition revisions, context revisions)
Extension(vocabulary, version, raw_payload, source_ref, semantic_status)
```

`inspect_sources` remains the phase-1 facade. A new builder converts its
envelopes into a separate canonical result with accepted records, rejected
records and diagnostics. `schema_version: 1` in Markdown frontmatter is the
intake version; it must not be mistaken for the canonical schema version.
Context bindings refer to a definition key **and exact revision**, so changing
the source does not silently update a prior interpretation. Initial canonical
records can be Python/Pydantic types; a public JSON wire format should be
versioned only when a real consumer is selected.

## DEC-003: proposed graph and compatibility contract

Keep first-class typed relationship records as canonical data, with relationship
identity/revision and role-labeled participants. Derive disposable graph views:
semantic relationships, connectors, provider dependencies and derivations. An
internal NetworkX `MultiDiGraph` may use a relationship node to retain n-ary
roles, but public queries return domain records. A processor's required inputs
and capabilities remain one conjunctive requirement set; separate providers
remain alternatives, even if graph edges are used for indexing.

For v1, require exact artifact-type identity **and schema revision** and exact
capability identity. An explicit, validated processor/adapter may transform
between different types. Do not infer subtype, version-range or unit conversion
from similar labels. Missing schema information is unresolved; an explicit
mismatch is incompatible. This conservative rule can later be widened by a
versioned compatibility rule without rewriting earlier findings.

Semantic cycles are allowed when the relationship type permits them. Connector
cycles require connector-specific checks. Provider cycles cannot derive an
output from themselves: seed evaluation from explicit inventory or an
independent provider and run a deterministic fixed point. A strongly connected
component locates a candidate cycle; it is not a blanket rejection. Proof
derivations remain acyclic and cite the external seed/path. Keep graph query
methods narrow (`providers_for`, `requirements_for`, `relationships_for`) so a
future graph-library change does not change the domain API.

## DEC-004: proposed result and inventory contract

Use a run-scoped immutable result with a random `run_id` for distinct runs and
a separate deterministic `input_fingerprint` for comparing identical pinned
inputs. Pin source/canonical snapshots, target, inventory revision, context,
policy/rule versions and evaluator version. Store findings and derivations in
stable order, independent of run ID.

Each finding has a claim kind (structural validity, abstract feasibility,
provider availability or operational evidence), epistemic class (`proven`,
`conditional`, `unresolved`), separate severity, and evidence/rule/assumption
references. Contradictions and invalid compositions are explicit finding kinds;
they are not a fourth epistemic success class. Expected bad input yields
diagnostics or findings; unexpected bugs use a distinct internal-failure
container. A projection error cannot mutate the completed evaluation result.

Inventory is **open-world by default**. An absent provider entry means unknown,
not unavailable. Only an explicit negative assertion with context, provenance
and revision may support “unavailable” in v1. A disabled rule is recorded in the
pinned policy and contributes no conclusion; if it blocks a needed conclusion,
that claim is unresolved rather than silently proven. An unsupported constraint
is unresolved. An unaccepted assumption makes only its dependent branch
conditional. These choices give F-01–F-06 in
[evaluation scenarios](evaluation-scenarios.md) concrete expected outcomes.

## DEC-008: proposed scope disposition

Adopt WB-001–006, WB-008, WB-010 and WB-012 as **contract and verification
constraints** for phases 2–3, staged with the owning modules. This does not
commit to a full workbench service, storage system or runtime evidence source.
Keep WB-007, WB-009, WB-013 and WB-014 deferred as the existing mapping says.
WB-011 continues through the existing change-control record. Promote an item
only with a selected task, fixture and affected baseline; do not infer release
scope from the source document's imperative language.

For example, renaming P01's display label leaves `(model_id, P01)` intact but
creates a new source-block revision. An earlier run keeps its old snapshot and
rule version. If a later rule version permits a previously incompatible
artifact conversion, it produces a new finding in a new run; it does not edit
the earlier finding. A graph projection can be rebuilt for either pinned
snapshot without becoming a second source of truth.

## Reengineering sequence and decision gates

1. **Freeze the intake seam:** keep the merged phase-1 syntax and tests. Add
   representative P1-01 source fixtures with logical source keys, inventory,
   target and expected F-01–F-06 outcomes before changing the parser.
2. **Add a conversion boundary:** build canonical v1 records from `IntakeResult`
   in P2-03. Preserve the original source block, extra data and diagnostics;
   report every conversion loss or unsupported field explicitly.
3. **Derive and compare:** build graph projections from the canonical snapshot
   in P2-01/02. Test n-ary roles, AND/OR groups, exact-match compatibility and
   seeded versus unseeded cycles without exposing NetworkX objects.
4. **Pin runs:** implement P3 inference/results against immutable snapshot,
   inventory and policy references. Keep an old run readable when source,
   builder or rules change; a rerun gets a new run ID.
5. **Evolve by adapters:** when a canonical schema changes, add an explicit
   versioned converter and fixture showing old input, new output and any loss.
   Preserve old manifest/result artifacts. Introduce durable storage only when
   restoration, editing or cross-run queries require it.

Before moving DEC-002/003 details to resolved, review the logical source-key
rule, digest algorithm/version, exact-match compatibility and graph query
fixtures. Before resolving DEC-004/008, review F-01–F-06 expected result
envelopes and the proposed active/deferred requirement split. No option above
is authorized for runtime implementation merely by appearing in this document.
