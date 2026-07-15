# Learning Studio Workflow

> Locked under `locks/sentinel/DETERMINEX_LEARNING_STUDIO_WORKFLOW_LOCK_001.json`.

The teaching/explanation surface. Non-authorizing by construction.

## 9 modes

`explain_this_repo`, `explain_this_file`, `explain_this_error`,
`explain_this_test_failure`, `teach_me_the_concept`,
`compare_possible_fixes`, `walk_me_through_the_patch`,
`show_beginner_vs_professional_version`,
`generate_learning_checklist`.

## Hard rules

| Rule | Refusal |
|---|---|
| `claims_repair_success` | `BLOCKED_FALSE_SUCCESS` |
| `claims_authorized_apply` | `BLOCKED_FALSE_SUCCESS` |
| Forbidden phrase in text ("patch applied", "now fixed", "source mutation authorized", "approved", "training row written") | `BLOCKED_FALSE_SUCCESS` |
| `suggests_fix=True` without `routes_to="repo_clinic"` | `BLOCKED_MUTATION_CONFUSION` |
| `suggests_new_project=True` without `routes_to="idea_lab"` | `BLOCKED_MUTATION_CONFUSION` |
| Unknown mode | `BLOCKED_MUTATION_CONFUSION` |

Learning **explains**. It does not authorize, approve, or apply.
Suggestions route to the appropriate gated workflow.
