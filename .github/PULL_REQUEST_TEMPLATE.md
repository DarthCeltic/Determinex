## What does this PR do?

<!-- One paragraph. What changed and why. -->

## Type of change

- [ ] Bug fix
- [ ] New feature
- [ ] Performance improvement
- [ ] Documentation
- [ ] Refactor (no behavior change)

## Test evidence

<!-- Paste the output of the relevant test. For compiler loop changes, paste determinex_limits_test.py output. -->

```
paste output here
```

## Checklist

- [ ] I ran `python scripts/determinex_limits_test.py --lang rust` and all 6 levels pass
- [ ] No hardcoded absolute paths (`C:\`, `T:\`, `/home/username/`) introduced
- [ ] No API keys, IPs, or SSH key names in the diff
- [ ] Shell scripts use `shell=False` with argument arrays, not `shell=True` with string concat
- [ ] I have read `CONTRIBUTING.md`

## Licensing — required

Determinex is **AGPL-3.0-or-later**. That is a strong copyleft licence, so a contribution
whose provenance is unclear cannot be accepted later without relicensing work that may be
impossible. Confirming it once, here, is cheaper than untangling it afterwards.

- [ ] **I wrote this, or I have the right to submit it**, and I license it under
      **AGPL-3.0-or-later** — the same terms as the project.
- [ ] Any third-party code included carries a compatible licence, and **its copyright notice
      and licence text travel with it** (MIT, BSD and ISC all require this; dropping the
      notice is the most common way an otherwise-fine contribution becomes unmergeable).
- [ ] This contains **no AI-generated code I have not read and verified**. The project's
      entire premise is that a model's output is not trusted until an oracle passes it; that
      applies to contributions too.

<!--
  Sign your commits with `git commit -s` to add a Developer Certificate of Origin line.
  It is the same statement as the first box above, recorded per-commit and in git history
  rather than only in a PR description that can be edited after review.
-->

## Security

- [ ] This change does not widen what model-generated code can reach. If it touches the
      sandbox, the oracle, `hardened_runner`, or a provider boundary, I have said so above
      and explained why. See `docs/policy/INCIDENT_DERIVED_HARDENING.md` for the threat model
      this project actually defends against.
