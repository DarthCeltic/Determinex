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
