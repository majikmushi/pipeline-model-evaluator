# Proposed evaluation acceptance scenarios

Status: WB-DES-02 design proposal, 2026-10-20. These examples define expected
distinctions for P3-06 and QA-01 review. They do not select a public result wire
format, numerical score, provider registry or executable inference algorithm.
DEC-004 and DEC-008 remain open. The [contract boundary proposal](workbench-contract-boundaries.md)
supplies illustrative identity, revision and graph-kind vocabulary.

## Claims that an evaluation must keep separate

| Claim | Evidence needed | A claim cannot be inferred from |
| --- | --- | --- |
| Structural validity | Resolved definitions, typed relationships and applicable contract checks | A well-formed Markdown/YAML block alone |
| Abstract feasibility | Explicit starting inventory, processor prerequisites, compatible artifacts/capabilities and accepted assumptions | A simple path or an output declaration alone |
| Provider availability | An inventory entry for a provider or input in the selected context, with its source and status | An abstractly feasible composition |
| Operational demonstration | Run or observation evidence tied to a particular implementation and context | A declaration, simulation or design-time proof |

An evaluation may establish one claim and leave another unresolved or false.
`proven` means proven only within the validated model, selected rules and
accepted assumptions. `conditional` names a missing assumption or contract;
`unresolved` names missing knowledge. Contradictions and invalid compositions
need separate findings rather than being folded into uncertainty. Severity is
independent of epistemic class. The exact field names/encoding remain DEC-004.

## Minimal fixture vocabulary

Each scenario specifies a frozen model/source snapshot, target, inventory,
policy, rule revisions and expected evidence chain. The following shorthand is
for review, not a parser input. `A + B -> C` means one processor needs both A
and B; `A | B -> C` means distinct alternative providers. An inventory item is
an asserted availability input, with provenance, not an artifact definition.

| ID | Inputs and trigger | Expected result and evidence | Coverage |
| --- | --- | --- | --- |
| F-01: abstractly valid, provider status split | Snapshot S1 declares `P: A -> T` with compatible types and no contradictions; target T. Inventory has A. Variant a has no P status and incomplete inventory; variant b explicitly marks P unavailable with source evidence. | Structural composition can be valid. Abstract feasibility is proven within S1 if P is treated as a declared processor. Concrete provider availability is unresolved in a and unavailable in b; operational demonstration is unproven in both. Cite P's definition revision, A inventory assertion, P status evidence when present and policy. Do not report T as operationally ready. | WB-002, RES-001/002, SEL-001 |
| F-02: conjunction and alternatives | S1 has `P1: A + B -> T`, `P2: C -> T`; inventory has A and C but lacks B. | P1 remains blocked by B; P2 is a viable conceptual alternative. A result for T retains both branches and the complete prerequisite set of P1. If P2's provider is unavailable, concrete availability remains separate from its conceptual path. Cite each processor revision and every inventory input used. | CMP-001/002, WB-002/012 |
| F-03: unknown contract and assumption | S1 has `P: A -> T` with an unsupported constraint X; inventory has A; an assumption Y is proposed but not accepted. | Do not call T proven. Return unresolved for X and conditional only for the branch that explicitly depends on Y, with separate references to X's source span and Y's status. A policy disabling X must be recorded as a different policy revision, not silently change this result. | RES-001/002, WB-005/012, EVA-001 |
| F-04: contradictory declarations | S1 declares P both compatible and incompatible with required artifact schema revision R under the same selected rule; target T depends on P. | Flag the contradiction/invalid composition explicitly. Do not convert it into a clean `unresolved` or choose one declaration by ordering. Cite both conflicting source locations and the compatibility rule. | RES-001, REP-002, WB-005 |
| F-05: bootstrap and external seed | S1 has `P: A -> B` and `Q: B -> A`. Run 1 inventory is empty; run 2 inventory explicitly includes A; target B. | Run 1 has no self-justifying proof of B. Run 2 may derive B from the external A seed if P's remaining contracts pass. Preserve distinct run and inventory identities; cite the seed and derivation. | CMP-003, WB-004/005 |
| F-06: rerun provenance | Re-evaluate F-02 after changing P2's rule or inventory status; source snapshot S1 stays fixed. | New run identity and changed rule/inventory reference. Earlier finding still points to the original input set and derivation. Ordering is deterministic for a fixed snapshot/policy/inventory. | WB-001/005, EVA-003, REP-002 |

For F-01, “unavailable” is supported by the explicit negative assertion in
variant b. Mere absence of an entry in variant a means unknown availability.
The inventory completeness contract must be selected before an exact executable
oracle is frozen.

## Proposed result envelope for fixture review

```yaml
run_id: run-f02-a
source_snapshot_id: S1
target_id: T
inventory_revision: inv-f02-a
policy_revision: policy-1
evaluator_version: proposed
claims:
  - {kind: abstract_feasibility, class: proven, via: P2}
  - {kind: provider_availability, class: unresolved, via: P2}
alternatives:
  - {provider: P1, prerequisite_set: [A, B], blocked_by: [B]}
  - {provider: P2, prerequisite_set: [C], supported_by: [C]}
derivation_refs: [source-P1-r1, source-P2-r1, inventory-C-r1, rule-compat-r1]
```

This is an example of information to preserve, not a committed JSON/YAML
schema. A real finding must point to exact definition/source revisions, selected
rules, assumptions and the derivation edges that justify it. A finding should
not imply that all alternative branches passed merely because one did.

## Verification handoff

QA-01 can turn these into executable fixtures after DEC-002/003/004/008 settle
canonical records and result encoding. Each fixture should assert the separate
claim classes, branch prerequisites, source/rule/inventory links and stable
ordering, not just a Boolean reachability result. P3-06 owns the combined result
contract; P3-03/04/05 own the inference behavior. Phase-1 `inspect_sources` has
no target inventory or evaluation API, so none of these cases is a passing
runtime test today.

Open choices for adoption: inventory completeness and negative assertions;
whether policy-disabled rules produce a finding; exact distinction between
conditional and unresolved for unsupported constraints; result identity and
serialization; and how provider availability evidence is acquired. No live
provider query or operational execution is required by this proposal.
