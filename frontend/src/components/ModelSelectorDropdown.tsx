"use client";
import { memo, useMemo, useState } from "react";

interface ModelEntry {
  id: string;
  name: string;
  desc: string;
  // Optional: only present when sourced from a real scored registry entry
  // (models_registry.json). Client-built tiers (installed add-ons, local
  // Ollama models) never fabricate a rating here.
  elo_rating?: number;
  context_window: number;
}

function formatContextWindow(tokens: number): string {
  if (tokens >= 1000) return `${Math.round(tokens / 1000)}K ctx`;
  return `${tokens} ctx`;
}
interface TierEntry {
  tier_id: string;
  title: string;
  color: string;
  models: ModelEntry[];
}
interface TandemPreset {
  name: string;
  topology: { sentinel: string; engineer: string; observer: string };
}

interface ModelSelectorDropdownProps {
  selectedModel: string;
  modelTiers: TierEntry[];
  tandemPresets: TandemPreset[];
  onSelectModel: (id: string) => void;
  onSelectTopology: (
    topology: { sentinel: string; engineer: string; observer: string },
    name: string
  ) => void;
}

export const ModelSelectorDropdown = memo(function ModelSelectorDropdown({
  selectedModel,
  modelTiers,
  tandemPresets,
  onSelectModel,
  onSelectTopology,
}: ModelSelectorDropdownProps) {
  const [modelMenuOpen, setModelMenuOpen] = useState(false);

  const activeName = useMemo(() => {
    for (const t of modelTiers) {
      for (const m of t.models) {
        if (m.id === selectedModel) return m.name;
      }
    }
    return "Model Pack";
  }, [modelTiers, selectedModel]);

  return (
    <div className="relative">
      <button
        onClick={() => setModelMenuOpen(!modelMenuOpen)}
        className={`border ${modelMenuOpen ? "border-cyan-500 bg-cyan-950/30" : "bg-[#010409] border-cyan-500/30"} hover:border-cyan-500 text-[10px] uppercase tracking-wider font-bold text-cyan-400 rounded-full px-3 py-1.5 outline-none cursor-pointer flex items-center gap-2 shadow-md transition-all`}
      >
        {activeName} <span className="opacity-50 text-[8px]">{modelMenuOpen ? "▲" : "▼"}</span>
      </button>

      {modelMenuOpen && (
        <>
          <div className="fixed inset-0 z-[40]" onClick={() => setModelMenuOpen(false)} />
          <div className="absolute bottom-full right-0 mb-3 w-80 bg-[#0d1117] border border-[#30363d] shadow-[0_-10px_40px_rgba(0,0,0,0.9)] rounded-xl overflow-hidden z-[50] flex flex-col animate-in slide-in-from-bottom-2 fade-in duration-200">
            <div className="max-h-[60vh] overflow-y-auto no-scrollbar pb-2">
              {tandemPresets.length > 0 && (
                <div className="flex flex-col">
                  <div className="px-4 py-2 mt-1 text-[9px] uppercase tracking-widest font-black bg-emerald-950/40 border-y border-[#30363d] text-emerald-400">
                    Pack Topologies
                  </div>
                  {tandemPresets.map((preset, idx) => (
                    <div
                      key={`preset-${idx}`}
                      onClick={() => {
                        onSelectTopology(preset.topology, preset.name);
                        setModelMenuOpen(false);
                      }}
                      className="p-3 cursor-pointer transition-colors border-b border-[#30363d]/50 hover:bg-[#161b22]"
                    >
                      <div className="flex items-center justify-between">
                        <div className="text-xs font-bold leading-none text-emerald-400">
                          {preset.name}
                        </div>
                      </div>
                      <div className="text-[10px] mt-1.5 leading-snug text-gray-500">
                        Sentinel: {preset.topology.sentinel.split("/").pop()} <br />
                        Engineer: {preset.topology.engineer.split("/").pop()} <br />
                        Observer: {preset.topology.observer.split("/").pop()}
                      </div>
                    </div>
                  ))}
                </div>
              )}

              {modelTiers.map((tier, idx) => (
                <div key={idx} className="flex flex-col">
                  <div
                    className={`px-4 py-2 mt-1 text-[9px] uppercase tracking-widest font-black bg-[#161b22] border-y border-[#30363d] ${tier.color}`}
                  >
                    {tier.title}
                  </div>
                  {tier.models.map((model) => (
                    <div
                      key={model.id}
                      onClick={() => {
                        onSelectModel(model.id);
                        setModelMenuOpen(false);
                      }}
                      className={`p-3 cursor-pointer transition-colors border-b border-[#30363d]/50 last:border-0 ${selectedModel === model.id ? "bg-cyan-900/30" : "hover:bg-[#161b22]"}`}
                    >
                      <div className="flex items-center justify-between">
                        <div
                          className={`text-xs font-bold leading-none ${selectedModel === model.id ? "text-cyan-400" : "text-gray-200"}`}
                        >
                          {model.name}
                        </div>
                        <span className="text-[9px] text-cyan-400/50 font-mono">
                          {model.elo_rating ? `ELO: ${model.elo_rating}` : formatContextWindow(model.context_window)}
                        </span>
                      </div>
                      <div
                        className={`text-[10px] mt-1.5 leading-snug ${selectedModel === model.id ? "text-cyan-200/70" : "text-gray-500"}`}
                      >
                        {model.desc}
                      </div>
                    </div>
                  ))}
                </div>
              ))}
            </div>
          </div>
        </>
      )}
    </div>
  );
});
