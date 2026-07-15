#!/usr/bin/env python3
"""
determinex_progress.py -- Progress / Loop Detector (Amplifier piece #5)
====================================================================
Weak models thrash: they emit the same wrong fix, or oscillate between two wrong
fixes, or plateau (the partial score stops improving). Without a detector the
loop burns budget forever. This promotes the seed in verified_search into a
standalone primitive that watches a stream of attempts and emits a DIRECTIVE:

    CONTINUE      -- making progress (partial score improving), keep going
    WIDEN         -- stalled but still producing novelty; raise temperature / K
    RE_DECOMPOSE  -- novelty but no progress; the step is too big -> split it
    ESCALATE      -- looping (no novelty) or repeated plateau -> route up / human

It is deterministic and model-agnostic: feed it (candidate_digest, score) tuples,
where score is "closer to solved is higher" (e.g. -n_failures). It never lets the
system spin in place, and it never *quits* without a reason it can name.

    from determinex_progress import ProgressTracker, Directive
    pt = ProgressTracker()
    d = pt.observe(digest="abc123", score=-7)   # 7 failing checks
    if d == Directive.ESCALATE: ...
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Directive(str, Enum):
    CONTINUE = "CONTINUE"
    WIDEN = "WIDEN"
    RE_DECOMPOSE = "RE_DECOMPOSE"
    ESCALATE = "ESCALATE"


@dataclass
class ProgressTracker:
    plateau_patience: int = 4        # rounds of no score improvement before acting
    loop_patience: int = 2           # rounds of zero novelty before escalating
    _best_score: float = field(default=float("-inf"))
    _rounds_since_improve: int = 0
    _seen: set = field(default_factory=set)
    _rounds_no_novelty: int = 0
    _history: list = field(default_factory=list)

    def observe(self, digest: str, score: float) -> Directive:
        self._history.append((digest, score))
        novel = digest not in self._seen
        self._seen.add(digest)

        # novelty tracking (loop detection)
        if novel:
            self._rounds_no_novelty = 0
        else:
            self._rounds_no_novelty += 1

        # progress tracking (plateau detection)
        if score > self._best_score:
            self._best_score = score
            self._rounds_since_improve = 0
            return Directive.CONTINUE
        self._rounds_since_improve += 1

        # decide
        if self._rounds_no_novelty >= self.loop_patience:
            return Directive.ESCALATE      # the model only repeats itself
        if self._rounds_since_improve >= self.plateau_patience:
            # still producing novel-but-no-better candidates -> the step is too hard
            return Directive.RE_DECOMPOSE if novel else Directive.ESCALATE
        return Directive.WIDEN             # stalled but not yet stuck

    @property
    def best_score(self) -> float:
        return self._best_score

    def summary(self) -> dict:
        return {"attempts": len(self._history), "best_score": self._best_score,
                "rounds_since_improve": self._rounds_since_improve,
                "rounds_no_novelty": self._rounds_no_novelty}


if __name__ == "__main__":
    # demo: a model that plateaus then loops
    pt = ProgressTracker(plateau_patience=3, loop_patience=2)
    stream = [("a", -9), ("b", -7), ("c", -7), ("d", -7), ("d", -7), ("d", -7)]
    for dg, sc in stream:
        print(f"observe({dg}, {sc}) -> {pt.observe(dg, sc).value}")
    print("summary:", pt.summary())
