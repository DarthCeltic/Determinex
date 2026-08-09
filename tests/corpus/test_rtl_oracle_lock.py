"""Guards on the formal-equivalence oracle.

This is the strongest oracle in the project and therefore the most dangerous one to get wrong.
Every other oracle here samples; this one claims a PROOF over all inputs. A false PASS from a
compiler costs a failed build. A false PASS from this costs a transformation that changed
behaviour being accepted as behaviour-preserving, in RTL, on its way to silicon.

THE FAILURE THIS FILE EXISTS FOR. `eqy` partitions a design into many small equivalence problems
and answers each. A run can therefore return 47 partitions proven and 3 unresolved. That design is
NOT proven equivalent -- it is 94% checked, and the difference is as likely to live in the 3 as in
the 47. An adapter that reported the majority, or that read "no counterexample found" as success,
would be the exact thing this project exists to prevent: an oracle that silently passes.

So the invariant, asserted several ways below: PROVEN requires every partition proven and none
unresolved. Everything else is UNKNOWN, and UNKNOWN is a DIFFERENT verdict from NOT_EQUIVALENT --
"we could not decide" and "we found a difference" call for opposite next actions.
"""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT / "scripts"))

import determinex_rtl_oracle as rtl  # noqa: E402


def _outdir(tmp_path: Path, status: str) -> Path:
    d = tmp_path / "job"
    d.mkdir(exist_ok=True)
    (d / "status").write_text(status, encoding="utf-8")
    return d


def _partitions(n_pass: int = 0, n_unknown: int = 0, n_fail: int = 0) -> str:
    lines = [f"partition p{i} status: PASS" for i in range(n_pass)]
    lines += [f"partition u{i} status: timeout" for i in range(n_unknown)]
    lines += [f"partition f{i} status: FAIL counterexample at cycle 3" for i in range(n_fail)]
    return "\n".join(lines)


# ── the invariant ────────────────────────────────────────────────────────────


def test_all_partitions_proven_is_the_only_pass(tmp_path):
    r = rtl.parse_result(_outdir(tmp_path, _partitions(n_pass=12)), 0)
    assert r.passed is True
    assert r.verdict == rtl.PROVEN
    assert r.partitions_proven == 12 and r.partitions_unresolved == 0


def test_a_single_unresolved_partition_blocks_the_pass(tmp_path):
    """THE test. 47 of 50 proven is not a proof, and reporting it as one would be the worst
    failure this module could have."""
    r = rtl.parse_result(_outdir(tmp_path, _partitions(n_pass=47, n_unknown=3)), 0)
    assert r.passed is False, "a partially-checked design was accepted as proven"
    assert r.verdict == rtl.UNKNOWN
    assert r.partitions_unresolved == 3
    assert "not a proof" in r.detail


def test_one_unresolved_out_of_a_hundred_still_blocks(tmp_path):
    """No threshold, no percentage. One undecided partition is undecided."""
    r = rtl.parse_result(_outdir(tmp_path, _partitions(n_pass=99, n_unknown=1)), 0)
    assert r.passed is False
    assert r.verdict == rtl.UNKNOWN


def test_coverage_is_reported_but_never_a_pass_condition(tmp_path):
    r = rtl.parse_result(_outdir(tmp_path, _partitions(n_pass=95, n_unknown=5)), 0)
    assert 0.94 < r.coverage < 0.96, "coverage should be reported"
    assert r.passed is False, "high coverage must not become a pass"


# ── undecided and disproven are different ────────────────────────────────────


def test_a_counterexample_is_not_equivalent_not_unknown(tmp_path):
    r = rtl.parse_result(_outdir(tmp_path, _partitions(n_pass=9, n_fail=1)), 0)
    assert r.verdict == rtl.NOT_EQUIV
    assert r.counterexamples
    assert "changed behaviour" in r.detail


def test_a_counterexample_outranks_unresolved_partitions(tmp_path):
    """A proven difference is decisive; being undecided elsewhere does not soften it."""
    r = rtl.parse_result(_outdir(tmp_path, _partitions(n_pass=5, n_unknown=5, n_fail=1)), 0)
    assert r.verdict == rtl.NOT_EQUIV


def test_the_two_failures_get_opposite_advice():
    """Undecided is a verification-effort problem; disproven means the transformation is wrong.
    Collapsing them wastes the next attempt in the wrong direction."""
    undecided = rtl.explain(rtl.RtlOracleResult(passed=False, verdict=rtl.UNKNOWN))
    disproven = rtl.explain(rtl.RtlOracleResult(passed=False, verdict=rtl.NOT_EQUIV))
    assert "depth" in undecided.lower()
    assert "reject" in disproven.lower()
    assert "does not make a real difference go away" in disproven


# ── silence is never success ─────────────────────────────────────────────────


def test_no_output_directory_is_an_error_not_a_pass(tmp_path):
    r = rtl.parse_result(tmp_path / "never_created")
    assert r.passed is False
    assert r.verdict == rtl.ERROR


def test_an_empty_status_file_is_an_error_not_a_pass(tmp_path):
    r = rtl.parse_result(_outdir(tmp_path, "   \n\n"), 0)
    assert r.passed is False
    assert r.verdict == rtl.ERROR
    assert "nothing was established" in r.detail


def test_zero_partitions_is_not_a_proof(tmp_path):
    """eqy ran, wrote something, and decided nothing parseable. Vacuously "no failures" must
    not read as success."""
    r = rtl.parse_result(_outdir(tmp_path, "eqy 0.4 starting\nreading design\ndone\n"), 0)
    assert r.passed is False
    assert r.verdict in (rtl.UNKNOWN, rtl.ERROR)


def test_an_unrecognised_partition_status_counts_as_unresolved(tmp_path):
    """Tolerance to format drift must be one-directional. A status this parser has never seen
    is exactly when it must not assume success."""
    r = rtl.parse_result(
        _outdir(tmp_path, "partition p0 status: PASS\npartition p1 status: banana"), 0
    )
    assert r.passed is False
    assert r.partitions_unresolved == 1


def test_a_nonzero_exit_code_blocks_a_pass(tmp_path):
    """Every parsed partition passed, but the tool itself reported failure. Undecided."""
    r = rtl.parse_result(_outdir(tmp_path, _partitions(n_pass=4)), 1)
    assert r.passed is False
    assert r.verdict == rtl.UNKNOWN


# ── the config it generates ──────────────────────────────────────────────────


def test_the_dummy_strategy_is_refused(tmp_path):
    """`dummy` decides nothing. An oracle wired to it returns clean having verified nothing --
    the most dangerous misconfiguration available, because it fails toward confidence."""
    try:
        rtl.write_eqy_config("a.v", "b.v", "top", tmp_path / "j.eqy", strategy="dummy")
    except ValueError as e:
        assert "verified nothing" in str(e)
    else:
        raise AssertionError("the dummy strategy was accepted")


def test_the_config_names_both_designs_and_the_top(tmp_path):
    cfg = rtl.write_eqy_config("gold.v", "gate.v", "riscduino_core", tmp_path / "j.eqy")
    assert "[gold]" in cfg and "[gate]" in cfg
    assert "gold.v" in cfg and "gate.v" in cfg
    assert "prep -top riscduino_core" in cfg
    assert (tmp_path / "j.eqy").exists()


# ── the verified-search contract ─────────────────────────────────────────────


def test_verify_fn_satisfies_the_oracle_protocol(tmp_path):
    gold = tmp_path / "gold.v"
    gold.write_text("module m(input a, output b); assign b = a; endmodule\n", encoding="utf-8")

    def fake_run(cfg: Path, out: Path) -> tuple[int, Path]:
        out.mkdir(parents=True, exist_ok=True)
        (out / "status").write_text(_partitions(n_pass=3), encoding="utf-8")
        return 0, out

    verify = rtl.make_verify_fn(gold, "m", tmp_path / "w", run_fn=fake_run)
    r = verify("module m(input a, output b); assign b = a; endmodule\n")
    assert isinstance(r.passed, bool) and isinstance(r.failures, list)
    assert r.passed is True


def test_a_crashed_run_is_a_verdict_not_an_exception(tmp_path):
    """This runs inside a search loop; raising would end the whole run over one candidate."""
    gold = tmp_path / "gold.v"
    gold.write_text("module m; endmodule\n", encoding="utf-8")

    def boom(_cfg, _out):
        raise RuntimeError("eqy not installed")

    r = rtl.make_verify_fn(gold, "m", tmp_path / "w", run_fn=boom)("module m; endmodule\n")
    assert r.passed is False
    assert r.verdict == rtl.ERROR
    assert "eqy not installed" in r.detail


def test_the_candidate_is_written_and_the_gold_is_never_touched(tmp_path):
    """The reference is the thing being measured against. Overwriting it would make every
    subsequent comparison meaningless and the corruption would be invisible."""
    gold = tmp_path / "gold.v"
    original = "module m(input a, output b); assign b = a; endmodule\n"
    gold.write_text(original, encoding="utf-8")
    seen: dict[str, str] = {}

    def fake_run(cfg: Path, out: Path) -> tuple[int, Path]:
        seen["gate"] = (cfg.parent / "gate.v").read_text(encoding="utf-8")
        out.mkdir(parents=True, exist_ok=True)
        (out / "status").write_text(_partitions(n_pass=1), encoding="utf-8")
        return 0, out

    rtl.make_verify_fn(gold, "m", tmp_path / "w", run_fn=fake_run)(
        "module m; /* changed */ endmodule\n"
    )
    assert "changed" in seen["gate"]
    assert gold.read_text(encoding="utf-8") == original, "the golden reference was modified"


# ── the runner, its flags, and the no-solve preflight ────────────────────────


def test_toolchain_status_reports_per_tool_not_one_boolean():
    """ "eqy failed" with no further detail sends someone debugging their design when the real
    problem is that yosys is not installed. Different causes, different remedies."""
    s = rtl.toolchain_status()
    for tool in ("eqy", "yosys", "sby"):
        assert tool in s and "found" in s[tool] and "path" in s[tool]
    assert isinstance(s["ready"], bool)


def test_a_missing_toolchain_refuses_with_an_actionable_message(tmp_path, monkeypatch):
    """A bare FileNotFoundError several layers away makes the obvious next move the wrong one."""
    monkeypatch.setattr(rtl.shutil, "which", lambda _n: None)
    gold = tmp_path / "gold.v"
    gold.write_text("module m; endmodule\n", encoding="utf-8")
    r = rtl.make_verify_fn(gold, "m", tmp_path / "w")("module m; endmodule\n")
    assert r.passed is False
    assert r.verdict == rtl.ERROR
    # Assert the EQY message specifically. "not on PATH" alone is satisfied by the yosys check
    # too, so disabling the eqy check left this green -- one guard covering for another, which
    # is the same masking that made an earlier test in this suite worthless.
    assert "eqy is not on PATH" in r.detail
    assert "Nothing was verified" in r.detail


def test_yosys_absence_is_reported_separately_from_eqy(tmp_path, monkeypatch):
    """eqy is a front-end for yosys and cannot run alone; saying so saves a wrong debug session."""
    monkeypatch.setattr(rtl.shutil, "which", lambda n: "/usr/bin/eqy" if n == "eqy" else None)
    gold = tmp_path / "gold.v"
    gold.write_text("module m; endmodule\n", encoding="utf-8")
    r = rtl.make_verify_fn(gold, "m", tmp_path / "w")("module m; endmodule\n")
    assert "yosys is not on PATH" in r.detail


def test_the_preflight_is_never_reported_as_a_pass(tmp_path, monkeypatch):
    """`-m/--setup` builds partitions and stops before any solver. The plumbing works and
    nothing has been verified -- reporting that as a pass would be the whole failure mode of
    this module, arrived at from the cheap direction."""
    monkeypatch.setattr(rtl.shutil, "which", lambda n: f"/usr/bin/{n}")

    def fake(cmd, **kw):
        # eqy -m writes partition files but decides nothing.
        out = Path(cmd[cmd.index("-d") + 1])
        out.mkdir(parents=True, exist_ok=True)
        (out / "status").write_text(
            "partition p0 created\npartition p1 created\n", encoding="utf-8"
        )

        class P:
            returncode = 0
            stdout = "setup complete"
            stderr = ""

        return P()

    monkeypatch.setattr(rtl.subprocess, "run", fake)
    gold = tmp_path / "g.v"
    gold.write_text("module m; endmodule\n", encoding="utf-8")
    gate = tmp_path / "t.v"
    gate.write_text("module m; endmodule\n", encoding="utf-8")
    r = rtl.preflight(gold, gate, "m", tmp_path / "w")
    assert r.passed is False, "a setup-only run was reported as a proof"
    assert "preflight, no solver run" in r.detail


def test_setup_only_passes_the_m_flag_and_normal_runs_do_not(tmp_path, monkeypatch):
    """The flags were verified against eqy's own argument parser; this keeps them honest."""
    monkeypatch.setattr(rtl.shutil, "which", lambda n: f"/usr/bin/{n}")
    seen: list[list[str]] = []

    def fake(cmd, **kw):
        seen.append(list(cmd))

        class P:
            returncode = 0
            stdout = ""
            stderr = ""

        return P()

    monkeypatch.setattr(rtl.subprocess, "run", fake)
    rtl._default_runner(tmp_path / "j.eqy", tmp_path / "o", setup_only=True)
    rtl._default_runner(tmp_path / "j.eqy", tmp_path / "o", jobs=4)
    assert "-m" in seen[0], "setup mode did not pass -m"
    assert "-m" not in seen[1], "a normal run passed -m and would decide nothing"
    assert seen[1][seen[1].index("-j") + 1] == "4"
    for c in seen:
        assert c[0] == "eqy" and "-f" in c and "-d" in c


def test_a_timeout_is_undecided_not_a_design_failure(tmp_path, monkeypatch):
    """A solver that ran out of time says nothing about the transformation. Reporting it as a
    crash sends the next attempt at fixing code that may be perfectly correct."""
    monkeypatch.setattr(rtl.shutil, "which", lambda n: f"/usr/bin/{n}")

    def boom(cmd, **kw):
        raise rtl.subprocess.TimeoutExpired(cmd, 1)

    monkeypatch.setattr(rtl.subprocess, "run", boom)
    rc, out = rtl._default_runner(tmp_path / "j.eqy", tmp_path / "o", timeout_s=1)
    res = rtl.parse_result(out, rc)
    assert res.verdict == rtl.UNKNOWN
    assert res.partitions_unresolved >= 1
