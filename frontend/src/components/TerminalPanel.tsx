"use client";
import { useEffect, useRef, useState } from "react";
import { listen } from "@tauri-apps/api/event";
import { isTauri, invokeSafe } from "@/lib/api";
import "@xterm/xterm/css/xterm.css";

type Props = {
  workspacePath?: string;
};

// Fixed id (not per-mount random) -- this is what makes the terminal
// persistent across the panel being closed/reopened: the underlying shell
// process on the Rust side is keyed by this id and survives even though the
// React component and its xterm instance get disposed and recreated. On
// remount, pty_spawn detects the session is already alive and returns the
// buffered scrollback instead of starting a new shell.
const TERMINAL_ID = "primary";

function displayPath(path: string): string {
  return path;
}

export function TerminalPanel({ workspacePath = "C:\\Dev\\Determinex" }: Props) {
  const terminalRef = useRef<HTMLDivElement>(null);
  const termInstance = useRef<any>(null);
  const fitAddonRef = useRef<any>(null);
  const sendCommandRef = useRef<(command: string) => void>(() => {});
  const tauriMode = isTauri();
  const [exited, setExited] = useState(false);

  useEffect(() => {
    if (!terminalRef.current) return;
    if (!tauriMode) return; // browser mode: nothing to attach to, static message renders instead

    let isMounted = true;
    let resizeObserver: ResizeObserver | null = null;
    let unlistenOutput: (() => void) | null = null;
    let unlistenExit: (() => void) | null = null;

    Promise.all([
      import("@xterm/xterm").then((m) => m.Terminal),
      import("@xterm/addon-fit").then((m) => m.FitAddon),
    ]).then(async ([Terminal, FitAddon]) => {
      if (!isMounted || !terminalRef.current) return;

      const term = new Terminal({
        cursorBlink: true,
        convertEol: true,
        fontFamily: '"JetBrains Mono", "Cascadia Mono", Consolas, monospace',
        fontSize: 12,
        lineHeight: 1.18,
        scrollback: 8000,
        theme: {
          background: "#010409",
          foreground: "#e6edf3",
          cursor: "#00ffcc",
          selectionBackground: "#12343b",
        },
      });
      termInstance.current = term;

      const fitAddon = new FitAddon();
      fitAddonRef.current = fitAddon;
      term.loadAddon(fitAddon);
      term.open(terminalRef.current);
      requestAnimationFrame(() => fitAddon.fit());

      setExited(false);

      // Spawn (or reconnect to) the persistent shell. Returns buffered
      // scrollback if a session for TERMINAL_ID is already running.
      const scrollback = await invokeSafe<string>("pty_spawn", {
        id: TERMINAL_ID,
        cwd: workspacePath,
        rows: term.rows,
        cols: term.cols,
      });
      if (!isMounted) return;
      if (scrollback) {
        term.write(scrollback);
      }

      unlistenOutput = await listen<{ id: string; chunk: string }>("pty-output", (event) => {
        if (event.payload.id === TERMINAL_ID) {
          term.write(event.payload.chunk);
        }
      });
      unlistenExit = await listen<{ id: string; code: number | null }>("pty-exit", (event) => {
        if (event.payload.id === TERMINAL_ID) {
          setExited(true);
        }
      });

      sendCommandRef.current = (command: string) => {
        void invokeSafe("pty_write", { id: TERMINAL_ID, data: `${command}\r` });
      };

      term.onData((data) => {
        void invokeSafe("pty_write", { id: TERMINAL_ID, data });
      });

      const doResize = () => {
        fitAddon.fit();
        void invokeSafe("pty_resize", { id: TERMINAL_ID, rows: term.rows, cols: term.cols });
      };
      resizeObserver = new ResizeObserver(() => requestAnimationFrame(doResize));
      resizeObserver.observe(terminalRef.current);
    });

    return () => {
      isMounted = false;
      resizeObserver?.disconnect();
      unlistenOutput?.();
      unlistenExit?.();
      sendCommandRef.current = () => {};
      // Deliberately does NOT call pty_kill -- the whole point of this
      // component is that the shell survives being unmounted. Use the
      // "Kill Terminal" button to actually end the session.
      if (termInstance.current) {
        termInstance.current.dispose();
        termInstance.current = null;
      }
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [tauriMode]);

  const killTerminal = () => {
    void invokeSafe("pty_kill", { id: TERMINAL_ID });
    setExited(true);
  };

  const restartTerminal = async () => {
    await invokeSafe("pty_kill", { id: TERMINAL_ID });
    setExited(false);
    const term = termInstance.current;
    if (term) {
      term.clear();
      const scrollback = await invokeSafe<string>("pty_spawn", {
        id: TERMINAL_ID,
        cwd: workspacePath,
        rows: term.rows,
        cols: term.cols,
      });
      if (scrollback) term.write(scrollback);
    }
  };

  const quickCommands = ["git status", "npm run build", "ls"];

  return (
    <div
      className="flex h-full min-h-0 flex-col overflow-hidden"
      style={{ background: "#010409", fontFamily: '"JetBrains Mono", monospace' }}
    >
      <div className="flex shrink-0 flex-wrap items-center gap-2 border-b border-white/8 bg-black/60 px-4 py-2">
        <span className="text-[10px] font-mono text-gray-500">
          terminal — {displayPath(workspacePath).split(/[\\/]/).pop() || "workspace"}
        </span>
        <div className="ml-auto flex min-w-0 flex-wrap items-center justify-end gap-1.5">
          {tauriMode &&
            quickCommands.map((command) => (
              <button
                key={command}
                type="button"
                onClick={() => sendCommandRef.current(command)}
                className="rounded-md border border-white/8 bg-white/[0.03] px-2 py-1 text-[8px] font-bold text-gray-500 transition hover:border-emerald-400/30 hover:text-emerald-300"
              >
                {command}
              </button>
            ))}
          {tauriMode && (
            <button
              type="button"
              onClick={exited ? restartTerminal : killTerminal}
              title={exited ? "Restart shell" : "Kill shell"}
              className="rounded-md border border-white/8 bg-white/[0.03] px-2 py-1 text-[8px] font-bold text-gray-500 transition hover:border-red-400/30 hover:text-red-300"
            >
              {exited ? "Restart" : "Kill"}
            </button>
          )}
          {!tauriMode && (
            <span className="rounded border border-amber-400/20 bg-amber-500/10 px-2 py-1 text-[8px] font-mono text-amber-300">
              BROWSER VIEW
            </span>
          )}
        </div>
      </div>

      {!tauriMode ? (
        <div className="flex flex-1 flex-col items-center justify-center gap-2 p-6 text-center text-xs text-gray-500">
          <p>A real, interactive terminal (real PTY, streaming, persistent shell state) requires the desktop runtime.</p>
          <p className="text-gray-600">Open Determinex as the desktop app to use the terminal.</p>
        </div>
      ) : (
        <div className="relative min-h-0 flex-1 overflow-hidden p-2">
          <div ref={terminalRef} className="absolute inset-0 pl-2 pt-2" />
          {exited && (
            <div className="absolute inset-x-0 bottom-2 flex justify-center">
              <span className="rounded border border-amber-400/30 bg-black/80 px-3 py-1 text-[10px] font-mono text-amber-300">
                Shell exited. Click "Restart" to start a new one.
              </span>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
