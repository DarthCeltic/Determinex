# gping Lessons

- Official eval must be the score authority. Local mini-eval improved the tool,
  but the final lock required Docker ProgramBench.
- Raw eval JSON can contain `not_run` and `skipped` entries outside the official
  runnable denominator. For this lock, the runner-reported score is `628/628`.
- Exact clap/gping stderr matters more than broad behavior. Several failures
  were fixed by matching one golden string exactly.
- TUI tests assert visible tokens and graph glyph classes, not real network
  behavior. A deterministic rendering stub was enough once it respected simple
  graphics, margins, command labels, and IPv6/hostname display.
- Pinger tests use fake `ping` binaries on `PATH`; detecting their `-V` output
  and triggering the expected messages was required for the last stretch.
