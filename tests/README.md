# Contract tests

No behavioral tests exist yet because domain contracts have not been approved.
Add accepted/rejected model fixtures in phase 1, graph-check cases in phase 2,
and report serialization/invocation cases in phase 3. A pytest exit code of 5
currently means no tests were collected; do not report it as a passing suite.
