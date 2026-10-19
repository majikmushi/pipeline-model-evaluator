# Decision register

Owner means the project owner. Approval date/evidence is absent until explicitly
recorded. Proposed choices below are discussion inputs, not adopted defaults.

| ID | State | Question / proposed direction | Blocks |
| --- | --- | --- | --- |
| DEC-001 | open | What authoritative model and examples are evaluated? Recover earlier plan or provide examples | P1-01, P1-02 |
| DEC-002 | open | Input encoding, schema version, required fields, ID type, coercion and unknown fields | P1-02 |
| DEC-003 | open | Edge direction, parallel edges, loops, cycles and disconnected components | P1-03, P2-01, P2-02 |
| DEC-004 | open | Rule catalogue, severity, blocking behavior, ordering and report identity | P2-02, P3-01 |
| DEC-005 | open | Library-only or CLI; supported platforms, exit codes and integration needs | P3-02, QA-01 |
| DEC-006 | proposed | Python >=3.12; runtime verification currently only on 3.14.8 | QA-01 |

## Recording an adopted decision

Add date, decision owner, source/PR evidence, alternatives considered, selected
choice, rationale, affected requirement/work IDs, and consequences. Mark old
choices superseded rather than rewriting history. Update contracts, requirements,
and work dependencies in the same change. New plans do not silently resolve
engineering questions.
