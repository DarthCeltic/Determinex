# Corpus NEEDS — operator action queue (what the system is missing; NOT ceilings)

## Missing tool images (82 of 200 canonical tasks have no local image)
- Docker stores images on **C:** which has only ~74G free; T: has 805G.
- **Pulling overnight (tractable, high-frontier, fits disk):** calculator, blake3, htmlq, sd,
  zoxide, ripsecrets, shellharden, tokei, brotli, pingu — `:task` images (observe + chew).
- **Disk-gated / deferred (need C: headroom OR move Docker storage to T:):** the rest of the 82.
- **Mega / infeasible-from-scratch (skip for resolve; partials only):** ffmpeg, php-src, gromacs,
  gdal, duckdb, samtools, bedtools2, sox, typst, tree-sitter, quickjs, pandoc, proj, lazygit.
- ACTION on wake (or auto next wave): free C: or repoint Docker data-root to T: to pull the full
  tractable set; then `determinex_pb_overnight.py --retry-needs` picks them up (resumable).

## Live failure NEEDS (appended by the campaign as it runs)

## [UPDATE 01:13] Missing images are AUTH/ACCESS-gated, not just disk
- `docker pull programbench/<tool>:task` → **"pull access denied / repository does not exist
  or may require 'docker login'"**. The 82 missing images are NOT publicly pullable as-is.
- The 118 present images were obtained somehow (prior `docker login` to the programbench
  registry? built locally? HF dataset?). **OPERATOR NEED:** how were the 118 acquired —
  `docker login` creds, or a build/sync script? With that, `--retry-needs` + a pull of the
  tractable missing set (blake3/htmlq/sd/zoxide/ripsecrets/shellharden/tokei/brotli/pingu) runs.
- `testorg__calculator.abc1234` is a TEST placeholder (not a real published task).
- Until then the overnight march chews the **118 present tools** (more than enough for the night).
- [03:32] **gron** needs `budget`: exceeded per-tool time budget (raise budget / split decompose) (retry after provisioning — NOT a ceiling)
- [03:32] **csview** needs `image`: task image missing (retry after provisioning — NOT a ceiling)
- [04:07] **elfcat** needs `budget`: exceeded per-tool time budget (raise budget / split decompose) (retry after provisioning — NOT a ceiling)
- [04:15] **hck** needs `more-chew`: low local score -> needs more corpus chew / oracle growth (NOT a ceiling) (retry after provisioning — NOT a ceiling)
- [04:57] **loop** needs `budget`: exceeded per-tool time budget (raise budget / split decompose) (retry after provisioning — NOT a ceiling)
- [05:12] **go-mod-outdated** needs `more-chew`: low local score -> needs more corpus chew / oracle growth (NOT a ceiling) (retry after provisioning — NOT a ceiling)
- [05:34] **cmatrix** needs `more-chew`: low local score -> needs more corpus chew / oracle growth (NOT a ceiling) (retry after provisioning — NOT a ceiling)
- [05:56] **pastel** needs `more-chew`: low local score -> needs more corpus chew / oracle growth (NOT a ceiling) (retry after provisioning — NOT a ceiling)
[06:01] WAVE 2 (corrected): right languages + monolithic native + enforced timeout
- [06:26] **gron** needs `budget`: exceeded per-tool time budget (raise budget / split decompose) (retry after provisioning — NOT a ceiling)
- [06:26] **csview** needs `image`: task image missing (retry after provisioning — NOT a ceiling)
- [06:51] **hck** needs `more-chew`: low local score -> needs more corpus chew / oracle growth (NOT a ceiling) (retry after provisioning — NOT a ceiling)
- [07:17] **loop** needs `budget`: exceeded per-tool time budget (raise budget / split decompose) (retry after provisioning — NOT a ceiling)
- [07:29] **go-mod-outdated** needs `more-chew`: low local score -> needs more corpus chew / oracle growth (NOT a ceiling) (retry after provisioning — NOT a ceiling)
- [07:54] **cmatrix** needs `budget`: exceeded per-tool time budget (raise budget / split decompose) (retry after provisioning — NOT a ceiling)
- [08:19] **pastel** needs `budget`: exceeded per-tool time budget (raise budget / split decompose) (retry after provisioning — NOT a ceiling)
- [08:44] **hexyl** needs `budget`: exceeded per-tool time budget (raise budget / split decompose) (retry after provisioning — NOT a ceiling)
- [09:09] **hyperfine** needs `budget`: exceeded per-tool time budget (raise budget / split decompose) (retry after provisioning — NOT a ceiling)
- [09:34] **grex** needs `budget`: exceeded per-tool time budget (raise budget / split decompose) (retry after provisioning — NOT a ceiling)
[09:54] WAVE 3 (official): 13 cleanroom tools, native, chat-only, monolithic k=4/r=1, fuzz=12, 30min cap
- [09:54] **csview** needs `image`: task image missing (retry after provisioning — NOT a ceiling)
[09:58] WAVE 3b: _image_for now falls back to cleanroom_v6 -> all 13 cleanroom tools observe+official
[10:36] WAVE 4: leak-fixed observe (docker rm -f on timeout). elfcat proved pipeline=55/564 official; text tools should score, binary/domain tools need domain-input oracles (NEXT BUILD)
- [10:56] **csview** needs `more-chew`: low local score -> needs more corpus chew / oracle growth (NOT a ceiling) (retry after provisioning — NOT a ceiling)
[11:07] WAVE 5 (release march): ALL fixes — harvest domain-inputs + case-memory poison-gate + leak-fix + correct lang. Cleanroom-first, autonomous, full march.
- [11:21] **csview** needs `more-chew`: low local score -> needs more corpus chew / oracle growth (NOT a ceiling) (retry after provisioning — NOT a ceiling)
- [11:33] **elfcat** needs `more-chew`: low local score -> needs more corpus chew / oracle growth (NOT a ceiling) (retry after provisioning — NOT a ceiling)
[11:48] WAVE 6: CRITICAL -i stdin fix (faithful stdin oracles) + harvest + sandbox + poison-gate + 3 levers (k6/r2, fuzz24, chat->reasoner escalation). Cleanroom-first.
- [12:00] **csview** needs `more-chew`: low local score -> needs more corpus chew / oracle growth (NOT a ceiling) (retry after provisioning — NOT a ceiling)
