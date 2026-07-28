# knip configuration notes

`npm run knip` reports unused files, exports and dependencies. Two entries in
`knip.json`'s `ignore` list are deliberate and must not be "cleaned up":

- **`src/lib/ide-panel-bindings.ts`** — unreferenced from TypeScript, but pinned by
  `scripts/ide/systematic_ide_user_audit.py:277`, which reads this file to check
  that each repair panel calls the command it claims to. Deleting it breaks that
  audit, not just a lint rule.
- **`src/lib/ide-invoke-client.ts`** — same lane. It carries
  `FRONTEND_COMMAND_INVOKE_CLIENT_LOCK_001` and has archived evidence under
  `assurance/evidence/frontend_command_invoke_client/`.

- **`src/components/ide-repair/**` and `src/components/ide-product-shell/**`** — their
  `*_STATUS_TOKENS` constants are read by **219 Python lock tests** in
  `tests/ide_frontend/`, not by any TypeScript. knip cannot see a cross-language
  reference, so it reports them as dead; deleting them breaks those tests. The panels
  themselves ARE live -- `RepairPanelShell` imports nine of them by name and the
  `/ide-repair` route renders it.

  Worth recording how close this came to going wrong: a first pass grepped only
  `scripts/` for those token names, found nothing, and concluded they were dead. The
  references were in `tests/`. Grep the whole repo (ripgrep, not `grep -r` -- this
  checkout is 10 GB and plain grep times out) before deleting anything a lint calls
  unused.

Everything else knip reports is a genuine backlog, tracked in
`docs/audits/` rather than silenced here. Adding an ignore to make the
report green is the same mistake as a collection cap that makes a test suite look
complete.
