"use client";

import {
  Play,
  Square,
  Terminal,
  CheckCircle2,
  CircleDashed,
  AlertCircle,
  Zap,
  Activity,
  MessageSquare,
  Bot,
  User,
  Check,
  Info
} from "lucide-react";
import { useState } from "react";

interface ProjectArchitectProps {
  selectedProjectName?: string;
}

export function ProjectArchitect({ selectedProjectName }: ProjectArchitectProps) {
  const [tasks, setTasks] = useState([
    { id: 1, title: "Refactor Proof Center", status: "done" },
    { id: 2, title: "Refactor Space Overlay", status: "done" },
    { id: 3, title: "Build Kanban Cockpit", status: "in-progress" },
    { id: 4, title: "Update Telemetry Brain", status: "pending" },
    { id: 5, title: "Capability Manager Grid", status: "pending" },
  ]);

  const stream = [
    { type: "system", msg: "Session initialized for Determinex overhaul", time: "10:24 AM" },
    { type: "agent", msg: "I've completed the SpaceOverlay refactor. Moving on to the Work Cockpit.", time: "10:28 AM" },
    { type: "action", msg: "Agent is writing c:/Dev/Determinex/frontend/src/components/ProjectArchitect.tsx", time: "10:29 AM" },
  ];

  return (
    <div className="flex h-full w-full flex-col md:flex-row gap-4 p-4 bg-black/40">
      {/* Left Column: Kanban Tasks */}
      <div className="w-full md:w-80 flex flex-col gap-4">
        <div className="flex items-center justify-between rounded-xl border border-white/10 bg-black/40 p-4">
          <div className="flex items-center gap-2">
            <Activity size={16} className="text-emerald-400" />
            <h3 className="text-[12px] font-bold text-white tracking-wide uppercase">Active Plan</h3>
          </div>
          <span className="text-[10px] font-mono text-gray-500">5 items</span>
        </div>

        <div className="flex-1 overflow-y-auto no-scrollbar flex flex-col gap-2">
          {tasks.map(t => (
            <div key={t.id} className={`p-3 rounded-xl border ${
              t.status === 'done' ? 'border-emerald-500/20 bg-emerald-950/10' :
              t.status === 'in-progress' ? 'border-[var(--determinex-accent)]/30 bg-[var(--determinex-accent)]/10' :
              'border-white/5 bg-white/5'
            }`}>
              <div className="flex items-center gap-3">
                {t.status === 'done' ? <CheckCircle2 size={14} className="text-emerald-400" /> :
                 t.status === 'in-progress' ? <CircleDashed size={14} className="text-[var(--determinex-accent)] animate-spin-slow" /> :
                 <CircleDashed size={14} className="text-gray-600" />}
                <span className={`text-[11px] font-bold ${
                  t.status === 'done' ? 'text-emerald-400 line-through opacity-70' :
                  t.status === 'in-progress' ? 'text-white' : 'text-gray-400'
                }`}>{t.title}</span>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Main Column: Agent Stream */}
      <div className="flex-1 flex flex-col gap-4 overflow-hidden rounded-2xl border border-white/10 bg-black/20">
        <div className="p-4 border-b border-white/10 bg-black/40 flex justify-between items-center shrink-0">
          <div className="flex items-center gap-2">
            <Zap size={14} className="text-[var(--determinex-accent)]" />
            <h2 className="text-[12px] font-bold text-white uppercase tracking-wider">Agent Stream</h2>
          </div>
          <div className="flex items-center gap-2">
            <button className="flex items-center gap-1.5 px-3 py-1.5 rounded bg-rose-500/20 text-rose-400 border border-rose-500/30 text-[10px] font-bold uppercase tracking-widest hover:bg-rose-500 hover:text-white transition-colors">
              <Square size={10} fill="currentColor" /> Stop
            </button>
          </div>
        </div>

        <div className="flex-1 overflow-y-auto p-6 flex flex-col gap-6">
          {stream.map((s, i) => (
            <div key={i} className={`flex gap-4 ${s.type === 'action' ? 'opacity-70' : ''}`}>
              <div className="w-8 shrink-0 flex flex-col items-center">
                <div className={`h-8 w-8 rounded-full flex items-center justify-center border ${
                  s.type === 'agent' ? 'bg-[var(--determinex-accent)]/20 border-[var(--determinex-accent)]/50 text-[var(--determinex-accent)]' :
                  s.type === 'action' ? 'bg-blue-500/20 border-blue-500/50 text-blue-400' :
                  'bg-gray-800 border-gray-600 text-gray-400'
                }`}>
                  {s.type === 'agent' ? <Bot size={14} /> : s.type === 'action' ? <Terminal size={14} /> : <Info size={14} />}
                </div>
              </div>
              <div className="flex-1 min-w-0 pt-1">
                <div className="text-[10px] text-gray-500 font-mono mb-1">{s.time}</div>
                <div className={`text-[13px] leading-relaxed ${s.type === 'action' ? 'font-mono text-[11px] text-blue-300' : 'text-gray-200'}`}>
                  {s.msg}
                </div>
              </div>
            </div>
          ))}
          <div className="flex items-center gap-3 text-[var(--determinex-accent)] animate-pulse">
            <div className="h-2 w-2 rounded-full bg-current" />
            <span className="text-[10px] uppercase tracking-widest font-bold">Agent is thinking...</span>
          </div>
        </div>

        {/* Input Bar */}
        <div className="p-4 border-t border-white/10 bg-black/40 shrink-0">
          <div className="relative">
            <MessageSquare size={14} className="absolute left-4 top-3 text-gray-500" />
            <input 
              type="text" 
              placeholder="Give the agent a new directive or correction..." 
              className="w-full bg-white/5 border border-white/10 rounded-xl py-3 pl-10 pr-4 text-sm text-white placeholder-gray-600 focus:outline-none focus:border-[var(--determinex-accent)] transition-colors"
            />
          </div>
        </div>
      </div>
    </div>
  );
}
