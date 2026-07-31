# Determinex Third-Party Notices

Determinex is distributed under `AGPL-3.0-or-later`; see `LICENSE`.

Third-party dependency inventory is recorded in the generated SBOM evidence:

- `assurance/sbom/determinex-python.spdx.json`
- `assurance/sbom/determinex-python.cyclonedx.json`
- `assurance/sbom/determinex-npm.cyclonedx.json`

Installer and package artifacts must keep the SBOM and download manifest current
with the release commit. External tools, model weights, and remote services
retain their own licenses and are not relicensed by this project.

## Redistributed corpus (benchmark knowledge layer)

The knowledge layer under `corpus/` is **published**, so the upstream projects
vendored inside it are redistributed by this project and their notices apply
directly. This paragraph previously read "optional benchmark corpora ... retain
their own licenses", which was accurate only while the corpus stayed local.

The full inventory — every vendored tree, its SPDX identifier, upstream URL,
pinned commit, and license text — is:

- `corpus/THIRD_PARTY_NOTICES.md` — the attribution notices themselves
- `corpus/REDISTRIBUTION_BOUNDARY.json` — the machine-readable boundary:
  what is published, what is withheld, and why

The boundary rule is that a vendored tree is published only if it carries its own
license text. Trees whose license could not be established are withheld from
distribution and fetched from upstream on demand by
`scripts/determinex_corpus_fetch.py`, at a pinned commit, rather than shipped.
Counts are recorded in the boundary manifest, not asserted here, because they
move whenever the corpus does.

The Hugging Face hackathon companion subtree has its own notices under
`docs/companions/hf-hackathon/THIRD_PARTY.md`.
