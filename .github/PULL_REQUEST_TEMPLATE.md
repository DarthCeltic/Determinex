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
