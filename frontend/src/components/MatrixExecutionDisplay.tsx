"use client";

import React, { useEffect, useRef, useState } from "react";
import { XOctagon, Cpu, Code2, Eye, CheckCircle2, AlertTriangle } from "lucide-react";
import { VanguardToggle } from "@/components/VanguardToggle";

// ─── Agent definitions — maps to the 3 sequential MoA stages ─────────────────
const AGENTS = [
  {
    id: "sentinel",
    label: "SENTINEL",
    model: "determinex-sentinel-v3",
    role: "Architect & Planner",
    color: "#00e5ff", // cyan
    glow: "rgba(0,229,255,0.6)",
    icon: Cpu,
  },
  {
    id: "engineer",
    label: "ENGINEER",
    model: "determinex-engineer-v10-dsl",
    role: "Code Synthesis",
    color: "#a78bfa", // violet
    glow: "rgba(167,139,250,0.6)",
    icon: Code2,
  },
  {
    id: "observer",
    label: "OBSERVER",
    model: "determinex-observer-v5-dsl",
    role: "Audit & Verdict",
    color: "#f97316", // amber-orange
    glow: "rgba(249,115,22,0.6)",
    icon: Eye,
  },
] as const;

type AgentId = (typeof AGENTS)[number]["id"];

export interface AgentStatus {
  /** Which agent currently holds the VRAM tollbooth. null = idle. */
  currentAgent: AgentId | null;
  /** Whether the full pipeline is running */
  isExecuting: boolean;
  /** CLEAN | HALLUCINATION | PARTIAL — populated after Observer completes */
  verdict: string | null;
  /** Observer confidence 0–1 */
  confidence: number | null;
  /** True if accepted (CLEAN + confidence >= 0.75) */
  accepted: boolean | null;
  /** Structured error if the pipeline hard-aborted */
  error: { stage: string; message: string } | null;
}

interface MatrixExecutionDisplayProps {
  agentStatus: AgentStatus;
  logs: string[];
  onAbort: () => void;
  retryCount?: number;
}

export function MatrixExecutionDisplay({
  agentStatus,
  logs,
  onAbort,
  retryCount = 0,
}: MatrixExecutionDisplayProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const terminalRef = useRef<HTMLDivElement>(null);
  const prevLogsLengthRef = useRef(0);
  const [displayLog, setDisplayLog] = useState("Initializing MoA sequential pipeline...");
  const [timestampedLogs, setTimestampedLogs] = useState<{ time: string; text: string }[]>([]);

  // ── Matrix rain animation ──────────────────────────────────────────────────
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    let width = (canvas.width = canvas.parentElement?.clientWidth || window.innerWidth);
    let height = (canvas.height = canvas.parentElement?.clientHeight || window.innerHeight);

    const ro = new ResizeObserver(() => {
      if (canvas.parentElement) {
        width = canvas.width = canvas.parentElement.clientWidth;
        height = canvas.height = canvas.parentElement.clientHeight;
      }
    });
    if (canvas.parentElement) ro.observe(canvas.parentElement);

    const chars =
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$+-*/=%\"'#&_(),.;:?!\\|{}<>[]^~アァカサタナハマヤャラワガザダバパイィキシチニヒミリヰギジヂビピウゥクスツヌフムユュルグズブヅプエェケセテネヘメレゲゼデベペオォコソトノホモヨョロゴゾドボポヴッン";
    const charArr = chars.split("");
    const columns = Math.floor(width / 14);
    const drops = Array(columns).fill(1);

    let rafId: number;
    const draw = () => {
      ctx.fillStyle = "rgba(0,0,0,0.05)";
      ctx.fillRect(0, 0, width, height);
      ctx.font = "14px monospace";
      for (let i = 0; i < drops.length; i++) {
        ctx.fillStyle = Math.random() > 0.98 ? "#0ff" : "#0F0";
        ctx.fillText(charArr[Math.floor(Math.random() * charArr.length)], i * 14, drops[i] * 14);
        if (drops[i] * 14 > height && Math.random() > 0.975) drops[i] = 0;
        drops[i]++;
      }
      rafId = requestAnimationFrame(draw);
    };

    draw();
    return () => {
      cancelAnimationFrame(rafId);
      ro.disconnect();
    };
  }, []);

  // ── Log display — surface latest meaningful entry ─────────────────────────
  useEffect(() => {
    if (logs.length > 0) {
      const latest = logs[logs.length - 1];
      const clean = latest
        .replace(/\x1b\[[0-9;]*m/g, "")
        .replace("[SYSTEM]", "")
        .trim();
      if (clean.length > 5) setDisplayLog(clean.substring(0, 72) + (clean.length > 72 ? "…" : ""));
    }
  }, [logs]);

  // ── Timestamped terminal — append new entries as they arrive ──────────────
  useEffect(() => {
    if (logs.length <= prevLogsLengthRef.current) return;
    const newEntries = logs.slice(prevLogsLengthRef.current).map((text) => ({
      time: new Date().toLocaleTimeString("en-US", {
        hour12: false,
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
      }),
      text,
    }));
    setTimestampedLogs((prev) => [...prev, ...newEntries]);
    prevLogsLengthRef.current = logs.length;
  }, [logs]);

  // ── Auto-scroll terminal to bottom on new entries ─────────────────────────
  useEffect(() => {
    if (terminalRef.current) {
      terminalRef.current.scrollTop = terminalRef.current.scrollHeight;
    }
  }, [timestampedLogs]);

  const activeAgent = AGENTS.find((a) => a.id === agentStatus.currentAgent) ?? null;
  const AgentIcon = activeAgent?.icon ?? Cpu;

  return (
    <div className="absolute inset-0 z-50 w-full h-full flex items-center justify-center bg-black overflow-hidden pointer-events-none">
      <canvas ref={canvasRef} className="absolute inset-0 z-0 opacity-60" />
      <div className="absolute inset-0 z-10 bg-[radial-gradient(ellipse_at_center,_rgba(0,0,0,0.55)_0%,_rgba(0,0,0,0.95)_100%)]" />

      <div className="relative z-20 flex flex-col items-center gap-5 pointer-events-auto w-full max-w-lg px-4">
        {/* ── VRAM Tollbooth Banner ─────────────────────────────────────────── */}
        <div
          className="w-full border rounded-2xl p-5 backdrop-blur-md flex flex-col items-center gap-4"
          style={{
            borderColor: activeAgent ? activeAgent.color + "55" : "#22c55e55",
            boxShadow: `0 0 40px ${activeAgent?.glow ?? "rgba(0,255,0,0.2)"}`,
            background: "rgba(0,0,0,0.6)",
          }}
        >
          {/* Agent icon + label */}
          <div className="flex items-center gap-3">
            <AgentIcon
              className="animate-pulse"
              size={28}
              style={{
                color: activeAgent?.color ?? "#00e5ff",
                filter: `drop-shadow(0 0 8px ${activeAgent?.glow ?? "#00e5ff"})`,
              }}
            />
            <div className="text-center">
              <p className="text-eyebrow tracking-[0.4em] uppercase font-mono text-gray-500">
                VRAM TOLLBOOTH — ACTIVE NODE
              </p>
              <h2
                className="font-black tracking-[0.25em] font-mono uppercase text-sm"
                style={{
                  color: activeAgent?.color ?? "#00e5ff",
                  textShadow: `0 0 12px ${activeAgent?.glow ?? "#00e5ff"}`,
                }}
              >
                {activeAgent ? activeAgent.label : "INITIALIZING"}
              </h2>
              {activeAgent && (
                <p className="text-meta font-mono text-gray-400 mt-0.5">
                  {activeAgent.model} · {activeAgent.role}
                </p>
              )}
            </div>
          </div>

          {/* Live log line */}
          <p className="text-label font-mono text-center text-green-400/80 leading-relaxed min-h-[2.5rem]">
            {displayLog}
          </p>
        </div>

        {/* ── Sequential Pipeline Progress ─────────────────────────────────── */}
        <div className="w-full flex items-center justify-between px-2 relative">
          {AGENTS.map((agent, idx) => {
            const Icon = agent.icon;
            const isActive = agentStatus.currentAgent === agent.id;
            const agentIdx = AGENTS.findIndex((a) => a.id === agentStatus.currentAgent);
            const isDone = agentIdx > idx || (agentStatus.verdict !== null && agentIdx === -1);
            const isPending = !isActive && !isDone;

            return (
              <React.Fragment key={agent.id}>
                <div className="flex flex-col items-center gap-1.5">
                  <div
                    className="w-10 h-10 rounded-full border-2 flex items-center justify-center transition-all duration-500"
                    style={{
                      borderColor: isActive ? agent.color : isDone ? "#22c55e" : "#374151",
                      background: isActive
                        ? `${agent.color}15`
                        : isDone
                          ? "rgba(34,197,94,0.1)"
                          : "transparent",
                      boxShadow: isActive ? `0 0 16px ${agent.glow}` : "none",
                    }}
                  >
                    {isDone ? (
                      <CheckCircle2 size={16} className="text-green-400" />
                    ) : (
                      <Icon
                        size={16}
                        style={{ color: isActive ? agent.color : "#4b5563" }}
                        className={isActive ? "animate-pulse" : ""}
                      />
                    )}
                  </div>
                  <span
                    className="text-eyebrow font-black tracking-widest uppercase font-mono"
                    style={{ color: isActive ? agent.color : isDone ? "#22c55e" : "#4b5563" }}
                  >
                    {agent.label}
                  </span>
                  <span className="text-meta text-gray-600 font-mono">
                    {isPending ? "STANDBY" : isDone ? "DONE" : "ACTIVE"}
                  </span>
                </div>
                {idx < AGENTS.length - 1 && (
                  <div
                    className="flex-1 h-[2px] mx-1 transition-all duration-700"
                    style={{
                      background: isDone ? "#22c55e" : "#1f2937",
                      boxShadow: isDone ? "0 0 6px rgba(34,197,94,0.5)" : "none",
                    }}
                  />
                )}
              </React.Fragment>
            );
          })}
          {retryCount > 0 && (
            <div
              className="absolute -top-3 right-0 flex items-center gap-1 px-2 py-0.5 rounded-full border border-amber-500/50 bg-amber-950/60 font-mono"
              title="Observer rejection loop count"
            >
              <span className="w-1.5 h-1.5 rounded-full bg-amber-400 animate-pulse inline-block" />
              <span className="text-meta font-black text-amber-400 tracking-wider">
                RETRY ×{retryCount}
              </span>
            </div>
          )}
        </div>

        {/* ── Verdict badge — appears after Observer completes ──────────────── */}
        {agentStatus.verdict && (
          <div
            className="w-full flex items-center justify-between px-4 py-3 rounded-xl border font-mono"
            style={{
              borderColor: agentStatus.accepted ? "#22c55e55" : "#ef444455",
              background: agentStatus.accepted ? "rgba(34,197,94,0.08)" : "rgba(239,68,68,0.08)",
            }}
          >
            <div className="flex items-center gap-2">
              {agentStatus.accepted ? (
                <CheckCircle2 size={14} className="text-green-400" />
              ) : (
                <AlertTriangle size={14} className="text-red-400" />
              )}
              <span
                className="text-meta font-black tracking-widest uppercase"
                style={{ color: agentStatus.accepted ? "#22c55e" : "#ef4444" }}
              >
                {agentStatus.verdict}
              </span>
            </div>
            {agentStatus.confidence !== null && (
              <span className="text-meta text-gray-400">
                confidence: {(agentStatus.confidence * 100).toFixed(0)}%
              </span>
            )}
          </div>
        )}

        {/* ── Error badge ────────────────────────────────────────────────────── */}
        {agentStatus.error && (
          <div className="w-full flex items-start gap-2 px-4 py-3 rounded-xl border border-red-500/30 bg-red-950/20 font-mono">
            <AlertTriangle size={14} className="text-red-400 mt-0.5 shrink-0" />
            <div>
              <p className="text-eyebrow text-red-400 font-black tracking-widest uppercase mb-0.5">
                [{agentStatus.error.stage}] PIPELINE ABORTED
              </p>
              <p className="text-meta text-red-300/70 leading-relaxed">
                {agentStatus.error.message}
              </p>
            </div>
          </div>
        )}

        {/* ── Abort control ─────────────────────────────────────────────────── */}
        <button
          onClick={onAbort}
          className="flex items-center gap-2 px-6 py-3 bg-red-950/80 text-red-500 border border-red-500/50 rounded-lg hover:bg-red-900 transition-colors uppercase text-xs tracking-widest font-bold font-mono shadow-[0_0_15px_rgba(255,0,0,0.3)]"
        >
          <XOctagon size={16} /> Halt Orchestration
        </button>

        {/* ── Vanguard Telemetry Opt-In ──────────────────────────────────────── */}
        {/* Surfaced during execution so users can consent in context. Default OFF.
            The toggle persists for the lifetime of the Tauri process — a page
            re-render does not reset it because state lives in the Rust backend. */}
        <VanguardToggle className="w-full" />

        {/* ── Scrolling terminal ────────────────────────────────────────────── */}

        <div className="w-full rounded-xl border border-green-500/20 bg-black/70 backdrop-blur-sm overflow-hidden">
          <div className="px-3 py-1.5 border-b border-green-500/20 flex items-center gap-2">
            <div className="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse" />
            <span className="text-eyebrow font-black tracking-[0.4em] uppercase text-green-500/70 font-mono">
              PIPELINE TELEMETRY
            </span>
          </div>
          <div
            ref={terminalRef}
            className="h-32 overflow-y-auto px-3 py-2 flex flex-col gap-0.5 font-mono text-meta leading-relaxed"
            style={{ scrollbarWidth: "none" }}
          >
            {timestampedLogs.length === 0 ? (
              <span className="text-green-500/30 italic">Awaiting signal...</span>
            ) : (
              timestampedLogs.map((entry, i) => (
                <div key={i} className="flex gap-2">
                  <span className="text-green-500/40 shrink-0 select-none">{entry.time}</span>
                  <span className="text-green-400/80">{entry.text}</span>
                </div>
              ))
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
