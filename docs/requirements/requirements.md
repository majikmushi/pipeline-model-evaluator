# Requirements and acceptance criteria

Status labels: confirmed = directly requested preparation constraint;
proposed = future product behavior for review. No proposed item is adopted merely
by merging these planning documents. Work items are in ../tracking/work-items.json.

| ID | Status | Requirement | Acceptance evidence | Work |
| --- | --- | --- | --- | --- |
| PRE-001 | confirmed | Use uv with Pydantic, NetworkX, pytest | Locked sync, imports, package build; lock committed | PREP-01 |
| PRE-002 | confirmed | Preserve content and stage through PR | Original README text retained; main unchanged | PREP-01 |
| PRE-003 | confirmed | Document phases, interfaces, requirements, implementation and tracking | Linked docs, work register, checkpoint | PLAN-01 |
| PRE-004 | confirmed | Avoid substantial implementation at preparation stage | Source limited to package docstring; design signatures remain docs | PREP-01 |
| MOD-001 | proposed | Parse a versioned, explicit pipeline model | Accepted fixture validates; malformed and unsupported versions return structured errors | P1-02 |
| MOD-002 | proposed | Enforce unique node IDs and resolvable edge references | Duplicate and missing-reference fixtures yield stable location/code diagnostics | P1-03 |
| MOD-003 | proposed | Define unknown-field and graph-shape policy explicitly | Reviewed decision plus positive/negative fixtures | P1-01 |
| EVA-001 | proposed | Evaluate only checks enabled by explicit policy | Disabled checks absent; enabled checks produce expected results | P2-02 |
| EVA-002 | proposed | Analyze graph without mutating input | Before/after input equality and repeated-run tests | P2-01 |
| EVA-003 | proposed | Report findings in deterministic order | Equivalent input reorderings produce agreed stable ordering | P2-02 |
| REP-001 | proposed | Produce a versioned JSON report with model/policy identity | Validated golden reports and round-trip checks | P3-01 |
| REP-002 | proposed | Separate malformed input, findings, and internal failures | Cases have distinct documented outputs; no false success | P3-02 |
| SEC-001 | proposed | Treat models as data; never execute described code or fetch resources | Code inspection and hostile-string fixtures show no execution/network path | P1-02 |
| QUA-001 | proposed | Keep graph representation internal to analysis | Public APIs use domain models/reports, not mutable NetworkX objects | P2-01 |
| QUA-002 | proposed | Verify each adopted behavior with meaningful cases | Requirement-to-test mapping and recorded check evidence | QA-01 |

## Before adopting product requirements

Provide a representative source model and one expected evaluation report.
Resolve DEC-001 through DEC-004 before implementing affected behavior.
Review feasibility and revise requirements with provenance; retain superseded IDs.

## Non-goals and unresolved limits

No pipeline runtime, arbitrary imports, remote retrieval, numeric quality score,
or GUI. File-size, graph-size, runtime, memory, confidentiality, and supported
platform limits need representative inputs before measurable thresholds are set.
A CLI is conditional on DEC-005, not an existing feature commitment.
