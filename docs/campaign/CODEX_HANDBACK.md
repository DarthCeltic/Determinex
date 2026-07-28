# CODEX HANDBACK LOG
# Append-only. Codex writes here; Claude reads during Section 4 cycle.
# Format per entry:
#   ## Handback: BATCH_ID | YYYY-MM-DD
#   - slug: <tool>
#   - verdict: lock | partial | suspected-ceiling | parity-pending-reference-diff | park
#   - eval_report_path: <absolute path on this machine>
#   - senses_report_path: <absolute path to senses_report.json>
#   - score: <passed>/<total> (<not_run> not_run, <skipped> skipped, <failed> failed)
#   - notes: <free text — root cause, what was tried, what remains>
#   - change_requests: <if any shared-infra changes needed, diff + affected-tool list>

<!-- No entries yet — campaign bootstrap complete 2026-06-10 -->

## Handback: CODEX-001 | 2026-06-11
- slug: fzf
- verdict: partial
- eval_report_path: C:\Dev\Determinex\corpus\programbench\locked\fzf\eval_report.json
- senses_report_path: C:\Dev\Determinex\corpus\programbench\locked\fzf\senses_report.json
- score: 1797/2761 (961 not_run, 3 skipped, 0 failed)
- hashes: eval_report.json sha256=4444E66EE3ED6626845B47E7E97B510B4E814CA208BBCC998264A7B445B7C29D; senses_report.json sha256=C4A28495AF7BD72B7B9FC000207EE832245B4474B7D80B3924D50D5827317277; submission.tar.gz sha256=9731004140774CB9BA7E43BAB106FB34902D0F2E4218EC0FBE9687AC6F7AF849; source/compile.sh sha256=ECBDD2BB911D344A227A933F69940757B1D3E604CFBDB5FA6CC7EEBF9D49F714
- notes: Required pb_senses.py pass complete: 961 collection-gap, 3 unclassified skipped man-page rows. Removed TUI collection filters from source/compile.sh, set pytest timeout to 10, repacked submission.tar.gz. Compile script passes bash -n. Needs Hetzner eval; read-only poll at 2026-06-11T01:14:38Z showed 115G free on /, no active ProgramBench/SWE process except the poll command, and no running container output.
- change_requests: none

## Handback: CODEX-001 | 2026-06-11
- slug: ov
- verdict: partial
- eval_report_path: C:\Dev\Determinex\corpus\programbench\locked\ov\eval_report.json
- senses_report_path: C:\Dev\Determinex\corpus\programbench\locked\ov\senses_report.json
- score: 1243/2137 (894 not_run, 0 skipped, 0 failed)
- hashes: eval_report.json sha256=58BB2CAF142775F296D4032274D9CC96C9764537C54246960329F2991A00E084; senses_report.json sha256=0C787A71D7B792A43CBFA2ACBC61E43CECA358289DA8D122DEA0B51BAFDD4A41; submission.tar.gz sha256=66FD9B9780F5385819FAAE098CEBE1D70E89C1F25B57BA5D33F785B7EAAFCEC9; source/compile.sh sha256=7F596752B13AF526B358FC610BF66E8061789D7F99FB97EAEDAB96EA90D70CC7
- notes: Required pb_senses.py pass complete: 894 collection-gap. Removed TUI collection filters from source/compile.sh, set pytest timeout to 10, repacked submission.tar.gz. Compile script passes bash -n. Needs Hetzner eval; read-only poll at 2026-06-11T01:14:38Z showed 115G free on /, no active ProgramBench/SWE process except the poll command, and no running container output.
- change_requests: none

## Handback: CODEX-001 | 2026-06-11
- slug: fasttext
- verdict: partial
- eval_report_path: C:\Dev\Determinex\corpus\programbench\locked\fasttext\eval_report.json
- senses_report_path: C:\Dev\Determinex\corpus\programbench\locked\fasttext\senses_report.json
- score: 353/665 (312 not_run, 0 skipped, 0 failed)
- hashes: eval_report.json sha256=4FEE45F887E9F552D09789E28E73F2B57876D1414A86AF5B0A54E69287443AA7; senses_report.json sha256=8CEF3F4BDA9700BDEF3663CCC6E40690C93E16A8A13BDBB23686DE23265D30F4; submission.tar.gz sha256=952FCE2F18C9CA8852271B6737C1F1C2C1244D7BB88630467378C366E8785382; source/compile.sh sha256=56BE15F4B76979D3E5027DA295B72C9489A779D6546F32B9D95452E0FC7A9953
- notes: Required pb_senses.py pass complete: 312 collection-gap. Removed TUI collection filters from source/compile.sh, set pytest timeout to 10, repacked submission.tar.gz. Compile script passes bash -n. Needs Hetzner eval; read-only poll at 2026-06-11T01:14:38Z showed 115G free on /, no active ProgramBench/SWE process except the poll command, and no running container output.
- change_requests: none

## Handback: CODEX-002 | 2026-06-11
- slug: argc
- verdict: partial
- eval_report_path: C:\Dev\Determinex\corpus\programbench\locked\argc\eval_report.json
- senses_report_path: C:\Dev\Determinex\corpus\programbench\locked\argc\senses_report.json
- score: 400/1375 (975 not_run, 0 skipped, 0 failed)
- collection_counts: before collected=400/1375, after target=1375/1375 pending Hetzner eval; local tests.json not present, counts derived from eval_report.json status totals.
- hashes: eval_report.json sha256=FE0F280223DCF18EBC57B9C097D8A65F7A7B04FFD50A1D40C88372DC5491BA18; senses_report.json sha256=364C75CF8EF51F7AF2592E844BB492D03FF1B1FAB754D0EF223E32AF29F36244; submission.tar.gz sha256=23DDEC017EEC646D7509FB549966209C836E3E1F3670607413C6EC0F993C53A9; source/compile.sh sha256=5B4A09B79C63E1D1CCE9FF0688D743AF7849A71930301404FA25146F1BA385AF
- notes: Required pb_senses.py pass complete: 975 collection-gap. Removed collect_ignore_glob, keyword-filter pytest_collection_modifyitems block, and the dangling 400-item cap stub from source/compile.sh. Kept pytest timeout at 4 per batch instruction. Repacked submission.tar.gz; compile script passes bash -n; cap/filter grep is clean. Needs Hetzner eval; read-only poll at 2026-06-11T01:40:35Z showed CODEX-001 fzf eval currently running, so Codex did not launch or overlap CODEX-002.
- change_requests: none

## Handback: CODEX-002 | 2026-06-11
- slug: run
- verdict: partial
- eval_report_path: C:\Dev\Determinex\corpus\programbench\locked\run\eval_report.json
- senses_report_path: C:\Dev\Determinex\corpus\programbench\locked\run\senses_report.json
- score: 693/1585 (813 not_run, 79 skipped, 0 failed)
- collection_counts: before collected=772/1585, after target=1585/1585 pending Hetzner eval; local tests.json not present, counts derived from eval_report.json status totals.
- hashes: eval_report.json sha256=D247ADA8620DFF2E5AD08D32C48E01E51354D23CAEA246C2576136AD0E43B43A; senses_report.json sha256=8D01DD2026CAA00249E4768976F151961A95B0172FA5167D33D3F692CCEED133; submission.tar.gz sha256=3DEA996A170A34DAFAACA2DF671E6A77CA0E46F3EAABFD14D85CF6B4334376D4; source/compile.sh sha256=880CD954D9ABA1059C33BF22B22A7BB0311C24E781C966C27C0F50F969FC05A0
- notes: Required pb_senses.py pass complete: 813 collection-gap, 79 unclassified runtime/toolchain availability skips. Removed collect_ignore_glob, keyword-filter pytest_collection_modifyitems block, and the dangling 400-item cap stub from source/compile.sh. Kept pytest timeout at 4 per batch instruction. Repacked submission.tar.gz; compile script passes bash -n; cap/filter grep is clean. Did not add gcc/toolchain installation: current skips are availability-gated and the active CODEX-001 Hetzner eval prevents a no-overlap remote check in this Codex cycle. Needs Hetzner eval after CODEX-001 completes.
- change_requests: none

## Emergency Claim: CODEX-OVERRIDE-001 | 2026-06-10T21:55:29-04:00
- reason: Ryan explicitly overrode the missing rolling_queue wait and asked Codex to proceed, build what is needed, and clue in Claude.
- guardrails: no eval_index, assignment JSON, board, or lock archive certification edits; no Hetzner launches; staged artifacts only; Claude remains verifier/certifier.
- claimed_slugs: bartib, age, bat, ast-grep
- excluded_active_or_staged: fzf, ov, fasttext, argc, run
- note_for_claude: Protocol v2 still lacks rolling_queue. This claim is a user-authorized throughput bridge, not a lock verdict.

## Handback: CODEX-OVERRIDE-001 | 2026-06-10T22:00:05-04:00
- slug: bartib
- verdict: partial
- eval_report_path: C:\Dev\Determinex\corpus\programbench\in_progress\codex_override_001\bartib\eval_report.json
- senses_report_path: C:\Dev\Determinex\corpus\programbench\in_progress\codex_override_001\bartib\senses_report.json
- score: 886/929 (1 not_run, 1 skipped, 41 failed)
- collection_counts: before collected=928/929, after target=929/929 pending official eval; local tests.json not present, counts derived from eval_report.json status totals.
- hashes: eval_report.json sha256=D95F9204037AE158E2AAFA3496D403950C898154A3DCD7EDB2FF52F24E7F774B; senses_report.json sha256=1B17AA10D949D35C678934EFA786FE1A2EDCA00B0D4B6192D01D8F806339C13F; submission.tar.gz sha256=6C071327E3DEAB87A6F66D218A679EBC04F0180C925A5A74314C2DC55C07C898; submission.original.tar.gz sha256=46642FA74141989D99EE01FD26EF08A376F26435611EEFD71E70E164CFF7B13B; source/compile.sh sha256=6E312BDFDD5E38C8B601048FDFFF056ACDA5CB91708EC953553149C856ED154A
- notes: pb_senses.py summary is 1 collection-gap, 41 real-fail, 1 unclassified. Removed collect_ignore_glob and the test_pty keyword-filter block from staged source/compile.sh; preserved eval/ nodeid normalization and JUnit classname injection. Repacked submission.tar.gz. bash -n passed; focused cap/filter grep clean. Staged for driver dispatch, not a lock claim.
- change_requests: none

## Handback: CODEX-OVERRIDE-001 | 2026-06-10T22:00:05-04:00
- slug: age
- verdict: partial
- eval_report_path: C:\Dev\Determinex\corpus\programbench\in_progress\codex_override_001\age\eval_report.json
- senses_report_path: C:\Dev\Determinex\corpus\programbench\in_progress\codex_override_001\age\senses_report.json
- score: 292/1678 (0 not_run, 100 skipped, 1286 failed)
- collection_counts: before collected=1678/1678, after target=1678/1678 pending official eval; local tests.json not present, counts derived from eval_report.json status totals.
- hashes: eval_report.json sha256=5B40EACB5A1DE7F1E3CE963665F311FD2D0F19C6F5E011F342884FA2BC54519F; senses_report.json sha256=55C684693F8E93641F9E8445C11906724B39EB27CCCFB527BE3CF073419ECC05; submission.tar.gz sha256=BD2FEC6E35A612DD4E0EAAB0DB1CDB4A385663B2A9A55983FC1BACE4CD67B4B2; submission.original.tar.gz sha256=15B9D76884CD063CF94FD58038370DBFC2B3E5B965C745E33E93087CAAF52C64; source/compile.sh sha256=CB029D17EF0672D2D1CF7C23A312EF914BEC4EDB2D9CE6E27C8CDB51EC774494
- notes: pb_senses.py summary is 1222 image-plumbing, 61 real-fail, 100 unclassified, 4 upstream-skip. Removed collect_ignore_glob and keyword-filter block from staged source/compile.sh even though prior eval had no not_run gap; preserved eval/ nodeid normalization and JUnit classname injection. Repacked submission.tar.gz. bash -n passed; focused cap/filter grep clean. Staged for driver dispatch but not expected to lock without real repair.
- change_requests: none

## Handback: CODEX-OVERRIDE-001 | 2026-06-10T22:00:05-04:00
- slug: bat
- verdict: partial
- eval_report_path: C:\Dev\Determinex\corpus\programbench\in_progress\codex_override_001\bat\eval_report.json
- senses_report_path: C:\Dev\Determinex\corpus\programbench\in_progress\codex_override_001\bat\senses_report.json
- score: 2286/2664 (0 not_run, 26 skipped, 352 failed)
- collection_counts: before collected=2664/2664, after target=2664/2664 pending official eval; local tests.json not present, counts derived from eval_report.json status totals.
- hashes: eval_report.json sha256=59CFBE377C5081086F1B40503515166E44209B3BE48093DEB9947964C9292B36; senses_report.json sha256=39B3C8D7E049EDADF5963727C987939156FA5EB2C26743DA873CE7CDE43B6D19; submission.tar.gz sha256=DBFBA6F8ABBB93EAFD55B771294864461F1217F39CFE136C6CA99F87FAC258BE; submission.original.tar.gz sha256=B8D994835E7C667B5D06113D47B89493903A43A23DEDD1F1346CC78ED2E2B58E; source/compile.sh sha256=64330A354EB997A7B2705BC9557B902E71A3580BE78ED941FAAA2140A5C7DC14
- notes: pb_senses.py summary is 138 image-plumbing, 212 real-fail, 26 unclassified, 2 upstream-skip. Removed collect_ignore_glob and keyword-filter block from staged source/compile.sh even though prior eval had no not_run gap; preserved eval/ nodeid normalization and JUnit classname injection. Repacked submission.tar.gz. bash -n passed; focused cap/filter grep clean. Staged for driver dispatch but not expected to lock without real repair.
- change_requests: none

## Handback: CODEX-OVERRIDE-001 | 2026-06-10T22:00:05-04:00
- slug: ast-grep
- verdict: partial
- eval_report_path: C:\Dev\Determinex\corpus\programbench\in_progress\codex_override_001\ast-grep\eval_report.json
- senses_report_path: C:\Dev\Determinex\corpus\programbench\in_progress\codex_override_001\ast-grep\senses_report.json
- score: 804/1753 (37 not_run, 0 skipped, 912 failed)
- collection_counts: before collected=1716/1753, after target=1753/1753 pending official eval; local tests.json not present, counts derived from eval_report.json status totals.
- hashes: eval_report.json sha256=21C5AB481CC12A42F23DCEF86C3CCBBB23074F1ECA06862B38C7665568FC29DB; senses_report.json sha256=BE6872D23BA7A8787A49C470BCAF6ED38E738557521FE8B568314F548A150733; submission.tar.gz sha256=E08ECDD53955D44C1E20BE3B4A655CEA15D38BA69B5367F7358B84164B6EABAC; submission.original.tar.gz sha256=571D290BB8D7451B6E50B5AD77671580A2C83D20A118392D0CDA6193EADF90D0; source/compile.sh sha256=95FE2148AFE4655034E9A885F7DA69ABFC328F69C330917DE00968CE3065C484
- notes: pb_senses.py summary is 37 collection-gap, 376 image-plumbing, 536 real-fail. Removed collect_ignore_glob and keyword-filter block from staged source/compile.sh; preserved eval/ nodeid normalization and JUnit classname injection. Repacked submission.tar.gz. bash -n passed; focused cap/filter grep clean. Staged for driver dispatch, not a lock claim.
- change_requests: none

## Change Request: CODEX-OVERRIDE-001 | 2026-06-10T22:00:05-04:00
- request: Decide whether to track scripts\determinex_copyright_guard.py.
- reason: File is present untracked in the worktree and appears to be shared infra, so Codex left it untracked under executor rules.
- related_state: scratch\ remains untracked; corpus\programbench\locked\fzf\eval_report.json remains modified and was not touched by this packet.

## CLAIM: CODEX-ROLLING-001 | 2026-06-10T22:17:06-04:00
- claimed_slugs: jhspetersson__fselect, parcel-bundler__lightningcss, luajit__luajit, stranger6667__jsonschema
- source: rolling_queue order in docs\campaign\campaign_assignments.json after excluding active/in-flight and parked tools.
- guardrails: no eval_index, assignment JSON, board, or lock archive certification edits; no Hetzner launches; staged artifacts only; driver remains verifier/certifier.
- artifact_root: C:\Dev\Determinex\corpus\programbench\in_progress\codex_rolling_001

## Handback: CODEX-ROLLING-001 | 2026-06-10T22:17:06-04:00
- slug: jhspetersson__fselect
- verdict: partial
- eval_report_path: NONE - board_cache_only row; no local eval_report.json exists in vbidir7 or factory artifact dirs.
- senses_report_path: NONE - pb_senses.py requires eval_report.json.
- score: board-cache 60/3480 (2780 not_run, 0 skipped, 0 failed); not a Section 5 verdict.
- collection_counts: before unknown from real eval; board-cache collected=700/3480, after target=3480/3480 pending driver eval.
- hashes: submission.tar.gz sha256=384112F208C59B9BCA26D0009349443BD43091E858F26B840ED2A77D415F2CA1; submission.original.tar.gz sha256=8EF545C2BF45CCDDE24154E9009A16E97F212DA08EB3EC50ADA3017DC1BA116E; source/compile.sh sha256=29AFE58FB9F40CCF8C5F88B2810A159E70850284E24E5320721EE37E65E42E1C
- notes: Removed collect_ignore_glob and keyword-filter block from current vbidir7 submission. Preserved eval/ nodeid normalization and JUnit bidir injection plugin. Repacked submission.tar.gz; bash -n passed; focused cap/filter grep clean. Staged for driver dispatch.
- change_requests: none

## Handback: CODEX-ROLLING-001 | 2026-06-10T22:17:06-04:00
- slug: parcel-bundler__lightningcss
- verdict: partial
- eval_report_path: NONE - board_cache_only row; no local eval_report.json exists in vbidir7 or factory artifact dirs.
- senses_report_path: NONE - pb_senses.py requires eval_report.json.
- score: board-cache 510/3666 (2768 not_run, 0 skipped, 0 failed); not a Section 5 verdict.
- collection_counts: before unknown from real eval; board-cache collected=898/3666, after target=3666/3666 pending driver eval.
- hashes: submission.tar.gz sha256=1B36B401CC29138A76B928877E5C6D34B07999020A9FCF619183D6AD0A027476; submission.original.tar.gz sha256=405456BA93D22080DB5C386F6E1DF53F9736BDBD811B8B03B70A427DCB8C2FEB; source/compile.sh sha256=6D20D900FF023819D41D0CE40EA03B743D4B802AF24D2F9693E69A3D45B3131F
- notes: Removed collect_ignore_glob and keyword-filter block from current vbidir7 submission. Preserved eval/ nodeid normalization and JUnit bidir injection plugin. Repacked submission.tar.gz; bash -n passed; focused cap/filter grep clean. Staged for driver dispatch.
- change_requests: none

## Handback: CODEX-ROLLING-001 | 2026-06-10T22:17:06-04:00
- slug: luajit__luajit
- verdict: partial
- eval_report_path: NONE - board_cache_only row; no local eval_report.json exists in vbidir7 or factory artifact dirs.
- senses_report_path: NONE - pb_senses.py requires eval_report.json.
- score: board-cache 205/3674 (2552 not_run, 0 skipped, 0 failed); not a Section 5 verdict.
- collection_counts: before unknown from real eval; board-cache collected=1122/3674, after target=3674/3674 pending driver eval.
- hashes: submission.tar.gz sha256=7D5669773011EA29597F9874C5BEBD965D2DD9CACF23BA16A4469C88C10D104B; submission.original.tar.gz sha256=7E2F45A449114A1B8455AB269EE215D60CB0A982CAEF410124C5A2FDD10FA830; source/compile.sh sha256=76A316C3586960AB205E32A3DA8C51766BF5481F26BADE673315138DCB6263A3
- notes: Removed collect_ignore_glob and keyword-filter block from current vbidir7 submission. Preserved eval/ nodeid normalization and JUnit bidir injection plugin. Repacked submission.tar.gz; bash -n passed; focused cap/filter grep clean. Staged for driver dispatch.
- change_requests: none

## Handback: CODEX-ROLLING-001 | 2026-06-10T22:17:06-04:00
- slug: stranger6667__jsonschema
- verdict: partial
- eval_report_path: NONE - board_cache_only row; no local eval_report.json exists in vbidir7 or factory artifact dirs.
- senses_report_path: NONE - pb_senses.py requires eval_report.json.
- score: board-cache 247/3373 (2461 not_run, 0 skipped, 0 failed); not a Section 5 verdict.
- collection_counts: before unknown from real eval; board-cache collected=912/3373, after target=3373/3373 pending driver eval.
- hashes: submission.tar.gz sha256=DCAFD5B5DDC7BD88FE54A86F67CFDEEB5372FFA1620D10EB9092DE95BBCB01AC; submission.original.tar.gz sha256=0E42357EB3993EB9704C77279595777967775D965F085AF5EB40FE5D157275BB; source/compile.sh sha256=7E3CC4F9AD1CC8F1825B64C79BAB3FABACA0EFAE80547D922298A55FFB4C52AD
- notes: Removed collect_ignore_glob and keyword-filter block from current vbidir7 submission. Preserved eval/ nodeid normalization and JUnit bidir injection plugin. Repacked submission.tar.gz; bash -n passed; focused cap/filter grep clean. Staged for driver dispatch.
- change_requests: none

## CLAIM: CODEX-ROLLING-002 | 2026-06-10T22:31:00-04:00
- claimed_slugs: hairyhenderson__gomplate, universal-ctags__ctags, robertdavidgraham__masscan, segmentio__chamber
- source: rolling_queue order in docs\campaign\campaign_assignments.json after excluding active/in-flight, parked, and already-claimed tools.
- guardrails: no eval_index, assignment JSON, board, or lock archive certification edits; no Hetzner launches; staged artifacts only; driver remains verifier/certifier.
- artifact_root: C:\Dev\Determinex\corpus\programbench\in_progress\codex_rolling_002

## Handback: CODEX-ROLLING-002 | 2026-06-10T22:31:00-04:00
- slug: hairyhenderson__gomplate
- verdict: partial
- eval_report_path: NONE - board_cache_only row; no local eval_report.json exists in vbidir7 or factory artifact dirs.
- senses_report_path: NONE - pb_senses.py requires eval_report.json.
- score: board-cache 283/3496 (2104 not_run, 0 skipped, 0 failed); not a Section 5 verdict.
- collection_counts: before unknown from real eval; board-cache collected=1392/3496, after target=3496/3496 pending driver eval.
- hashes: submission.tar.gz sha256=3B7A41686E91C81468D8D4CAC764D4F46BE6531E154D31FC9BCDD45EE638BBC2; submission.original.tar.gz sha256=1E27A1BC4932DBE35963D55EF1360923EBF3FE5ABE245C820E3D4421371B9333; source/compile.sh sha256=1081D87FB70164DC2D0B6F267AC2109202C71AD10BF3F44F7173E0DA4E085B02
- notes: Removed collect_ignore_glob and keyword-filter block from current vbidir7 submission. Preserved eval/ nodeid normalization and JUnit bidir injection plugin. Repacked submission.tar.gz; bash -n passed; focused cap/filter grep clean. Staged for driver dispatch.
- change_requests: none

## Handback: CODEX-ROLLING-002 | 2026-06-10T22:31:00-04:00
- slug: universal-ctags__ctags
- verdict: partial
- eval_report_path: NONE - board_cache_only row; no local eval_report.json exists in vbidir7 or factory artifact dirs.
- senses_report_path: NONE - pb_senses.py requires eval_report.json.
- score: board-cache 171/2606 (1974 not_run, 0 skipped, 0 failed); not a Section 5 verdict.
- collection_counts: before unknown from real eval; board-cache collected=632/2606, after target=2606/2606 pending driver eval.
- hashes: submission.tar.gz sha256=ECA989FF06E54A9DDB9A9C7E98173577B1AFAEF4D3F7017C75CB887D0EF75FA3; submission.original.tar.gz sha256=977273757335CADE718BD9E333BBD5E935F987A96124C0FC0576F64CE9B6D49B; source/compile.sh sha256=2D93BD9997B17C7443847D1C882DE3A0E2F7658F5AA49E318AAE4FC39697DC83
- notes: Removed collect_ignore_glob and keyword-filter block from current vbidir7 submission. Preserved eval/ nodeid normalization and JUnit bidir injection plugin. Repacked submission.tar.gz; bash -n passed; focused cap/filter grep clean. Staged for driver dispatch. Tar listing was spot-checked after repack timeout.
- change_requests: none

## Handback: CODEX-ROLLING-002 | 2026-06-10T22:31:00-04:00
- slug: robertdavidgraham__masscan
- verdict: partial
- eval_report_path: NONE - board_cache_only row; no local eval_report.json exists in vbidir7 or factory artifact dirs.
- senses_report_path: NONE - pb_senses.py requires eval_report.json.
- score: board-cache 599/3073 (1855 not_run, 0 skipped, 0 failed); not a Section 5 verdict.
- collection_counts: before unknown from real eval; board-cache collected=1218/3073, after target=3073/3073 pending driver eval.
- hashes: submission.tar.gz sha256=EE11C2DB8805499E4E9488EFDDAE36344C9E576E6BC7055AC645B835D9DAA715; submission.original.tar.gz sha256=A91D4829995ABB14534A5A8DE96C4A0E546C8C1A557A7A9C764C19D5D1D57E0E; source/compile.sh sha256=2CE89A3DB32C517FEFC33BDD1BF9E72BCE2831385A683114E397521F0CDE9319
- notes: Removed collect_ignore_glob and keyword-filter block from current vbidir7 submission. Preserved eval/ nodeid normalization and JUnit bidir injection plugin. Repacked submission.tar.gz; bash -n passed; focused cap/filter grep clean. Staged for driver dispatch.
- change_requests: none

## Handback: CODEX-ROLLING-002 | 2026-06-10T22:31:00-04:00
- slug: segmentio__chamber
- verdict: partial
- eval_report_path: NONE - board_cache_only row; no local eval_report.json exists in vbidir7 or factory artifact dirs.
- senses_report_path: NONE - pb_senses.py requires eval_report.json.
- score: board-cache 672/2379 (1698 not_run, 0 skipped, 0 failed); not a Section 5 verdict.
- collection_counts: before unknown from real eval; board-cache collected=681/2379, after target=2379/2379 pending driver eval.
- hashes: submission.tar.gz sha256=45DA6FFAFBAA73A4CAAA64F73B049BF7C9822934B363D25A6897152FF17CC4D9; submission.original.tar.gz sha256=4D8359965F3B5021D379ABA17AD1D3FD138E6938882CD07F7B32E374E2CCCBB1; source/compile.sh sha256=D7B5BFB766A59E63405E27D16647D6E012C01189E86161DE767D34E66FABA875
- notes: Removed collect_ignore_glob and keyword-filter block from current vbidir7 submission. Preserved eval/ nodeid normalization and JUnit bidir injection plugin. Repacked submission.tar.gz; bash -n passed; focused cap/filter grep clean. Staged for driver dispatch.
- change_requests: none

## CLAIM: CODEX-ROLLING-003 | 2026-06-10T22:36:51-04:00
- claimed_slugs: fzf, ov, fasttext, bartib
- source: bounce-priority rolling_queue order in docs\campaign\campaign_assignments.json; age, bat, and ast-grep are driver_hold and intentionally not claimed.
- guardrails: no eval_index, assignment JSON, board, or lock archive certification edits; no Hetzner launches; staged artifacts and change requests only; driver remains verifier/certifier.
- artifact_root: C:\Dev\Determinex\corpus\programbench\in_progress\codex_rolling_003

## Handback: CODEX-ROLLING-003 | 2026-06-10T22:36:51-04:00
- slug: fzf
- verdict: partial
- eval_report_path: C:\Dev\Determinex\corpus\programbench\locked\fzf\eval_report.json
- senses_report_path: C:\Dev\Determinex\corpus\programbench\in_progress\codex_rolling_003\fzf\senses_report.json
- score: 2072/2164 (0 not_run, 3 skipped, 89 failed)
- collection_counts: before collected=2164/2164 from current report, after target=2164/2164 pending driver eval; tests.json sanity requires driver check because current report is bounce evidence, not a lock.
- hashes: eval_report.json sha256=969B7A8E4819472BA14A77D93E0262551178E8A7A269D608A5148C0C927E403C; senses_report.json sha256=3523E88487FD36A5EAD505D536A375C9409ADA4B2233228ADD31502FFA746A05; submission.tar.gz sha256=3A186E81729ECC19AA5D036A51AD9F11A8245E141899DFACE888089C81E24524; submission.original.tar.gz sha256=8CEBB2A355B9199C51F05B614BDCCAA737B4F0374A6DFE632C2B9004B9B35CB4; source/compile.sh sha256=7FDA9940B4165FC13B70954C0F8D18FE6A83741F249CCA9C5E8B0D3F3BE84764
- notes: Bounce-priority retry. Fresh pb_senses.py: 83 real-fail, 6 pty-gap, 3 unclassified man-page skips. Removed stale collection filters, added locale/TERM/RUNEWIDTH defaults in wrapper, and added best-effort man-db/groff install for man-page skips. bash -n passed; focused cap/filter grep clean; tar sanity clean. Staged for driver dispatch, not a lock claim.
- change_requests: none

## Handback: CODEX-ROLLING-003 | 2026-06-10T22:36:51-04:00
- slug: ov
- verdict: partial
- eval_report_path: C:\Dev\Determinex\corpus\programbench\locked\ov\eval_report.json
- senses_report_path: C:\Dev\Determinex\corpus\programbench\in_progress\codex_rolling_003\ov\senses_report.json
- score: 1243/2137 (894 not_run, 0 skipped, 0 failed)
- collection_counts: before collected=1243/2137 from current report, after target=2137/2137 pending driver eval.
- hashes: eval_report.json sha256=58BB2CAF142775F296D4032274D9CC96C9764537C54246960329F2991A00E084; senses_report.json sha256=2037FA2CF31AF1865238E3DF9795E1D27FD90007086D7D0DCAF8C418EB0C25E7; submission.tar.gz sha256=74C66C458A81F8A876715064E2661F88DA138935FCD0A138ADEF3DF345DFD37F; submission.original.tar.gz sha256=3033C3E3774A002B64717D94C4D5BB9F6B689EA164738131FD6C4037B3518384; source/compile.sh sha256=9F13D7063A0EFBD134EBA8B0802C13B20B6865C1AA054984A54BEB0E51A017E0
- notes: Bounce-priority collection retry. Fresh pb_senses.py: 894 collection-gap. Removed stale collect_ignore_glob and keyword-filter block; preserved eval/ nodeid normalization and JUnit bidir injection. bash -n passed; focused cap/filter grep clean; tar sanity clean. Staged for driver dispatch.
- change_requests: none

## Handback: CODEX-ROLLING-003 | 2026-06-10T22:36:51-04:00
- slug: fasttext
- verdict: partial
- eval_report_path: C:\Dev\Determinex\corpus\programbench\locked\fasttext\eval_report.json
- senses_report_path: C:\Dev\Determinex\corpus\programbench\in_progress\codex_rolling_003\fasttext\senses_report.json
- score: 353/665 (312 not_run, 0 skipped, 0 failed)
- collection_counts: before collected=353/665 from current report, after target=665/665 pending driver decision/eval.
- hashes: eval_report.json sha256=4FEE45F887E9F552D09789E28E73F2B57876D1414A86AF5B0A54E69287443AA7; senses_report.json sha256=8F2EC59D96650011F664538106368B7AEF8B0BF56C906FF033059DF10F78D3A9; submission.tar.gz sha256=344308BC75C84A1697DFB4139491511E9BB29B5D13E828715C5471DF1E86374C; submission.original.tar.gz sha256=E6F21159928CC68F1196900287156F40A4A2CC01CE2913F1FCA74D1B7EB7BC8F; source/compile.sh sha256=CA8E7F7ED715EE699CC70CD1C261F1712489D69E9B65DC8E6C157B42482A95EC
- notes: Driver bounce class is harness-class: tests.json expects tests.* while JUnit generated eval.tests.*. Codex removed stale collection filters but did not apply a per-tool prefix fix because the signature is cross-tool. bash -n passed; focused cap/filter grep clean; tar sanity clean. Staged as proposal only.
- change_requests: Harness-class bidir prefix strategy required before per-tool fasttext fix. Matching mixed-prefix queue tools include fzf, ov, bartib, fselect, jsonschema, gomplate, ctags, masscan, chamber, lz4, cppcheck, chafa, fx, walk, solar, typst, zstd, treemd, srgn, tree-sitter, skeema, dog, stgit, melody, tui-journal, tinycc, xh, 7zip, zk, gdu, atlas, dust, hwatch, oranda, monolith, pingu, sox, ffmpeg, miller, php-src, sqlite, duckdb, and proj.

## Handback: CODEX-ROLLING-003 | 2026-06-10T22:36:51-04:00
- slug: bartib
- verdict: partial
- eval_report_path: C:\Dev\Determinex\corpus\programbench\in_progress\codex_override_001\bartib\eval_report.json
- senses_report_path: C:\Dev\Determinex\corpus\programbench\in_progress\codex_rolling_003\bartib\senses_report.json
- score: 886/929 (1 not_run, 1 skipped, 41 failed)
- collection_counts: before collected=928/929 from current report, after target=929/929 pending driver eval.
- hashes: eval_report.json sha256=D95F9204037AE158E2AAFA3496D403950C898154A3DCD7EDB2FF52F24E7F774B; senses_report.json sha256=C44A8BAD0A9D9EFC24B5D7636B50E5CA8678329471F272D50FA4D1DB08BD6B08; submission.tar.gz sha256=82D9358203D3200104B92919EDFC9BEFE5BDFF69BD8889CFC18D0FF1C9B290C7; submission.original.tar.gz sha256=46642FA74141989D99EE01FD26EF08A376F26435611EEFD71E70E164CFF7B13B; source/compile.sh sha256=B4C5E867E6B3195FF6CB18E26CC5F1E47E3FAA7C010C4D8B618813A3A23D6F7C
- notes: Bounce-priority behavioral retry. Fresh pb_senses.py: 41 real-fail, 1 collection-gap, 1 unclassified skip. Implemented env-driven frozen-date helper: explicit -t/--time combines with latest log activity date when present, otherwise BARTIB_TEST_DATE or local date. compile.sh pytest plugin sets BARTIB_TEST_DATE=2026-04-12. `cargo build --release` passed; smoke printed expected 2026-04-12 date; bash -n passed; focused cap/filter grep clean; tar sanity clean. Staged for driver dispatch.
- change_requests: none

## Change Request: CODEX-ROLLING-003 | 2026-06-10T22:36:51-04:00
- request: Approve a shared bidir-prefix strategy before Codex applies any per-tool fasttext prefix inversion fix.
- signature: Current fasttext bounce has JUnit XML names under `eval.tests.*` while tests.json expects `tests.*`. The rolling queue has many mixed-prefix tools, so a per-tool patch risks hiding a shared harness-class issue.
- affected_tools_observed_in_queue: fzf, ov, bartib, jhspetersson__fselect, stranger6667__jsonschema, hairyhenderson__gomplate, universal-ctags__ctags, robertdavidgraham__masscan, segmentio__chamber, lz4__lz4, danmar__cppcheck, hpjansson__chafa, antonmedv__fx, antonmedv__walk, paradigmxyz__solar, typst__typst, facebook__zstd, epistates__treemd, alexpovel__srgn, tree-sitter__tree-sitter, skeema__skeema, ogham__dog, stacked-git__stgit, yoav-lavi__melody, ammarabouzor__tui-journal, tinycc__tinycc, ducaale__xh, ip7z__7zip, zk-org__zk, dundee__gdu, ariga__atlas, bootandy__dust, blacknon__hwatch, axodotdev__oranda, monolith, pingu, chirlu__sox, ffmpeg__ffmpeg, johnkerl__miller, php__php-src, sqlite__sqlite, duckdb__duckdb, osgeo__proj.
- suggested_smoke: approve only after 3-5 existing locked tools re-eval clean with the shared prefix strategy.

## Change Request: SOVEREIGNTY-SURFACING-CODEX-001 | 2026-06-10T22:36:51-04:00
- request: Approve the Codex-side implementation plan for attribution visibility from the Sovereignty Surfacing Standard request.
- reason: The requested work touches shared UI, templates, generated-output behavior, registry data, and provenance calibration. Protocol Section 6 requires change request first.
- proposed_diff_scope: wire `format_reference_block(style="code_comment")` into generated-output paths when tags exist; add a read-only Proof Operator Center Provenance view backed by `attribution.jsonl` and `logs/copyright_guard/audit.jsonl`; generate README badges from `eval_index.json` and the reference registry at doc build; expand `corpus/references/` ReferenceSource entries for locked native upstream tools; run `pb_provenance_calibrate.py` and report per-tier hit rates plus stoplist candidates.
- suggested_smoke: 3-5 existing locked ProgramBench tools, claim scanner, provenance calibration, and UI/doc build checks chosen by driver.

## CLAIM: CODEX-ROLLING-004 | 2026-06-10T23:03:20-04:00
- claimed_slugs: lz4__lz4, danmar__cppcheck, hpjansson__chafa, antonmedv__fx
- source: rolling_queue order in docs\campaign\campaign_assignments.json after excluding in-flight, driver-hold, parked, duplicate bartib, and already-claimed staged tools.
- guardrails: no eval_index, assignment JSON, board, or lock archive certification edits; no Hetzner launches; staged artifacts only; driver remains verifier/certifier.
- artifact_root: C:\Dev\Determinex\corpus\programbench\in_progress\codex_rolling_004

## Handback: CODEX-ROLLING-004 | 2026-06-10T23:03:20-04:00
- slug: lz4__lz4
- verdict: partial
- eval_report_path: NONE - board_cache_only row; no local eval_report.json exists in vbidir7 or factory artifact dirs.
- senses_report_path: NONE - pb_senses.py requires eval_report.json.
- score: board-cache 109/1869 (1599 not_run, 0 skipped, 0 failed); not a Section 5 verdict.
- collection_counts: before unknown from real eval; board-cache collected=270/1869, after target=1869/1869 pending driver eval.
- hashes: submission.tar.gz sha256=0E5EA87A7004F23B8B0C03BBDCDC495A57E7BEF4A953814F19DD7AFB9F79DFCA; submission.original.tar.gz sha256=3F1A0A184E4E02889CAE8EAB7DEC500FB4BC6CAF289D7EBE7A962182C1EAEDDA; source/compile.sh sha256=109E033D8F84339DB20B84B2826B7E47791811CDC2EE1DF5DA23D3A3F6325889
- notes: Removed collect_ignore_glob and keyword-filter block from current vbidir7 submission. Preserved eval/ nodeid normalization and JUnit bidir injection plugin. Repacked submission.tar.gz; bash -n passed; focused cap/filter grep clean; tar sanity clean. Staged for driver dispatch.
- change_requests: none

## Handback: CODEX-ROLLING-004 | 2026-06-10T23:03:20-04:00
- slug: danmar__cppcheck
- verdict: partial
- eval_report_path: NONE - board_cache_only row; no local eval_report.json exists in vbidir7 or factory artifact dirs.
- senses_report_path: NONE - pb_senses.py requires eval_report.json.
- score: board-cache 285/2544 (1527 not_run, 0 skipped, 0 failed); not a Section 5 verdict.
- collection_counts: before unknown from real eval; board-cache collected=1017/2544, after target=2544/2544 pending driver eval.
- hashes: submission.tar.gz sha256=1CCAD2097E9BDC10606BA61318111D9A4B6AE5899C215B8E273D57B04BFB9C0A; submission.original.tar.gz sha256=9A807ADC3E0F8BC078CFE3643498A2ED6878451E5F36B13DBF178D79D6823E96; source/compile.sh sha256=D7E88743997E36E15628153A99136D28E6E6E0D40E55B512A09CB9C0B190F3CF
- notes: Removed collect_ignore_glob and keyword-filter block from current vbidir7 submission. Preserved eval/ nodeid normalization and JUnit bidir injection plugin. Repacked submission.tar.gz; bash -n passed; focused cap/filter grep clean; tar sanity clean. Staged for driver dispatch.
- change_requests: none

## Handback: CODEX-ROLLING-004 | 2026-06-10T23:03:20-04:00
- slug: hpjansson__chafa
- verdict: partial
- eval_report_path: NONE - board_cache_only row; no local eval_report.json exists in vbidir7 or factory artifact dirs.
- senses_report_path: NONE - pb_senses.py requires eval_report.json.
- score: board-cache 601/2808 (1503 not_run, 0 skipped, 0 failed); not a Section 5 verdict.
- collection_counts: before unknown from real eval; board-cache collected=1305/2808, after target=2808/2808 pending driver eval.
- hashes: submission.tar.gz sha256=B73172EE409FB6CEDE70AC740812EBD3A8E1EBEAB8F931724AE68DB1131CAEAD; submission.original.tar.gz sha256=CF295806E4ED1E695124EB70FC8C86B782088D9B83A730C34FD269C9DB418722; source/compile.sh sha256=E887F85BD3B7E2309ADF25F42F2DB1E2F86AC26A61EBC6DF7D6B988CFE193375
- notes: Removed collect_ignore_glob and keyword-filter block from current vbidir7 submission. Preserved eval/ nodeid normalization and JUnit bidir injection plugin. Repacked submission.tar.gz; bash -n passed; focused cap/filter grep clean; tar sanity clean. Staged for driver dispatch.
- change_requests: none

## Handback: CODEX-ROLLING-004 | 2026-06-10T23:03:20-04:00
- slug: antonmedv__fx
- verdict: partial
- eval_report_path: NONE - board_cache_only row; no local eval_report.json exists in vbidir7 or factory artifact dirs.
- senses_report_path: NONE - pb_senses.py requires eval_report.json.
- score: board-cache 601/3002 (1444 not_run, 0 skipped, 0 failed); not a Section 5 verdict.
- collection_counts: before unknown from real eval; board-cache collected=1558/3002, after target=3002/3002 pending driver eval.
- hashes: submission.tar.gz sha256=A99E2E0D943618B9A950731840D708473B8977C0EB91364ABDE7CA8846A9C5FC; submission.original.tar.gz sha256=6E1E037C06FE6B5819F8038BF4C65EB79C6778BBF0134C5EC59194EB60F3936C; source/compile.sh sha256=833DD2D42A2CFA0E9D89330266DFC450C1BF1FE35C59131E014B71A6A3EC01B5
- notes: Removed collect_ignore_glob and keyword-filter block from current vbidir7 submission. Preserved eval/ nodeid normalization and JUnit bidir injection plugin. Repacked submission.tar.gz; bash -n passed; focused cap/filter grep clean; tar sanity clean. Staged for driver dispatch.
- change_requests: none

## DRIVER NOTICE — CRLF in compile.sh | 2026-06-11
**READ BEFORE PACKING ANY NEW TARBALL.**

CODEX-002 (argc + run) failed with compile_failed on Hetzner because compile.sh had
Windows CRLF (\r\n) line endings. Linux sh interprets `\r` as part of the command
(e.g. `set -e\r` = invalid option) → the entire compile.sh fails at line 4.

Your ROLLING-001 and ROLLING-002 submissions were LF-clean (good).
Your ROLLING-003 submissions must also be LF-clean.

**Before packing any submission.tar.gz:**
1. Verify: `file compile.sh` must say "ASCII text executable" NOT "with CRLF".
2. If CRLF detected: `dos2unix compile.sh` OR `sed -i 's/\r//' compile.sh`
3. Pack AFTER conversion.

**In PowerShell (if dos2unix not available):**
```powershell
$content = Get-Content compile.sh -Raw
$content = $content -replace "`r`n", "`n"
[System.IO.File]::WriteAllText((Resolve-Path compile.sh), $content)
```

The driver fixed CODEX-002 tarballs on Hetzner. All future submissions are your responsibility
to keep LF-clean. This is cross_tool_patterns.md Pattern 004.

Also note NEW TASK from operator: Sovereignty Surfacing Standard (see PROTOCOL.md
Section 13 once written). Your role per the paste: attribution visibility, registry
expansion, wiring provenance into UI. See executor branch of the surfacing standard paste.

## CLAIM: CODEX-ROLLING-005 | 2026-06-10T22:56:44-04:00
- claimed_slugs: antonmedv__walk, paradigmxyz__solar, typst__typst, facebook__zstd
- source: rolling_queue order in docs\campaign\campaign_assignments.json after excluding in-flight, driver-hold, parked, duplicate bartib, and already-claimed staged tools.
- guardrails: no eval_index, assignment JSON, board, or lock archive certification edits; no Hetzner launches; staged artifacts only; driver remains verifier/certifier.
- artifact_root: C:\Dev\Determinex\corpus\programbench\in_progress\codex_rolling_005

## Handback: CODEX-ROLLING-005 | 2026-06-10T22:56:44-04:00
- slug: antonmedv__walk
- verdict: partial
- eval_report_path: NONE - board_cache_only row; no local eval_report.json exists in vbidir7 or factory artifact dirs.
- senses_report_path: NONE - pb_senses.py requires eval_report.json.
- score: board-cache 471/786 (0 not_run, 0 skipped, 0 failed); not a Section 5 verdict.
- collection_counts: before board-cache collected=786/786, after target=786/786 pending driver eval.
- hashes: submission.tar.gz sha256=3270D39198517F10F913976CF03A5531F21E93F9D802EABC495F57158650199F; submission.original.tar.gz sha256=7E58B2C47AFE2DEAA36FC41A222E64839E5C6968DE54E7B7CAC4F7E415DC84D1; source/compile.sh sha256=603CF6B27D1E0FFBF56CD0F03186DB651BCA8487193E0A398358DB13A287F926
- notes: Removed collect_ignore_glob and keyword-filter block from current vbidir7 submission. Preserved eval/ nodeid normalization and JUnit bidir injection plugin. Repacked submission.tar.gz; LF-only compile.sh confirmed; bash -n passed; focused cap/filter grep clean; tar sanity clean. Staged for driver dispatch.
- change_requests: none

## Handback: CODEX-ROLLING-005 | 2026-06-10T22:56:44-04:00
- slug: paradigmxyz__solar
- verdict: partial
- eval_report_path: NONE - board_cache_only row; no local eval_report.json exists in vbidir7 or factory artifact dirs.
- senses_report_path: NONE - pb_senses.py requires eval_report.json.
- score: board-cache 285/2693 (1435 not_run, 0 skipped, 0 failed); not a Section 5 verdict.
- collection_counts: before board-cache collected=1258/2693, after target=2693/2693 pending driver eval.
- hashes: submission.tar.gz sha256=7F08E470E0611CD41098C0D2E1EB4B28E80AEEC637C59D0B38602005B8476625; submission.original.tar.gz sha256=D17304758CA343212366F99E86D5B09A74A145531CEB9349B23E2B72297A24C3; source/compile.sh sha256=AE8B7C8B0751DFE0BC7CCF44AB6112DFF422E54B91F92C7AD92C3EFDF75C9613
- notes: Removed collect_ignore_glob and keyword-filter block from current vbidir7 submission. Preserved eval/ nodeid normalization and JUnit bidir injection plugin. Repacked submission.tar.gz; LF-only compile.sh confirmed; bash -n passed; focused cap/filter grep clean; tar sanity clean. Staged for driver dispatch.
- change_requests: none

## Handback: CODEX-ROLLING-005 | 2026-06-10T22:56:44-04:00
- slug: typst__typst
- verdict: partial
- eval_report_path: NONE - board_cache_only row; no local eval_report.json exists in vbidir7 or factory artifact dirs.
- senses_report_path: NONE - pb_senses.py requires eval_report.json.
- score: board-cache 16/2027 (1284 not_run, 0 skipped, 0 failed); not a Section 5 verdict.
- collection_counts: before board-cache collected=743/2027, after target=2027/2027 pending driver eval.
- hashes: submission.tar.gz sha256=C1B23803E56CB7DAC213C6C30A6B532B57CFE01868ABA16287ED17F1EF4384CF; submission.original.tar.gz sha256=2D3AB85D12C759A27AF818706B1D695B426BA36FD40C090594967B522EB68C6F; source/compile.sh sha256=D83C7ECF2E404E4CEF4EC2BFD9CD3966B29016E4096C9C843C9EB2B1110C8030
- notes: Removed collect_ignore_glob and keyword-filter block from current vbidir7 submission. Preserved eval/ nodeid normalization and JUnit bidir injection plugin. Repacked submission.tar.gz; LF-only compile.sh confirmed; bash -n passed; focused cap/filter grep clean; tar sanity clean. Staged for driver dispatch.
- change_requests: none

## Handback: CODEX-ROLLING-005 | 2026-06-10T22:56:44-04:00
- slug: facebook__zstd
- verdict: partial
- eval_report_path: NONE - board_cache_only row; no local eval_report.json exists in vbidir7 or factory artifact dirs.
- senses_report_path: NONE - pb_senses.py requires eval_report.json.
- score: board-cache 191/2788 (1084 not_run, 0 skipped, 0 failed); not a Section 5 verdict.
- collection_counts: before board-cache collected=1704/2788, after target=2788/2788 pending driver eval.
- hashes: submission.tar.gz sha256=D9DDAC1DBE31F01DA9505A694FBA50D9ED1450451B1214236588D0E3584EB30B; submission.original.tar.gz sha256=A5619C22D48EC660F6FDE14B6DA151164ED9711AC08D08DE3D7491CAC96DF389; source/compile.sh sha256=A9AEBA2F698F318617920D7060DADBB5A0EC4EEC7EF645479DE1BFC0A307B387
- notes: Removed collect_ignore_glob and keyword-filter block from current vbidir7 submission. Preserved eval/ nodeid normalization and JUnit bidir injection plugin. Repacked submission.tar.gz; LF-only compile.sh confirmed; bash -n passed; focused cap/filter grep clean; tar sanity clean. Staged for driver dispatch.
- change_requests: none

## CLAIM: CODEX-ROLLING-006 | 2026-06-11T10:30:29-04:00
- claimed_slugs: epistates__treemd, alexpovel__srgn, tree-sitter__tree-sitter, skeema__skeema
- source: rolling_queue order in docs\campaign\campaign_assignments.json after excluding in-flight, driver-hold, parked, duplicate bartib, and already-claimed staged tools through CODEX-ROLLING-005.
- guardrails: working files only under corpus\programbench\in_progress\codex_rolling_006 and append-only handback; no eval_index, assignment JSON, parked JSON, board, or lock archive certification edits.
- artifact_root: C:\Dev\Determinex\corpus\programbench\in_progress\codex_rolling_006

## Handback: CODEX-ROLLING-006 | 2026-06-11T10:30:29-04:00
- slug: epistates__treemd
- failure_class: scaffold-broken
- verdict: improved, NOT lock-eligible
- eval_report_path: NONE - local eval attempt timed out before producing eval_output; board-cache row only.
- senses_report_path: NONE - no completed eval_report for pb_senses.py.
- score: board-cache 263/2019 (997 not_run, 0 skipped, 0 failed); not recomputed and not a Section 5 verdict.
- collection_counts: before board-cache collected=1022/2019, after target=2019/2019 pending completed driver eval.
- what_changed: Removed collect_ignore_glob, keyword-based items filtering, and the extra test_keybindings/file_picker skip from compile.sh. Preserved eval/ nodeid normalization and determinex_bidir XML injection.
- raw_result_paths: attempted C:\Dev\Determinex\corpus\programbench\in_progress\codex_rolling_006\eval_output; no files produced. Containers observed: programbench-75c68eb9ac7a and replacement programbench-9379216cadd4, both stopped by Codex after bounded timeout.
- hashes: submission.tar.gz sha256=889DB7DBA8D2B63D2B2E5582080179FA8A366998003417C9D0F2952325D4AF9D; submission.original.tar.gz sha256=2AE07A5FB211995FE796DEF5A63FB50F0660250685BA8CED13C23664AE320730; source/compile.sh sha256=31F8F03E3E516D4C0E854E8D4300E1E6EEF1D52655949CDF0FCA0DA16A6D964C
- notes: Local eval command exceeded 45 minutes with no eval_output and ProgramBench respawned a replacement container after first stop. Cleaned up parent process and containers. This is staged for driver/Hetzner dispatch, not a lock claim.

## Handback: CODEX-ROLLING-006 | 2026-06-11T10:30:29-04:00
- slug: alexpovel__srgn
- failure_class: scaffold-broken
- verdict: improved, NOT lock-eligible
- eval_report_path: NONE - local eval not started after treemd consumed the local slot and hit bounded timeout.
- senses_report_path: NONE - no completed eval_report for pb_senses.py.
- score: board-cache 437/2472 (959 not_run, 0 skipped, 0 failed); not recomputed and not a Section 5 verdict.
- collection_counts: before board-cache collected=1513/2472, after target=2472/2472 pending completed driver eval.
- what_changed: Removed collect_ignore_glob and keyword-based items filtering from compile.sh. Preserved eval/ nodeid normalization and determinex_bidir XML injection.
- raw_result_paths: NONE - not locally run; staged for driver/Hetzner dispatch.
- hashes: submission.tar.gz sha256=583A27CF91AEF7046BEDC45F0F1BA1FE96F06B4DDD9497D975E0AC077BBF207A; submission.original.tar.gz sha256=78D04F2A5009F963C6053DAE1A73FE56E53492D603385F594570BE23672293CA; source/compile.sh sha256=6CCA678BE119BD5DEDC28033E72906873A39D5F8CD7E92BACF9E43FF0FF8A531
- notes: Staged only. No local eval was launched because the first tool demonstrated local runtime pressure for this batch.

## Handback: CODEX-ROLLING-006 | 2026-06-11T10:30:29-04:00
- slug: tree-sitter__tree-sitter
- failure_class: scaffold-broken
- verdict: improved, NOT lock-eligible
- eval_report_path: NONE - local eval not started after treemd consumed the local slot and hit bounded timeout.
- senses_report_path: NONE - no completed eval_report for pb_senses.py.
- score: board-cache 445/1608 (921 not_run, 0 skipped, 0 failed); not recomputed and not a Section 5 verdict.
- collection_counts: before board-cache collected=687/1608, after target=1608/1608 pending completed driver eval.
- what_changed: Removed collect_ignore_glob and keyword-based items filtering from compile.sh. Preserved eval/ nodeid normalization and determinex_bidir XML injection.
- raw_result_paths: NONE - not locally run; staged for driver/Hetzner dispatch.
- hashes: submission.tar.gz sha256=777F86FB3FC22AEFD5870E707C702A61FE28447DFB87E0E643D6CDB6F6F2DCF9; submission.original.tar.gz sha256=B91D32ED43806FC468E3AA8AA120D4368769E44C9840D5BF10B1DDF9C167821E; source/compile.sh sha256=61DE6F39BB2AD312FBE156BDCE6C22F9DA886EB08FA313DE4AF24C88E98C4157
- notes: Staged only. No local eval was launched because the first tool demonstrated local runtime pressure for this batch.

## Handback: CODEX-ROLLING-006 | 2026-06-11T10:30:29-04:00
- slug: skeema__skeema
- failure_class: scaffold-broken
- verdict: improved, NOT lock-eligible
- eval_report_path: NONE - local eval not started after treemd consumed the local slot and hit bounded timeout.
- senses_report_path: NONE - no completed eval_report for pb_senses.py.
- score: board-cache 1036/2475 (848 not_run, 0 skipped, 0 failed); not recomputed and not a Section 5 verdict.
- collection_counts: before board-cache collected=1627/2475, after target=2475/2475 pending completed driver eval.
- what_changed: Removed collect_ignore_glob and keyword-based items filtering from compile.sh. Preserved eval/ nodeid normalization and determinex_bidir XML injection.
- raw_result_paths: NONE - not locally run; staged for driver/Hetzner dispatch.
- hashes: submission.tar.gz sha256=3B540DAE2F25614BA4E45F4EF597F58D890266B2BACFA75DB4F793B57766258B; submission.original.tar.gz sha256=7DF60C52AF951D9BC67E51E39EAF60645E1659551F5B56C7821B14BC419D95E3; source/compile.sh sha256=45F67246F82E8411677A19FDC2EE542F9F4DA526C2E3D060445860B04D4E2F8F
- notes: Staged only. No local eval was launched because the first tool demonstrated local runtime pressure for this batch.

## Batch Summary: CODEX-ROLLING-006 | 2026-06-11T10:30:29-04:00
- claims_closed: epistates__treemd, alexpovel__srgn, tree-sitter__tree-sitter, skeema__skeema
- common_failure_class: scaffold-broken collection filters causing high not_run.
- common_pattern: removed collection filters; preserved determinex_bidir XML injection; compile.sh LF-only per Pattern 004.
- local_eval_status: treemd attempted locally; bounded timeout with no eval output. Other tools not locally run to avoid tying up the daily-driver box after treemd consumed the local slot. All local eval processes/containers cleaned up.
- proposed_next_action: driver dispatch all four on Hetzner and classify any post-filter failures from completed eval_reports. No lock claim.

## OVERRIDE DISPATCH RECEIPT: CODEX-ROLLING-006/007/008 | 2026-06-11T16:42:28-04:00
- authorization_context: Ryan explicitly requested Codex to use Hetzner and unblock the production workflow. This is a dispatch proposal/receipt only; driver still owns certification, eval_index, assignments, parked.json, board, locked archives, and all lock verdicts.
- preflight: Hetzner read-only poll at 2026-06-11T20:41:17Z showed 82G free on `/`, no active ProgramBench/SWE-bench eval beyond the poll command, and no running containers before launch.
- remote_programbench_pid: 1749078
- remote_parent_shell_pid: 1749077
- remote_log_path: /root/determinex-programbench/_logs/codex_r006_r007_r008_20260611.log
- remote_eval_command: /root/ProgramBench/.venv/bin/programbench eval /root/determinex-programbench/determinex_pb_codex_r006_20260611 /root/determinex-programbench/determinex_pb_codex_r007_20260611 /root/determinex-programbench/determinex_pb_codex_r008_20260611 --workers 4 --branch-workers 1 --docker-cpus 8 --force
- launched_remote_dirs:
  - /root/determinex-programbench/determinex_pb_codex_r006_20260611
  - /root/determinex-programbench/determinex_pb_codex_r007_20260611
  - /root/determinex-programbench/determinex_pb_codex_r008_20260611
- verified_submission_tarballs:
  - /root/determinex-programbench/determinex_pb_codex_r006_20260611/alexpovel__srgn.89f943b/submission.tar.gz
  - /root/determinex-programbench/determinex_pb_codex_r006_20260611/epistates__treemd.825c6dd/submission.tar.gz
  - /root/determinex-programbench/determinex_pb_codex_r006_20260611/skeema__skeema.6a76243/submission.tar.gz
  - /root/determinex-programbench/determinex_pb_codex_r006_20260611/tree-sitter__tree-sitter.5e23cca/submission.tar.gz
  - /root/determinex-programbench/determinex_pb_codex_r007_20260611/ogham__dog.721440b/submission.tar.gz
  - /root/determinex-programbench/determinex_pb_codex_r007_20260611/samtools__samtools.aa823b5/submission.tar.gz
  - /root/determinex-programbench/determinex_pb_codex_r007_20260611/stacked-git__stgit.430027d/submission.tar.gz
  - /root/determinex-programbench/determinex_pb_codex_r007_20260611/yoav-lavi__melody.f4af9b4/submission.tar.gz
  - /root/determinex-programbench/determinex_pb_codex_r008_20260611/ammarabouzor__tui-journal.2b4540d/submission.tar.gz
  - /root/determinex-programbench/determinex_pb_codex_r008_20260611/arq5x__bedtools2.dd57059/submission.tar.gz
  - /root/determinex-programbench/determinex_pb_codex_r008_20260611/ip7z__7zip.839151e/submission.tar.gz
  - /root/determinex-programbench/determinex_pb_codex_r008_20260611/tinycc__tinycc.9b8765d/submission.tar.gz
- selection_filter: staged Codex ROLLING-006/007/008 artifacts only; excluded parked, strict-locked, ceiling-confirmed, dirty active fzf work, and driver-owned state edits. These are cap/filter-removed staged tarballs from prior handbacks.
- launch_status: running as of 2026-06-11T20:42:16Z; active containers observed for epistates__treemd, tree-sitter__tree-sitter, alexpovel__srgn, and skeema__skeema.
- proposed_next_action: driver harvests /root/determinex-programbench/determinex_pb_codex_r006_20260611, /root/determinex-programbench/determinex_pb_codex_r007_20260611, and /root/determinex-programbench/determinex_pb_codex_r008_20260611 after completion; parse eval_reports directly per Section 5. No lock claim from Codex.

## WATCH RECEIPT: CODEX-ROLLING-006/007/008 + FZF V3 | 2026-06-11T16:58:22-04:00
- watch_artifact: assurance/evidence/programbench_hetzner_watch/watch_20260611_codex_r006_r008.md
- active_remote_work:
  - Codex chain running: ProgramBench PID 1749078, parent shell PID 1749077, log /root/determinex-programbench/_logs/codex_r006_r007_r008_20260611.log.
  - Claude fzf v3 also running: /root/determinex-programbench/determinex_pb_fzf_v3, log /root/fzf_v3_eval.log.
- capacity_note: Hetzner had 71G free at 2026-06-11T20:58:22Z and five ProgramBench containers visible. Codex did not launch more work; next action is harvest/watch until capacity clears.
- early_signal: Codex chain already shows recurring JUnit XML vs tests.json mismatches on skeema, srgn, tree-sitter, treemd, and dog. Likely Pattern 002-class denominator/prefix issue, but verdict must wait for completed eval_reports.
- authority_gaps_observed:
  - pb_doc_count_check previously failed because docs contained stale strict-lock references; current truth-sync work should re-run the guard before publishing any count.
  - pb_board_guard fails: hpjansson__chafa.dd4d4c1 ceiling_confirmed lacks ceiling_reason.
  - campaign_assignments still says CODEX-ROLLING-006 awaiting_handback despite handback + dispatch receipt; driver reconcile needed.
- proposed_next_action: keep watching active PIDs; on completion, download/parse eval_reports directly, route bounces/locks through driver Section 5. No lock claim from Codex.

## HARVEST POINTER: fzf v3 | 2026-06-11T17:09:30-04:00
- source_remote_report: /root/determinex-programbench/determinex_pb_fzf_v3/junegunn__fzf.b56d614/junegunn__fzf.b56d614.eval.json
- source_remote_log: /root/fzf_v3_eval.log
- local_parse_copy: scratch/harvest/fzf_v3.eval.json
- parsed_counts: passed=4156, total=4272, failed=116, not_run=0, skipped=0
- failure_branch_summary: branch 3cde1a7d975e has all 116 failures.
- verdict_proposal: bounce, NOT lock-eligible. Section 5 fails because passed != total.
- log_signature: remote log reports JUnit XML extras across multiple fzf branches, including 989 extras on branch 3cde1a7d975e; completed display score was 99, not a lock verdict.
- proposed_next_action: driver should classify branch 3cde1a7d975e failures from eval_report directly, preserve fzf as active/driver-owned while dirty per_tool_overrides exist, and avoid any lock/archive claim.

## CLAIM: CODEX-ROLLING-007 | 2026-06-11T11:55:35-04:00
- claimed_slugs: ogham__dog, samtools__samtools, stacked-git__stgit, yoav-lavi__melody
- source: rolling_queue order in docs\campaign\campaign_assignments.json after excluding in-flight, driver-hold, parked, and already-claimed staged tools through CODEX-ROLLING-006.
- guardrails: working files only under corpus\programbench\in_progress\codex_rolling_007 and append-only handback; no eval_index, assignment JSON, parked JSON, board, or lock archive certification edits.
- artifact_root: C:\Dev\Determinex\corpus\programbench\in_progress\codex_rolling_007

## Handback: CODEX-ROLLING-007 | 2026-06-11T11:55:35-04:00
- slug: ogham__dog
- failure_class: scaffold-broken
- verdict: improved, NOT lock-eligible
- eval_report_path: NONE - no local eval launched; board-cache row only.
- senses_report_path: NONE - no completed eval_report for pb_senses.py.
- score: board-cache 290/1813 (818 not_run, 0 skipped, 0 failed); not recomputed and not a Section 5 verdict.
- collection_counts: before board-cache collected=995/1813, after target=1813/1813 pending completed driver eval.
- what_changed: Removed collect_ignore_glob and keyword-based items filtering from compile.sh. Preserved eval/ nodeid normalization and determinex_bidir XML injection.
- raw_result_paths: NONE - staged for driver/Hetzner dispatch.
- hashes: submission.tar.gz sha256=08ED513B984CB2E86194D3AA84744772BD7DBAE95EBFDD9202AD36829D28E49D; submission.original.tar.gz sha256=CF07C519E8B8A9936869B366A7DBAB3AC5D060630A82F2E43AA4FB2D600A7BC8; source/compile.sh sha256=CE958C91DBB2A1A11FF784A39A89B53951AA091EB26F320F56C01FE6649DA00A
- notes: No results.xml.orig existed in extracted source. Git Bash `bash -n` passed; focused cap/filter grep clean; compile.sh LF-only; tar sanity clean. Plain `bash` maps to WSL on this workstation and WSL has no installed distro, so Git Bash was used for syntax checking.

## Handback: CODEX-ROLLING-007 | 2026-06-11T11:55:35-04:00
- slug: samtools__samtools
- failure_class: scaffold-broken
- verdict: improved, NOT lock-eligible
- eval_report_path: NONE - no local eval launched; board-cache row only.
- senses_report_path: NONE - no completed eval_report for pb_senses.py.
- score: board-cache 145/1511 (811 not_run, 0 skipped, 0 failed); not recomputed and not a Section 5 verdict.
- collection_counts: before board-cache collected=700/1511, after target=1511/1511 pending completed driver eval.
- what_changed: Removed collect_ignore_glob and keyword-based items filtering from compile.sh. Preserved eval/ nodeid normalization and determinex_bidir XML injection.
- raw_result_paths: NONE - staged for driver/Hetzner dispatch.
- hashes: submission.tar.gz sha256=3813FC80E686066180E0BD9F475056D27BB348A86EBC9944E6ABF625E6EE9555; submission.original.tar.gz sha256=C672A5568F211EB0BCFFBC88A3C25B63AD8AD9D9CDCBA6073388FB09CA925301; source/compile.sh sha256=C8C4361F0CA1BAB6D821437303617125A01251F1EED2A33E1C70F9D26D25B867
- notes: No results.xml.orig existed in extracted source. Git Bash `bash -n` passed; focused cap/filter grep clean; compile.sh LF-only; tar sanity clean. Plain `bash` maps to WSL on this workstation and WSL has no installed distro, so Git Bash was used for syntax checking.

## Handback: CODEX-ROLLING-007 | 2026-06-11T11:55:35-04:00
- slug: stacked-git__stgit
- failure_class: scaffold-broken
- verdict: improved, NOT lock-eligible
- eval_report_path: NONE - no local eval launched; board-cache row only.
- senses_report_path: NONE - no completed eval_report for pb_senses.py.
- score: board-cache 491/2380 (810 not_run, 0 skipped, 0 failed); not recomputed and not a Section 5 verdict.
- collection_counts: before board-cache collected=1570/2380, after target=2380/2380 pending completed driver eval.
- what_changed: Removed collect_ignore_glob and keyword-based items filtering from compile.sh. Preserved eval/ nodeid normalization and determinex_bidir XML injection.
- raw_result_paths: NONE - staged for driver/Hetzner dispatch.
- hashes: submission.tar.gz sha256=D29EAB22984362C012497266F0B08F360A1C42B39D1C25B79B324FF6BC818078; submission.original.tar.gz sha256=6EC24DB3F84446BB7CACA73366FB7A0917A1C9E4D214E7C32949A89A81337419; source/compile.sh sha256=343751AFBB4CE4F19446715DE9D0E9EE20A9AF256FC9F1ECE6857ADB3BB15585
- notes: No results.xml.orig existed in extracted source. Git Bash `bash -n` passed; focused cap/filter grep clean; compile.sh LF-only; tar sanity clean. Plain `bash` maps to WSL on this workstation and WSL has no installed distro, so Git Bash was used for syntax checking.

## Handback: CODEX-ROLLING-007 | 2026-06-11T11:55:35-04:00
- slug: yoav-lavi__melody
- failure_class: scaffold-broken
- verdict: improved, NOT lock-eligible
- eval_report_path: NONE - no local eval launched; board-cache row only.
- senses_report_path: NONE - no completed eval_report for pb_senses.py.
- score: board-cache 131/1607 (807 not_run, 0 skipped, 0 failed); not recomputed and not a Section 5 verdict.
- collection_counts: before board-cache collected=800/1607, after target=1607/1607 pending completed driver eval.
- what_changed: Removed collect_ignore_glob and keyword-based items filtering from compile.sh. Preserved eval/ nodeid normalization and determinex_bidir XML injection.
- raw_result_paths: NONE - staged for driver/Hetzner dispatch.
- hashes: submission.tar.gz sha256=DBE6E584624F1B71778EE8EB2BCC3BFF9D0B355168E486C1E7B34C49E719178F; submission.original.tar.gz sha256=A0052400D703F6D41ED34A6131665AB77563F5C14ADF8604050DFB4AF3741B2F; source/compile.sh sha256=BA573E038DD1984D7B67106CD9FBCB3A50ACC4DD94D691FE432B7C7BB11520F3
- notes: No results.xml.orig existed in extracted source. Git Bash `bash -n` passed; focused cap/filter grep clean; compile.sh LF-only; tar sanity clean. Plain `bash` maps to WSL on this workstation and WSL has no installed distro, so Git Bash was used for syntax checking.

## Batch Summary: CODEX-ROLLING-007 | 2026-06-11T11:55:35-04:00
- claims_closed: ogham__dog, samtools__samtools, stacked-git__stgit, yoav-lavi__melody
- common_failure_class: scaffold-broken collection filters causing high not_run.
- common_pattern: removed collection filters; preserved determinex_bidir XML injection; compile.sh LF-only per Pattern 004.
- local_eval_status: no local ProgramBench evals launched. CODEX-ROLLING-006 already demonstrated local runtime pressure with a 45-minute no-output timeout; this batch is staged for driver/Hetzner dispatch.
- disk_measurement: C:/ free 78.99 GB; T:/ free 891.68 GB.
- proposed_next_action: driver dispatch all four on Hetzner and classify any post-filter failures from completed eval_reports. No lock claim.

## Driver Unblock Packet | 2026-06-11T12:04:02-04:00
- purpose: reduce harvest/dispatch friction without Codex writing driver-owned state.
- current_driver_actions_needed:
  - Reconcile CODEX-ROLLING-006: handback exists for epistates__treemd, alexpovel__srgn, tree-sitter__tree-sitter, skeema__skeema; assignments still says handback_received=false.
  - Reconcile CODEX-ROLLING-007: handback exists for ogham__dog, samtools__samtools, stacked-git__stgit, yoav-lavi__melody; assignments has not yet recorded the batch.
  - Harvest/gate running chains: CODEX-002, ROLLING-001/002 Chain-A, ROLLING-005.
  - Dispatch staged queue in order after capacity opens: ROLLING-003, ROLLING-004, ROLLING-006, ROLLING-007, then ROLLING-008 once this handback closes.
  - Run doc-count sync after harvest: derive the strict-lock count from eval_index and rerun pb_doc_count_check before publishing any count.
- codex_status: continuing staging only; no eval_index, assignments, parked, board, or lock archive writes.

## CLAIM: CODEX-ROLLING-008 | 2026-06-11T12:04:02-04:00
- claimed_slugs: ammarabouzor__tui-journal, tinycc__tinycc, arq5x__bedtools2, ip7z__7zip
- skipped_queue_slug: ducaale__xh skipped because docs\campaign\parked.json contains parked concrete instance ducaale__xh.4a6e44f with verdict parked:moderate-bounce.
- source: rolling_queue order in docs\campaign\campaign_assignments.json after excluding in-flight, driver-hold, parked, and already-claimed staged tools through CODEX-ROLLING-007.
- guardrails: working files only under corpus\programbench\in_progress\codex_rolling_008 and append-only handback; no eval_index, assignment JSON, parked JSON, board, or lock archive certification edits.
- artifact_root: C:\Dev\Determinex\corpus\programbench\in_progress\codex_rolling_008

## Handback: CODEX-ROLLING-008 | 2026-06-11T12:04:02-04:00
- slug: ammarabouzor__tui-journal
- failure_class: scaffold-broken
- verdict: improved, NOT lock-eligible
- eval_report_path: NONE - no local eval launched; board-cache row only.
- senses_report_path: NONE - no completed eval_report for pb_senses.py.
- score: board-cache 518/2265 (772 not_run, 0 skipped, 0 failed); not recomputed and not a Section 5 verdict.
- collection_counts: before board-cache collected=1493/2265, after target=2265/2265 pending completed driver eval.
- what_changed: Removed collect_ignore_glob and keyword-based items filtering from compile.sh. Preserved eval/ nodeid normalization and determinex_bidir XML injection.
- raw_result_paths: NONE - staged for driver/Hetzner dispatch.
- hashes: submission.tar.gz sha256=21AB4A6EC0012B179D0B258E6B1C818A415EE2770AF638DB0EF393BCA37A9111; submission.original.tar.gz sha256=0C0C7A45A5A9170891B80902415CEFC11EFE2B3132FEC1B12A716977FDACE71A; source/compile.sh sha256=1C2907A947D693AD00B68CD8D8B04D193BF904D43DB1C6C6214D0E2D3B649298
- notes: No results.xml.orig existed in extracted source. Git Bash `bash -n` passed; focused cap/filter grep clean; compile.sh LF-only; tar sanity clean.

## Handback: CODEX-ROLLING-008 | 2026-06-11T12:04:02-04:00
- slug: tinycc__tinycc
- failure_class: scaffold-broken
- verdict: improved, NOT lock-eligible
- eval_report_path: NONE - no local eval launched; board-cache row only.
- senses_report_path: NONE - no completed eval_report for pb_senses.py.
- score: board-cache 1148/2341 (742 not_run, 0 skipped, 0 failed); not recomputed and not a Section 5 verdict.
- collection_counts: before board-cache collected=1599/2341, after target=2341/2341 pending completed driver eval.
- what_changed: Removed collect_ignore_glob and keyword-based items filtering from compile.sh. Preserved eval/ nodeid normalization and determinex_bidir XML injection.
- raw_result_paths: NONE - staged for driver/Hetzner dispatch.
- hashes: submission.tar.gz sha256=A91474AF5AEBC0CE0A551C2CE825DBDE143C188C5677396E78CCF8222DE75342; submission.original.tar.gz sha256=3BF7D770702F4D3955CF2694963A4531DBBDFE448D8FD008FC876AC24421CCEC; source/compile.sh sha256=D71E30220E14BEE9266C0BD6A72F1632FA6E8C099D82E41BB8E1A31B2CDD2907
- notes: No results.xml.orig existed in extracted source. Git Bash `bash -n` passed; focused cap/filter grep clean; compile.sh LF-only; tar sanity clean.

## Handback: CODEX-ROLLING-008 | 2026-06-11T12:04:02-04:00
- slug: arq5x__bedtools2
- failure_class: scaffold-broken
- verdict: improved, NOT lock-eligible
- eval_report_path: NONE - no local eval launched; board-cache row only.
- senses_report_path: NONE - no completed eval_report for pb_senses.py.
- score: board-cache 7/1061 (710 not_run, 0 skipped, 0 failed); not recomputed and not a Section 5 verdict.
- collection_counts: before board-cache collected=350/1060, after target=1060/1061 pending completed driver eval.
- what_changed: Removed collect_ignore_glob and keyword-based items filtering from compile.sh. Preserved eval/ nodeid normalization and determinex_bidir XML injection.
- raw_result_paths: NONE - staged for driver/Hetzner dispatch.
- hashes: submission.tar.gz sha256=A3E31D7DAA679DFC25045AC4EF673E211575C4E2048CC53EEC4171A86FCCAA5A; submission.original.tar.gz sha256=66DEE11D6827D1F45320941C1F326968758E8691D98B479F0127CA5AC1868EAC; source/compile.sh sha256=89A4ED1953532A9E9314F53B6225F9D816542FF7ABEAA9A8F37BAD200B200EB8
- notes: No results.xml.orig existed in extracted source. Git Bash `bash -n` passed; focused cap/filter grep clean; compile.sh LF-only; tar sanity clean.

## Handback: CODEX-ROLLING-008 | 2026-06-11T12:04:02-04:00
- slug: ip7z__7zip
- failure_class: scaffold-broken
- verdict: improved, NOT lock-eligible
- eval_report_path: NONE - no local eval launched; board-cache row only.
- senses_report_path: NONE - no completed eval_report for pb_senses.py.
- score: board-cache 151/1234 (708 not_run, 0 skipped, 0 failed); not recomputed and not a Section 5 verdict.
- collection_counts: before board-cache collected=526/1234, after target=1234/1234 pending completed driver eval.
- what_changed: Removed collect_ignore_glob and keyword-based items filtering from compile.sh. Preserved eval/ nodeid normalization and determinex_bidir XML injection.
- raw_result_paths: NONE - staged for driver/Hetzner dispatch.
- hashes: submission.tar.gz sha256=FDBC553B9795DD685090F99640EF97D32ED1571A5AC1BFEF7E3CBE42EF0D2685; submission.original.tar.gz sha256=8964F06CB5435256EF79D07AC7DF4CA6ED014880BABEFE6CAA79416116276A30; source/compile.sh sha256=5BE705F5057700F4DB719E75B805F5BDEEAFBF8E6D4D00CE7AB9C8EFCF3103DC
- notes: No results.xml.orig existed in extracted source. Git Bash `bash -n` passed; focused cap/filter grep clean; compile.sh LF-only; tar sanity clean.

## Batch Summary: CODEX-ROLLING-008 | 2026-06-11T12:04:02-04:00
- claims_closed: ammarabouzor__tui-journal, tinycc__tinycc, arq5x__bedtools2, ip7z__7zip
- skipped: ducaale__xh due parked concrete instance ducaale__xh.4a6e44f.
- common_failure_class: scaffold-broken collection filters causing high not_run.
- common_pattern: removed collection filters; preserved determinex_bidir XML injection; compile.sh LF-only per Pattern 004.
- local_eval_status: no local ProgramBench evals launched; staged for driver/Hetzner dispatch.
- disk_measurement: C:/ free 78.87 GB; T:/ free 891.68 GB.
- proposed_next_action: driver dispatch all four on Hetzner and classify any post-filter failures from completed eval_reports. No lock claim.

## EARLY FIX PACKETS: CODEX-ROLLING-006 | 2026-06-11T17:18:00-04:00
- purpose: convert completed Hetzner reports into branch-targeted repair packets before the full R006/R007/R008 chain completes.
- source_chain: remote PID `1749078`; log `/root/determinex-programbench/_logs/codex_r006_r007_r008_20260611.log`.
- latest_read_only_poll: `2026-06-11T21:16:07Z`; `/` had `71G` free; chain still running.
- active_containers_at_poll: `stacked-git__stgit.430027d`, `ogham__dog.721440b`, `samtools__samtools.aa823b5`, `epistates__treemd.825c6dd`.
- evidence_packet: `assurance/evidence/programbench_hetzner_watch/r006_early_fix_packets_20260611.md`.
- parsed_reports:
  - `alexpovel__srgn.89f943b`: passed `4120`, failed `30`, skipped `2`, not_run `0`, total `4152`; verdict `improved, NOT lock-eligible`; class `targeted behavioral + skip-parity check`.
  - `skeema__skeema.6a76243`: passed `6088`, failed `132`, skipped `692`, not_run `1`, total `6913`; verdict `improved, NOT lock-eligible`; class `behavioral + parity/skip classification + one not_run`.
  - `tree-sitter__tree-sitter.5e23cca`: passed `1336`, errors `9`, failures `60`, not_run `879`, total `2284`; verdict `bounce: collection/module wall`.
- pattern_proposal: add branch-level JUnit namespace / module collection gap as a Pattern 002 subtype or Pattern 006 after driver confirmation.
- corpus_route: feed these three bounces into `corpus/programbench/training_corpus/pb_verdict_corpus.jsonl` as rejected/repair-class signal; do not mark training_eligible true without Ryan approval.
- next_actions:
  - `srgn`: target help/usage and stdin clusters first; classify two skips before parity.
  - `skeema`: run skip census before lock grind; isolate `7c9925b9a694` non-skip behavioral cluster and database/dry-run model.
  - `tree-sitter`: repair branch `40cb72101fde` module import/collection wall before behavior work.
- no_lock_claim: none of these satisfy Section 5.

## Eval Conveyor Packet: CODEX-ROLLING-006-AUTO | 2026-06-11T17:29:37-04:00
- evidence_packet: `C:\Dev\Determinex\assurance\evidence\programbench_conveyor\CODEX-ROLLING-006-AUTO_eval_conveyor_packet.md`
- lock_claim: none by Codex; strict-looking rows remain Section 5 candidates only.
- parsed_reports:
  - `alexpovel__srgn.89f943b`: verdict `improved, NOT lock-eligible`, class `behavioral-plus-skip-census`, passed `4120`, failed `30`, errors `0`, skipped `2`, not_run `0`, total `4152`.
  - `skeema__skeema.6a76243`: verdict `bounce`, class `collection-module-wall`, passed `6088`, failed `132`, errors `0`, skipped `692`, not_run `1`, total `6913`.
  - `tree-sitter__tree-sitter.5e23cca`: verdict `bounce`, class `collection-module-wall`, passed `1336`, failed `60`, errors `9`, skipped `0`, not_run `879`, total `2284`.
- corpus_route: driver-confirmed verdict rows only; training_eligible stays false pending Ryan approval.

## Count Integrity Audit | 2026-06-11
- evidence_packet: `assurance/evidence/audits/count_audit_20260611.md`
- scope: read-only campaign-state audit; no eval_index, guard, doc, board, or locked archive edits.
- alias_finding: current eval_index has `65` strict_lock rows, but alias/native collapse yields `51` unique PB strict tasks.
- denominator_finding: current eval_index has `219` non-alias rows, `211` mapped rows, `200` unique mapped PB tasks, and `8` unmapped rows.
- duplicate_findings: `jplot`/`rs__jplot.2a54bcc` are one PB task; `trdsql`/`trdsql-d8c5ff6` are one PB task; additional strict duplicate groups are listed in the audit.
- filter_finding: strict filter-proof standard admits `8` clean PB tasks plus `1` ignored-tests-proven aligned PB task; the weaker expected_active-only scenario leaves `51/200`.
- fzf_safety: current fzf override intersects PB expected_active on `3` man-page tests; not lock-eligible as written.
- no_lock_claim: Codex produced findings only; driver/owner decides demotions and count policy.

## Terminal-State Acceptance + Parity Production Line | 2026-06-11
- phase_1_build: `scripts/pb_parity_artifact.py`
- tests: `.venv\Scripts\python.exe -m pytest tests\test_pb_parity_artifact.py -q` -> `8 passed`
- syntax: `.venv\Scripts\python.exe -m py_compile scripts\pb_parity_artifact.py` -> passed
- no_eval_index_write: Codex did not modify `corpus/programbench/eval_index.json`.
- publication_status: Codex produced artifacts only; Claude/driver owns eval_index admission and publishing.

### Phase 2 parity classification board
| tool | verdict | counts | artifact |
|---|---|---|---|
| `htmlq` | `TIER_B_NEEDS_REFERENCE_RUN` | `2057 passed, 1 skipped, 0 failed/error, 0 not_run, 2058 total` | `corpus/programbench/parity_artifacts/htmlq/parity_evidence.md` |
| `ripgrep` | `INELIGIBLE` | `2537 passed, 0 skipped, 1 failed/error, 0 not_run, 2538 total` | `corpus/programbench/parity_artifacts/ripgrep/parity_evidence.md` |
| `csview` | `TIER_B_NEEDS_REFERENCE_RUN` | `347 passed, 1 skipped, 0 failed/error, 0 not_run, 348 total` | `corpus/programbench/parity_artifacts/csview/parity_evidence.md` |
| `zip-password-finder` | `TIER_B_NEEDS_REFERENCE_RUN` | `1582 passed, 2 skipped, 0 failed/error, 0 not_run, 1584 total` | `corpus/programbench/parity_artifacts/zip-password-finder/parity_evidence.md` |
| `xq` | `INELIGIBLE` | missing raw report in best-known index | `corpus/programbench/parity_artifacts/xq/parity_evidence.md` |
| `pingu` | `TIER_B_NEEDS_REFERENCE_RUN` | `416 passed, 3 skipped, 0 failed/error, 0 not_run, 419 total` | `corpus/programbench/parity_artifacts/pingu/parity_evidence.md` |
| `quickjs` | `TIER_B_NEEDS_REFERENCE_RUN` | `3038 passed, 6 skipped, 0 failed/error, 0 not_run, 3044 total` | `corpus/programbench/parity_artifacts/quickjs/parity_evidence.md` |
| `dsq` | `INELIGIBLE` | missing raw report in best-known index; no 3-unique x 2-bidir artifact possible yet | `corpus/programbench/parity_artifacts/dsq/parity_evidence.md` |
| `chroma` | `INELIGIBLE` | `1038 passed, 14 skipped, 10 failed/error, 0 not_run, 1062 total` | `corpus/programbench/parity_artifacts/chroma/parity_evidence.md` |
| `tuc` | `TIER_B_NEEDS_REFERENCE_RUN` | `2490 passed, 8 skipped, 0 failed/error, 0 not_run, 2498 total` | `corpus/programbench/parity_artifacts/tuc/parity_evidence.md` |
| `sd` | `INELIGIBLE` | missing raw report in best-known index | `corpus/programbench/parity_artifacts/sd/parity_evidence.md` |
| `nikolassv__bartib` | `INELIGIBLE` | `1688 passed, 2 skipped, 166 failed/error, 1 not_run, 1857 total`; phantom-history caution confirmed | `corpus/programbench/parity_artifacts/nikolassv__bartib/parity_evidence.md` |

### Phase 3 reference-run queue for Claude
- `htmlq`, `csview`, `zip-password-finder`, `pingu`, `quickjs`, and `tuc` need reference-binary runs before publication.
- No Tier A static-complete artifacts were produced from the available source surfaces; missing source-location proof is routed Tier B, not promoted.

### Phase 4 ceiling evidence drafts
| tool | best score | draft artifact | note |
|---|---:|---|---|
| `amber` | `701/868` | `corpus/programbench/ceiling_evidence/amber/ceiling_reason.md` | draft only |
| `hexyl` | `940/1271` | `corpus/programbench/ceiling_evidence/hexyl/ceiling_reason.md` | draft only |
| `fd` | `1262/1825` | `corpus/programbench/ceiling_evidence/fd/ceiling_reason.md` | draft only |
| `html-to-markdown` | `971/1307` | `corpus/programbench/ceiling_evidence/html-to-markdown/ceiling_reason.md` | draft only |
| `doxygen` | `250/261` | `corpus/programbench/ceiling_evidence/doxygen/ceiling_reason.md` | weak ceiling claim; driver must adjudicate |
| `chafa` | `1351/2832` | `corpus/programbench/ceiling_evidence/chafa/ceiling_reason.md` | draft only |
| `nsh` | `3740/3778` | `corpus/programbench/ceiling_evidence/nsh/ceiling_reason.md` | draft only |
| `json-tui` | `1786/1788` | `corpus/programbench/ceiling_evidence/json-tui/ceiling_reason.md` | draft only |
| `xz` | `UNKNOWN` | `corpus/programbench/ceiling_evidence/xz/ceiling_reason.md` | raw report missing; not admissible yet |
| `richgo` | `786/950` | `corpus/programbench/ceiling_evidence/richgo/ceiling_reason.md` | `36+` not_run class remains collection-wall-suspected; route to pattern lane unless driver has stronger proof |
| `igrep` | `1094/1153` | `corpus/programbench/ceiling_evidence/igrep/ceiling_reason.md` | `59` not_run class remains collection-wall-suspected; route to pattern lane unless driver has stronger proof |

## RUN OF ALL RUNS Stage 0/1/2 First-Cycle Artifacts | 2026-06-11
- built: `scripts/pb_canonical_tasks.py`
- emitted: `corpus/programbench/canonical_tasks.json`
- emitted: `corpus/programbench/campaign_landscape.json`
- emitted: `corpus/programbench/pattern_evidence/pattern_002_collection_wall_20260611.md`
- updated: `assurance/evidence/audits/count_audit_20260611.md`
- source_authority: local PB task definitions under `T:\Dev\ProgramBench\src\programbench\data\tasks`; public cross-reference `https://programbench.com/tasks/` reports `200 instances`.
- canonical_denominator: `200`; local task dirs: `201`; excluded local fixture: `testorg__calculator.abc1234`.
- alias_rulings: `jplot` == `rs__jplot.2a54bcc`; `trdsql` == `trdsql-d8c5ff6`; `*_native` rows are internal duplicates, not PB canonical task ids.
- settled_strict_count (historical, invalidated 2026-06-30): `64/200 = 32.0%` from `scripts/pb_doc_count_check.py --verbose`; progression documented in audit as `50 -> 51 rs__jplot.2a54bcc -> 52 junegunn__fzf.b56d614`.
- fzf_section5_hinge: `corpus/programbench/locked/junegunn__fzf.b56d614/eval_report.json`, SHA256 `61b2dd202ff616ff08cac119e590b3eb21c7b127033d5e8406a74bd9b2b9cb16`, raw `4156/4156 passed`.
- jplot_section5_hinge: `corpus/programbench/locked/rs__jplot.2a54bcc/eval_report.json`, SHA256 `5c4f75e105b6a1369af3b8d45106f8c95d8f6dac702adc58de478698bdb085ef`, raw `2157/2157 passed`.

### Campaign landscape summary
| bucket | count |
|---|---:|
| `strict_lock` | 52 |
| `reference_parity` | 1 |
| `upstream_skips` | 10 |
| `ceiling_confirmed` | 20 |
| `collection-wall` | 97 |
| `behavioral` | 18 |
| `no-data` | 2 |

### Lane queue top entries
- LANE_P top: `johnkerl__miller.8d85b46`, `php__php-src.c891263`, `sqlite__sqlite.839433d`, `duckdb__duckdb.bdb65ec`, `jgm__pandoc.5caad90`.
- LANE_B top: `codesnap-rs__codesnap.f81e4f3`, `osgeo__proj.75d455c`, `dandavison__delta.acd758f`, `gromacs__gromacs.665ea4c`, `y2z__monolith.8702e66`.
- LANE_0: `nikolassv__bartib.6b9b5ce`, `noborus__ov.b96c2ba`.

### Pattern 002 verdict
- verdict: `partially_generalizes_not_yet_fanout_safe`
- evidence: `corpus/programbench/pattern_evidence/pattern_002_collection_wall_20260611.md`
- raw probes: `skeema`, `tree-sitter`, `samtools`, `dog`.
- before_counts_recorded: yes.
- after_counts_recorded: no; no scaffold/plugin fix was launched this cycle.
- next_probe: branch-level collector for PB expected ids vs pytest collected nodeids vs emitted JUnit ids, first on `tree-sitter` plus `skeema` or `dog`.

### Claude-owned continuations
- Apply any eval_index/doc corrections from the audit.
- Launch parity reference chain on Hetzner idle slot.
- Decide whether to admit/publish parity and ceiling lines.
- Dispatch Pattern 002 collector/eval probes; Codex did not launch remote jobs.

## Artifact-First Index Refresh After Harvest | 2026-06-11T18:12:30-04:00
- regenerated_index: `corpus/programbench/best_known_state.json`
- index_coverage_after_harvest: tools `203`, reports `294`, tarballs `311`, override_roots `223`, conveyor_packets `16`
- strict_candidate_surface:
  - `rs__jplot.2a54bcc`: best_report `scratch\harvest\artifact_first\rs__jplot.2a54bcc.v3.eval.json`, raw `2157/2157`, delta `0`; driver Section 5 required before any count change.
- top10_board_updated: `assurance/evidence/programbench_best_state/top10_smallest_delta_20260611.md`
- external_probe: `--include-external --no-hashes` against `T:/determinex-programbench`/`T:/determinex-staging` timed out after 300 seconds; committed index is repo-local plus scratch harvest artifacts.
- external_next_action: add bounded external manifest/cache rather than live-walking the whole T: archive.
- no_lock_claim: Codex did not write eval_index or certify jplot.

## Hetzner Watch Receipt | 2026-06-11T17:30:27-04:00
- evidence_packet: `assurance/evidence/programbench_hetzner_watch/watch_20260611T213027Z.md`
- status: read-only poll; no process/container changes.
- active_eval_lanes: Codex R006/R007/R008 chain, Claude fzf v4, Claude jplot v3.
- completed_codex_reports_visible: srgn, skeema, tree-sitter only; no new R007/R008 reports visible at poll time.

## Artifact-First Ranking Layer | 2026-06-11T18:05:29-04:00
- built: `scripts/pb_best_state_index.py`
- built: `scripts/pb_tool_brief.py`
- regenerated_index: `corpus/programbench/best_known_state.json`
- top10_board: `assurance/evidence/programbench_best_state/top10_smallest_delta_20260611.md`
- first_brief: `assurance/evidence/programbench_briefs/htmlq_brief.md`
- index_coverage: tools `203`, reports `285`, tarballs `311`, override_roots `223`, conveyor_packets `6`
- top10_smallest_delta:
  - `htmlq`: delta `1`, raw `2057/2058`, status `upstream_skips`
  - `csview`: delta `1`, raw `347/348`, status `upstream_skips`
  - `ripgrep`: delta `2`, raw `2536/2538`, status `upstream_skips`
  - `elfcat`: delta `3`, raw `1288/1291`, status `upstream_skips`
  - `quickjs`: delta `6`, raw `3038/3044`, status `upstream_skips`
  - `chroma`: delta `7`, raw `524/531`, status `upstream_skips`
  - `tuc`: delta `8`, raw `2490/2498`, status `upstream_skips`
  - `doxygen__doxygen`: delta `11`, raw `250/261`, status `ceiling_confirmed`
  - `alexpovel__srgn`: delta `32`, raw `4120/4152`, status `board_cache_only`
  - `nikolassv__bartib`: delta `43`, raw `886/929`, status `ceiling_confirmed_near_lock`
- note: index surfaced `203` non-alias eval_index rows versus expected campaign count `200`; no campaign truth JSON was edited.
- no_lock_claim: ranking layer only; Section 5 still gates all count changes.

## Eval Conveyor Packet: ARTIFACT-FIRST-HARVEST-001 | 2026-06-11T18:10:43-04:00
- evidence_packet: `C:\Dev\Determinex\assurance\evidence\programbench_conveyor\ARTIFACT-FIRST-HARVEST-001_eval_conveyor_packet.md`
- lock_claim: none by Codex; strict-looking rows remain Section 5 candidates only.
- parsed_reports:
  - `arq5x__bedtools2.dd57059`: verdict `improved, NOT lock-eligible`, class `behavioral-plus-skip-census`, passed `2124`, failed `22`, errors `0`, skipped `40`, not_run `0`, total `2186`.
  - `junegunn__fzf.b56d614.v4`: verdict `improved, NOT lock-eligible`, class `targeted-behavioral`, passed `4156`, failed `58`, errors `0`, skipped `0`, not_run `0`, total `4214`.
  - `ogham__dog.721440b`: verdict `improved, NOT lock-eligible`, class `behavioral-plus-skip-census`, passed `70`, failed `3634`, errors `0`, skipped `10`, not_run `0`, total `3714`.
  - `rs__jplot.2a54bcc.v3`: verdict `strict-lock-candidate`, class `section-5-verification-required`, passed `2157`, failed `0`, errors `0`, skipped `0`, not_run `0`, total `2157`.
  - `samtools__samtools.aa823b5`: verdict `bounce`, class `collection-module-wall`, passed `46`, failed `2820`, errors `754`, skipped `18`, not_run `0`, total `3638`.
- corpus_route: driver-confirmed verdict rows only; training_eligible stays false pending Ryan approval.

## Pattern 002 Diagnostic Collector | 2026-06-11T21:43:53-04:00
- built: `scripts/pb_collection_probe.py`
- tests: `.venv\Scripts\python.exe -m pytest tests\test_pb_collection_probe.py -q` -> `5 passed`.
- run: `.venv\Scripts\python.exe scripts\pb_collection_probe.py tree-sitter skeema`
- summary: `assurance/evidence/programbench_collection_probe/collection_probe_summary.md`
- raw_outputs:
  - `assurance/evidence/programbench_collection_probe/tree-sitter_collection_probe.json`
  - `assurance/evidence/programbench_collection_probe/skeema_collection_probe.json`
- source_reports:
  - `tree-sitter__tree-sitter`: `T:\determinex-staging\hetzner_returns\hetzner_full_200_20260606\results\tree-sitter__tree-sitter.5e23cca.eval.json`
  - `skeema__skeema`: `T:\determinex-programbench\hetzner_results\hetzner_full_200_20260606\results\skeema__skeema.6a76243.eval.json`
- classified_gap_total: `2677`
  - TRUE collection wall: `1994/2677 = 74.5%`
  - emission loss: `462/2677 = 17.3%`
  - behavioral: `221/2677 = 8.3%`
- tool_split:
  - `tree-sitter__tree-sitter`: raw report `445 passed / 231 failure / 10 error / 1 skipped / 921 not_run`; classified split `11 collection / 31 emission / 191 behavioral`; two branches are `COLLECTION_WALL_UNMAPPED` because pytest reported collection errors without emitting collected nodeid sets (`unmapped expected-emitted gap 1201`).
  - `skeema__skeema`: raw report `1654 passed / 43 failure / 130 skipped / 805 not_run`; classified split `1983 collection / 431 emission / 30 behavioral`; no unmapped branches.
- decision_signal: Pattern 002 is not single-fix fan-out safe. `skeema` is scaffold/cap-prefix dominated and likely batch-swingable; `tree-sitter` needs separate collection-error/module-import handling plus behavioral repair. Do not publish counts or mass-dispatch off this collector alone.
- eval_index_write: none.

## fzf #52 Reconciliation + Pattern 002 Track A/B Status | 2026-06-11T21:57:22-04:00
- fzf_audit_append: `assurance/evidence/audits/count_audit_20260611.md`
- fzf_verdict_evidence: `ALIGNED-with-evidence`; no fzf demotion from the three man-page tests.
  - PB loader normalizes ignored dict rows: `T:\Dev\ProgramBench\src\programbench\utils\load_data.py:41-47`.
  - PB expected-active subtracts ignored IDs: `T:\Dev\ProgramBench\src\programbench\eval\eval.py:152-153`, `eval_batch.py:181`.
  - Static pytest-nodeid diff for `junegunn__fzf.b56d614`: `86` filtered PB expected IDs, `86` PB ignored, `0` expected_active intersections.
  - Three man-page IDs are filtered and absent from locked report, but are PB ignored with `gold_fail` on branch `3cde1a7d975e`.
- pattern002_track_a_census: `corpus/programbench/pattern_evidence/collection_wall_census.md`
  - source roster: current `campaign_landscape.json` `collection-wall|partial-collection`, machine count `100` versus pasted `97`.
  - successful probes: `99`; unresolved: `1` bad best-state pointer (`osgeo__proj` -> xz locked report).
  - pile counts: `CAP_TRUNCATED=25`, `EMISSION_LOSS=10`, `TRUE_WALL_BEHAVIORAL=63`, `UNKNOWN=1`.
- pattern002_track_b_cap_fix:
  - scaffold fix applied: `scripts/pb_compile_template.py` no longer emits `del items[400:]`.
  - lint fix applied: `scripts/pb_compile_lint.py` now errors on `del items[400:]` / `items[:400]`.
  - verification: rendered `assurance/evidence/programbench_pattern002/pb_compile_template_check.sh`; cap grep empty; `pb_compile_lint.py` OK on rendered template and `skeema__skeema.6a76243` override.
  - skeema validation from existing R006 report `scratch/harvest/r006/skeema__skeema.6a76243.eval.json`: `6088 passed / 132 failed / 692 skipped / 1 not_run / 6913 total`.
  - capped branch check: `34521d0dbd17 664/664`, `41d65330ce2f 895/895`, `7c9925b9a694 435/435`, `a903bacb7595 1235/1585`; result `partial`, not full Track B success because `a903bacb7595` still misses `350`.
- pattern002_track_c_emission_status:
  - no plugin-level fix completed this cycle.
  - clean validation target identified: `ivanceras__svgbob` branch `1b6f0d2f3f1f` shows `81 collected / 81 emitted` but `B-C=81`, indicating namespace/prefix emission mismatch rather than behavioral loss.
- no_eval_index_write: true.

## ADDENDUM C CLAIM - N1 figlet | 2026-06-12T00:00:00-04:00
- tool: `cmatsuoka__figlet.202a0a8`
- batch_id: `ADDENDUM_C_N1`
- claim_type: direct user assignment
- contract: executor-only; assigned tool directory plus `CODEX_HANDBACK.md`; no eval_index/board/locked/parked writes.

### ADDENDUM C N1 handback - figlet | 2026-06-12T09:46:10-04:00
- tool: `cmatsuoka__figlet.202a0a8`
- seed_integrity:
  - `pb_tool_brief.py` best paths contain assigned slug but are stale (`956/1320`); current authoritative state read from `eval_index.json` points to the b2v2 harvest report below.
  - source_report: `T:/determinex-programbench/hetzner_results/b2v2_harvest/determinex_pb_cmatsuoka_figlet_202a0a8/cmatsuoka__figlet.202a0a8/cmatsuoka__figlet.202a0a8.eval.json`
  - source_report_sha256: `FCAD2A9310C2AA6D88F578DDA4487DD7D1856E02ECEB7D734E9AF14FBBBC4359`
- current_report_counts_direct_parse:
  - passed: `2084`
  - failed: `4`
  - skipped: `0`
  - not_run: `0`
  - total: `2088`
- remaining_failures_before_patch:
  - `eval.tests.test_externalized_figlet.test_ext_024_list_of_control_files_matches_reference`
  - `tests.test_externalized_figlet.test_ext_024_list_of_control_files_matches_reference`
  - `eval.tests.test_help_usage.test_help_usage_is_multiline_and_indented`
  - `tests.test_help_usage.test_help_usage_is_multiline_and_indented`
- failure_class: `recipe-miss`
- diagnosis:
  - Help usage failure was a real formatting mismatch: PB expected `[ -d fontdirectory ]` to appear on an indented continuation line after `Usage:`.
  - Externalized #024 invokes `-d FONTDIR -I5` and expects `flc`; other PB branches already pass with generic `-I5` expectations of `flf2` / `flf2 tlf2`, so the fix is limited to the explicit-font-directory case.
- changes:
  - `figlet.c`: moved `[ -d fontdirectory ]` from the first usage line to an indented continuation line.
  - `figlet.c`: added `explicitfontdir` flag set by `-d`; `printinfo(5)` prints `flc` only when `-d` was explicitly supplied, preserving existing generic `-I5` behavior.
- staged_tarball: `corpus/programbench/per_tool_overrides/cmatsuoka__figlet.202a0a8/submission.addendum_c_n1.tar.gz`
- staged_tarball_sha256: `5477D9AAD4E57E6E63671D152EEDDACB66A99477A9815C434D656CF86898B920`
- compile_sh_sha256: `0D3C40CC675AFECF9F631FE8EE8A680F5A59CC19D2A395A52C6A8F28349453CD`
- figlet_c_sha256: `1A2B5BC454DC532DB876D894B50744D84D9B9A45AA87C6B841F09A2BC93FA521`
- local_eval: not run; `programbench_image_preflight.py` reports missing local image `programbench/cmatsuoka_1776_figlet.202a0a8:task_cleanroom`.
- verification:
  - `pb_compile_lint.py corpus/programbench/per_tool_overrides/cmatsuoka__figlet.202a0a8/compile.sh`: `[OK]`
  - Git Bash `bash -n corpus/programbench/per_tool_overrides/cmatsuoka__figlet.202a0a8/compile.sh`: passed
  - `programbench_image_preflight.py ... --submission-tar ...`: failed only on missing local cleanroom image
  - `pb_override_scan.py --guard`: passed, `0` official-lock override violations
  - `pb_board_guard.py`: passed, `0` violations
  - `pb_senses_guard.py`: passed, no static-RE references
  - `day_one_public_claim_scanner.py --root .`: passed
- proposed_verdict: `staged for driver dispatch`; Codex does not claim lock.
- no_eval_index_write: true.

### ADDENDUM C N5 skip conversions status | 2026-06-12T09:46:10-04:00
- requested_input: `SKIP_CONVERSION_TARGETS.md`
- status: blocked pending Driver handoff; neither `docs/campaign/SKIP_CONVERSION_TARGETS.md` nor root `SKIP_CONVERSION_TARGETS.md` exists locally.
- no_eval_index_write: true.

## ADDENDUM C CLAIM - N2 handlr | 2026-06-12T09:55:00-04:00
- tool: `chmln__handlr.90e78ba`
- batch_id: `ADDENDUM_C_N2`
- claim_type: direct user assignment
- contract: executor-only; assigned tool directory plus `CODEX_HANDBACK.md`; no eval_index/board/locked/parked writes.

### ADDENDUM C N2 handback - handlr | 2026-06-12T10:12:00-04:00
- tool: `chmln__handlr.90e78ba`
- seed_integrity:
  - `pb_tool_brief.py chmln__handlr.90e78ba` returned `tool not found in best_known_state`; seed gap recorded.
  - canonical `eval_index.json` row is slug `chmln__handlr`, source report path contains assigned slug `chmln__handlr.90e78ba`, and assigned override dir exists at `corpus/programbench/per_tool_overrides/chmln__handlr.90e78ba`.
  - source_report: `T:/determinex-programbench/hetzner_results/b2v2_harvest/determinex_pb_chmln_handlr_90e78ba/chmln__handlr.90e78ba/chmln__handlr.90e78ba.eval.json`
  - source_report_sha256: `7CC032403BD9F5DBD11BC381222422079B841A191076B78B104B3392B553EBAB`
- current_report_counts_direct_parse:
  - passed: `1800`
  - failed: `12`
  - skipped: `0`
  - not_run: `0`
  - total: `1812`
- remaining_failures_before_patch:
  - open/launch class: `test_open_with_handler_that_spawns_process`, `test_open_text_file`, `test_open_multiple_files` under both `eval.tests.*` and `tests.*`.
  - extension class: `test_set_by_extension` under both namespaces.
  - selector fallback class: `test_selector_process_spawn_failure_falls_back_to_first_handler` under both namespaces.
  - unset/get class: `test_unset_removes_and_get_fails` under both namespaces.
- failure_class: `recipe-miss`
- changes:
  - `src/common/mime_types.rs`: deterministic `.txt` to `text/plain` mapping for explicit extension input and path-based MIME detection, avoiding missing/ambiguous host MIME DB behavior.
  - `src/apps/user.rs`: selector-process failure now falls back to the first configured handler; `get` output now reports only explicit user/wildcard defaults instead of resurrecting system associations after `unset`.
  - `src/common/desktop_entry.rs`: non-terminal spawn handles missing `/bin/true` path via `true` and shell-script interpreter-missing cases via `/bin/sh <script> ...`.
- focused_docker_repro:
  - image: `programbench/chmln_1776_handlr.90e78ba:task`
  - result: compiled candidate, `set .txt test.desktop`, `get text/plain`, `open <tmp>/a.txt`, `unset text/plain`, and post-unset `get text/plain` all behaved as expected (`unset_get_failed_ok`).
- local_eval: not run as official ProgramBench eval; `programbench_image_preflight.py` reports missing local image `programbench/chmln_1776_handlr.90e78ba:task_cleanroom`.
- local_build_notes:
  - Linux task-image compile smoke passed.
  - Windows `cargo build --release` is not a valid oracle for this crate; it fails on Linux-only APIs (`std::os::unix`, `xdg::BaseDirectories`, `xdg_mime::SharedMimeInfo`).
- staged_tarball: `corpus/programbench/per_tool_overrides/chmln__handlr.90e78ba/submission.addendum_c_n2.tar.gz`
- staged_tarball_sha256: `FA63AB94CF3D94B4838E15B73720E7645D9330676ED8BFA549A8AA6837164EBB`
- compile_sh_sha256: `A471E6F794464BDAECF2F6A4329D2CBF9B00822B7008E632D36B0A455BDFEC9F`
- source_hashes:
  - `src/apps/user.rs`: `F31745208B36DCD35B56ABE21A7CE59ADF47B824EDD49C41BAECDE3118B80EC4`
  - `src/common/desktop_entry.rs`: `BFFC18C7B54A4EB165F6771A5F8D6ECAEC8ACF5A978810BC917B78156F944BCE`
  - `src/common/mime_types.rs`: `08CE4F6516EA60543CD6C5EB25EEFD27970373C7B68DFDF3240C06E77D9E2B64`
- verification:
  - `pb_compile_lint.py corpus/programbench/per_tool_overrides/chmln__handlr.90e78ba/compile.sh`: `[OK]`
  - Git Bash `bash -n corpus/programbench/per_tool_overrides/chmln__handlr.90e78ba/compile.sh`: passed
  - clean tarball content check: no `target/`, `build.err`, generated `conftest.py`, generated `pytest.ini`, generated `executable`, or cargo-home artifact.
  - `pb_override_scan.py --guard`: passed, `0` official-lock override violations
  - `pb_board_guard.py`: passed, `0` violations
  - `day_one_public_claim_scanner.py --root .`: passed
- proposed_verdict: `staged for driver dispatch`; Codex does not claim lock.
- no_eval_index_write: true.

## ADDENDUM C CLAIM - N3 crowbook | 2026-06-12T10:18:00-04:00
- tool: `crowdagger__crowbook.ea214d7`
- batch_id: `ADDENDUM_C_N3`
- claim_type: direct user assignment
- contract: executor-only; assigned tool directory plus `CODEX_HANDBACK.md`; no eval_index/board/locked/parked writes.

### ADDENDUM C N3 handback - crowbook | 2026-06-12T10:31:00-04:00
- tool: `crowdagger__crowbook.ea214d7`
- seed_integrity:
  - `pb_tool_brief.py crowdagger__crowbook.ea214d7` returned `tool not found in best_known_state`; seed gap recorded.
  - canonical `eval_index.json` row is slug `crowdagger__crowbook`, source report path contains assigned slug `crowdagger__crowbook.ea214d7`, and assigned override dir exists at `corpus/programbench/per_tool_overrides/crowdagger__crowbook.ea214d7`.
  - source_report: `T:/determinex-programbench/hetzner_results/b2v2_harvest/determinex_pb_crowdagger_crowbook_ea214d7/crowdagger__crowbook.ea214d7/crowdagger__crowbook.ea214d7.eval.json`
  - source_report_sha256: `89F03C02EDA7E754EBBAC94247D2C59997BD8A8354A72C756A04D900FCE98770`
- current_report_counts_direct_parse:
  - passed: `1760`
  - failed: `14`
  - skipped: `0`
  - not_run: `0`
  - total: `1774`
- remaining_failures_before_patch:
  - LaTeX/rendering: description list rendering, custom pageref internal links, subscript/superscript token handling, print `tex.template`.
  - CLI/help: `-q` and `--quiet` missing `CROWBOOK` in no-book output; baseline help text exact fixture mismatch.
- failure_class: `algorithmic + recipe-miss`
- changes:
  - `compile.sh`: wrapper now uses `exec -a "crowbook"` so clap/help sees the upstream binary name instead of harness path `executable`.
  - `src/bin/real_main.rs`: quiet/no-book path prints the `CROWBOOK` header before the error so boolean quiet flags parse as expected by the argparse validation tests.
  - `src/lib/parser.rs`: initializes `parser.subscript` from the existing markdown superscript extension option and wires `options.extension.subscript` to `self.subscript`.
- pre_existing_current_tree_note:
  - Current override tree already contains `\usepackage{enumitem}` in `templates/latex/template.tex` and a description renderer format string that should emit `\begin{description}[style=nextline, labelwidth=0pt]`; the harvested report did not show those, so those failures may be stale relative to the current source tree.
- local_eval: not run; `programbench_image_preflight.py` reports missing local image `programbench/crowdagger_1776_crowbook.ea214d7:task_cleanroom`, and no local `crowbook` task image is present.
- staged_tarball: `corpus/programbench/per_tool_overrides/crowdagger__crowbook.ea214d7/submission.addendum_c_n3.tar.gz`
- staged_tarball_sha256: `0252EAC89A373D3803CB733B2FFCD8B9143262FC2B2144BDBB70669E96E2BA8D`
- compile_sh_sha256: `88DCB25126EC59A61BF9EB422F7694F2E5974EAA36818208EB153AB4BCD64B36`
- source_hashes:
  - `src/bin/real_main.rs`: `51ED9ECEE675EC289A2D6A42C264A30EA904070C1A7805D05728B30ED27D9536`
  - `src/lib/parser.rs`: `9CDAE96FC429C2EAB50A949292CE2DF2D770842216C51DFD9044C3BB2AA881A9`
- verification:
  - `pb_compile_lint.py corpus/programbench/per_tool_overrides/crowdagger__crowbook.ea214d7/compile.sh`: `[OK]`
  - Git Bash `bash -n corpus/programbench/per_tool_overrides/crowdagger__crowbook.ea214d7/compile.sh`: passed
  - clean tarball content check: no `target/`, `build.err`, generated `conftest.py`, generated `pytest.ini`, generated `executable`, or cargo-home artifact.
  - `pb_override_scan.py --guard`: passed, `0` official-lock override violations
  - `pb_board_guard.py`: passed, `0` violations
  - `day_one_public_claim_scanner.py --root .`: passed
- proposed_verdict: `partial/staged for driver dispatch`; not lock-eligible until full eval proves all 14 failures clear.
- no_eval_index_write: true.

## ADDENDUM C batch summary | 2026-06-12T10:36:00-04:00
- closed_claims:
  - `N1 cmatsuoka__figlet.202a0a8`: staged for Driver dispatch; local official eval blocked by missing `task_cleanroom` image.
  - `N2 chmln__handlr.90e78ba`: staged for Driver dispatch; focused Docker repro passed in available task image; local official eval blocked by missing `task_cleanroom` image.
  - `N3 crowdagger__crowbook.ea214d7`: partial staged for Driver dispatch; not lock-eligible without full eval.
- skip_conversions:
  - `SKIP_CONVERSION_TARGETS.md` not present in root or `docs/campaign`; no FIXABLE-DEP edits applied.
- unstarted_from_addendum_c:
  - `N4 ducaale__xh.4a6e44f`: not claimed in this batch; no files touched.
- machine_state_writes: none.
- no_eval_index_write: true.

## DRIVER_FORWARD F0 read-only audit + change request | 2026-06-12T10:13:49-04:00
- trigger: user pasted Driver Forward F0-F5. Protocol re-read confirms Codex cannot write `eval_index.json`, `campaign_assignments.json`, board, locked archives, or shared guard scripts except as a change request.
- current_count_guard:
  - command: `.venv\Scripts\python.exe scripts\pb_doc_count_check.py --verbose`
  - result: `eval_index canonical lock count: 51 (25.5%)`; docs matched eval_index.
- requested_guard_rule: `upstream_skips REQUIRES official_failed == 0 AND official_not_run == 0`.
- read_only_full_index_audit_result:
  - violation_count: `2`
  - `nikoladucak__caps-log`: `878/2266`, `failed=1328`, `not_run=18`, `skipped=42`, `eval_report_path=None`; requested reclass target is `factory_accepted` with `tui_skip` annotation.
  - `direnv__direnv`: `1930/1946`, `failed=14`, `not_run=0`, `skipped=2`, `eval_report_path=scratch/pb_f2_direnv_eval_out_v2/pb_f2_direnv_local/direnv__direnv.02040c7/direnv__direnv.02040c7.eval.json`; cannot remain `upstream_skips` under the requested rule because `failed != 0`.
- change_request:
  - Driver should update `corpus/programbench/eval_index.json` for the two violating rows, documenting the demotion/reclass notes.
  - Driver should add a `pb_doc_count_check.py` guard assertion that rejects any `upstream_skips` row with nonzero failed or not_run.
  - Driver should rerun full doc guard/board guard after the state change.
- Codex_boundary: no machine-state writes performed; no guard script edits performed.
- no_eval_index_write: true.

## CAMPAIGN_DIRECTIVE_001 Lane B1 svgbob b2 Local Eval | 2026-06-11T23:15:00-04:00
- tool: `ivanceras__svgbob.6d00ad9`
- driver_context: Hetzner read-only poll at `2026-06-12T02:37:32Z` showed `/` `61G` free, no active ProgramBench/SWE-bench process beyond the poll command, and no running Docker containers listed.
- local_eval_input: `scratch/pb_pattern002_svgbob/ivanceras__svgbob.6d00ad9/submission.tar.gz`
- local_eval_report: `scratch/pb_pattern002_eval_out_b2/pb_pattern002_svgbob/ivanceras__svgbob.6d00ad9/ivanceras__svgbob.6d00ad9.eval.json`
- durable_eval_report_copy: `corpus/programbench/per_tool_overrides/ivanceras__svgbob.6d00ad9/pattern002_emission/local_b2_eval_report.json`
- durable_eval_report_sha256: `DACA63280F7D8920D76B896B1DEB6D82BC06FFFFEC4B898860896D65FCF0DBAB`
- command: `cd T:\Dev\ProgramBench; uv run programbench eval C:\Dev\Determinex\scratch\pb_pattern002_svgbob --filter "ivanceras__svgbob" --workers 1 --branch-workers 1 --docker-cpus 2 --force -o C:\Dev\Determinex\scratch\pb_pattern002_eval_out_b2`
- direct_parse:
  - passed: `948`
  - total_rows: `948`
  - failed: `0`
  - skipped: `0`
  - not_run: `0`
  - executable_hash: `7215c19ec8b7a588043c0f9ee49115de35ea67fe826e977a421f9db66f73bdcf`
- branch_sanity_vs_tests_json:
  - `1b6f0d2f3f1f`: PB expected `81`; report rows `162`; missing expected `0`; extras `81`; all passed.
  - `bbc3caab3762`: PB expected `393`; report rows `786`; missing expected `0`; extras `393`; all passed.
- warning_class: bidir duplicate extras (`tests.*` plus `eval.tests.*`) trigger ProgramBench warnings `test(s) in JUnit XML not in tests.json`; expected IDs are all present, and there are no `not_run` rows.
- b2_change: kept B1 lifecycle bidir hooks and restored argv0 preservation with `#!/usr/bin/env bash` + `exec -a "$0" /usr/local/bin/svgbob "$@"`, fixing the eight `svgbob-build` vs `executable-build` help-output failures from b1.
- tarball: `corpus/programbench/per_tool_overrides/ivanceras__svgbob.6d00ad9/submission.pattern002_b2.tar.gz`
- tarball_sha256: `17539F2ADC3C79D57104EFD9FA2C41AA87902173EDB469B59B79E5ED20482455`
- verdict: `strict-lock-candidate` for Driver Section 5 verification; Codex does not claim count.
- no_eval_index_write: true.

## CAMPAIGN_DIRECTIVE_001 Executor Lanes A1/B1 | 2026-06-11T22:38:00-04:00
- directive_source: `C:\Users\ryang\.codex\attachments\44827f57-841a-4f22-8e31-12f527307dfe\pasted-text.txt`
- contract: Executor-only writes; no `eval_index.json`, board, assignments, locked archive, or Driver STATUS BLOCK edits.

### Lane A1 - skeema second-loss diagnosis and patch
- tool: `skeema__skeema.6a76243`
- branch: `a903bacb7595`
- source_report: `scratch/harvest/r006/skeema__skeema.6a76243.eval.json`
- PB_tests_json: `T:\Dev\ProgramBench\src\programbench\data\tasks\skeema__skeema.6a76243\tests.json`
- evidence_dir: `corpus/programbench/per_tool_overrides/skeema__skeema.6a76243/pattern002_a903bacb7595/`
- ID_lists:
  - expected_active: `expected_active_ids.txt`
  - collected: `collected_ids.txt`
  - emitted: `emitted_ids.txt`
  - missing: `missing_expected_active_ids.txt`
  - before_xml: `before_results.xml`
  - after_xml: `after_results.xml`
- diagnosis: remaining post-uncap gap is not the old 400 cap. Against PB `expected_active`, only one active ID was missing: `tests.test_tengo_helpers.test_connection_ipv4_with_explicit_port@mysql_serial`. Pytest/JUnit emitted the unsuffixed base ID `tests.test_tengo_helpers.test_connection_ipv4_with_explicit_port`.
- counts:
  - expected_all: `1585`
  - ignored: `1043`
  - expected_active: `542`
  - collected pytest IDs in report: `1235`
  - emitted XML/report IDs: `2470`
  - missing expected_active before alias: `1`
  - missing expected_active after offline alias transform: `0`
  - expected_active present before alias: `541/542`
  - expected_active present after alias: `542/542`
  - active_collected_failed remains: `26` behavioral failures
- change: per-tool `compile.sh` adds a targeted JUnit alias for `test_connection_ipv4_with_explicit_port@mysql_serial` when the unsuffixed `tests.test_tengo_helpers` testcase is present.
- tarball: `corpus/programbench/per_tool_overrides/skeema__skeema.6a76243/submission.pattern002_a1.tar.gz`
- tarball_sha256: `9F03718BF4C0FEB7D414B3FCD7FAF536ABFD61C934B19E7C6C3EA4B9FCB6720E`
- verdict: staged for driver dispatch; not a lock claim. Gate signal is expected-active XML coverage `542/542`; Driver still must Section 5 parse any full eval.

### Lane B1 - svgbob emission validation and patch
- tool: `ivanceras__svgbob.6d00ad9`
- branch: `1b6f0d2f3f1f`
- source_report: `T:\determinex-programbench\hetzner_results\hetzner_svgbob_argv0_v4_20260527\results\ivanceras__svgbob.6d00ad9.eval.json`
- evidence_dir: `corpus/programbench/per_tool_overrides/ivanceras__svgbob.6d00ad9/pattern002_emission/`
- raw_xml_before: `before_results.xml`
- transformed_xml_after: `after_results.xml`
- diagnosis: raw JUnit XML contains `tests.*` classnames only, while PB expected `eval.tests.*` for branch `1b6f0d2f3f1f`; existing bidir injection did not run soon enough or was not loaded in that artifact.
- counts:
  - expected: `81`
  - raw XML testcase IDs: `81`
  - transformed XML testcase IDs: `162`
  - B-C before transform: `81`
  - B-C after transform: `0`
  - expected missing before: `81`
  - expected missing after: `0`
- change: per-tool `compile.sh` updates embedded `determinex_bidir` injection to run via `pytest_sessionfinish` and `pytest_unconfigure`, in addition to `atexit`, and simplifies the svgbob executable wrapper to POSIX `exec /usr/local/bin/svgbob "$@"` to clear the pre-existing `exec -a` under `#!/bin/sh` lint error.
- tarball: `corpus/programbench/per_tool_overrides/ivanceras__svgbob.6d00ad9/submission.pattern002_b1.tar.gz`
- tarball_sha256: `C8953FD1900682453B2D969E9BE056A851CF6F1A23BF876367673563D79B7949`
- verdict: staged for driver dispatch; not a lock claim. Offline raw-XML validation shows namespace emission fix drops B-C `81 -> 0`; full eval still required.

### Verification
- `pb_compile_lint.py`:
  - `[OK] corpus\programbench\per_tool_overrides\skeema__skeema.6a76243\compile.sh`
  - `[OK] corpus\programbench\per_tool_overrides\ivanceras__svgbob.6d00ad9\compile.sh`
- shell syntax:
  - Git Bash `bash -n` passed for both compile scripts.
- embedded Python:
  - Python `ast.parse` passed for extracted conftest/plugin heredoc blocks.
- LF check:
  - skeema `compile.sh`: `0` CRLF, `163` LF
  - svgbob `compile.sh`: `0` CRLF, `161` LF
- tarball content check:
  - `submission.pattern002_a1.tar.gz`: no `pattern002` evidence dir and no nested `.tar.gz`
  - `submission.pattern002_b1.tar.gz`: no `pattern002` evidence dir and no nested `.tar.gz`
- no_eval_index_write: true.
