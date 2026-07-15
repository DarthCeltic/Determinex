/// windows_process.rs — suppress the console-window flash for spawned subprocesses
///
/// Windows allocates a visible console window for any spawned console-subsystem
/// process (git, rustc, ollama, where.exe, ...) unless the parent explicitly says
/// not to. Determinex's UI is a windowless GUI app, so every subprocess spawn
/// without this flag briefly flashes a black command-prompt box on screen.
///
/// Apply via `no_window(&mut Command::new(...))` or, when chaining args first,
/// `no_window(Command::new(...).arg(...))` (the chain already yields `&mut Command`).
/// No-op on non-Windows platforms.
const CREATE_NO_WINDOW: u32 = 0x0800_0000;

#[cfg(target_os = "windows")]
pub fn no_window(cmd: &mut std::process::Command) -> &mut std::process::Command {
    use std::os::windows::process::CommandExt;
    cmd.creation_flags(CREATE_NO_WINDOW)
}
#[cfg(not(target_os = "windows"))]
pub fn no_window(cmd: &mut std::process::Command) -> &mut std::process::Command {
    cmd
}

#[cfg(target_os = "windows")]
pub fn no_window_tokio(cmd: &mut tokio::process::Command) -> &mut tokio::process::Command {
    cmd.creation_flags(CREATE_NO_WINDOW)
}
#[cfg(not(target_os = "windows"))]
pub fn no_window_tokio(cmd: &mut tokio::process::Command) -> &mut tokio::process::Command {
    cmd
}
