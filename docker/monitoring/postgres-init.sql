-- Determinex Postgres schema (replaces SQLite for production)
-- Includes pgvector for embeddings (RAG layer)

CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- ── tools / evals (mirror of determinex_db.py schema) ──────────────
CREATE TABLE IF NOT EXISTS tools (
    instance_id TEXT PRIMARY KEY,
    family TEXT,
    version TEXT,
    last_eval_at TIMESTAMPTZ,
    locked_pct REAL,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS iterations (
    id BIGSERIAL PRIMARY KEY,
    label TEXT,
    started_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    ended_at TIMESTAMPTZ,
    scaffold_version TEXT,
    total_tools INT,
    scored INT,
    agg_weighted REAL,
    agg_per_tool REAL,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS evals (
    id BIGSERIAL PRIMARY KEY,
    instance_id TEXT NOT NULL REFERENCES tools(instance_id) ON DELETE CASCADE,
    branch TEXT,
    iteration_id BIGINT REFERENCES iterations(id) ON DELETE SET NULL,
    ran_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    passed INT,
    total INT,
    pct REAL GENERATED ALWAYS AS (CASE WHEN total > 0 THEN 100.0 * passed / total ELSE NULL END) STORED,
    duration_s INT,
    rc INT,
    error TEXT,
    source_path TEXT,
    UNIQUE(instance_id, ran_at)
);
CREATE INDEX IF NOT EXISTS idx_evals_inst ON evals(instance_id);
CREATE INDEX IF NOT EXISTS idx_evals_iter ON evals(iteration_id);
CREATE INDEX IF NOT EXISTS idx_evals_pct ON evals(pct);
CREATE INDEX IF NOT EXISTS idx_evals_ran_at ON evals(ran_at DESC);

CREATE TABLE IF NOT EXISTS test_results (
    id BIGSERIAL PRIMARY KEY,
    eval_id BIGINT NOT NULL REFERENCES evals(id) ON DELETE CASCADE,
    test_name TEXT NOT NULL,
    status TEXT NOT NULL,
    message TEXT
);
CREATE INDEX IF NOT EXISTS idx_results_eval ON test_results(eval_id);
CREATE INDEX IF NOT EXISTS idx_results_status ON test_results(status);

-- ── Real queue (replaces /root/queue/*.txt) ─────────────────────
CREATE TABLE IF NOT EXISTS work_queue (
    instance_id TEXT PRIMARY KEY,
    tier TEXT NOT NULL DEFAULT 'light',
    claimed_by TEXT,
    claimed_at TIMESTAMPTZ,
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'claimed', 'done', 'error')),
    priority INT NOT NULL DEFAULT 0,
    enqueued_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_queue_status_tier ON work_queue(status, tier, priority DESC, enqueued_at);

-- Atomic claim function: workers call this, get one tool or null
CREATE OR REPLACE FUNCTION claim_next(p_worker TEXT, p_tier TEXT DEFAULT 'any')
RETURNS TEXT AS $$
DECLARE
    v_inst TEXT;
BEGIN
    WITH claimed AS (
        SELECT instance_id FROM work_queue
        WHERE status = 'pending'
          AND (p_tier = 'any' OR tier = p_tier OR p_tier = 'heavy')  -- heavy falls back to light
        ORDER BY priority DESC, enqueued_at
        LIMIT 1
        FOR UPDATE SKIP LOCKED
    )
    UPDATE work_queue w
    SET status = 'claimed', claimed_by = p_worker, claimed_at = now()
    FROM claimed
    WHERE w.instance_id = claimed.instance_id
    RETURNING w.instance_id INTO v_inst;
    RETURN v_inst;
END $$ LANGUAGE plpgsql;

-- ── RAG: ingest embeddings ──────────────────────────────────────
CREATE TABLE IF NOT EXISTS rag_chunks (
    id BIGSERIAL PRIMARY KEY,
    corpus TEXT NOT NULL,  -- 'programbench' / 'swebench' / 'docs'
    source_path TEXT NOT NULL,
    chunk_idx INT NOT NULL,
    text TEXT NOT NULL,
    embedding vector(1024),
    meta JSONB,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_rag_corpus ON rag_chunks(corpus);
CREATE INDEX IF NOT EXISTS idx_rag_embedding ON rag_chunks USING hnsw (embedding vector_cosine_ops);

-- ── Per-tool failure analytics (replaces failure_analysis.json) ──
CREATE TABLE IF NOT EXISTS failure_buckets (
    eval_id BIGINT REFERENCES evals(id) ON DELETE CASCADE,
    bucket TEXT NOT NULL,
    count INT NOT NULL,
    sample_message TEXT,
    PRIMARY KEY (eval_id, bucket)
);

-- ── Per-tool memo / suggestion log (for human + agent annotations) ──
CREATE TABLE IF NOT EXISTS tool_memos (
    id BIGSERIAL PRIMARY KEY,
    instance_id TEXT REFERENCES tools(instance_id) ON DELETE CASCADE,
    author TEXT,
    kind TEXT,  -- 'suggestion', 'finding', 'todo', 'override'
    text TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ── Convenient views ────────────────────────────────────────────
CREATE OR REPLACE VIEW latest_scores AS
SELECT DISTINCT ON (instance_id)
    instance_id, ran_at, passed, total, pct, duration_s, rc
FROM evals
ORDER BY instance_id, ran_at DESC;

CREATE OR REPLACE VIEW dashboard_buckets AS
SELECT
    CASE
        WHEN pct >= 95 THEN '95-100'
        WHEN pct >= 70 THEN '70-94'
        WHEN pct >= 40 THEN '40-69'
        WHEN pct >= 10 THEN '10-39'
        ELSE '0-9'
    END AS bucket,
    COUNT(*) AS n
FROM latest_scores
WHERE pct IS NOT NULL
GROUP BY bucket
ORDER BY bucket;
