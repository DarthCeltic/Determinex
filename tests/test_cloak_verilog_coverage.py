"""Cloak must see a Verilog design's names -- all of them.

WHY THIS FILE IS SEPARATE FROM test_cloak_language_coverage.py. That one plants zzq-prefixed
names in nine software languages. Verilog needs its own because two of its lexical rules break
the shared literal-stripper, and both break it in the direction that LOSES identifiers:

    backtick      `define / `include / `timescale is a directive prefix, not a string delimiter
    single-quote  8'hFF / 4'b1010 / '0 is a sized literal, not a string

An identifier lost that way never enters the forward map, is never obfuscated, and cannot be
reported as a leak -- so a green audit and a real leak look identical. Every test below plants a
name in a position that the shared stripper would have blanked.

Names are zzq-prefixed for the same reason as the sibling file: nonsense to any safe-list, so
anything surviving is a genuine capture rather than a coincidence.
"""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "scripts"))

from determinex_cloak.lang_extractor import (  # noqa: E402
    _extract_lang_identifiers,
    _is_pdk_cell,
)


def extract(src: str) -> frozenset:
    return _extract_lang_identifiers(src, "verilog", frozenset())


# ── the two lexical traps ────────────────────────────────────────────────────


def test_an_identifier_between_two_directives_survives():
    """The shared stripper treats backtick as a string delimiter and blanks everything between
    two directives, taking every declaration in that span with it."""
    src = "`define ZZQ_A 1\nwire zzq_between_directives;\n`define ZZQ_B 2\n"
    assert "zzq_between_directives" in extract(src)


def test_an_identifier_between_two_sized_literals_survives():
    """Single-quote introduces a sized literal. Treating it as a string delimiter blanks the
    code between two literals -- which in real RTL is most of a module body."""
    src = "assign x = 8'hFF;\nwire zzq_between_literals;\nassign y = 4'b1010;\n"
    assert "zzq_between_literals" in extract(src)


def test_a_real_double_quoted_string_is_still_stripped():
    """The fix must not go the other way: a genuine string is not a declaration."""
    src = 'initial $display("zzq_inside_a_string");\nwire zzq_real_signal;\n'
    got = extract(src)
    assert "zzq_real_signal" in got
    assert "zzq_inside_a_string" not in got


# ── every declaration form a design actually uses ────────────────────────────


def test_every_declaration_kind_is_captured():
    src = """
`define ZZQ_MACRO 4
module zzq_top #(parameter ZZQ_PARAM = 8) (
    input  wire                  clk,
    input  wire [ZZQ_PARAM-1:0]  zzq_in_port,
    output reg  [31:0]           zzq_out_port
);
    localparam ZZQ_LOCAL = 3;
    wire  [7:0] zzq_net;
    reg  [63:0] zzq_register;
    logic       zzq_logic_sig;
    typedef enum { ZZQ_IDLE } zzq_type_t;
    zzq_submodule #(.W(ZZQ_PARAM)) zzq_instance (.a(clk), .b(zzq_net));
    always @(posedge clk) begin : zzq_named_block
        zzq_out_port <= 32'd0;
    end
    function automatic [7:0] zzq_func;
        input [7:0] v;
        zzq_func = v;
    endfunction
endmodule
"""
    got = extract(src)
    expected = [
        "zzq_top",
        "ZZQ_PARAM",
        "zzq_in_port",
        "zzq_out_port",
        "ZZQ_LOCAL",
        "zzq_net",
        "zzq_register",
        "zzq_logic_sig",
        "zzq_type_t",
        "zzq_submodule",
        "zzq_instance",
        "zzq_named_block",
        "zzq_func",
        "ZZQ_MACRO",
    ]
    missing = [n for n in expected if n not in got]
    assert not missing, f"these would travel to the model in the clear: {missing}"


def test_a_function_with_a_return_range_is_captured():
    """`function automatic [7:0] name;` -- a pattern that stops before the range loses every
    width-returning function in the design."""
    assert "zzq_ranged" in extract("function automatic [15:0] zzq_ranged;\nendfunction\n")


def test_an_instantiation_with_nested_parameter_parens_is_captured():
    """`mod #(.W(P)) inst (...)` -- the override list contains inner parens, and a pattern
    using [^)]* stops at the first one, losing BOTH the module type and the instance name."""
    got = extract("  zzq_modtype #(.WIDTH(SOME_P)) zzq_instname (.a(b));\n")
    assert "zzq_modtype" in got
    assert "zzq_instname" in got


# ── what must NOT be captured ────────────────────────────────────────────────


def test_foundry_cells_are_left_alone():
    """PDK names belong to the fab, not the customer. Obfuscating them hides nothing that was
    secret and breaks synthesis, because the name has to resolve against the real library."""
    src = "sky130_fd_sc_hd__clkbuf_4 buf_i (.A(zzq_sig), .X(zzq_out));\n"
    got = extract(src)
    assert not [g for g in got if g.lower().startswith("sky130")]
    assert "zzq_sig" in got, "the proprietary net beside it must still be captured"


def test_pdk_prefixes_cover_the_common_foundries():
    for cell in (
        "sky130_fd_sc_hd__inv_2",
        "sg13g2_nand2_1",
        "gf180mcu_fd_sc_mcu7t5v0__nor2_1",
        "asap7_invx1",
        "nangate_buf",
    ):
        assert _is_pdk_cell(cell), f"{cell} not recognised as a foundry cell"
    for name in ("zzq_crypto_core", "aes_sbox", "wb_interconnect"):
        assert not _is_pdk_cell(name), f"{name} wrongly treated as a foundry cell"


def test_language_keywords_are_never_captured():
    src = "module m; wire w; reg r; always @(posedge clk) begin end endmodule\n"
    got = extract(src)
    for kw in ("module", "wire", "reg", "always", "posedge", "begin", "end", "endmodule"):
        assert kw not in got, f"keyword {kw!r} would be obfuscated and break the design"


# ── the full round trip ──────────────────────────────────────────────────────
#
# Extraction alone is worthless: the product is obfuscate -> send -> restore. These guard the
# other two thirds, and the first one exists because the pipeline DESTROYED valid Verilog.

import re  # noqa: E402

from determinex_cloak.restoration import restore_file_content  # noqa: E402
from determinex_cloak.symbol_map import SymbolMap  # noqa: E402
from determinex_cloak.transformer import obfuscate_source  # noqa: E402

_RTL = """// header comment
`define ZZQ_ROUNDS 14
module zzq_crypto_core #(parameter ZZQ_KEYW = 128) (
    input  wire                clk,
    input  wire [ZZQ_KEYW-1:0] zzq_session_key,
    output reg  [31:0]         zzq_cipher_out
);
    sky130_fd_sc_hd__clkbuf_4 bufi (.A(clk), .X(zzq_bclk));
    zzq_keysched #(.W(ZZQ_KEYW)) zzq_u_ks (.clk(clk), .k(zzq_session_key));
    always @(posedge clk) zzq_cipher_out <= 32'd0;
endmodule
"""


def _cloak(src: str):
    names = frozenset(_extract_lang_identifiers(src, "verilog", frozenset()))
    sm = SymbolMap.build(names)
    return names, sm, obfuscate_source(src, sm, language="verilog")


def test_parameter_syntax_survives_obfuscation():
    """THE bug. The pipeline runs a PYTHON comment-stripper that truncates a line at the first
    `#`, so `module foo #(parameter W = 8) (` became `module foo`. Every parameterised module
    and instantiation in a real design was destroyed -- the output stopped being valid Verilog,
    which is a different and worse failure than leaking a name."""
    _n, _sm, cloaked = _cloak(_RTL)
    assert "#(" in cloaked, "parameter syntax was destroyed by the Python comment stripper"
    assert cloaked.count("#(") == _RTL.count("#(")


def test_a_literal_followed_by_a_hash_does_not_truncate():
    """A control proved my first version of this test asserted a trap that does not exist in
    this function: a lone `32'd0` survives, because the stripper only cuts at a `#`. The real
    exposure is a line carrying BOTH -- the quote opens a phantom string, and the parameter
    syntax after it is what gets cut. Asserting the reachable failure instead of the imagined
    one is the difference between a guard and a decoration."""
    src = "assign w = 8'hFF;\nmod_a #(.W(8)) zzq_inst (.a(w));\n"
    _n, _sm, cloaked = _cloak(src)
    assert "#(" in cloaked, "parameter syntax after a sized literal was truncated"
    assert cloaked.rstrip().endswith(";"), "the line was cut short"


def test_no_proprietary_name_survives_as_a_token():
    """Word-boundary, not substring. `clk` appears inside sky130_fd_sc_hd__clkbuf_4, and a
    substring check calls that a leak -- the same false positive as matching LICENSE inside a
    URL. A leak detector that cannot tell a token from a substring gets ignored."""
    names, _sm, cloaked = _cloak(_RTL)
    leaked = [n for n in names if re.search(r"\b" + re.escape(n) + r"\b", cloaked)]
    assert not leaked, f"these reached the cloaked output as real tokens: {leaked}"


def test_the_round_trip_is_byte_identical():
    """Restore has to give back exactly what was sent, or a returned patch cannot be applied."""
    _n, sm, cloaked = _cloak(_RTL)
    assert restore_file_content(cloaked, sm) == _RTL


def test_the_python_path_is_unchanged():
    """The language parameter defaults to python, so every existing caller behaves as before.
    A fix that silently changes Python obfuscation would be a regression in the path that is
    actually in production."""
    src = "def zzq_fn(zzq_arg):  # a comment\n    return zzq_arg\n"
    names = frozenset({"zzq_fn", "zzq_arg"})
    sm = SymbolMap.build(names)
    out = obfuscate_source(src, sm)
    assert "zzq_fn" not in out and "zzq_arg" not in out
    assert "# a comment" not in out, "python comment stripping stopped happening"


# ── the whole-repo entry point ───────────────────────────────────────────────
#
# Everything above tests _extract_lang_identifiers directly. Production does not call it
# directly -- it calls build_cloak_context() over a repo, and that function dispatches on
# language. The dispatch tuple did not list verilog, so RTL fell through to the PYTHON AST
# scanner, which parses no Verilog, produces an empty map, and returns a context that a green
# extraction test cannot distinguish from a working one. An empty map obfuscates nothing and
# reports no leak, so the design would have shipped in the clear.

import tempfile  # noqa: E402

from determinex_cloak.lang_extractor import build_cloak_context  # noqa: E402


def _repo(files: dict[str, str]) -> Path:
    d = Path(tempfile.mkdtemp())
    for name, body in files.items():
        p = d / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body, encoding="utf-8")
    return d


def test_whole_repo_verilog_actually_reaches_the_verilog_scanner():
    """The dispatch bug. Asserts a non-empty map AND the specific names, because an empty map
    is the exact shape of the failure and `>= 0` would have passed throughout the bug."""
    repo = _repo(
        {
            "rtl/core.v": (
                "module zzq_core #(parameter ZZQ_W = 32) ("
                "input wire clk, output reg [ZZQ_W-1:0] zzq_result);\n"
                "  wire [7:0] zzq_internal;\nendmodule\n"
            ),
            "rtl/pkg.sv": "typedef enum logic [1:0] { ZZQ_IDLE, ZZQ_RUN } zzq_state_t;\n",
        }
    )
    ctx = build_cloak_context("t", repo, language="verilog")
    assert ctx.symbol_map.forward, "empty map -- verilog fell through to the python scanner"
    for name in ("zzq_core", "ZZQ_W", "zzq_result", "zzq_internal", "zzq_state_t"):
        assert name in ctx.symbol_map.forward, f"{name} would travel in the clear"


def test_an_unknown_language_fails_closed_rather_than_returning_an_empty_map():
    """The reason the dispatch bug was invisible: an unlisted language got the Python scanner
    and an empty map instead of an error. Anything unrecognised must now raise."""
    repo = _repo({"a.cob": "IDENTIFICATION DIVISION.\n"})
    try:
        build_cloak_context("t", repo, language="cobol")
    except ValueError as e:
        assert "cobol" in str(e).lower()
    else:
        raise AssertionError("an unsupported language returned a context instead of raising")


def test_python_still_reaches_the_python_scanner():
    """The fail-closed raise must not catch the language that is actually in production."""
    repo = _repo({"m.py": "def zzq_handler(zzq_payload):\n    return zzq_payload\n"})
    ctx = build_cloak_context("t", repo, language="python")
    assert "zzq_handler" in ctx.symbol_map.forward


# ── SystemVerilog forms a chip company actually writes ───────────────────────


def test_a_braced_typedef_is_captured():
    """`typedef struct packed { logic a; logic b; } name;` -- the inner semicolons stop a
    pattern written as [^;]*, so the struct's own type name was lost."""
    src = (
        "typedef struct packed {\n  logic [7:0] zzq_field_a;\n  logic zzq_field_b;\n} zzq_bus_t;\n"
    )
    got = extract(src)
    for n in ("zzq_bus_t", "zzq_field_a", "zzq_field_b"):
        assert n in got, f"{n} missing from a packed struct"


def test_every_enum_member_is_captured_not_just_the_first():
    """One regex yields one capture per match, so `{A, B, C}` gave up A alone. Enum members are
    STATE NAMES -- ZZQ_FETCH/ZZQ_EXEC/ZZQ_WB describes what a design does more plainly than the
    signal names around it, so two in three leaking is a leak with a tidy count beside it."""
    src = (
        "typedef enum logic [2:0] {\n"
        "  ZZQ_FETCH = 3'd0,\n  ZZQ_EXEC = 3'd1,\n  ZZQ_WB = 3'd2\n"
        "} zzq_fsm_t;\n"
    )
    got = extract(src)
    missing = [n for n in ("ZZQ_FETCH", "ZZQ_EXEC", "ZZQ_WB") if n not in got]
    assert not missing, f"enum states leaking: {missing}"
    assert "logic" not in got, "the enum pass swept up a keyword"


def test_an_implicitly_declared_net_is_captured():
    """`assign zzq_x = ...;` with no prior declaration is legal Verilog and common in glue."""
    got = extract("assign zzq_implicit = a & b;\nalways_comb zzq_comb_out = c | d;\n")
    for n in ("zzq_implicit", "zzq_comb_out"):
        assert n in got, f"{n} implicit net missing"


def test_the_extractor_source_carries_no_control_characters():
    """A heredoc turned every `\\b` in the enum pass into a literal BACKSPACE (0x08), so the
    pattern matched nothing and the pass silently found zero members -- no error, no failing
    test, one identifier quietly absent from a set. The project has a preflight gate for exactly
    this; this pins it to the file where it did damage."""
    import determinex_cloak.lang_extractor as le

    text = Path(le.__file__).read_text(encoding="utf-8")
    ctl = sorted({hex(ord(c)) for c in text if ord(c) < 32 and c not in "\n\t"})
    assert not ctl, f"control characters in the extractor: {ctl}"
