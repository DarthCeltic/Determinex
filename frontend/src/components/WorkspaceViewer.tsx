"use client";

import { useEffect, useState } from "react";
import { invokeSafe, isTauri } from "@/lib/api";

interface WorkspaceViewerProps {
  filename: string;
}

export function WorkspaceViewer({ filename }: WorkspaceViewerProps) {
  const [content, setContent] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    setIsLoading(true);
    setError(null);
    setContent(null);

    if (!isTauri()) {
      setContent("// WorkspaceViewer requires the Tauri runtime.");
      setIsLoading(false);
      return;
    }

    invokeSafe<string>("read_workspace_file", { relativePath: filename })
      .then((code) => {
        setContent(code);
        setIsLoading(false);
      })
      .catch((err: unknown) => {
        setError(String(err));
        setIsLoading(false);
      });
  }, [filename]);

  // Infer a display language from the file extension for the header label.
  const ext = filename.split(".").pop()?.toLowerCase() ?? "";
  const langLabel: Record<string, string> = {
    rs: "Rust",
    ts: "TypeScript",
    tsx: "TypeScript/JSX",
    js: "JavaScript",
    jsx: "JavaScript/JSX",
    py: "Python",
    go: "Go",
    json: "JSON",
    toml: "TOML",
    md: "Markdown",
    sh: "Shell",
  };
  const lang = langLabel[ext] ?? ext.toUpperCase();

  return (
    <div className="flex flex-col h-full w-full bg-[#0d1117] border border-green-500/20 rounded-xl overflow-hidden font-mono">
      {/* Header */}
      <div className="px-4 py-2 bg-[#161b22] border-b border-green-500/20 flex items-center justify-between shrink-0">
        <div className="flex items-center gap-2">
          <span className="w-2 h-2 rounded-full bg-green-500 inline-block" />
          <span className="text-[10px] font-black uppercase tracking-widest text-green-400">
            {filename}
          </span>
        </div>
        <div className="flex items-center gap-3">
          {lang && (
            <span className="text-[8px] font-mono text-green-500/40 uppercase tracking-widest">
              {lang}
            </span>
          )}
          <span className="text-[8px] text-gray-600 uppercase tracking-widest">
            GENERATED OUTPUT
          </span>
        </div>
      </div>

      {/* Body */}
      <div className="flex-1 overflow-auto relative">
        {isLoading && (
          <div className="absolute inset-0 flex items-center justify-center">
            <span className="text-[10px] font-mono text-green-500/40 animate-pulse tracking-widest uppercase">
              Reading file...
            </span>
          </div>
        )}

        {!isLoading && error && (
          <div className="p-5 flex flex-col gap-2">
            <p className="text-[9px] font-black uppercase tracking-widest text-red-400">
              Read Error
            </p>
            <p className="text-[10px] text-red-300/70 leading-relaxed">{error}</p>
          </div>
        )}

        {!isLoading && content !== null && !error && (
          <pre className="p-4 text-[11px] leading-relaxed text-green-300/90 overflow-auto whitespace-pre-wrap break-words">
            <code>{content}</code>
          </pre>
        )}
      </div>
    </div>
  );
}
