---
name: swebench-cli__cli
description: SWE-bench repo behavioral spec for cli/cli. Aggregated from 397 bug-fix instances across 1 dataset(s). Inject into builder prompt for SWE-bench tasks targeting this repo.
type: swebench-repo-spec
---

# cli/cli — SWE-bench Repo Spec

> **397 bug-fix instances** across 1 dataset(s); language(s): go.

## Section 1 — Dataset coverage

| Dataset | Instances |
|---------|-----------|
| multi-swe-bench | 397 |

## Section 2 — Where bugs typically live (top files touched in fixes)

| File | Times touched |
|------|---------------|
| `pkg/cmd/pr/create/create.go` | 27 |
| `api/queries_pr.go` | 22 |
| `command/pr.go` | 22 |
| `pkg/cmd/pr/merge/merge.go` | 20 |
| `api/queries_repo.go` | 18 |
| `pkg/cmd/repo/create/create.go` | 17 |
| `pkg/cmd/repo/fork/fork.go` | 16 |
| `pkg/cmd/pr/checks/checks.go` | 16 |
| `pkg/cmd/extension/command.go` | 16 |
| `pkg/cmd/issue/create/create.go` | 16 |
| `pkg/cmd/release/create/create.go` | 16 |
| `command/issue.go` | 16 |
| `pkg/cmd/api/api.go` | 15 |
| `pkg/cmd/run/shared/shared.go` | 15 |
| `api/queries_issue.go` | 15 |
| `go.mod` | 14 |
| `api/query_builder.go` | 13 |
| `pkg/cmd/auth/login/login.go` | 13 |
| `pkg/cmd/pr/view/view.go` | 13 |
| `pkg/cmd/browse/browse.go` | 13 |
| `go.sum` | 12 |
| `pkg/cmd/gist/edit/edit.go` | 11 |
| `pkg/cmd/root/root.go` | 11 |
| `pkg/cmd/pr/list/list.go` | 11 |
| `cmd/gh/main.go` | 11 |
| `pkg/cmd/pr/status/status.go` | 10 |
| `pkg/cmd/auth/status/status.go` | 10 |
| `pkg/cmd/run/list/list.go` | 10 |
| `pkg/cmd/secret/list/list.go` | 10 |
| `pkg/cmd/issue/view/view.go` | 10 |

## Section 3 — Test framework signal

Detected: **unknown — sample names: **

Sample FAIL_TO_PASS test names (first 10):
```
```

## Section 4 — Problem-theme distribution

Top themes across 397 issue statements (auto-clustered):

| Theme | Count | % |
|-------|-------|---|

## Section 5 — Sample issues (no patches — those are the answer)

## Section 6 — Builder guidance

When building a fix for an instance in cli/cli:

1. **Read the problem statement carefully** — the issue text describes the bug and often hints at root cause.
2. **Likely files**: see §2 above. pkg/cmd/pr/create/create.go appears in most fixes.
3. **Run the FAIL_TO_PASS tests** to see the failure first (`pytest <test_name> -v`).
4. **Inspect surrounding code** at the file paths from §2 — common bug locations.
5. **Match the theme** (§4) to known repo patterns: regression vs edge case vs API change.
6. **Generate minimal patch** — SWE-bench scoring rewards smallest viable fix.
7. **Verify PASS_TO_PASS still pass** — don't break existing functionality.

## Section 7 — Index of all instances in this repo

All 397 instance_ids live in `c:/tmp/swebench_instance_index.jsonl` (filterable by `repo == "cli/cli"`).

First 20 instance_ids:

- `cli__cli-10388` (dataset: `multi-swe-bench`)
- `cli__cli-10364` (dataset: `multi-swe-bench`)
- `cli__cli-10363` (dataset: `multi-swe-bench`)
- `cli__cli-10362` (dataset: `multi-swe-bench`)
- `cli__cli-10354` (dataset: `multi-swe-bench`)
- `cli__cli-10329` (dataset: `multi-swe-bench`)
- `cli__cli-10239` (dataset: `multi-swe-bench`)
- `cli__cli-10180` (dataset: `multi-swe-bench`)
- `cli__cli-10158` (dataset: `multi-swe-bench`)
- `cli__cli-10154` (dataset: `multi-swe-bench`)
- `cli__cli-10139` (dataset: `multi-swe-bench`)
- `cli__cli-10124` (dataset: `multi-swe-bench`)
- `cli__cli-10078` (dataset: `multi-swe-bench`)
- `cli__cli-10074` (dataset: `multi-swe-bench`)
- `cli__cli-10072` (dataset: `multi-swe-bench`)
- `cli__cli-10048` (dataset: `multi-swe-bench`)
- `cli__cli-10043` (dataset: `multi-swe-bench`)
- `cli__cli-10016` (dataset: `multi-swe-bench`)
- `cli__cli-10009` (dataset: `multi-swe-bench`)
- `cli__cli-9983` (dataset: `multi-swe-bench`)
- ... (377 more)

---

*Determinex · Lunarian Data Systems · auto-generated from SWE-bench-family datasets*

---

## Section 8 — Anchor-grade hand-curated reference (top-3 by instance count, 397 instances, Go)

### Repo overview
GitHub's official `gh` CLI. Single Go binary built on `cobra` (subcommand framework) + `httpClient`
for GitHub API calls. Heavy use of `oauth2`, table rendering, JSON output flags.

### High-leverage bug zones

| Subsystem | Touch count | Common bug pattern |
|-----------|------------|--------------------|
| `pkg/cmd/pr/create/create.go` | 27 | PR creation flow; auto-detection of base branch |
| `api/queries_pr.go` | 22 | GraphQL query field selection; pagination |
| `command/pr.go` | 22 | Legacy command dispatch (pre-pkg/cmd refactor) |
| `pkg/cmd/issue/list/list.go` | ~15 | Issue filtering + listing |
| `pkg/cmd/repo/clone/clone.go` | ~12 | Repo URL parsing; SSH vs HTTPS |
| `pkg/iostreams/iostreams.go` | ~10 | stdin/stdout discipline; color detection |

### Test framework
**Go's built-in `testing` package** + `testify` for assertions. FAIL_TO_PASS names look like:
`TestPRCreate_setsCorrectBranch` or `pkg/cmd/pr/create.TestRun`.

### Builder rules specific to gh CLI

1. **Cobra command structure**: each subcommand is `pkg/cmd/<verb>/<noun>/<verb_noun>.go` with `NewCmd<X>` constructor.
2. **`iostreams.IOStreams`**: ALL output through `io.Out`, `io.ErrOut` — never `fmt.Print*` directly.
3. **GraphQL queries**: in `api/queries_*.go`. Adding a field requires updating both the query string AND the response struct.
4. **Mocking**: tests use `httpmock` for API responses. New API call paths need a mock fixture.
5. **`--json FIELDS`** flag: each command supports JSON output via `pkg/cmdutil/json_flags.go`.
6. **Auto-detection**: many commands auto-detect repo from cwd via `git remote`. Tests stub this with `httpClient.Repo(...)`.
7. **Color**: `cs := iostreams.ColorScheme()` — never hardcode ANSI codes.

### Where 90→100% lives

- `Test*PR*` → `pkg/cmd/pr/` — base branch detection, draft PR semantics
- `Test*Issue*` → `pkg/cmd/issue/` — labels, milestones, assignees
- `Test*Repo*` → `pkg/cmd/repo/` — clone protocol, fork detection
- `Test*Auth*` → `pkg/cmd/auth/` — token refresh, scope validation
- `Test*Workflow*` → `pkg/cmd/workflow/run/` — workflow_dispatch input parsing

### Estimated lock cost per instance
~5-12 min on Sonnet; ~15-30 min on local Qwen 14b. Most fixes are 5-30 line targeted patches.
