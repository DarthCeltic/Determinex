use rusqlite::{params, Connection};
use serde_json::json;
use std::{env, fs, path::PathBuf};

#[test]
fn companion_seeded_db_supports_local_vector_query() {
    let db_path = PathBuf::from(
        env::var("DETERMINEX_COMPANION_QUERY_DB")
            .expect("DETERMINEX_COMPANION_QUERY_DB must point to a seeded companion DB copy"),
    );
    let output_path = PathBuf::from(
        env::var("DETERMINEX_RAG_QUERY_SMOKE_OUTPUT")
            .expect("DETERMINEX_RAG_QUERY_SMOKE_OUTPUT must point to the result artifact"),
    );

    unsafe {
        rusqlite::ffi::sqlite3_auto_extension(Some(std::mem::transmute(
            sqlite_vec::sqlite3_vec_init as *const (),
        )));
    }

    let conn = Connection::open(&db_path).expect("open seeded companion DB");
    let companion_rows: i64 = conn
        .query_row("SELECT COUNT(*) FROM knowledge_companion", [], |row| {
            row.get(0)
        })
        .expect("count knowledge_companion rows");
    let vector_rows: i64 = conn
        .query_row("SELECT COUNT(*) FROM vss_companion", [], |row| row.get(0))
        .expect("count vss_companion rows");

    let query_vector: Vec<u8> = conn
        .query_row(
            "SELECT embedding_vector FROM vss_companion WHERE rowid = 1",
            [],
            |row| row.get(0),
        )
        .expect("read stored companion vector");

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
        .query_map(params![query_vector, 5_i64], |row| {
            Ok(json!({
                "id": row.get::<_, i64>(0)?,
                "content_excerpt": row.get::<_, String>(1)?.chars().take(160).collect::<String>(),
                "metadata": row.get::<_, String>(2)?,
                "distance": row.get::<_, f64>(3)?,
            }))
        })
        .expect("execute vector query");
    let results: Vec<_> = mapped.filter_map(Result::ok).collect();

    let first = results.first().expect("at least one vector result");
    let first_distance = first["distance"]
        .as_f64()
        .expect("first distance is numeric");
    let first_metadata = first["metadata"].as_str().unwrap_or_default();

    let payload = json!({
        "db_path": db_path.display().to_string(),
        "knowledge_companion_rows": companion_rows,
        "vss_companion_rows": vector_rows,
        "query_mode": "stored_vector_nearest_neighbor",
        "query_vector_source_rowid": 1,
        "result_count": results.len(),
        "first_result_metadata": first_metadata,
        "first_result_distance": first_distance,
        "results": results,
        "proves_vector_index_queryable": companion_rows >= 53
            && vector_rows >= 53
            && first_distance <= 0.0001
            && first_metadata.contains("cloak-safety"),
        "does_not_prove_natural_language_answer_quality": true,
        "does_not_prove_full_rag_correctness": true,
    });

    fs::write(
        output_path,
        serde_json::to_string_pretty(&payload).expect("serialize query result"),
    )
    .expect("write RAG query smoke output");

    assert!(companion_rows >= 53);
    assert!(vector_rows >= 53);
    assert!(first_distance <= 0.0001);
    assert!(first_metadata.contains("cloak-safety"));
}
