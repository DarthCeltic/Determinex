"use client";
import { Zap } from "lucide-react";

interface BootOverlayProps {
  bootError: string | null;
  bootProgress: number;
  onDismiss: () => void;
}

export function BootOverlay({ bootError, bootProgress, onDismiss }: BootOverlayProps) {
  return (
    <div className="absolute inset-0 z-[110] bg-black flex flex-col items-center justify-center font-mono overflow-hidden">
      <div className="absolute inset-0 opacity-10 pointer-events-none select-none overflow-hidden text-green-500 text-xs leading-none break-all">
        {"01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホ".repeat(800)}
      </div>
      <div className="relative z-10 flex flex-col items-center gap-6 max-w-md w-full text-center px-8">
        <div
          className="w-20 h-20 rounded-full border-2 border-cyan-500/60 flex items-center justify-center"
          style={{
            boxShadow: "0 0 40px rgba(0,229,255,0.35), inset 0 0 20px rgba(0,229,255,0.08)",
          }}
        >
          <Zap size={34} className="text-cyan-400 animate-pulse" />
        </div>

        <div className="flex flex-col gap-1">
          <p className="text-[9px] tracking-[0.5em] uppercase text-gray-500">DETERMINEX SYSTEM</p>
          <h1
            className="text-2xl font-black tracking-[0.18em] text-cyan-400 uppercase"
            style={{ textShadow: "0 0 24px rgba(0,229,255,0.5)" }}
          >
            {bootError ? "BOOT FAILURE" : "INITIALIZING"}
          </h1>
          <p className="text-[11px] text-gray-500 mt-1">
            {bootError
              ? "Hardware requirements not met."
              : "Probing hardware · Building inference models..."}
          </p>
        </div>

        {bootError ? (
          <div className="w-full bg-red-950/50 border border-red-500/40 rounded-xl px-5 py-4 text-left">
            <p className="text-[9px] uppercase tracking-widest text-red-400 font-black mb-2">
              Error
            </p>
            <p className="text-[10px] text-red-300/80 leading-relaxed font-mono">{bootError}</p>
            <button
              onClick={onDismiss}
              className="mt-4 w-full py-2 bg-red-950 hover:bg-red-900 border border-red-500/40 text-red-400 text-[10px] font-black uppercase tracking-widest rounded-lg transition-colors"
            >
              Continue Anyway
            </button>
          </div>
        ) : (
          <div className="w-full max-w-xs flex flex-col gap-1">
            <div className="h-[2px] bg-[#1a1a2e] rounded-full overflow-hidden">
              <div
                className="h-full bg-cyan-500 rounded-full transition-all duration-500 ease-out"
                style={{
                  width: `${bootProgress}%`,
                  boxShadow: "0 0 8px rgba(0,229,255,0.6)",
                }}
              />
            </div>
            <p className="text-[9px] text-gray-600 text-right tabular-nums">{bootProgress}%</p>
          </div>
        )}
      </div>
    </div>
  );
}
