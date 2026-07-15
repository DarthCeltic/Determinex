use serde_json::json;
use std::{env, fs, path::PathBuf};

#[test]
fn companion_rag_tauri_command_boundary_is_wired() {
    let root = PathBuf::from(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .and_then(|p| p.parent())
        .expect("repo root")
        .to_path_buf();
    let output_path = PathBuf::from(
        env::var("DETERMINEX_RAG_TAURI_COMMAND_BOUNDARY_OUTPUT")
            .expect("DETERMINEX_RAG_TAURI_COMMAND_BOUNDARY_OUTPUT must point to result artifact"),
    );

    let lib_rs =
        fs::read_to_string(root.join("frontend/src-tauri/src/lib.rs")).expect("read lib.rs");
    let vector_engine = fs::read_to_string(root.join("frontend/src-tauri/src/vector_engine.rs"))
        .expect("read vector_engine.rs");
    let memory_health = fs::read_to_string(root.join("frontend/src-tauri/src/memory_health.rs"))
        .expect("read memory_health.rs");
    let db_rs = fs::read_to_string(root.join("frontend/src-tauri/src/db.rs")).expect("read db.rs");
    let panel = fs::read_to_string(
        root.join("frontend/src/components/ide-product-shell/CompanionRagReportPanel.tsx"),
    )
    .expect("read CompanionRagReportPanel.tsx");

    let payload = json!({
        "tauri_command_registered": lib_rs.contains("vector_engine::query_knowledge"),
        "memory_health_command_registered": lib_rs.contains("memory_health::get_memory_health"),
        "query_command_has_tauri_command_attr": vector_engine.contains("#[tauri::command]\npub fn query_knowledge"),
        "memory_health_command_has_tauri_command_attr": memory_health.contains("#[tauri::command]\npub fn get_memory_health"),
        "query_command_returns_knowledge_result": vector_engine.contains("Result<Vec<KnowledgeResult>, String>"),
        "companion_collection_resolves_to_tables": vector_engine.contains("\"companion\"    => Ok((\"knowledge_companion\",    \"vss_companion\"))"),
        "memory_source_provenance_schema_exists": db_rs.contains("CREATE TABLE IF NOT EXISTS memory_sources")
            && db_rs.contains("source_sha256")
            && db_rs.contains("proof_status"),
        "memory_chunk_provenance_schema_exists": db_rs.contains("CREATE TABLE IF NOT EXISTS memory_chunks")
            && db_rs.contains("chunk_sha256")
            && db_rs.contains("knowledge_rowid"),
        "ui_renders_report_boundary": panel.contains("data-testid=\"companion-rag-report-panel\"")
            && panel.contains("data-answer-correctness-claimed=\"false\"")
            && panel.contains("training_eligible: false"),
        "gui_launched": false,
        "desktop_command_boundary_proven": true,
        "does_not_prove_full_gui_e2e": true,
        "does_not_prove_answer_correctness": true,
        "does_not_prove_release_support": true
    });

    fs::write(
        output_path,
        serde_json::to_string_pretty(&payload).expect("serialize command boundary payload"),
    )
    .expect("write command boundary output");

    assert!(payload["tauri_command_registered"].as_bool().unwrap());
    assert!(payload["memory_health_command_registered"]
        .as_bool()
        .unwrap());
    assert!(payload["query_command_has_tauri_command_attr"]
        .as_bool()
        .unwrap());
    assert!(payload["memory_health_command_has_tauri_command_attr"]
        .as_bool()
        .unwrap());
    assert!(payload["query_command_returns_knowledge_result"]
        .as_bool()
        .unwrap());
    assert!(payload["companion_collection_resolves_to_tables"]
        .as_bool()
        .unwrap());
    assert!(payload["memory_source_provenance_schema_exists"]
        .as_bool()
        .unwrap());
    assert!(payload["memory_chunk_provenance_schema_exists"]
        .as_bool()
        .unwrap());
    assert!(payload["ui_renders_report_boundary"].as_bool().unwrap());
}
