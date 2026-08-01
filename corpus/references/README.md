# corpus/references/ — Attribution & Inspiration Sources

This directory seeds the **Determinex Attribution Tagger** (`scripts/determinex_copyright_guard.py`).

Every file here is registered at startup via `_auto_seed()`. When any Determinex-generated output
matches content from a registered reference, an `AttributionTag` is written to
`logs/copyright_guard/attribution.jsonl` — giving direct, automatic recognition to the
inspiration behind the output.

This is distinct from `corpus/protected/` (verbatim copyright guard). References are for
inspiration tracking; protected works are for blocking verbatim reproduction.

---

## Directory Structure

```
corpus/references/
├── README.md                   ← this file
├── academic/
│   ├── metadata.json           ← source_type=academic applies to all .txt in this dir
│   └── <arxiv_id>.txt          ← abstract or relevant excerpt
├── open_source/
│   ├── metadata.json           ← source_type=open_source applies to all .txt in this dir
│   └── <repo_slug>.txt         ← README or doc excerpt
├── patents/
│   ├── metadata.json           ← source_type=patent applies to all .txt in this dir
│   └── <patent_number>.txt     ← abstract or claims excerpt
└── <custom_subdir>/
    ├── metadata.json           ← set source_type, license, url, authors, year, label
    └── *.txt
```

## Subdirectory metadata.json Format

```json
{
  "label":       "Human-readable name (optional — defaults to filename stem)",
  "source_type": "open_source | academic | patent | commercial | proprietary | private | unknown",
  "license":     "MIT | Apache-2.0 | GPL-3.0 | proprietary | unknown | ...",
  "url":         "https://canonical-url",
  "authors":     ["Author One", "Author Two"],
  "year":        2023
}
```

All files in the directory inherit the directory's metadata.json fields.
If a file needs its own metadata (different license, different URL), put it in its own
subdirectory with its own metadata.json.

## Adding a New Reference

1. Create a `.txt` file in the appropriate subdirectory with the relevant text excerpt
   (abstract, README, key code section — enough for meaningful bigram matching)
2. If the directory's `metadata.json` doesn't cover this source, create a new subdirectory
   with its own `metadata.json`
3. The next Determinex run will auto-register it

## Detection Thresholds (defaults, override via env vars)

| Tier | Signal | Default | Env Override |
|------|--------|---------|-------------|
| `verbatim_reproduction` | Consecutive token match | ≥50 tokens | `DETERMINEX_COPYRIGHT_MIN_TOKENS` |
| `substantial_similarity` | Token match OR bigram Jaccard | ≥30 tokens OR ≥25% | `DETERMINEX_SUBSTANTIAL_TOKENS`, `DETERMINEX_SUBSTANTIAL_BIGRAM` |
| `inspiration` | Bigram Jaccard | ≥15% | `DETERMINEX_INSPIRATION_BIGRAM` |

## Audit Logs

- **Copyright alerts**: `logs/copyright_guard/audit.jsonl`
- **Attribution tags**: `logs/copyright_guard/attribution.jsonl`

Both are append-only JSONL. Each line is a standalone JSON record.
