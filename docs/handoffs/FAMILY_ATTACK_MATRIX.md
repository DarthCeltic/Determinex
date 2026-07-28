# 31-Family Native-Support — Attack Matrix (the compounding plan)

> Goal: ledger `native_support_verified_families` = 31/31, every family ≥3 REAL external
> upstream repos, each passing the mechanical loop: clone@commit → install → baseline-green →
> seed-defect → DETECT(exit≠0) → repair(git checkout) → REVERIFY-green. No fake green.
> Runner: `scripts/hetzner_family_loop.py`. Evidence builder: `scripts/build_family_locks.py`.

## Why this compounds (the math)

Every family proof is the **same loop** on 3 repos. The runner automates the loop. The only
per-repo intellectual work is **(1) install+test command** and **(2) a seed anchor**. Both
collapse to ~zero once you have:

1. **Toolchain pattern per ecosystem** — 8 needed, **8 already PROVEN** (the 7 locked language
   families + php at 2/3). No new toolchain research for python/node/ruby/go/rust/java/c++/php.
2. **Seed pattern per ecosystem** — known (see cookbook below). Repo-find time → ~0.
3. **A repo of the right shape** — *the pool already exists*:
   - **63 PB-locked tools** (rust/go/c/c++ CLI) — real, already building + tested.
   - **89 SWE-bench repos on T:** (`T:/determinex-datasets/swe-bench/determinex-swebench{,-full,-ml}`).
   - Well-known libs for the long tail.

So the cost is NOT `23 families × 3 repos × 3 scout-rounds = 207 rounds`. It is:
`1× cookbook + 1× repo→family manifest + N batched runner jobs (9 repos/job, 8 cores) × 2 boxes`.
Claude + Codex run jobs on two boxes in parallel ⇒ ~2× throughput, ~halved wall-clock.

**The single biggest lever: ~16 of the 23 remaining families are SHAPE/DOMAIN families that
reuse the 8 proven ecosystems.** They are repo-MAPPING, not toolchain work. A "cli_script" repo
is just a CLI tool in a proven ecosystem; "data_science_notebooks" is a python repo; etc.

## Seed cookbook (apply, don't re-derive)

| Ecosystem | install | test | reliable seed |
|-----------|---------|------|---------------|
| python | `pip install -e . pytest` | `python -m pytest <file> -q` | flip a default-arg (`=True`→`=False`) / module constant / operator in a tested pure fn |
| node | `npm install --no-audit --no-fund` | `npx mocha/jest/vitest <file>` | flip an operator/default in one tested source fn |
| ruby | `bundle config set --local path vendor/bundle; bundle install` | `bundle exec rake test` / rspec | flip a constant/operator |
| go | `go mod download` | `go test ./<pkg>` | flip operator/return value |
| rust | (cargo fetches) | `cargo test -q` | flip an operator |
| java | (maven) | `mvn -q test` | flip operator/constant; seed = parse-number style |
| c/c++ | `cmake -B build; cmake --build build` | `ctest --test-dir build` | flip operator |
| php | `composer install` | `vendor/bin/phpunit` | flip a constant/operator |

Runner phase = install+test in ONE container (env doesn't cross `docker run`). Detect = exit code.

## State

- **LOCKED 7/31** (pushed, behavioral seeds): rust, go, python, node_typescript, ruby, java, c_cpp.
- **#8 launching**: package_library_projects (ramda + inflection + python-slugify).

## Lane split — by ECOSYSTEM, so the two lanes never touch the same repos

### Claude lane (python / node / frontend — the fast path) ~11
| Family | Ecosystem | Repo source |
|--------|-----------|-------------|
| package_library_projects ✅#8 | node+py | ramda / inflection / python-slugify |
| data_science_notebooks | python | pandas-adjacent pure-py libs (e.g. tabulate, more-itertools, patsy) |
| ml_inference | python | host-testable ML libs (tokenizers-py, sentencepiece-py, tiktoken, safetensors) |
| local_api_services | py/node | flask-restful / fastapi-users / express-validator apps |
| testing_qa_projects | py/node | pytest-plugins (pytest-mock, freezegun) / jest matchers |
| static_web_docs | py/node | mkdocs-material / docusaurus-plugin / pelican |
| react_vite_apps | node | vite-plugin / a vitest-tested react lib |
| agent_workflow_automation | python | prefect-task libs / celery-adjacent / langchain-core helpers |
| browser_extensions | node/TS | webextension-polyfill / a jest-tested extension lib |
| tauri_electron_desktop | node | electron-store / electron-builder helper (host-testable) |
| sqlite_local_db | python | sqlite-utils / dataset / aiosqlite |

### Codex lane (systems / JVM / heavy — Codex owns PB + its own box) ~12
| Family | Ecosystem | Repo source |
|--------|-----------|-------------|
| cli_script_projects | rust/go | **3 REAL-upstream PB locks** (NOT ripgrep=golden): zoxide / hyperfine / gping — already build! near-free |
| security_audit_compliance | rust/go | PB locks: ripsecrets / deadnix / shellharden — already build |
| sqlite via go | go | PB locks: dsq / trdsql / parqeye (SQL-on-data) — coordinate w/ Claude's sqlite lane |
| php_projects (3rd row) | php | one clean php:8.3 repo (php-cs-fixer+carbon already 2/3) |
| devops_ci_projects | go/py | terraform-provider w/ `go test` / ansible-module w/ pytest |
| iac_config_projects | go/py | cdktf libs / pulumi providers (host-testable) |
| multi_service_local_apps | py/go | a compose repo w/ a service + unit tests |
| enterprise_integration | java | apache-camel component / spring-integration module (mvn test) |
| embedded_hardware_routes | c/c++ | host-testable firmware libs (TinyUSB host tests, an embedded HAL w/ native unit tests) |
| dotnet_projects | .NET | Newtonsoft.Json ✅ + Polly + FluentValidation (single-target net8.0; avoid multi-target) |
| kotlin_projects | JVM | gradle:jdk21 — kotlinx libs (kotlinx-datetime, kotlinx-serialization) |
| swift_projects | swift | swift:5.10 Linux image — swift-argument-parser / swift-algorithms (`swift test`) |
| unknown_novel_intake | any | any 3 novel repos not used elsewhere (catch-all) |

## Honesty invariants (unchanged)
- Each row REAL_UPSTREAM (integrity gate `lock_integrity_audit_001.py`); no golden-embedding reimpls.
- Distinct repos per family (no double-count appearance vs language families).
- Evidence via `build_family_locks.py` only — real verbatim summary + parsed count; NEVER fabricate per-test rows.
- `release_supported_families` stays 0; this ledger is `native_support_verified_families` (lower, derived bar).
