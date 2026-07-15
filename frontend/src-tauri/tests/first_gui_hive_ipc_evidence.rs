use std::fs;
use std::path::PathBuf;

fn repo_src(path: &str) -> PathBuf {
    PathBuf::from(env!("CARGO_MANIFEST_DIR")).join(path)
}

#[test]
fn first_gui_hive_ipc_evidence_command_is_registered() {
    let lib = fs::read_to_string(repo_src("src/lib.rs")).expect("read lib.rs");
    assert!(lib.contains("mod first_gui_hive_ipc;"));
    assert!(lib.contains("first_gui_hive_ipc::record_first_gui_hive_ipc_evidence"));
}

#[test]
fn first_gui_hive_ipc_evidence_writer_uses_required_files_and_boundary() {
    let src =
        fs::read_to_string(repo_src("src/first_gui_hive_ipc.rs")).expect("read evidence writer");

    assert!(src.contains("assurance"));
    assert!(src.contains("first_gui_hive_ipc"));
    assert!(src.contains("request.json"));
    assert!(src.contains("result.json"));
    assert!(src.contains("transcript.md"));
    assert!(src.contains("claim_boundary.md"));
    assert!(src.contains(
        "This proves one bounded GUI-to-Hive workflow. It does not prove universal IDE support, all-language support, clean-host support, or release readiness."
    ));
}
