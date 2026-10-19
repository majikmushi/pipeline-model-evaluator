# Verification strategy

## Preparation evidence

At initial scaffold commit d230af169888f481822da81cd17638e5ba8e88fe:
Python 3.14.8; locked dependency sync passed; package/Pydantic/NetworkX imports
passed; wheel and source archive build passed. Pytest collected zero tests and
returned 5. This is not a passing behavioral suite. Python 3.12 is unverified.

Planning follow-up: validate documentation relative links, JSON structure,
unique work IDs, dependency references, requirement references and acyclic work
dependencies before publishing. Record actual results in the work log.

## Future acceptance checks

| Requirement IDs | Check scope |
| --- | --- |
| MOD-001, MOD-003 | Accepted/rejected fixtures, unsupported versions, explicit unknown-field policy |
| MOD-002 | Duplicates, missing endpoints and locations |
| EVA-001 | Enabled/disabled rule selection and policy errors |
| EVA-002, QUA-001 | Graph fidelity, no input mutation, domain-only public API |
| EVA-003 | Repeated runs and equivalent reordered inputs |
| REP-001 | Golden JSON, schema version, canonical identities and serialization round-trip |
| REP-002 | Invalid input vs findings vs internal error behavior |
| SEC-001 | Hostile strings remain data, no execution/network behavior |
| QUA-002 | Every adopted requirement mapped to meaningful executed cases |

Run locked installation and package build alongside adopted behavioral checks.
Test declared supported Python versions before compatibility claims.
Introduce CI only with agreed supported-version and repository workflow policy.
Do not add tests that merely reproduce implementation or always pass.
