import json

path = "../../.determinex_staging/evals/swebench_tasks.jsonl"

with open(path, encoding="utf-8") as f:
    tasks = [json.loads(l) for l in f if l.strip()]

for t in tasks:
    # Fix adversarial_sql_001 - rewrite as SQLite (AFTER trigger recursive loop, same concept)
    if t["task_id"] == "adversarial_sql_001":
        t["prompt"] = (
            "Write a SQLite schema script that creates an `audit_log` table with columns "
            "`id INTEGER PRIMARY KEY AUTOINCREMENT`, `payload TEXT`, `last_updated TEXT DEFAULT (datetime('now'))`. "
            "Deliberately write an AFTER UPDATE trigger on `audit_log` that runs another UPDATE on the same table, "
            "causing an infinite recursive trigger loop. "
            "Do NOT add a recursion guard. "
            "Then INSERT one row and UPDATE it to trigger the infinite loop. "
            "Use ONLY standard SQLite syntax - no PL/pgSQL, no SERIAL, no PostgreSQL extensions."
        )
        t["canonical_solution"] = (
            "CREATE TABLE audit_log (\n"
            "    id INTEGER PRIMARY KEY AUTOINCREMENT,\n"
            "    payload TEXT,\n"
            "    last_updated TEXT DEFAULT (datetime('now'))\n"
            ");\n\n"
            "-- TRAP: AFTER UPDATE triggers the same UPDATE = infinite loop\n"
            "CREATE TRIGGER trg_auto_update\n"
            "AFTER UPDATE ON audit_log\n"
            "FOR EACH ROW\n"
            "BEGIN\n"
            "    UPDATE audit_log SET last_updated = datetime('now') WHERE id = NEW.id;\n"
            "END;\n\n"
            "INSERT INTO audit_log (payload) VALUES ('Initial Entry');\n"
            "UPDATE audit_log SET payload = 'Trigger Test' WHERE id = 1;\n"
        )
        t["test_cases"] = [
            "-- SQLite recursive trigger test: this UPDATE should hit the trigger depth limit\n"
            "UPDATE audit_log SET payload = 'Fire It' WHERE id = 1;\n"
            "SELECT 'DONE' AS result;\n"
        ]
        print(f"[OK] Rewrote adversarial_sql_001 to SQLite syntax")

with open(path, "w", encoding="utf-8") as f:
    for t in tasks:
        f.write(json.dumps(t) + "\n")

print("Dataset saved.")
