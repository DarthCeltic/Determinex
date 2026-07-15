"use client";
import { useState } from "react";
import { Bot, Code2, Gauge, GitBranch, GraduationCap, LayoutGrid, Package, Blocks, Search, ShieldCheck, Terminal, Wrench } from "lucide-react";
import { MarketplacePanel } from "./MarketplacePanel";
import { ToolsRegistry } from "./ToolsRegistry";
import { useSettings } from "@/contexts/SettingsContext";
import { NETWORK_POLICY_COPY } from "@/lib/networkPolicy";

type Tab = "workspace" | "providers" | "installed" | "browse";

type Props = {
  toolCatalog: any;
  toolCoverage: any;
  onShowServiceLogin: (id: string) => void;
  onLaunchTool: (id: "terminal" | "editor" | "build" | "trace" | "search" | "health" | "mission" | "roadmap") => void;
  activeTool?: string | null;
  onOpenBrain?: () => void;
};

const TABS: { id: Tab; label: string; icon: typeof Package; desc: string }[] = [
  { id: "workspace", label: "Workspace Tools", icon: Wrench,  desc: "Attach IDE tools to the active screen" },
  { id: "providers", label: "AI Providers",    icon: Bot,     desc: "Route Codex, Claude, Gemini, OpenAI, Ollama, and hybrids" },
  { id: "installed", label: "Installed",       icon: Blocks,  desc: "Active tools and integrations" },
  { id: "browse",    label: "Browse",          icon: Package, desc: "Discover and install extensions" },
];

export function ToolsHub({
  toolCatalog,
  toolCoverage,
  onShowServiceLogin,
  onLaunchTool,
  activeTool,
  onOpenBrain,
}: Props) {
  const [activeTab, setActiveTab] = useState<Tab>("workspace");
  const {
    networkPolicy,
    setSettingsTab,
    setShowSettings,
    keyStatus,
  } = useSettings();
  const networkCopy = NETWORK_POLICY_COPY[networkPolicy];

  // The backend's static tool registry has no visibility into the real API
  // key vault (registry.rs hardcodes "needs_key" for every key-gated tool),
  // so a tool whose key the user HAS already saved in Settings would show
  // "Connect Service" forever. Only OPENAI_API_KEY has a real counterpart in
  // ApiKeyStatus today -- the rest (GITHUB_TOKEN, LINEAR_API_KEY, etc.) have
  // no storage anywhere in the app yet, so "needs_key" stays honest for them.
  const REQUIRES_TO_KEY_STATUS: Record<string, keyof typeof keyStatus> = {
    OPENAI_API_KEY: "openai",
  };
  const liveToolCatalog = Array.isArray(toolCatalog)
    ? toolCatalog.map((tool) => {
        const mappedKey = tool?.requires ? REQUIRES_TO_KEY_STATUS[tool.requires] : undefined;
        if (mappedKey && keyStatus[mappedKey]) {
          return { ...tool, status: "online" };
        }
        return tool;
      })
    : toolCatalog;
  const workspaceTools = [
    { id: "terminal" as const, name: "Terminal", icon: Terminal, detail: "Run commands beside Work, Space, Brain, or Proof instead of opening a separate page." },
    { id: "editor" as const, name: "Code", icon: Code2, detail: "Inspect files, generated output, and diffs while staying in the current project screen." },
    { id: "build" as const, name: "Build", icon: Gauge, detail: "Watch tasks, tests, problems, artifacts, dependencies, and environment checks." },
    { id: "trace" as const, name: "Trace", icon: GitBranch, detail: "Replay worker events, WAL records, retries, and handoff history." },
    { id: "search" as const, name: "Search", icon: Search, detail: "Search project context and verified snippets from the active workspace." },
    { id: "health" as const, name: "Health", icon: LayoutGrid, detail: "View oracle health, file readiness, and scan results for the selected project." },
    { id: "mission" as const, name: "Mission", icon: GraduationCap, detail: "Open the interactive guide with current release gates, runbooks, and proof boundaries." },
    { id: "roadmap" as const, name: "Roadmap", icon: ShieldCheck, detail: "Open the Determinex successor roadmap, exact blockers, and release-lock contract." },
  ];
  const providers = [
    ["Codex", "Code review, repo edits, explanations, and direct worker handoff."],
    ["Claude", "Long-context planning, architecture review, and implementation critique."],
    ["Gemini", "Fast multimodal review, screenshots, and broad context passes."],
    ["OpenAI", "API-backed models, embeddings, structured tools, and hosted reasoning."],
    ["Ollama Local", "Offline local models for private builder, observer, and fallback routes."],
    ["Hybrid Stack", "Role slots can mix local and API models by Oracle, Architect, Builder, and Monitor."],
  ];

  return (
    <div className="flex h-full min-h-0 flex-col overflow-hidden" style={{ background: "var(--determinex-bg)" }}>
      {/* Tab bar */}
      <div
        className="flex shrink-0 items-center gap-1 border-b px-4 pt-3"
        style={{ borderColor: "var(--determinex-border)", background: "rgba(0,0,0,0.3)" }}
      >
        {TABS.map(({ id, label, icon: Icon, desc }) => (
          <button
            key={id}
            onClick={() => setActiveTab(id)}
            title={desc}
            className={`flex items-center gap-2 rounded-t-xl border-b-2 px-4 py-2.5 text-[10px] font-black uppercase tracking-widest transition-all ${
              activeTab === id
                ? "border-[var(--determinex-accent)] text-[var(--determinex-accent)]"
                : "border-transparent text-gray-600 hover:text-gray-400"
            }`}
          >
            <Icon size={12} />
            {label}
          </button>
        ))}
      </div>

      {/* Tab content */}
      <div className="flex-1 min-h-0 overflow-hidden">
        {activeTab === "workspace" && (
          <div className="h-full overflow-y-auto p-6 no-scrollbar">
            <div className="mb-6 border-b border-white/10 pb-5">
              <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-[var(--determinex-accent)]">
                <Wrench size={14} /> Attachable IDE Tools
              </div>
              <p className="mt-2 max-w-3xl text-sm leading-relaxed text-[var(--determinex-muted)]">
                These are not separate destinations. They dock into the current screen so a user can keep proof, code, terminal output, and search beside the work they are doing.
              </p>
            </div>
            <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
              {workspaceTools.map(({ id, name, icon: Icon, detail }) => (
                <button
                  key={name}
                  type="button"
                  onClick={() => onLaunchTool(id)}
                  data-testid={`tools-launch-${id}`}
                  className={`group rounded-2xl border p-5 text-left transition-all hover:-translate-y-0.5 hover:shadow-[0_14px_38px_rgba(0,0,0,0.35)] ${
                    activeTool === id
                      ? "border-[var(--determinex-accent)] bg-[var(--determinex-accent)]/10"
                      : "border-white/10 bg-black/30 hover:border-[var(--determinex-accent)]/40"
                  }`}
                >
                  <div className="flex items-center gap-3">
                    <div className="flex h-10 w-10 items-center justify-center rounded-xl border border-[var(--determinex-border)] bg-[var(--determinex-accent)]/10 text-[var(--determinex-accent)]">
                      <Icon size={18} />
                    </div>
                    <div className="min-w-0">
                      <div className="text-sm font-black text-white">{name}</div>
                      <div className="mt-0.5 text-[8px] font-black uppercase tracking-widest text-[var(--determinex-accent)] opacity-0 transition-opacity group-hover:opacity-100">
                        {activeTool === id ? "Open" : "Attach"}
                      </div>
                    </div>
                  </div>
                  <p className="mt-3 text-[11px] leading-relaxed text-gray-500">{detail}</p>
                </button>
              ))}
            </div>
          </div>
        )}

        {activeTab === "providers" && (
          <div className="h-full overflow-y-auto p-6 no-scrollbar">
            <div className="mb-6 border-b border-white/10 pb-5">
              <div className="flex flex-wrap items-center justify-between gap-3">
                <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-[var(--determinex-accent)]">
                  <Bot size={14} /> Model and Agent Providers
                </div>
                <button
                  type="button"
                  onClick={() => {
                    setSettingsTab("network");
                    setShowSettings(true);
                  }}
                  className="rounded-full border border-white/10 bg-white/[0.03] px-3 py-1.5 text-[9px] font-black uppercase tracking-widest text-gray-400 transition hover:border-[var(--determinex-accent)]/40 hover:text-[var(--determinex-accent)]"
                  title="Open Network Policy settings"
                >
                  Network: {networkCopy.shortLabel}
                </button>
              </div>
              <p className="mt-2 max-w-3xl text-sm leading-relaxed text-[var(--determinex-muted)]">
                Providers are slotable. A role can use a local model, an API call, or a hybrid route depending on privacy, speed, cost, and proof requirements.
              </p>
              <div className="mt-4 rounded-xl border border-white/10 bg-black/25 px-4 py-3 text-[11px] leading-relaxed text-gray-500">
                {networkCopy.summary} ProgramBench and hardened benchmark runners remain network-denied even when the IDE is online.
              </div>
            </div>
            <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
              {providers.map(([name, detail]) => (
                <div key={name} className="rounded-2xl border border-white/10 bg-black/30 p-5">
                  <div className="flex items-center justify-between gap-3">
                    <div className="text-sm font-black text-white">{name}</div>
                    <span className="rounded-full border border-white/10 bg-white/[0.03] px-2 py-1 text-[8px] font-black uppercase tracking-widest text-gray-500">
                      Slotable
                    </span>
                  </div>
                  <p className="mt-3 text-[11px] leading-relaxed text-gray-500">{detail}</p>
                  <button
                    type="button"
                    onClick={() => {
                      if (name === "Ollama Local" || name === "Hybrid Stack") onOpenBrain?.();
                      else if (networkPolicy === "offline") {
                        setSettingsTab("network");
                        setShowSettings(true);
                      }
                      else onShowServiceLogin(name.toLowerCase().replace(/\s+/g, "-"));
                    }}
                    className="mt-4 rounded-lg border border-white/10 bg-white/[0.03] px-3 py-2 text-[9px] font-black uppercase tracking-widest text-gray-400 transition hover:border-[var(--determinex-accent)]/40 hover:text-[var(--determinex-accent)]"
                  >
                    {name === "Ollama Local" || name === "Hybrid Stack" ? "Open model slots" : networkPolicy === "offline" ? "Enable network policy" : "Configure provider"}
                  </button>
                </div>
              ))}
            </div>
          </div>
        )}

        {activeTab === "browse" && <MarketplacePanel />}

        {activeTab === "installed" && (
          <div className="h-full overflow-y-auto no-scrollbar">
            <ToolsRegistry
              toolCatalog={liveToolCatalog}
              toolCoverage={toolCoverage}
              onShowServiceLogin={onShowServiceLogin}
              onOpenBrowse={() => setActiveTab("browse")}
            />
          </div>
        )}
      </div>
    </div>
  );
}
