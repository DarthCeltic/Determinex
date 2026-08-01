# Snippet bucket: `help_rc0`

Extracted from 36 tool override(s). Higher-scoring tools' versions are preferred for reuse.

## nikoladucak__caps-log.2cf2d1e  (cpp, 46.57%)
```python
if '--help' in argv or '-h' in argv or '-help' in argv or '--HELP' in argv:
            print_help()
            sys.exit(0)
```

## sharkdp__hyperfine.327d5f4  (rs, 41.95%)
```python
if a in ("-h", "--help"):
            print_help()
            sys.exit(0)
```

## foriequal0__git-trim.07c2f50  (rs, 38.18%)
```python
if "--help" in argv or "-h" in argv:
        print_help()
        sys.exit(0)
```

## oppiliappan__eva.41ae245  (rs, 37.33%)
```python
if a in ("-h", "--help"):
            print_help()
            sys.exit(0)
```

## mfridman__tparse.2416b4b  (go, 37.25%)
```python
if a in ("-h", "--help"):
            print(USAGE); sys.exit(0)
```

## skeema__skeema.6a76243  (go, 33.33%)
```python
if not args or args[0] in ('--help', '-h', '-help'):
        print_help()
        sys.exit(0)
```

## mgdm__htmlq.6e31bc8  (rs, 30.61%)
```python
if arg in ('-h', '--help'):
            print_help()
            sys.exit(0)
```

## arthursonzogni__json-tui.17a22b6  (cpp, 29.97%)
```python
if '-h' in args or '--help' in args or '-help' in args or '--HELP' in args or '--help-me' in args:
            print_help()
            sys.exit(0)
```

## wfxr__code-minimap.0ddeea5  (rs, 24.71%)
```python
if a in ("-h", "--help"):
            print_help(); sys.exit(0)
```

## guumaster__hostctl.d6d9699  (go, 23.82%)
```python
if args[0] in ('--help', '-h'):
        print_help()
        sys.exit(0)
```

## nikolassv__bartib.6b9b5ce  (rs, 23.64%)
```python
if args[i] == "-h" or args[i] == "--help":
            print(HELP_START)
            sys.exit(0)
```

## byron__dua-cli.8570c15  (rs, 22.16%)
```python
if arg in ("-h", "--help"):
            sys.stdout.write(HELP_TEXT)
            sys.stdout.write("\n")
            sys.exit(0)
```

## sibprogrammer__xq.b89f681  (go, 21.54%)
```python
if not args or args[0] in ('-h', '--help', '--help...'):
        print_help()
        sys.exit(0)
```

## wfxr__csview.8ac4de0  (rs, 21.26%)
```python
if '-h' in args or '--help' in args:
        print_help()
        sys.exit(0)
```

## trasta298__keifu.3331426  (rs, 20.72%)
```python
if '--help' in argv or '-h' in argv:
        sys.stdout.write(HELP_TEXT + '\n')
        sys.stdout.flush()
        sys.exit(0)
```

## segmentio__chamber.5f93f5f  (go, 19.0%)
```python
if cmd in ("-h", "--help"):
        print(usage())
        sys.exit(0)
```

## antonmedv__fx.86d0d34  (go, 16.39%)
```python
if '-h' in args or '--help' in args:
        sys.stdout.write(HELP_TEXT)
        sys.stdout.write("\n")
        sys.exit(0)
```

## rust-lang__mdbook.37273ba  (rs, 15.68%)
```python
if args[0] in ('-h', '--help'):
        print_help()
        sys.exit(0)
```

## dandavison__delta.acd758f  (rs, 14.99%)
```python
if sys.argv[1] in ('-h', '--help'):
            print(HELP_TEXT)
            sys.exit(0)
```

## kaushiksrini__parqeye.8072121  (rs, 14.49%)
```python
if args[0] in ("--help", "-h"):
        print_help()
        sys.exit(0)
```

## mookid__diffr.2152742  (rs, 13.53%)
```python
if not args or args[0] in ("-h", "--help"):
        print(USAGE, end="")
        sys.exit(0 if args else 2)
    
    # Handle --version / -V
    if args[0] in ("-V", "--version"):
        print(VERSION)
        sys.exit(0)
```

## nuta__nsh.bdd0702  (rs, 13.33%)
```python
if not args or args[0] in ('-h', '--help'):
        sys.stdout.write(print_help())
        sys.exit(0)
```

## rust-embedded__svd2rust.1760b5e  (rs, 12.64%)
```python
if a in ("-h", "--help"):
            sys.stdout.write(HELP)
            sys.exit(0)
```

## crowdagger__crowbook.ea214d7  (rs, 11.81%)
```python
if arg in ('-h', '--help'):
            print_usage()
            sys.exit(0)
```

## paradigmxyz__solar.5190d0e  (rs, 10.58%)
```python
if not args or args[0] in ("-h", "--help"):
        if args and args[0] in ("-h", "--help"):
            sys.stdout.write(HELP_TEXT)
            sys.exit(0)
```

## unhappychoice__gittype.34b72d0  (rs, 10.39%)
```python
if sub in ("-h", "--help"):
        return 0, textwrap.dedent(f"""\
            {TOOL_NAME}-cache
            Manage cached challenges

            Usage: {TOOL_NAME} cache [OPTIONS] <COMMAND>

            Commands:
              clear  Clear the cache
              list   List cached challenges
              stats  Show cache statistics

            Options:
              -h, --help  Print help
        """)

    if sub == "stats":
        json_output = "--json" in args or "-j" in args
        stats = _get_cache_stats()
        return 0, _format_cache_stats(stats, json_output)

    if sub == "list":
        if not os.path.exists(CHALLENGES_DIR):
            return 0, "No cached challenges found."
        challenges = []
        for root, dirs, files in os.walk(CHALLENGES_DIR):
            for f in files:
                challenges.append(os.path.relpath(os.path.join(root, f), CHALLENGES_DIR))
        if not challenges:
            return 0, "No cached challenges found."
        return 0, "\n".join(sorted(challenges))

    if sub == "clear":
        if os.path.exists(CACHE_DIR):
            import shutil
            shutil.rmtree(CACHE_DIR)
        return 0, "Cache cleared."

    return 2, _error(f"unknown cache subcommand '{sub}'")


def main() -> None:
    """Main entry point."""
    try:
        _main()
    except BrokenPipeError:
        sys.stderr.close()
        sys.exit(0)
```

## pemistahl__grex.fa3e8ed  (rs, 9.4%)
```python
if arg in ('-h', '--help'):
            print_help()
            sys.exit(0)
```

## pls-rs__pls.4e1ae50  (rs, 9.04%)
```python
if a in ("-h", "--help"):
            print_help(); sys.exit(0)
```

## svenstaro__miniserve.8449e8b  (rs, 8.53%)
```python
if args[0] in ('-h', '--help'):
        print_help()
        sys.exit(0)
```

## wintermute-cell__ngrrram.8ea13c3  (rs, 7.54%)
```python
if arg in ("-h", "--help"):
            print(_help_text())
            sys.exit(0)
```

## shashwatah__jot.a92aad8  (rs, 7.46%)
```python
if args[0] in ('-h', '--help', '-help'):
        print_help()
        sys.exit(0)
```

## robertdavidgraham__masscan.b99d433  (c, 7.39%)
```python
if args[0] in ('-h', '--help'):
        print_help()
        sys.exit(0)
```

## sharkdp__pastel.b60e899  (rs, 6.67%)
```python
if args[0] in ('-h', '--help'):
        print(HELP_TEXT)
        sys.exit(0)
```

## xorg62__tty-clock.f2f847c  (c, 6.43%)
```python
if arg in ('-h', '--help'):
            print(_help_text())
            sys.exit(0)
```

## thezoraiz__ascii-image-converter.d05a757  (go, 6.19%)
```python
if "--help" in args or "-h" in args:
        print(_help_text())
        sys.exit(0)
```

## xampprocky__tokei.505d648  (rs, 5.74%)
```python
if len(sys.argv) == 2 and sys.argv[1] in ('-h', '--help'):
        print(_help(), file=sys.stdout)
        sys.exit(0)
```
