"""
determinex_cloak/lang_extractor.py — Multi-language identifier extraction + pipeline entry.

Covers:
  - Regex-based extraction for Java/Rust/Ruby/PHP/C/C++ (definition-site patterns)
  - tree-sitter real AST extraction (preferred when grammar available)
  - Go and TypeScript/JavaScript bridge to dedicated extractor modules
  - build_cloak_context() — the main pipeline entry point
"""

from __future__ import annotations

import logging
import re
from pathlib import Path

from ._treesitter_bridge import (
    _ALLOW_DEGRADED,
    _TS_AVAILABLE,
    TS_SUPPORTED_LANGUAGES,
    extract_treesitter_identifiers,
)
from .classifier import build_private_identifier_set
from .context import CloakContext
from .safe_list import _build_safe_list
from .symbol_map import SymbolMap

log = logging.getLogger("determinex_cloak")

# ── Multi-language regex-based identifier extractor ──────────────────────────

_COMMENT_STRIP: dict[str, re.Pattern] = {
    "java": re.compile(r"//[^\n]*|/\*.*?\*/", re.DOTALL),
    "rust": re.compile(r"//[^\n]*|/\*.*?\*/", re.DOTALL),
    "ruby": re.compile(r"#[^\n]*"),
    "php": re.compile(r"//[^\n]*|#[^\n]*|/\*.*?\*/", re.DOTALL),
    "c": re.compile(r"//[^\n]*|/\*.*?\*/", re.DOTALL),
    "cpp": re.compile(r"//[^\n]*|/\*.*?\*/", re.DOTALL),
    "verilog": re.compile(r"//[^\n]*|/\*.*?\*/", re.DOTALL),
}
_STR_STRIP = re.compile(r'"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'|`[^`]*`')

#: Verilog's own literal stripper. The shared one above is WRONG here, in the direction that
#: loses identifiers rather than the direction that keeps too many:
#:
#:   backtick      -- a macro/directive prefix (`define, `include, `timescale), NOT a string
#:                    delimiter. The shared pattern blanks everything between two directives.
#:   single-quote  -- introduces a sized literal (8'hFF, 4'b1010, '0), NOT a string. The shared
#:                    pattern blanks everything between two literals.
#:
#: Either mistake silently removes real declarations from the text being scanned, so those
#: identifiers never enter the forward map -- and an identifier that was never captured cannot
#: be obfuscated and cannot be reported as a leak. It simply leaves in the clear.
#:
#: Only double-quoted strings are strings in Verilog.
_VERILOG_STR_STRIP = re.compile(r'"(?:[^"\\\n]|\\.)*"')

#: Foundry standard-cell and PDK names. These belong to the fab, not the customer: obfuscating
#: them protects nothing, breaks synthesis, and makes the cloaked output useless. Matched as a
#: prefix because a PDK ships thousands of cells under a handful of stems.
_PDK_PREFIXES: tuple[str, ...] = (
    "sky130_",
    "sg13g2_",
    "gf180mcu_",
    "gf180_",
    "ihp_",
    "asap7_",
    "freepdk",
    "nangate",
    "scs8",
    "sc7p5t",
    "tt_um_",
)


def _is_pdk_cell(name: str) -> bool:
    """A foundry cell name, which is never proprietary to the design being cloaked."""
    low = name.lower()
    return any(low.startswith(p) for p in _PDK_PREFIXES)


_LANG_KEYWORDS: dict[str, frozenset] = {
    "verilog": frozenset(
        {
            # Verilog-2005 reserved words
            "always",
            "and",
            "assign",
            "automatic",
            "begin",
            "buf",
            "bufif0",
            "bufif1",
            "case",
            "casex",
            "casez",
            "cell",
            "cmos",
            "config",
            "deassign",
            "default",
            "defparam",
            "design",
            "disable",
            "edge",
            "else",
            "end",
            "endcase",
            "endconfig",
            "endfunction",
            "endgenerate",
            "endmodule",
            "endprimitive",
            "endspecify",
            "endtable",
            "endtask",
            "event",
            "for",
            "force",
            "forever",
            "fork",
            "function",
            "generate",
            "genvar",
            "highz0",
            "highz1",
            "if",
            "ifnone",
            "incdir",
            "include",
            "initial",
            "inout",
            "input",
            "instance",
            "integer",
            "join",
            "large",
            "liblist",
            "library",
            "localparam",
            "macromodule",
            "medium",
            "module",
            "nand",
            "negedge",
            "nmos",
            "nor",
            "noshowcancelled",
            "not",
            "notif0",
            "notif1",
            "or",
            "output",
            "parameter",
            "pmos",
            "posedge",
            "primitive",
            "pull0",
            "pull1",
            "pulldown",
            "pullup",
            "pulsestyle_ondetect",
            "pulsestyle_onevent",
            "rcmos",
            "real",
            "realtime",
            "reg",
            "release",
            "repeat",
            "rnmos",
            "rpmos",
            "rtran",
            "rtranif0",
            "rtranif1",
            "scalared",
            "showcancelled",
            "signed",
            "small",
            "specify",
            "specparam",
            "strong0",
            "strong1",
            "supply0",
            "supply1",
            "table",
            "task",
            "time",
            "tran",
            "tranif0",
            "tranif1",
            "tri",
            "tri0",
            "tri1",
            "triand",
            "trior",
            "trireg",
            "unsigned",
            "use",
            "vectored",
            "wait",
            "wand",
            "weak0",
            "weak1",
            "while",
            "wire",
            "wor",
            "xnor",
            "xor",
            # SystemVerilog additions
            "alias",
            "always_comb",
            "always_ff",
            "always_latch",
            "assert",
            "assume",
            "before",
            "bind",
            "bins",
            "binsof",
            "bit",
            "break",
            "byte",
            "chandle",
            "class",
            "clocking",
            "const",
            "constraint",
            "context",
            "continue",
            "cover",
            "covergroup",
            "coverpoint",
            "cross",
            "dist",
            "do",
            "endclass",
            "endclocking",
            "endgroup",
            "endinterface",
            "endpackage",
            "endprogram",
            "endproperty",
            "endsequence",
            "enum",
            "expect",
            "export",
            "extends",
            "extern",
            "final",
            "first_match",
            "foreach",
            "forkjoin",
            "iff",
            "ignore_bins",
            "illegal_bins",
            "import",
            "inside",
            "int",
            "interface",
            "intersect",
            "join_any",
            "join_none",
            "local",
            "logic",
            "longint",
            "matches",
            "modport",
            "new",
            "null",
            "package",
            "packed",
            "priority",
            "program",
            "property",
            "protected",
            "pure",
            "rand",
            "randc",
            "randcase",
            "randsequence",
            "ref",
            "return",
            "sequence",
            "shortint",
            "shortreal",
            "solve",
            "static",
            "string",
            "struct",
            "super",
            "tagged",
            "this",
            "throughout",
            "timeprecision",
            "timeunit",
            "type",
            "typedef",
            "union",
            "unique",
            "var",
            "virtual",
            "void",
            "wait_order",
            "with",
            "within",
            # Directives (appear after a backtick, which the tokenizer will have dropped)
            "define",
            "ifdef",
            "ifndef",
            "endif",
            "elsif",
            "undef",
            "timescale",
            "resetall",
            "celldefine",
            "endcelldefine",
            "default_nettype",
            "line",
            "unconnected_drive",
            "nounconnected_drive",
        }
    ),
    "java": frozenset(
        [
            "abstract",
            "assert",
            "boolean",
            "break",
            "byte",
            "case",
            "catch",
            "char",
            "class",
            "const",
            "continue",
            "default",
            "do",
            "double",
            "else",
            "enum",
            "extends",
            "final",
            "finally",
            "float",
            "for",
            "goto",
            "if",
            "implements",
            "import",
            "instanceof",
            "int",
            "interface",
            "long",
            "native",
            "new",
            "package",
            "private",
            "protected",
            "public",
            "return",
            "short",
            "static",
            "strictfp",
            "super",
            "switch",
            "synchronized",
            "this",
            "throw",
            "throws",
            "transient",
            "try",
            "var",
            "void",
            "volatile",
            "while",
            "true",
            "false",
            "null",
            "String",
            "Object",
            "Integer",
            "Long",
            "Double",
            "Float",
            "Boolean",
            "Byte",
            "Short",
            "Character",
            "StringBuilder",
            "StringBuffer",
            "System",
            "Math",
            "Arrays",
            "List",
            "Map",
            "Set",
            "ArrayList",
            "HashMap",
            "HashSet",
            "LinkedList",
            "Optional",
            "Stream",
            "Collectors",
            "Exception",
            "RuntimeException",
            "Error",
            "Throwable",
            "Override",
            "Deprecated",
            "SuppressWarnings",
            "FunctionalInterface",
            "main",
            "args",
            "toString",
            "equals",
            "hashCode",
            "compareTo",
            "length",
            "size",
            "get",
            "set",
            "add",
            "remove",
            "contains",
            "iterator",
            "next",
            "hasNext",
            "println",
            "print",
            "format",
            "valueOf",
            "parseInt",
            "getClass",
            "getName",
            "getSimpleName",
            "out",
            "err",
            "in",
        ]
    ),
    "rust": frozenset(
        [
            "as",
            "async",
            "await",
            "break",
            "const",
            "continue",
            "crate",
            "dyn",
            "else",
            "enum",
            "extern",
            "false",
            "fn",
            "for",
            "if",
            "impl",
            "in",
            "let",
            "loop",
            "match",
            "mod",
            "move",
            "mut",
            "pub",
            "ref",
            "return",
            "self",
            "Self",
            "static",
            "struct",
            "super",
            "trait",
            "true",
            "type",
            "union",
            "unsafe",
            "use",
            "where",
            "while",
            "abstract",
            "become",
            "box",
            "do",
            "final",
            "macro",
            "override",
            "priv",
            "try",
            "typeof",
            "unsized",
            "virtual",
            "yield",
            "bool",
            "i8",
            "i16",
            "i32",
            "i64",
            "i128",
            "isize",
            "u8",
            "u16",
            "u32",
            "u64",
            "u128",
            "usize",
            "f32",
            "f64",
            "char",
            "str",
            "String",
            "Vec",
            "Option",
            "Result",
            "Box",
            "Rc",
            "Arc",
            "Cell",
            "RefCell",
            "HashMap",
            "HashSet",
            "BTreeMap",
            "BTreeSet",
            "Ok",
            "Err",
            "Some",
            "None",
            "true",
            "false",
            "println",
            "eprintln",
            "panic",
            "assert",
            "unreachable",
            "todo",
            "unimplemented",
            "Default",
            "Clone",
            "Debug",
            "Display",
            "From",
            "Into",
            "Iterator",
            "len",
            "new",
            "push",
            "pop",
            "iter",
            "map",
            "filter",
            "collect",
            "unwrap",
            "expect",
            "is_some",
            "is_none",
            "is_ok",
            "is_err",
        ]
    ),
    "ruby": frozenset(
        [
            "BEGIN",
            "END",
            "__ENCODING__",
            "__LINE__",
            "__FILE__",
            "alias",
            "and",
            "begin",
            "break",
            "case",
            "class",
            "def",
            "defined",
            "do",
            "else",
            "elsif",
            "end",
            "ensure",
            "false",
            "for",
            "if",
            "in",
            "module",
            "next",
            "nil",
            "not",
            "or",
            "redo",
            "rescue",
            "retry",
            "return",
            "self",
            "super",
            "then",
            "true",
            "undef",
            "unless",
            "until",
            "when",
            "while",
            "yield",
            "puts",
            "print",
            "raise",
            "require",
            "require_relative",
            "attr_accessor",
            "attr_reader",
            "attr_writer",
            "initialize",
            "new",
            "to_s",
            "to_i",
            "to_f",
            "to_a",
            "length",
            "size",
            "each",
            "map",
            "select",
            "reject",
            "include",
            "extend",
            "prepend",
            "freeze",
            "dup",
            "clone",
            "nil?",
            "empty?",
            "respond_to?",
        ]
    ),
    "php": frozenset(
        [
            "abstract",
            "and",
            "array",
            "as",
            "break",
            "callable",
            "case",
            "catch",
            "class",
            "clone",
            "const",
            "continue",
            "declare",
            "default",
            "die",
            "do",
            "echo",
            "else",
            "elseif",
            "empty",
            "enddeclare",
            "endfor",
            "endforeach",
            "endif",
            "endswitch",
            "endwhile",
            "eval",
            "exit",
            "extends",
            "final",
            "finally",
            "fn",
            "for",
            "foreach",
            "function",
            "global",
            "goto",
            "if",
            "implements",
            "include",
            "include_once",
            "instanceof",
            "insteadof",
            "interface",
            "isset",
            "list",
            "match",
            "namespace",
            "new",
            "or",
            "print",
            "private",
            "protected",
            "public",
            "readonly",
            "require",
            "require_once",
            "return",
            "static",
            "switch",
            "throw",
            "trait",
            "try",
            "unset",
            "use",
            "var",
            "while",
            "xor",
            "yield",
            "true",
            "false",
            "null",
            "TRUE",
            "FALSE",
            "NULL",
            "string",
            "int",
            "float",
            "bool",
            "array",
            "object",
            "callable",
            "void",
            "never",
            "self",
            "parent",
            "__CLASS__",
            "__DIR__",
            "__FILE__",
            "__FUNCTION__",
            "__LINE__",
            "__METHOD__",
            "__NAMESPACE__",
            "__TRAIT__",
            "count",
            "strlen",
            "in_array",
            "array_push",
            "array_pop",
            "array_merge",
            "isset",
            "empty",
            "unset",
            "echo",
            "var_dump",
            "print_r",
            "sprintf",
            "printf",
            "json_encode",
            "json_decode",
        ]
    ),
    "c": frozenset(
        [
            "auto",
            "break",
            "case",
            "char",
            "const",
            "continue",
            "default",
            "do",
            "double",
            "else",
            "enum",
            "extern",
            "float",
            "for",
            "goto",
            "if",
            "inline",
            "int",
            "long",
            "register",
            "restrict",
            "return",
            "short",
            "signed",
            "sizeof",
            "static",
            "struct",
            "switch",
            "typedef",
            "union",
            "unsigned",
            "void",
            "volatile",
            "while",
            "NULL",
            "true",
            "false",
            "bool",
            "_Bool",
            "_Complex",
            "_Imaginary",
            "printf",
            "scanf",
            "malloc",
            "free",
            "calloc",
            "realloc",
            "memcpy",
            "memmove",
            "memset",
            "strcmp",
            "strcpy",
            "strncpy",
            "strlen",
            "fprintf",
            "sprintf",
            "fopen",
            "fclose",
            "fread",
            "fwrite",
            "exit",
            "abort",
            "assert",
            "main",
            "FILE",
            "EOF",
            "NULL",
            "size_t",
            "uint8_t",
            "uint16_t",
            "uint32_t",
            "uint64_t",
            "int8_t",
            "int16_t",
            "int32_t",
            "int64_t",
        ]
    ),
    "cpp": frozenset(
        [
            "alignas",
            "alignof",
            "and",
            "and_eq",
            "asm",
            "auto",
            "bitand",
            "bitor",
            "bool",
            "break",
            "case",
            "catch",
            "char",
            "char8_t",
            "char16_t",
            "char32_t",
            "class",
            "compl",
            "concept",
            "const",
            "consteval",
            "constexpr",
            "constinit",
            "const_cast",
            "continue",
            "co_await",
            "co_return",
            "co_yield",
            "decltype",
            "default",
            "delete",
            "do",
            "double",
            "dynamic_cast",
            "else",
            "enum",
            "explicit",
            "export",
            "extern",
            "false",
            "float",
            "for",
            "friend",
            "goto",
            "if",
            "inline",
            "int",
            "long",
            "mutable",
            "namespace",
            "new",
            "noexcept",
            "not",
            "not_eq",
            "nullptr",
            "operator",
            "or",
            "or_eq",
            "private",
            "protected",
            "public",
            "register",
            "reinterpret_cast",
            "requires",
            "return",
            "short",
            "signed",
            "sizeof",
            "static",
            "static_assert",
            "static_cast",
            "struct",
            "switch",
            "template",
            "this",
            "thread_local",
            "throw",
            "true",
            "try",
            "typedef",
            "typeid",
            "typename",
            "union",
            "unsigned",
            "using",
            "virtual",
            "void",
            "volatile",
            "wchar_t",
            "while",
            "xor",
            "xor_eq",
            "override",
            "final",
            "string",
            "vector",
            "map",
            "set",
            "unordered_map",
            "unordered_set",
            "shared_ptr",
            "unique_ptr",
            "make_shared",
            "make_unique",
            "cout",
            "cin",
            "cerr",
            "endl",
            "printf",
            "std",
            "size_t",
            "nullptr",
            "NULL",
            "main",
            "int8_t",
            "int16_t",
            "int32_t",
            "int64_t",
            "uint8_t",
            "uint16_t",
            "uint32_t",
            "uint64_t",
            "begin",
            "end",
            "size",
            "empty",
            "push_back",
            "pop_back",
            "front",
            "back",
            "find",
            "insert",
            "erase",
            "clear",
        ]
    ),
}

_LANG_DEF_PATTERNS: dict[str, list[re.Pattern]] = {
    "verilog": [
        # module / interface / package / program declarations -- the top-level names
        re.compile(r"\b(?:module|macromodule|interface|package|program|primitive)\s+(\w+)"),
        # function / task
        # A return type AND a bit range can both sit between the keyword and the name:
        #   function automatic [7:0] rotate_left;
        # A pattern without the range clause silently loses every width-returning function.
        re.compile(
            r"\b(?:function|task)\s+"
            r"(?:automatic\s+|static\s+)?"
            r"(?:(?:signed|unsigned)\s+)?"
            r"(?:\w+\s+)?"
            r"(?:\[[^\]]*\]\s*)*"
            r"(\w+)\s*[\(;]"
        ),
        # net and variable declarations, with optional signedness and a bit range.
        # The range is skipped rather than parsed: `wire [WIDTH-1:0] name` must yield `name`,
        # and a pattern that stops at the bracket yields nothing at all.
        re.compile(
            r"\b(?:wire|reg|logic|bit|byte|int|integer|shortint|longint|real|realtime|time|"
            r"tri|triand|trior|tri0|tri1|wand|wor|supply0|supply1|uwire)\b"
            r"(?:\s+(?:signed|unsigned))?"
            r"(?:\s*\[[^\]]*\])*"
            r"\s+(\w+)"
        ),
        # ports in ANSI-style headers: input/output/inout, optional type, optional range
        re.compile(
            r"\b(?:input|output|inout)\b"
            r"(?:\s+(?:wire|reg|logic|bit|signed|unsigned))*"
            r"(?:\s*\[[^\]]*\])*"
            r"\s+(\w+)"
        ),
        # parameters and localparams
        re.compile(r"\b(?:parameter|localparam|specparam|genvar)\b(?:\s*\[[^\]]*\])?\s+(\w+)"),
        # typedef ... name;  -- the trailing identifier is the new type.
        # A packed struct/union body CONTAINS semicolons:
        #     typedef struct packed { logic [7:0] a; logic b; } zzq_pkt_t;
        # so a [^;]*? body stops at the first inner one and never reaches the type name.
        # Braced forms are matched separately, allowing semicolons inside the braces.
        re.compile(r"\btypedef\s+(?:struct|union|enum)\b[^{]*\{[^}]*\}\s*(\w+)\s*;", re.DOTALL),
        re.compile(r"\btypedef\b[^;{]*?\b(\w+)\s*;"),
        # Implicitly-declared nets. Verilog lets a name spring into existence on assignment:
        #     assign zzq_sig = ...;   always_comb zzq_sig = ...;
        # There is no declaration to match, and an obfuscator that only reads declarations
        # leaves every implicit net in the clear.
        re.compile(r"\bassign\s+(\w+)\s*(?:\[[^\]]*\]\s*)?="),
        re.compile(r"\balways(?:_comb|_ff|_latch)?\b[^;\n]*?\b(\w+)\s*<?=[^=]"),
        # enum members and struct fields are declared inside braces; catch simple cases
        re.compile(r"\b(?:enum|struct|union)\b[^;{]*\{[^}]*?\b(\w+)\s*[,}]"),
        # module INSTANTIATION: `my_module #(...) u_inst (...)` -- both names matter, and the
        # instance name is frequently the most descriptive thing in a netlist.
        re.compile(r"^\s*(\w+)\s+(?:#\s*\((?:[^()]|\([^()]*\))*\)\s*)?\w+\s*\(", re.MULTILINE),
        re.compile(r"^\s*\w+\s+(?:#\s*\((?:[^()]|\([^()]*\))*\)\s*)?(\w+)\s*\(", re.MULTILINE),
        # named port connections: .port_name(signal_name) -- capture both
        re.compile(r"\.(\w+)\s*\("),
        re.compile(r"\.\w+\s*\(\s*(\w+)"),
        # `define MACRO_NAME
        re.compile(r"`define\s+(\w+)"),
        # generate-block and named-block labels: begin : name
        re.compile(r"\bbegin\s*:\s*(\w+)"),
        # class / modport / clocking / covergroup names
        re.compile(r"\b(?:class|modport|clocking|covergroup|property|sequence)\s+(\w+)"),
    ],
    "java": [
        re.compile(r"\bclass\s+([A-Za-z_]\w*)"),
        re.compile(r"\binterface\s+([A-Za-z_]\w*)"),
        re.compile(r"\benum\s+([A-Za-z_]\w*)"),
        re.compile(
            r"(?:public|private|protected|static|final|abstract|synchronized)\s+(?:[\w<>\[\],\s]+\s+)?([a-z_]\w*)\s*\("
        ),
        re.compile(r"(?:private|protected)\s+[\w<>\[\]]+\s+([a-z_]\w*)\s*[;=]"),
    ],
    "rust": [
        re.compile(r"\bfn\s+([a-z_]\w*)"),
        re.compile(r"\bstruct\s+([A-Za-z_]\w*)"),
        re.compile(r"\benum\s+([A-Za-z_]\w*)"),
        re.compile(r"\btrait\s+([A-Za-z_]\w*)"),
        re.compile(r"\bimpl(?:\s+\w+\s+for)?\s+([A-Za-z_]\w*)"),
        re.compile(r"\blet\s+(?:mut\s+)?([a-z_]\w*)\s*[=:]"),
        re.compile(r"\bconst\s+([A-Z_]\w*)\s*:"),
        re.compile(r"\btype\s+([A-Za-z_]\w*)\s*="),
    ],
    "ruby": [
        re.compile(r"\bdef\s+([a-z_]\w*[!?]?)"),
        re.compile(r"\bclass\s+([A-Z]\w*)"),
        re.compile(r"\bmodule\s+([A-Z]\w*)"),
        re.compile(r"\b([a-z_]\w*)\s*=\s*(?:proc\s*\{|lambda\s*\{|Proc\.new)"),
        re.compile(r"\battr_(?:accessor|reader|writer)\s+:([a-z_]\w*)"),
    ],
    "php": [
        re.compile(r"\bfunction\s+([a-zA-Z_]\w*)"),
        re.compile(r"\bclass\s+([A-Za-z_]\w*)"),
        re.compile(r"\binterface\s+([A-Za-z_]\w*)"),
        re.compile(r"\btrait\s+([A-Za-z_]\w*)"),
        re.compile(r"\$([a-zA-Z_]\w*)\s*="),
    ],
    "c": [
        re.compile(r"\btypedef\s+(?:struct\s+\w+\s+)?(\w+)\s*;"),
        re.compile(r"\bstruct\s+([A-Za-z_]\w*)"),
        re.compile(r"\benum\s+([A-Za-z_]\w*)"),
        re.compile(
            r"^(?:static\s+|extern\s+|inline\s+)*\w[\w\s\*]+\s+([a-z_]\w*)\s*\(", re.MULTILINE
        ),
    ],
    "cpp": [
        re.compile(r"\bclass\s+([A-Za-z_]\w*)"),
        re.compile(r"\bstruct\s+([A-Za-z_]\w*)"),
        re.compile(r"\benum(?:\s+class)?\s+([A-Za-z_]\w*)"),
        re.compile(r"\bnamespace\s+([a-zA-Z_]\w*)"),
        re.compile(r"\btemplate\s*<[^>]*>\s*(?:class|struct)\s+([A-Za-z_]\w*)"),
        re.compile(
            r"^(?:static\s+|virtual\s+|explicit\s+|inline\s+|constexpr\s+)*[\w:]+[\w\s\*&<>:,]+\s+([a-z_]\w*)\s*\(",
            re.MULTILINE,
        ),
    ],
}

_SINGLE_CHAR_RE = re.compile(r"^[a-zA-Z_]$")


def _verilog_enum_members(cleaned: str) -> set[str]:
    """Every member of every enum body, not just the first.

    A per-pattern regex returns one capture group per match, so `{ A, B, C }` yields only A --
    and enum members are STATE NAMES. IDLE/LOADING/CRUNCHING describes what a design does more
    plainly than most signal names do, so capturing one in three is a leak with a tidy count
    beside it. Handled as a pass over the whole body rather than as another pattern, because
    this is the shape a pattern list cannot express.
    """
    out: set[str] = set()
    for body in re.finditer(r"\benum\b[^{]*\{([^}]*)\}", cleaned, re.DOTALL):
        for token in re.finditer(r"\b([A-Za-z_]\w*)\b", body.group(1)):
            out.add(token.group(1))
    return out


def _extract_lang_identifiers(
    source: str,
    language: str,
    safe: frozenset,
) -> frozenset:
    """
    Regex-based private identifier extraction for non-Python languages.
    Strips comments and string literals before matching to avoid false positives.
    """
    strip_re = _COMMENT_STRIP.get(language)
    cleaned = strip_re.sub(" ", source) if strip_re else source
    # Verilog gets its own literal stripper -- see _VERILOG_STR_STRIP. Using the shared one
    # here blanks code between macro directives and between sized literals, and every
    # identifier lost that way leaves the repository unobfuscated.
    cleaned = (_VERILOG_STR_STRIP if language == "verilog" else _STR_STRIP).sub('""', cleaned)

    keywords = _LANG_KEYWORDS.get(language, frozenset())
    patterns = _LANG_DEF_PATTERNS.get(language, [])

    found: set[str] = set()
    for pat in patterns:
        for m in pat.finditer(cleaned):
            name = m.group(1).strip()
            if not name:
                continue
            if _SINGLE_CHAR_RE.match(name):
                continue
            if len(name) < 3:
                continue
            if name in keywords or name in safe:
                continue
            if language == "verilog" and _is_pdk_cell(name):
                continue
            found.add(name)

    if language == "verilog":
        for name in _verilog_enum_members(cleaned):
            if (
                len(name) >= 3
                and name not in keywords
                and name not in safe
                and not _is_pdk_cell(name)
            ):
                found.add(name)

    return frozenset(found)


#: Cloak's own output token. Deliberately unlike any identifier a human writes, which is what
#: makes an already-cloaked file detectable rather than a judgement call.
_CLOAK_TOKEN_RE = re.compile(r"\bx_\d{4}\b")

#: Below this, a match is more likely a coincidence in a real design than a cloaked file.
_CLOAK_TOKEN_MIN = 3


def already_cloaked(text: str) -> int:
    """How many distinct Cloak tokens a file contains."""
    return len(set(_CLOAK_TOKEN_RE.findall(text or "")))


def assert_not_already_cloaked(hits: dict[str, int]) -> None:
    """Fail closed if any source already carries Cloak output.

    `hits` maps a file name to its distinct-token count, accumulated by the caller as it scans.
    Counts rather than text, so a large repo is not held in memory to answer a cheap question.

    Cloaking a cloaked file maps `x_0001` as though it were a design name. Restoration then
    returns text that is NEITHER the original NOR valid source -- real names in some places,
    stale tokens in others -- and a patch built from it carries `x_0001` into the customer's
    design. A leak audit does not catch it, because the tokens are legitimately in that run's
    forward map.

    Raising is the only safe answer. Skipping the file quietly would leave a design half
    obfuscated against a map that does not describe it.
    """
    hits = {k: v for k, v in hits.items() if v >= _CLOAK_TOKEN_MIN}
    if not hits:
        return
    listing = ", ".join(f"{k} ({v} tokens)" for k, v in sorted(hits.items())[:5])
    raise ValueError(
        "refusing to cloak: these files already contain Cloak output -- "
        f"{listing}. Cloaking them a second time maps x_NNNN tokens as if they were design "
        "names, and restoration then returns text that is neither the original nor valid "
        "source. Remove the cloaked artifacts from the workspace and re-run."
    )


def _build_cloak_context_nonpython(
    instance_id: str,
    repo_path: Path,
    language: str,
) -> CloakContext:
    """
    Scan all source files for a non-Python language and build a CloakContext.

    Extraction priority:
      1. tree-sitter (real AST — handles macros, generics, templates correctly)
      2. regex patterns (fallback when tree-sitter grammar unavailable)
    """
    _SKIP = {
        "vendor",
        "node_modules",
        "target",
        "build",
        "dist",
        ".git",
        "site-packages",
        "__pycache__",
        ".gradle",
        ".mvn",
        "testdata",
    }
    _EXT_MAP = {
        "java": [".java"],
        "rust": [".rs"],
        "ruby": [".rb"],
        "php": [".php"],
        "c": [".c", ".h"],
        "cpp": [".cpp", ".cc", ".cxx", ".hpp", ".h"],
        "go": [".go"],
        "typescript": [".ts", ".tsx"],
        "javascript": [".js", ".jsx"],
        # .vh and .svh are header files; leaving them out would miss every shared `define,
        # parameter and typedef -- which is where a design's most identifying names live.
        "verilog": [".v", ".sv", ".vh", ".svh"],
    }
    extensions = _EXT_MAP.get(language, [])
    safe: frozenset[str] = frozenset()

    ts_available = _TS_AVAILABLE and language in TS_SUPPORTED_LANGUAGES
    all_private: set[str] = set()
    files_scanned = 0
    ts_hits = 0
    regex_hits = 0

    _cloaked_files: dict[str, int] = {}
    for ext in extensions:
        for src_file in repo_path.rglob(f"*{ext}"):
            if any(part in _SKIP for part in src_file.parts):
                continue
            if src_file.stat().st_size > 500_000:
                continue
            try:
                source = src_file.read_text(encoding="utf-8", errors="replace")
                files_scanned += 1

                # Accumulated here, raised AFTER the loop. The `except Exception` below is
                # broad on purpose -- one unparseable file must not abort a repo scan -- and it
                # would swallow this, turning a fail-closed guard into a debug log line.
                n_tokens = already_cloaked(source)
                if n_tokens >= _CLOAK_TOKEN_MIN:
                    _cloaked_files[src_file.name] = n_tokens

                if ts_available:
                    ids = extract_treesitter_identifiers(source, language, safe)
                    if ids:
                        all_private |= ids
                        ts_hits += 1
                        continue

                ids = _extract_lang_identifiers(source, language, safe)
                all_private |= ids
                regex_hits += 1
            except Exception as e:
                log.debug("Cloak(%s): skipping %s: %s", language, src_file.name, e)

    assert_not_already_cloaked(_cloaked_files)

    backend = "tree-sitter" if ts_available else "regex"
    if ts_available and regex_hits:
        backend = f"tree-sitter({ts_hits})+regex({regex_hits})"
    log.info(
        "Cloak(%s): scanned %d files via %s, found %d private identifiers",
        language,
        files_scanned,
        backend,
        len(all_private),
    )

    # FAIL-CLOSED: scanning real source files and extracting NOTHING means obfuscate_source()
    # becomes an identity function -- the caller ships plaintext believing it is cloaked. That
    # is the exact leak CloakObfuscationError exists to prevent, so it must be loud.
    #
    # This is reachable today, not hypothetical. TS_SUPPORTED_LANGUAGES is a hardcoded frozenset
    # of 9 languages, but pyproject's [cloak] extra declares only 4 grammars, and
    # _LANG_DEF_PATTERNS has regex for a different 6. TypeScript falls in the gap with NO
    # extraction path at all: `ts_available` is True (the language IS in the advertised set),
    # extract_treesitter_identifiers returns empty (grammar not installed), the regex fallback
    # has no typescript entry, and a .ts file used to sail through untouched.
    # Measured 2026-07-26; see tests/test_cloak_language_coverage.py.
    if files_scanned and not all_private:
        from . import CloakObfuscationError

        if not _ALLOW_DEGRADED:
            log.error(
                "Cloak(%s): scanned %d file(s) via %s and extracted 0 identifiers — failing "
                "closed rather than sending plaintext.",
                language,
                files_scanned,
                backend,
            )
            raise CloakObfuscationError(
                path=str(repo_path),
                cause=RuntimeError(
                    f"no identifier-extraction path for language {language!r}: "
                    f"tree-sitter grammar loaded={ts_available and bool(ts_hits)}, "
                    f"regex patterns={'yes' if language in _LANG_DEF_PATTERNS else 'no'}. "
                    f"Install the grammar (pip install tree-sitter-{language}) or set "
                    f"DETERMINEX_CLOAK_ALLOW_DEGRADED=1 to accept reduced privacy."
                ),
                source_len=0,
            )
        log.warning(
            "Cloak(%s): 0 identifiers extracted from %d file(s); "
            "DETERMINEX_CLOAK_ALLOW_DEGRADED=1 set — proceeding with NO obfuscation.",
            language,
            files_scanned,
        )

    symbol_map = SymbolMap.build(frozenset(all_private))
    log.info(
        "Cloak(%s): symbol map ready — %d identifiers mapped", language, len(symbol_map.forward)
    )
    return CloakContext(
        instance_id=instance_id,
        symbol_map=symbol_map,
        star_import_warnings=[],
    )


_build_cloak_context_regex = _build_cloak_context_nonpython


def build_cloak_context(
    instance_id: str,
    repo_path: Path,
    language: str = "python",
) -> CloakContext:
    """
    Build a complete CloakContext for one solve() call.
    Scans the WHOLE REPO to build a consistent symbol map (Broad Scope guarantee).

    language routing:
      python                       → stdlib ast module (most precise)
      go/ts/js/java/rust/ruby/...  → tree-sitter real AST (preferred)
                                     → per-language regex module (fallback)
    """
    log.info("Cloak: building context for %s (language=%s)", instance_id, language)

    lang_norm = {"ts": "typescript", "js": "javascript", "c++": "cpp"}.get(language, language)

    # A language missing from this tuple does not error -- it falls through to the PYTHON
    # scanner at the bottom of this function, which finds nothing in non-Python source and
    # returns an EMPTY symbol map. obfuscate_source() then returns the text unchanged and the
    # caller ships plaintext believing it was cloaked. That is a leak wearing the costume of a
    # routing bug, and it is exactly what happened to verilog: single-file extraction was
    # correct while whole-repo cloaking silently produced zero mappings.
    if lang_norm in ("java", "rust", "ruby", "php", "c", "cpp", "verilog"):
        return _build_cloak_context_nonpython(instance_id, repo_path, lang_norm)

    if lang_norm == "go":
        if _TS_AVAILABLE and "go" in TS_SUPPORTED_LANGUAGES:
            return _build_cloak_context_nonpython(instance_id, repo_path, "go")
        return _build_cloak_context_go(instance_id, repo_path)

    if lang_norm in ("typescript", "javascript"):
        if _TS_AVAILABLE and lang_norm in TS_SUPPORTED_LANGUAGES:
            return _build_cloak_context_nonpython(instance_id, repo_path, lang_norm)
        return _build_cloak_context_ts(instance_id, repo_path)

    # FAIL CLOSED. Everything below is the Python AST scanner. Arriving here with any other
    # language means a routing gap, and the failure mode is silent plaintext -- so refuse
    # rather than return an empty map that looks like a clean run.
    if lang_norm != "python":
        raise ValueError(
            f"Cloak has no context builder for language {lang_norm!r}; it would fall through to "
            "the Python scanner, find nothing, and return an empty symbol map -- which reads as "
            "a successful cloak and ships plaintext. Add it to the dispatch above."
        )

    safe_names = _build_safe_list(repo_path)
    log.info("Cloak: safe-list = %d names", len(safe_names))
    private_ids, star_warnings = build_private_identifier_set(repo_path, safe_names)
    symbol_map = SymbolMap.build(private_ids)
    log.info("Cloak: symbol map ready — %d identifiers mapped", len(symbol_map.forward))
    if star_warnings:
        log.warning(
            "Cloak: %d star-import holes (names pass through uncloaked):", len(star_warnings)
        )
        for w in star_warnings[:5]:
            log.warning("  %s", w)
        if len(star_warnings) > 5:
            log.warning("  ... and %d more", len(star_warnings) - 5)
    return CloakContext(
        instance_id=instance_id,
        symbol_map=symbol_map,
        star_import_warnings=star_warnings,
    )


def _build_cloak_context_go(instance_id: str, repo_path: Path) -> CloakContext:
    """Build CloakContext for a Go repository (legacy regex bridge)."""
    try:
        from determinex_cloak_go import (  # type: ignore[import]
            GO_BUILTIN_SAFE,
            GoStdlibManifest,
            extract_go_private_identifiers,
        )
    except ImportError as e:
        log.error("determinex_cloak_go not available: %s — falling back to empty map", e)
        return CloakContext(
            instance_id=instance_id,
            symbol_map=SymbolMap.build(frozenset()),
            star_import_warnings=[],
        )

    manifest = GoStdlibManifest.build()
    combined_safe = manifest.safe_names | GO_BUILTIN_SAFE

    all_private: set[str] = set()
    go_files_scanned = 0
    for go_file in repo_path.rglob("*.go"):
        if any(part.startswith(".") for part in go_file.parts):
            continue
        if "vendor" in go_file.parts or "testdata" in go_file.parts:
            continue
        try:
            source = go_file.read_text(encoding="utf-8", errors="replace")
            ids = extract_go_private_identifiers(source)
            all_private |= ids
            go_files_scanned += 1
        except Exception as e:
            log.debug("Cloak(go): skipping %s: %s", go_file.name, e)

    all_private -= combined_safe
    log.info(
        "Cloak(go): scanned %d files, found %d private identifiers",
        go_files_scanned,
        len(all_private),
    )
    symbol_map = SymbolMap.build(frozenset(all_private))
    log.info("Cloak(go): symbol map ready — %d identifiers mapped", len(symbol_map.forward))
    return CloakContext(
        instance_id=instance_id,
        symbol_map=symbol_map,
        star_import_warnings=[],
    )


def _build_cloak_context_ts(instance_id: str, repo_path: Path) -> CloakContext:
    """Build CloakContext for a TypeScript/JavaScript repository (legacy bridge)."""
    try:
        from determinex_cloak_ts import (  # type: ignore[import]
            TS_BUILTIN_SAFE,
            extract_ts_private_identifiers,
        )
    except ImportError as e:
        log.error("determinex_cloak_ts not available: %s — falling back to empty map", e)
        return CloakContext(
            instance_id=instance_id,
            symbol_map=SymbolMap.build(frozenset()),
            star_import_warnings=[],
        )

    all_private: set[str] = set()
    ts_files_scanned = 0
    for ts_file in repo_path.rglob("*"):
        if not ts_file.is_file():
            continue
        if ts_file.suffix not in (".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs"):
            continue
        if any(part.startswith(".") for part in ts_file.parts):
            continue
        if any(skip in ts_file.parts for skip in ("node_modules", "dist", "build", "__pycache__")):
            continue
        if ts_file.stem.endswith((".min", ".bundle")):
            continue
        try:
            source = ts_file.read_text(encoding="utf-8", errors="replace")
            ids = extract_ts_private_identifiers(source)
            all_private |= ids
            ts_files_scanned += 1
        except Exception as e:
            log.debug("Cloak(ts): skipping %s: %s", ts_file.name, e)

    all_private -= TS_BUILTIN_SAFE
    log.info(
        "Cloak(ts): scanned %d files, found %d private identifiers",
        ts_files_scanned,
        len(all_private),
    )
    symbol_map = SymbolMap.build(frozenset(all_private))
    log.info("Cloak(ts): symbol map ready — %d identifiers mapped", len(symbol_map.forward))
    return CloakContext(
        instance_id=instance_id,
        symbol_map=symbol_map,
        star_import_warnings=[],
    )
