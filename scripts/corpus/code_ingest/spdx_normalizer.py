"""
SPDX license identifier normalizer.

Converts raw license strings found in LICENSE files, headers, and package
metadata into canonical SPDX identifiers (e.g. "MIT License" → "MIT").

Reference: https://spdx.org/licenses/
"""
from __future__ import annotations

import re

# Green: ingest allowed without review
GREEN_LICENSES: frozenset[str] = frozenset({
    "MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause",
    "ISC", "Unlicense", "CC0-1.0", "0BSD",
    "BlueOak-1.0.0", "BSD-2-Clause-Patent",
})

# Yellow: ingest allowed but requires metadata review before model training
YELLOW_LICENSES: frozenset[str] = frozenset({
    "MPL-2.0", "EPL-2.0", "EPL-1.0",
    "CC-BY-4.0", "CC-BY-3.0", "CC-BY-SA-4.0",
    "EUPL-1.2",
})

# Red: do not ingest into training corpus without explicit legal review
# LGPL is included: even library copyleft creates obligations for training data usage.
RED_LICENSES: frozenset[str] = frozenset({
    "GPL-2.0-only", "GPL-2.0-or-later", "GPL-3.0-only", "GPL-3.0-or-later",
    "AGPL-3.0-only", "AGPL-3.0-or-later",
    "LGPL-2.0-only", "LGPL-2.1-only", "LGPL-2.1-or-later",
    "LGPL-3.0-only", "LGPL-3.0-or-later",
    "SSPL-1.0", "Commons-Clause",
    "BUSL-1.1",
})

# Canonical normalizations: raw text fragment → SPDX identifier
_NORMALIZATIONS: list[tuple[re.Pattern, str]] = [
    # MIT
    (re.compile(r"\bmit\b", re.I), "MIT"),
    # Apache
    (re.compile(r"apache.{0,10}2\.0|apache.{0,10}license.{0,10}2", re.I), "Apache-2.0"),
    (re.compile(r"apache.{0,10}1\.[01]", re.I), "Apache-1.1"),
    # BSD
    (re.compile(r"bsd.{0,5}3.{0,10}clause|new bsd|modified bsd", re.I), "BSD-3-Clause"),
    (re.compile(r"bsd.{0,5}2.{0,10}clause|simplified bsd|freebsd", re.I), "BSD-2-Clause"),
    # ISC
    (re.compile(r"\bisc\b", re.I), "ISC"),
    # Unlicense
    (re.compile(r"\bunlicense\b", re.I), "Unlicense"),
    # CC0
    (re.compile(r"cc0|creative.commons.zero|public.domain", re.I), "CC0-1.0"),
    # GPL — handle both "v2"/"v3" and "version 2"/"version 3" forms
    (re.compile(r"(?:gnu.{0,20}general.{0,20}public.{0,20}licen[cs]e.{0,15}(?:v(?:ersion)?\.?\s*)?3)|(?:gpl.{0,5}v?3)|gplv3|gpl-3", re.I), "GPL-3.0-only"),
    (re.compile(r"(?:gnu.{0,20}general.{0,20}public.{0,20}licen[cs]e.{0,15}(?:v(?:ersion)?\.?\s*)?2)|(?:gpl.{0,5}v?2)|gplv2|gpl-2", re.I), "GPL-2.0-only"),
    # AGPL
    (re.compile(r"affero.{0,20}general.{0,20}public|agpl.{0,5}v?3", re.I), "AGPL-3.0-only"),
    # LGPL — handle both "v2.1" and "version 2.1" forms; check 2.1 before 2.0
    (re.compile(r"(?:lesser.{0,20}general.{0,20}public.{0,20}licen[cs]e.{0,15}(?:v(?:ersion)?\.?\s*)?3)|(?:lgpl.{0,5}v?3)|lgplv3|lgpl-3", re.I), "LGPL-3.0-only"),
    (re.compile(r"(?:lesser.{0,20}general.{0,20}public.{0,20}licen[cs]e.{0,15}(?:v(?:ersion)?\.?\s*)?2\.1)|(?:lgpl.{0,5}v?2\.1)|lgpl-2\.1", re.I), "LGPL-2.1-only"),
    (re.compile(r"(?:lesser.{0,20}general.{0,20}public.{0,20}licen[cs]e.{0,15}(?:v(?:ersion)?\.?\s*)?2(?!\.1))|(?:lgpl.{0,5}v?2(?!\.1))|lgplv2(?!\.1)|lgpl-2(?!\.)", re.I), "LGPL-2.0-only"),
    # MPL
    (re.compile(r"mozilla.{0,20}public.{0,20}license.{0,10}2|mpl.{0,5}2", re.I), "MPL-2.0"),
    # EPL
    (re.compile(r"eclipse.{0,20}public.{0,20}license.{0,10}2|epl.{0,5}2", re.I), "EPL-2.0"),
    (re.compile(r"eclipse.{0,20}public.{0,20}license.{0,10}1|epl.{0,5}1", re.I), "EPL-1.0"),
    # CC-BY
    (re.compile(r"creative.commons.{0,10}attribution.{0,10}4|cc.by.4", re.I), "CC-BY-4.0"),
    (re.compile(r"creative.commons.{0,10}attribution.{0,30}share.alike.{0,10}4|cc.by.sa.4", re.I), "CC-BY-SA-4.0"),
    # BUSL
    (re.compile(r"business.source.license|busl", re.I), "BUSL-1.1"),
    # SSPL
    (re.compile(r"server.side.public.license|sspl", re.I), "SSPL-1.0"),
]

# SPDX-License-Identifier header pattern
_SPDX_HEADER = re.compile(r"SPDX-License-Identifier:\s*([^\n\r*]+)", re.I)


def normalize(raw: str) -> str | None:
    """
    Convert a raw license string to its canonical SPDX identifier.
    Returns None if no match found.
    """
    raw = raw.strip()
    if not raw:
        return None

    # Check SPDX identifier header first (most reliable) — on original raw
    m = _SPDX_HEADER.search(raw)
    if m:
        candidate = m.group(1).strip().rstrip("*/")
        # validate it looks like an SPDX id (letters, digits, hyphens, dots)
        if re.match(r"^[\w.\-\+]+$", candidate):
            return candidate

    # Normalize whitespace so patterns work across multi-line license texts
    # (e.g. "GNU GPL\nVersion 2" becomes "GNU GPL Version 2")
    normalized = re.sub(r"[\r\n\t]+", " ", raw)
    normalized = re.sub(r" {2,}", " ", normalized)

    # Try normalizations
    for pattern, spdx_id in _NORMALIZATIONS:
        if pattern.search(normalized):
            return spdx_id

    return None


def bucket(spdx_id: str | None) -> str:
    """
    Return "green", "yellow", "red", or "unknown" for a given SPDX identifier.
    """
    if spdx_id is None:
        return "unknown"
    if spdx_id in GREEN_LICENSES:
        return "green"
    if spdx_id in YELLOW_LICENSES:
        return "yellow"
    if spdx_id in RED_LICENSES:
        return "red"
    return "unknown"


def ingest_allowed(spdx_id: str | None) -> bool:
    """True only for green-bucket licenses."""
    return bucket(spdx_id) == "green"
