"use client";
import { useState } from "react";
import { Panel, PanelGroup, PanelResizeHandle } from "react-resizable-panels";
import { EditorPanel } from "./EditorPanel";
import { TerminalPanel } from "./TerminalPanel";
import { X, TerminalSquare } from "lucide-react";

export function ExecutionWorkspace() {
  const [isTerminalOpen, setIsTerminalOpen] = useState(true);

  return (
    <div className="flex flex-col flex-1 w-full h-full overflow-hidden bg-black/90 relative">
      <PanelGroup direction="vertical" className="h-full">
        {/* Top pane: Monaco Editor */}
        <Panel defaultSize={isTerminalOpen ? 70 : 100} minSize={30} className="flex flex-col relative bg-[#0d1117]">
          <EditorPanel />
          
          {/* Toggle Button when terminal is closed */}
          {!isTerminalOpen && (
            <button 
              onClick={() => setIsTerminalOpen(true)}
              className="absolute bottom-4 right-6 bg-[#1a1b26] hover:bg-[#24283b] border border-cyan-500/30 text-cyan-400 p-2 rounded-lg shadow-[0_0_15px_rgba(0,229,255,0.1)] transition-all z-50 flex items-center gap-2 group"
              title="Open Terminal"
            >
              <TerminalSquare size={16} className="group-hover:text-white transition-colors" />
              <span className="text-[10px] uppercase font-bold tracking-wider group-hover:text-white transition-colors">Terminal</span>
            </button>
          )}
        </Panel>

        {isTerminalOpen && (
          <>
            {/* Resizer */}
            <PanelResizeHandle className="h-1.5 bg-black/40 hover:bg-[var(--determinex-accent)]/50 transition-colors cursor-row-resize z-10 flex items-center justify-center">
              <div className="h-0.5 w-8 bg-white/20 rounded-full" />
            </PanelResizeHandle>

            {/* Bottom pane: Xterm Terminal */}
            <Panel defaultSize={30} minSize={10} className="flex flex-col relative bg-[#010409]">
              <div className="h-7 bg-[#0d1117] border-b border-white/5 flex items-center justify-between px-3 select-none">
                <div className="flex items-center gap-2 text-gray-400">
                  <TerminalSquare size={12} />
                  <span className="text-[10px] font-bold uppercase tracking-wider">Integrated Terminal</span>
                </div>
                <div className="flex items-center gap-2">
                  <button 
                    onClick={() => setIsTerminalOpen(false)}
                    className="text-gray-500 hover:text-white hover:bg-white/10 p-1 rounded transition-colors"
                  >
                    <X size={12} />
                  </button>
                </div>
              </div>
              <div className="flex-1 overflow-hidden relative">
                <TerminalPanel />
              </div>
            </Panel>
          </>
        )}
      </PanelGroup>
    </div>
  );
}
