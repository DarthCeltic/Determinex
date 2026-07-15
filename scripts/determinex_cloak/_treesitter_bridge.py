"""
determinex_cloak/_treesitter_bridge.py — optional tree-sitter backend.

Provides a consistent interface whether or not tree-sitter is installed.
When unavailable, stubs return empty results and _TS_AVAILABLE=False so
all callers' `if _TS_AVAILABLE` guards prevent the stubs from being used.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable

try:
    from determinex_cloak_treesitter import (  # type: ignore[import]
        extract_treesitter_identifiers,
        resolve_python_star_imports,
        TS_SUPPORTED_LANGUAGES,
    )
    _TS_AVAILABLE = True
except ImportError:
    import logging
    log = logging.getLogger("determinex_cloak")
    log.critical(
        "PRIVACY DOWNGRADE: determinex_cloak_treesitter not installed! "
        "Cloak will use regex fallback for non-Python languages. "
        "Regex coverage for Go generics, Rust macros, and TS decorators is incomplete. "
        "Check at boot that tree-sitter is active before claiming privacy sovereignty."
    )
    _TS_AVAILABLE = False
    TS_SUPPORTED_LANGUAGES: frozenset[str] = frozenset()

    def extract_treesitter_identifiers(*_a, **_k) -> frozenset:  # type: ignore[misc]
        return frozenset()

    def resolve_python_star_imports(*_a, **_k) -> list:  # type: ignore[misc]
        return []
