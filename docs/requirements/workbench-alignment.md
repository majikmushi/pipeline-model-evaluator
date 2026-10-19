# Workbench requirements alignment

Mapping revision: 1, 2026-10-20 (Australia/Perth).
Scope: pipeline-model-evaluator; a selected component of a potential broader
workbench. This mapping is authorized by the user's request to use the supplied
document as a broader reference and map applicable requirements/backlog items.
Requirements below are proposed for evaluator adoption, not implemented behavior.

## Source and provenance

- Title: Meta-Machine Modeling and Workbench Requirements.
- Document version/date: 0.11 / 2026-10-16; status: evolving pre-implementation
  requirements and design inventory.
- Supplied filename: meta-machine-workbench-requirements (1).md.
- SHA-256 of supplied bytes:
  `3ca7c337d5bda91a9476b25a62f04a403ce70fa3fbbe8cd7d74706cd3cbd01de`.
- Section references below refer to that version. This mapping paraphrases the
  selected requirements; it does not redistribute the full source document.
- The recovered evaluator plan remains the phase 1–3 delivery baseline. This
  source provides broader context and proposed additions, not an automatic
  replacement or an instruction to implement the entire workbench.

The source's references to standards, protocols and toolkit candidates are
reported as source proposals. This mapping does not verify conformance or choose
a GUI, database, solver, protocol version or backend.

## Evaluator applicability and traceability

| ID | Source sections | Evaluator requirement | Existing links | Acceptance evidence | Work item |
| --- | --- | --- | --- | --- | --- |
| WB-001 | 4, 13.1, 13.4 | Distinguish stable identity from revision; evaluations identify exact model/source revisions and evaluator configuration | MOD-001, REP-001 | Two revisions of one model preserve identity; an earlier result still identifies its original inputs after later edits | WB-DES-01 |
| WB-002 | 2, 7, 9, 13.5 | Separate declarations, observations, inferred claims, abstract feasibility and concrete provider availability | RES-001, RES-002, SEL-001 | A compositionally valid model with an unavailable provider produces separate feasibility and availability conclusions, with evidence and uncertainty | WB-DES-02 |
| WB-003 | 6, 13.6, 24.3 | Preserve source meaning separately from contextual interpretation; identity does not depend on labels | MOD-001, MOD-002 | Two contextual interpretations share a source identity without overwriting it; equal labels do not merge distinct IDs | WB-DES-01 |
| WB-004 | 6, 9, 28.4 | Distinguish semantic relationships, connectors, provider dependencies and derivation graphs; apply graph-specific cycle rules | MOD-003, CMP-003 | Valid semantic cycle and invalid provider-initialization cycle receive different findings; multi-participant relationships retain roles | WB-DES-01 |
| WB-005 | 13.4, 13.6, 28.6 | Findings retain criteria, source/rule references, input identity and derivation; reruns do not rewrite earlier evidence | RES-001, REP-002 | A finding can be traced to inputs, rule and assumptions; changed-rule rerun has a separate result identity | WB-DES-02 |
| WB-006 | 12, 13.3, 13.6 | Preserve unsupported source/extension content with vocabulary/version provenance, while reporting unsupported semantics explicitly | SRC-003, MOD-001 | Unknown extension survives a supported representation round trip and is not reported as semantically validated | WB-DES-01 |
| WB-007 | 8 | Preservation results name information property, layer, context/task, criterion, evaluator and evidence | RES-001 | Structural preservation and semantic preservation can have different or unknown results without collapsing to one lossy flag | WB-EXT-01 |
| WB-008 | 28.1–28.4, 28.8 | Define module purpose, owned state, invariants, interfaces, errors, exclusions and test obligations; keep core independent of GUI/storage/providers | QUA-001, QUA-002 | Module concern contracts and dependency-direction checks; core test fixture runs without live providers or GUI/database | WB-DES-03 |
| WB-009 | 28.5, 29.1 | Distinguish retained intermediate data from a durable resumable checkpoint; declare versions and compatibility for restore | SRC-003 | Future checkpoint restores compatible inputs or reports incompatibility without changing meaning | WB-EXT-02 |
| WB-010 | 28.6, 30 | Keep diagnostic logs, evaluation evidence and project history distinct, with correlation references | REP-002, QUA-002 | A run failure can be correlated to a stage while diagnostic retention does not erase required evaluation evidence | WB-DES-03 |
| WB-011 | 16, 16.1 | Scope implementation baselines and trace subsequent requirement changes | PRE-003 | Baseline revision/scope, proposed change, impact and acceptance evidence are recorded without rewriting historical records | WB-MAP-01 |
| WB-012 | 28.6, 34 | Use small fixtures for observable contracts, including explanations, assumptions and alternatives | QUA-002, CMP-002, RES-001 | Known inputs yield expected outputs/evidence; tests cover uncertainty and alternatives without requiring the full workbench | WB-DES-02 |
| WB-013 | 32–33 | Future adapters use shared application contracts with explicit scope, revisions, effects and errors | SEL-001, REP-002 | Selected adapter passes shared contract tests and rejects stale revisions; supported subset is documented | WB-EXT-03 |
| WB-014 | 34, 34.1 | Preserve impact analysis, scenario comparison, dependency-health and experiment-notebook ideas without treating them as release commitments | PRE-003 | Captured idea has source, purpose, open questions and explicit promotion decision before implementation | WB-EXT-04 |

## Current implementation evidence and gaps

At phase-1 PR #2 head cc5df032059f45c0a519e5a937a38d8056cac1ab:

- ID/alias and source-span checks partially support WB-003/005, but there are no
  immutable revision records, run identities or contextual semantic mappings.
- Extra YAML fields are retained, partially supporting WB-006. Intake neither
  validates extension vocabulary/version nor guarantees serialized round trips.
- Retained documents/indexes/definitions support inspection only. There is no
  durable checkpoint, restoration API, backup or runtime resumption (WB-009).
- Existing tests cover intake and references. They do not verify graph-specific
  cycles, provider availability, preservation assessments or canonical semantics.
- Deterministic ordering and source evidence do not establish general
  reproducibility or operational behavior.

These are gaps to plan, not grounds to mark existing scoped intake work failed or
to claim that future semantics are already implemented.

## Explicit scope dispositions

| Source area | Disposition for evaluator |
| --- | --- |
| Definition/evidence/context foundations, sections 2–10 and 13 | Select applicable contracts above; full workbench schema is not required |
| KerML/SysML, sections 3 and 24 | Future interchange research; preserve external IDs if introduced; no conformance claim |
| GUI, editors, notation, labels and toolkit candidates, sections 11, 18–21, 25 | Outside current evaluator delivery; possible client of headless services |
| SQLite, editing history, backups and settings, sections 13, 26, 29 | Full storage/UI lifecycle deferred; revision/provenance contracts remain relevant |
| Simulation/runtime debugger, sections 22 and 31 | Deferred; design-time feasibility does not imply execution semantics |
| External tools/LSP/MCP, sections 32–33 | Deferred adapters; future interfaces should share application contracts |
| Resource objectives and optimization, sections 10 and 34 | Explicit future input; no hidden score or optimization requirement |
| Impact analysis, scenario comparison, notebook and other ideas, section 34 | Captured ideas; prioritization and release commitment remain open |

## Change-control proposal CR-WB-001

Use v0.11 as a reference input for WB-001–014. Preserve the merged evaluator plan
and PR #2 intake contract as their own scoped historical baselines. Review the
new requirements and concrete design effects before implementation; do not
retroactively rename past work as compliant with all workbench requirements.

Impact: primarily canonical model (P2-03), graph contracts (P2-01/P2-02), result
provenance/classification (P3-06) and verification (QA-01). No runtime/schema or
dependency changes are made by this mapping. Exact revision/run formats and
graph taxonomy remain DEC-008; accepted details should update the relevant
contracts, requirement versions and fixture expectations together.

See [workbench backlog](../planning/workbench-backlog.md) and the authoritative
[work register](../tracking/work-items.json).
