mod common;

use fastembed::{
    InitOptionsUserDefined, Pooling, TextEmbedding, TokenizerFiles, UserDefinedEmbeddingModel,
};
use rusqlite::{params, Connection};
use serde_json::json;
use std::{
    fs,
    path::{Path, PathBuf},
};

struct QueryCase {
    query: &'static str,
    expected_metadata_token: &'static str,
}

#[test]
fn companion_natural_language_queries_retrieve_expected_skill_chunks() {
    // Skip, do not panic: harness-supplied inputs. See tests/common/mod.rs.
    let Some(env_values) = common::required_env(
        "companion_natural_language_queries_retrieve_expected_skill_chunks",
        &[
            "DETERMINEX_COMPANION_QUERY_DB",
            "DETERMINEX_FASTEMBED_MODEL_DIR",
            "DETERMINEX_RAG_NL_QUERY_OUTPUT",
        ],
    ) else {
        return;
    };
    let db_path = PathBuf::from(&env_values[0]);
    let model_dir = PathBuf::from(&env_values[1]);
    let output_path = PathBuf::from(&env_values[2]);

    unsafe {
        rusqlite::ffi::sqlite3_auto_extension(Some(std::mem::transmute(
            sqlite_vec::sqlite3_vec_init as *const (),
        )));
    }

    let mut model = initialize_local_model(&model_dir).expect("initialize local fastembed model");
    let conn = Connection::open(&db_path).expect("open seeded companion DB");
    let companion_rows: i64 = conn
        .query_row("SELECT COUNT(*) FROM knowledge_companion", [], |row| {
            row.get(0)
        })
        .expect("count knowledge_companion rows");
    let vector_rows: i64 = conn
        .query_row("SELECT COUNT(*) FROM vss_companion", [], |row| row.get(0))
        .expect("count vss_companion rows");

    let cases = [
        QueryCase {
            query: "How does Project Cloak protect proprietary identifiers before cloud API calls?",
            expected_metadata_token: "cloak-safety",
        },
        QueryCase {
            query: "When should Flow AI planning guidance load for a multi-step user workflow?",
            expected_metadata_token: "flow-ai",
        },
        QueryCase {
            query: "How should mixture of agents and experts coordinate inside the system?",
            expected_metadata_token: "moa-moe",
        },
        QueryCase {
            query: "How should vibe coding constraints be handled without fake authority?",
            expected_metadata_token: "vibe-coding",
        },
        QueryCase {
            query: "How should Claude, Codex, Gemini, and the IDE share Determinex project memory without overwriting each other?",
            expected_metadata_token: "determinex-project-memory",
        },
    ];

    let mut case_results = Vec::new();
    for case in cases {
        let embeddings = model
            .embed(vec![case.query.to_string()], None)
            .expect("embed natural language query");
        assert_eq!(embeddings.len(), 1);
        assert_eq!(embeddings[0].len(), 384);
        let query_bytes = bytemuck::cast_slice::<f32, u8>(&embeddings[0]).to_vec();
        let mut stmt = conn
            .prepare(
                "SELECT r.id, r.content, r.metadata, v.distance
                 FROM vss_companion v
                 JOIN knowledge_companion r ON r.id = v.rowid
                 WHERE v.embedding_vector MATCH ?1 AND k = ?2
                 ORDER BY v.distance",
            )
            .expect("prepare vector query");
        let mapped = stmt
            .query_map(params![query_bytes, 5_i64], |row| {
                Ok(json!({
                    "id": row.get::<_, i64>(0)?,
                    "content_excerpt": row.get::<_, String>(1)?.chars().take(160).collect::<String>(),
                    "metadata": row.get::<_, String>(2)?,
                    "distance": row.get::<_, f64>(3)?,
                }))
            })
            .expect("execute vector query");
        let results: Vec<_> = mapped.filter_map(Result::ok).collect();
        let expected_rank = results
            .iter()
            .position(|row| {
                row["metadata"]
                    .as_str()
                    .unwrap_or_default()
                    .contains(case.expected_metadata_token)
            })
            .map(|rank| rank + 1);
        case_results.push(json!({
            "query": case.query,
            "expected_metadata_token": case.expected_metadata_token,
            "top_k": 5,
            "expected_rank": expected_rank,
            "passed": expected_rank.is_some(),
            "results": results,
        }));
    }

    let passed = companion_rows >= 53
        && vector_rows >= 53
        && case_results
            .iter()
            .all(|case| case["passed"].as_bool().unwrap_or(false));
    let payload = json!({
        "db_path": db_path.display().to_string(),
        "model_dir": resolve_model_dir(&model_dir).expect("resolve model dir").display().to_string(),
        "query_mode": "natural_language_fastembed_sqlite_vec_top_k",
        "knowledge_companion_rows": companion_rows,
        "vss_companion_rows": vector_rows,
        "query_count": case_results.len(),
        "passed_query_count": case_results.iter().filter(|case| case["passed"].as_bool().unwrap_or(false)).count(),
        "all_expected_companions_retrieved_top_k": passed,
        "cases": case_results,
        "does_not_prove_answer_quality": true,
        "does_not_prove_full_rag_correctness": true,
    });

    fs::write(
        output_path,
        serde_json::to_string_pretty(&payload).expect("serialize natural language query result"),
    )
    .expect("write natural language query output");

    assert!(passed);
}

fn initialize_local_model(model_dir: &Path) -> Result<TextEmbedding, String> {
    let resolved = resolve_model_dir(model_dir)?;
    let tokenizer_files = TokenizerFiles {
        tokenizer_file: fs::read(resolved.join("tokenizer.json")).map_err(|e| e.to_string())?,
        config_file: fs::read(resolved.join("config.json")).map_err(|e| e.to_string())?,
        special_tokens_map_file: fs::read(resolved.join("special_tokens_map.json"))
            .map_err(|e| e.to_string())?,
        tokenizer_config_file: fs::read(resolved.join("tokenizer_config.json"))
            .map_err(|e| e.to_string())?,
    };
    let user_defined_model = UserDefinedEmbeddingModel::new(
        fs::read(resolved.join("model.onnx")).map_err(|e| e.to_string())?,
        tokenizer_files,
    )
    .with_pooling(Pooling::Mean);
    TextEmbedding::try_new_from_user_defined(user_defined_model, InitOptionsUserDefined::default())
        .map_err(|e| e.to_string())
}

fn resolve_model_dir(model_dir: &Path) -> Result<PathBuf, String> {
    if model_dir.join("model.onnx").is_file() {
        return Ok(model_dir.to_path_buf());
    }
    let onnx = model_dir.join("onnx");
    if onnx.join("model.onnx").is_file() {
        return Ok(onnx);
    }
    Err(format!(
        "model.onnx not found under {}",
        model_dir.display()
    ))
}
