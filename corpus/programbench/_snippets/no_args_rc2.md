# Snippet bucket: `no_args_rc2`

Extracted from 4 tool override(s). Higher-scoring tools' versions are preferred for reuse.

## nikoladucak__caps-log.2cf2d1e  (cpp, 46.57%)
```python
if not argv:
            print_usage()
            sys.exit(2)
```

## foriequal0__git-trim.07c2f50  (rs, 38.18%)
```python
if not argv:
        print_help()
        sys.exit(2)
```

## trasta298__keifu.3331426  (rs, 20.72%)
```python
if not argv:
        if not is_git_repo():
            sys.stderr.write("Error: Git repository not found. Please run inside a Git repository.\n")
            sys.stderr.flush()
            sys.exit(2)
```

## wintermute-cell__ngrrram.8ea13c3  (rs, 7.54%)
```python
if not argv:
            print(_usage(), file=sys.stderr)
            sys.exit(2)
```
