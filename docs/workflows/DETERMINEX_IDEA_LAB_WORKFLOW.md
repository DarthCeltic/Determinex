# Idea Lab Workflow

> Locked under `locks/sentinel/DETERMINEX_IDEA_LAB_WORKFLOW_LOCK_001.json`.

New-project creation workflow that does NOT claim support for all
apps or all languages.

## 14 flow steps

1. idea_intake
2. structured_spec
3. beginner_summary
4. support_matrix_check
5. blueprint
6. scaffold_request
7. acceptance_tests
8. implementation_plan
9. build_test_verifier
10. smoke_plan
11. bounded_repair_plan
12. final_report
13. evidence
14. training_remains_blocked

## 11 UI states

`IDEA_CAPTURED`, `SPEC_WRITTEN`, `SUPPORT_CHECK_REQUIRED`,
`UNSUPPORTED_REQUEST`, `BLUEPRINT_READY`, `SCAFFOLD_READY`,
`GENERATED_UNVERIFIED`, `TESTS_PASSED`, `SMOKE_PASSED`,
`VERIFIED_WORKING_LOCAL_APP`, `HONEST_FAILURE`.

## Hard rules

| Rule | Refusal |
|---|---|
| "Build It" disabled until support check passes | `BLOCKED_MISSING_SUPPORT_CHECK` |
| "Working" disabled until build + test + smoke ALL pass | `BLOCKED_FALSE_SUCCESS` |
| Unsupported features must be visible | `BLOCKED_UNSUPPORTED_CLAIM` |
| External setup / cost caveats must be visible | `BLOCKED_UNSUPPORTED_CLAIM` |

`source_mutation_authorized` and `training_eligible` stay False
regardless of state.
