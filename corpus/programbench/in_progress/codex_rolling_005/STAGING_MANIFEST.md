# CODEX-ROLLING-005 Staging Manifest

Timestamp: 2026-06-10T22:56:44-04:00

Scope: rolling queue staging only. No local eval was run and no lock verdict is proposed.

Claimed slugs:
- `antonmedv__walk`
- `paradigmxyz__solar`
- `typst__typst`
- `facebook__zstd`

Source tarballs:
- `antonmedv__walk`: `T:\determinex-programbench\determinex_pb_walk_vbidir7\antonmedv__walk.bf802ef\submission.tar.gz`
- `paradigmxyz__solar`: `T:\determinex-programbench\determinex_pb_solar_vbidir7\paradigmxyz__solar.5190d0e\submission.tar.gz`
- `typst__typst`: `T:\determinex-programbench\determinex_pb_typst_vbidir7\typst__typst.88356d0\submission.tar.gz`
- `facebook__zstd`: `T:\determinex-programbench\determinex_pb_zstd_vbidir7\facebook__zstd.1168da0\submission.tar.gz`

Edits:
- Removed `collect_ignore_glob` and keyword-based `items[:] = keep` collection filters from `compile.sh`.
- Preserved eval nodeid normalization and the JUnit bidir injection plugin.
- Verified all four `compile.sh` files are LF-only before packing.

Board-cache collection targets:
- `antonmedv__walk`: before collected `786/786`; after target `786/786`; current board score `471/786`.
- `paradigmxyz__solar`: before collected `1258/2693`; after target `2693/2693`; current board score `285/2693`.
- `typst__typst`: before collected `743/2027`; after target `2027/2027`; current board score `16/2027`.
- `facebook__zstd`: before collected `1704/2788`; after target `2788/2788`; current board score `191/2788`.

Hashes:
- `walk/submission.tar.gz`: `3270D39198517F10F913976CF03A5531F21E93F9D802EABC495F57158650199F`
- `walk/submission.original.tar.gz`: `7E58B2C47AFE2DEAA36FC41A222E64839E5C6968DE54E7B7CAC4F7E415DC84D1`
- `walk/source/compile.sh`: `603CF6B27D1E0FFBF56CD0F03186DB651BCA8487193E0A398358DB13A287F926`
- `solar/submission.tar.gz`: `7F08E470E0611CD41098C0D2E1EB4B28E80AEEC637C59D0B38602005B8476625`
- `solar/submission.original.tar.gz`: `D17304758CA343212366F99E86D5B09A74A145531CEB9349B23E2B72297A24C3`
- `solar/source/compile.sh`: `AE8B7C8B0751DFE0BC7CCF44AB6112DFF422E54B91F92C7AD92C3EFDF75C9613`
- `typst/submission.tar.gz`: `C1B23803E56CB7DAC213C6C30A6B532B57CFE01868ABA16287ED17F1EF4384CF`
- `typst/submission.original.tar.gz`: `2D3AB85D12C759A27AF818706B1D695B426BA36FD40C090594967B522EB68C6F`
- `typst/source/compile.sh`: `D83C7ECF2E404E4CEF4EC2BFD9CD3966B29016E4096C9C843C9EB2B1110C8030`
- `zstd/submission.tar.gz`: `D9DDAC1DBE31F01DA9505A694FBA50D9ED1450451B1214236588D0E3584EB30B`
- `zstd/submission.original.tar.gz`: `A5619C22D48EC660F6FDE14B6DA151164ED9711AC08D08DE3D7491CAC96DF389`
- `zstd/source/compile.sh`: `A9AEBA2F698F318617920D7060DADBB5A0EC4EEC7EF645479DE1BFC0A307B387`

Verification:
- `bash -n` passed for all four `compile.sh` files.
- Focused cap/filter grep returned no matches.
- Tar sanity check confirmed root `./compile.sh` is present and no `target/` members matched.
