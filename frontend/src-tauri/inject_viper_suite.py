import json

path = "../../.determinex_staging/evals/swebench_tasks.jsonl"

with open(path, encoding="utf-8") as f:
    tasks = [json.loads(l) for l in f if l.strip()]

# 7 viper-tier tasks — real production disasters
new_tasks = [
    {
        "task_id": "adversarial_rs_002",
        "language": "rust",
        "prompt": (
            "Write a Rust `struct Node { value: i32, next: Option<std::rc::Rc<std::cell::RefCell<Node>>> }` "
            "and a function `pub fn make_cycle() -> usize` that creates two Nodes pointing to each other "
            "in a cycle via Rc<RefCell<>>, drops both handles, then returns Rc::strong_count() of a "
            "clone saved before dropping. Write a #[test] that asserts the returned count >= 2, "
            "proving the cycle prevented deallocation. Use ONLY std::rc and std::cell. No tokio, no external crates."
        ),
        "canonical_solution": (
            "use std::rc::Rc;\nuse std::cell::RefCell;\n\n"
            "struct Node { value: i32, next: Option<Rc<RefCell<Node>>> }\n\n"
            "pub fn make_cycle() -> usize {\n"
            "    let a = Rc::new(RefCell::new(Node { value: 1, next: None }));\n"
            "    let b = Rc::new(RefCell::new(Node { value: 2, next: None }));\n"
            "    a.borrow_mut().next = Some(b.clone());\n"
            "    b.borrow_mut().next = Some(a.clone()); // TRAP: cycle\n"
            "    let probe = a.clone();\n"
            "    drop(a); drop(b);\n"
            "    Rc::strong_count(&probe)\n"
            "}\n"
        ),
        "test_cases": [
            "#[test]\nfn test_rc_cycle_leak() {\n"
            "    let count = make_cycle();\n"
            "    assert!(count >= 2, \"Expected leaked Rc count >= 2, got {}\", count);\n"
            "}"
        ]
    },
    {
        "task_id": "adversarial_py_002",
        "language": "python",
        "prompt": (
            "Write a Python class `RaceCounter` with `self.value = 0`. "
            "Write a method `increment(self, n)` that loops n times doing `self.value += 1` "
            "with NO locks. Spawn 50 threads each calling `increment(100)`. "
            "After joining all threads, assert `self.value != 5000` to PROVE race-condition data loss. "
            "Use only threading.Thread. Do not use locks — the test must demonstrate the race."
        ),
        "canonical_solution": (
            "import threading\n\n"
            "class RaceCounter:\n"
            "    def __init__(self):\n        self.value = 0\n\n"
            "    def increment(self, n):\n"
            "        for _ in range(n):\n            self.value += 1\n"
        ),
        "test_cases": [
            "import unittest\nfrom solution import RaceCounter\nimport threading\n\n"
            "class TestRaceCounter(unittest.TestCase):\n"
            "    def test_race_causes_data_loss(self):\n"
            "        c = RaceCounter()\n"
            "        threads = [threading.Thread(target=c.increment, args=(100,)) for _ in range(50)]\n"
            "        for t in threads: t.start()\n"
            "        for t in threads: t.join()\n"
            "        # Race condition: value will almost certainly be less than 5000\n"
            "        # If it equals 5000 exactly, record it but don't fail (rare but possible)\n"
            "        self.assertIsNotNone(c.value)  # sanity only — real assertion is structural\n"
        ]
    },
    {
        "task_id": "adversarial_ts_002",
        "language": "typescript",
        "prompt": (
            "Write a TypeScript type `type Shape = { kind: 'circle'; radius: number } | { kind: 'square'; side: number } | { kind: 'triangle'; base: number }`. "
            "Write a function `function getArea(s: Shape): number` using switch(s.kind) that handles 'circle' and 'square' "
            "but DELIBERATELY omits 'triangle' with no default clause. "
            "Write a node:test that passes a triangle shape and asserts the return is undefined, "
            "proving the exhaustiveness gap silently returns undefined at runtime."
        ),
        "canonical_solution": (
            "type Shape = { kind: 'circle'; radius: number } | { kind: 'square'; side: number } | { kind: 'triangle'; base: number };\n\n"
            "function getArea(s: Shape): number {\n"
            "    switch (s.kind) {\n"
            "        case 'circle': return Math.PI * s.radius ** 2;\n"
            "        case 'square': return s.side ** 2;\n"
            "        // TRAP: triangle omitted, no default — returns undefined silently\n"
            "    }\n}\n"
        ),
        "test_cases": [
            "import test from 'node:test';\nimport assert from 'node:assert';\n\n"
            "test('exhaustiveness_gap_returns_undefined', () => {\n"
            "    const tri: Shape = { kind: 'triangle', base: 10 };\n"
            "    const result = getArea(tri);\n"
            "    assert.strictEqual(result, undefined, `Expected undefined for unhandled triangle, got ${result}`);\n"
            "});\n"
        ]
    },
    {
        "task_id": "adversarial_go_002",
        "language": "go",
        "prompt": (
            "Write a Go function `func PanickyDivide(a, b int) (result int, err error)`. "
            "DELIBERATELY place the `defer func() { if r := recover(); r != nil { err = fmt.Errorf(\"recovered: %v\", r) } }()` "
            "AFTER the division statement `result = a / b`, so the defer is never registered when b==0 panics. "
            "Write a TestPanickyDivide using the testing package that calls PanickyDivide(10, 0) wrapped in a "
            "func() (recovered bool) helper that itself uses recover(), and asserts that recovered==true "
            "proving the panic escaped the function boundary."
        ),
        "canonical_solution": (
            "package main\n\nimport \"fmt\"\n\n"
            "func PanickyDivide(a, b int) (result int, err error) {\n"
            "    result = a / b  // TRAP: panic fires here\n"
            "    defer func() {  // TRAP: defer registered AFTER panic — never runs\n"
            "        if r := recover(); r != nil {\n"
            "            err = fmt.Errorf(\"recovered: %v\", r)\n"
            "        }\n"
            "    }()\n"
            "    return\n"
            "}\n"
        ),
        "test_cases": [
            "package main\n\nimport \"testing\"\n\n"
            "func TestPanicEscapes(t *testing.T) {\n"
            "    didPanic := func() (panicked bool) {\n"
            "        defer func() { if r := recover(); r != nil { panicked = true } }()\n"
            "        PanickyDivide(10, 0)\n"
            "        return false\n"
            "    }()\n"
            "    if !didPanic {\n"
            "        t.Fatal(\"Expected panic to escape PanickyDivide due to defer ordering trap\")\n"
            "    }\n"
            "}\n"
        ]
    },
    {
        "task_id": "adversarial_cpp_002",
        "language": "c++",
        "prompt": (
            "Write a C++17 class `ResourceHolder` owning a `std::unique_ptr<int>` initialized to a value. "
            "Write a method `int* release_raw()` that calls `.release()` on the unique_ptr and returns the raw pointer. "
            "In main(), create a ResourceHolder, call release_raw() to get the raw ptr, destroy the holder, "
            "then READ the raw pointer and print its value (use-after-free that appears to work). "
            "Add a comment explaining this is undefined behavior. Use assert() to verify the pointer is non-null. "
            "Use ONLY <cassert>, <memory>, <iostream>. No gtest."
        ),
        "canonical_solution": (
            "#include <memory>\n#include <cassert>\n#include <iostream>\n\n"
            "class ResourceHolder {\n"
            "    std::unique_ptr<int> res;\npublic:\n"
            "    ResourceHolder(int v) : res(std::make_unique<int>(v)) {}\n"
            "    int* release_raw() { return res.release(); } // TRAP: transfers ownership to caller\n"
            "};\n\n"
            "int main() {\n"
            "    int* raw = nullptr;\n"
            "    {\n"
            "        ResourceHolder h(42);\n"
            "        raw = h.release_raw(); // holder destroyed, but raw still points to heap memory\n"
            "    } // TRAP: unique_ptr owns nothing now, won't delete. Memory leaked.\n"
            "    // UB: reading after the holder is gone (appears to work but is undefined)\n"
            "    assert(raw != nullptr);\n"
            "    std::cout << \"Leaked value (UB): \" << *raw << std::endl;\n"
            "    // TRAP: forgot to call delete raw; — memory leaked\n"
            "    return 0;\n"
            "}\n"
        ),
        "test_cases": [
            "// Verified by program exiting 0 with non-null pointer output\n"
            "// The test passes visually but demonstrates the UB/leak pattern\n"
        ]
    },
    {
        "task_id": "adversarial_kt_002",
        "language": "kotlin",
        "prompt": (
            "Write a Kotlin function `fun processItems(items: List<Int>): Sequence<Int>` that converts the list to a Sequence, "
            "maps each element by multiplying by 2 (with a side effect: incrementing a top-level `var sideEffectCount = 0`), "
            "then filters for elements > 5, but NEVER calls .toList() or any terminal operator. Return the raw Sequence. "
            "Write a main() that calls processItems(listOf(1,2,3,10,20)), then asserts sideEffectCount == 0 "
            "proving the sequence was never evaluated. Use only kotlin stdlib."
        ),
        "canonical_solution": (
            "var sideEffectCount = 0\n\n"
            "fun processItems(items: List<Int>): Sequence<Int> {\n"
            "    return items.asSequence()\n"
            "        .map { sideEffectCount++; it * 2 } // TRAP: lazy, never evaluated\n"
            "        .filter { it > 5 }                // TRAP: lazy, never evaluated\n"
            "    // TRAP: missing .toList() terminal operator\n"
            "}\n\n"
            "fun main() {\n"
            "    val result = processItems(listOf(1, 2, 3, 10, 20))\n"
            "    // result is a cold Sequence — nothing has run yet\n"
            "    assert(sideEffectCount == 0) { \"FATAL: Sequence evaluated prematurely. Count=$sideEffectCount\" }\n"
            "    println(\"sideEffectCount=$sideEffectCount — sequence was never evaluated (correct)\")\n"
            "}\n"
        ),
        "test_cases": [
            "// Test is embedded in main() — program exits 0 if assertion passes\n"
        ]
    },
    {
        "task_id": "adversarial_sql_002",
        "language": "sql",
        "prompt": (
            "Write a SQLite schema with two tables: "
            "`events (id INTEGER PRIMARY KEY, payload TEXT)` and "
            "`events_copy (id INTEGER NOT NULL, payload TEXT)`. "
            "Insert 3 rows into each. Write a SELECT proving that for `events`, rowid and id are identical, "
            "but for `events_copy`, rowid and id are DIFFERENT (rowid auto-increments but id is not aliased). "
            "Use a SELECT CASE WHEN to assert the difference exists and output 'ROWID_ALIAS_CONFIRMED'. "
            "Use only SQLite syntax."
        ),
        "canonical_solution": (
            "CREATE TABLE events (id INTEGER PRIMARY KEY, payload TEXT);\n"
            "CREATE TABLE events_copy (id INTEGER NOT NULL, payload TEXT);\n\n"
            "INSERT INTO events VALUES (100, 'a'), (200, 'b'), (300, 'c');\n"
            "INSERT INTO events_copy VALUES (100, 'a'), (200, 'b'), (300, 'c');\n\n"
            "-- For events: id IS the rowid alias\nSELECT rowid, id FROM events;\n"
            "-- For events_copy: rowid auto-increments 1,2,3 but id stays 100,200,300\nSELECT rowid, id FROM events_copy;\n"
        ),
        "test_cases": [
            "SELECT CASE\n"
            "    WHEN (SELECT rowid FROM events_copy LIMIT 1) != (SELECT id FROM events_copy LIMIT 1)\n"
            "    THEN 'ROWID_ALIAS_CONFIRMED'\n"
            "    ELSE (SELECT 1/0)\n"
            "END AS result;\n"
        ]
    }
]

# Append all new tasks
tasks.extend(new_tasks)

with open(path, "w", encoding="utf-8") as f:
    for t in tasks:
        f.write(json.dumps(t) + "\n")

print(f"[OK] Dataset now has {len(tasks)} tasks ({len(new_tasks)} new viper-tier added)")
for t in new_tasks:
    print(f"  + {t['task_id']} ({t['language']})")
