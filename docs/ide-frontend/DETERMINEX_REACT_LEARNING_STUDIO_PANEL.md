# React Learning Studio Panel

> Locked under
> `locks/sentinel/DETERMINEX_REACT_LEARNING_STUDIO_PANEL_LOCK_001.json`.

Rung 6. Teaching / explanation panel at
`frontend/src/components/ide-product-shell/LearningStudioPanel.tsx`.

## 9 modes

`explain_this_repo`, `explain_this_file`, `explain_this_error`,
`explain_this_test_failure`, `teach_me_the_concept`,
`compare_possible_fixes`, `walk_me_through_the_patch`,
`show_beginner_vs_professional_version`,
`generate_learning_checklist`.

## Hard rules

- Non-authorizing caption: "Learning explains. Learning does NOT
  approve, apply, or authorize source mutation."
- Route link **"Open in Repo Clinic"** (`data-routes-to="repo_clinic"`)
  for fix suggestions.
- Route link **"Open in Idea Lab"** (`data-routes-to="idea_lab"`)
  for new-project suggestions.
- Teaching window names the blocked gate (approval / verifier /
  snapshot / body hash / symlink refusal).
- Captions: "Learning cannot approve a patch", "Learning cannot
  mark repair success", "Learning cannot mutate source".
- Forbidden phrases blocked: "patch applied", "now fixed",
  "source mutation authorized", "training row written".
