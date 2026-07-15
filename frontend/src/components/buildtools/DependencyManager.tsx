"use client";
import { useState } from "react";
import { AlertTriangle, Check, Plus, ExternalLink, RefreshCw } from "lucide-react";

type Dep = { name: string; current: string; latest?: string; outdated?: boolean; vuln?: boolean; dev?: boolean };

const RUST_DEPS: Dep[] = [
  { name:"tokio",      current:"1.28.0",  latest:"1.36.0",  outdated:true  },
  { name:"serde",      current:"1.0.195", latest:"1.0.203", outdated:true  },
  { name:"anyhow",     current:"1.0.79",  latest:"1.0.86",  outdated:true  },
  { name:"clap",       current:"4.4.12",  latest:"4.5.4",   outdated:true  },
  { name:"reqwest",    current:"0.11.24",                                    },
  { name:"regex",      current:"1.10.3",                                     },
  { name:"tracing",    current:"0.1.40",                                     },
  { name:"uuid",       current:"1.7.0",                                      },
  { name:"chrono",     current:"0.4.35",                                     },
  { name:"rand",       current:"0.8.5",   latest:"0.9.0",   outdated:true  },
];

const GO_DEPS: Dep[] = [
  { name:"golang.org/x/tools",    current:"v0.19.0",                        },
  { name:"github.com/spf13/cobra", current:"v1.8.0",                        },
  { name:"go.uber.org/zap",        current:"v1.26.0", latest:"v1.27.0", outdated:true },
  { name:"github.com/stretchr/testify", current:"v1.9.0",                   },
];

const PYTHON_DEPS: Dep[] = [
  { name:"anthropic",   current:"0.23.1", latest:"0.25.0", outdated:true },
  { name:"openai",      current:"1.14.0", latest:"1.25.0", outdated:true },
  { name:"litellm",     current:"1.33.7",                                  },
  { name:"tree-sitter", current:"0.21.3",                                  },
  { name:"ruff",        current:"0.3.2",  latest:"0.4.1",  outdated:true, dev:true },
  { name:"pytest",      current:"8.1.1",                    dev:true },
  { name:"pyright",     current:"1.1.354",                  dev:true },
];

const NPM_DEPS: Dep[] = [
  { name:"next",               current:"16.2.6",                                },
  { name:"react",              current:"19.0.0",                                },
  { name:"@monaco-editor/react", current:"4.6.0",                              },
  { name:"lucide-react",       current:"0.368.0", latest:"0.381.0", outdated:true },
  { name:"tailwindcss",        current:"3.4.1",                                 },
  { name:"@tauri-apps/api",    current:"1.5.3",                                 },
];

const ECOSYSTEMS = [
  { id:"rust",   label:"Cargo",     deps: RUST_DEPS   },
  { id:"go",     label:"Go",        deps: GO_DEPS     },
  { id:"python", label:"Python",    deps: PYTHON_DEPS },
  { id:"node",   label:"NPM",       deps: NPM_DEPS    },
];

export function DependencyManager() {
  const [eco, setEco] = useState("rust");
  const [search, setSearch] = useState("");
  const [refreshing, setRefreshing] = useState(false);

  const current = ECOSYSTEMS.find((e) => e.id === eco)!;
  const filtered = current.deps.filter((d) => d.name.toLowerCase().includes(search.toLowerCase()));
  const outdatedCount = current.deps.filter((d) => d.outdated).length;

  const refresh = () => { setRefreshing(true); setTimeout(() => setRefreshing(false), 1500); };

  return (
    <div className="flex h-full flex-col overflow-hidden">
      {/* Ecosystem tabs */}
      <div className="shrink-0 flex items-center gap-1 border-b px-4 pt-2" style={{ borderColor: "var(--determinex-border)", background: "rgba(0,0,0,0.2)" }}>
        {ECOSYSTEMS.map(({ id, label, deps }) => {
          const outdated = deps.filter((d) => d.outdated).length;
          return (
            <button key={id} onClick={() => setEco(id)}
              className={`flex items-center gap-1.5 border-b-2 px-3 py-2 text-[9px] font-black uppercase tracking-widest transition-all ${eco === id ? "border-[var(--determinex-accent)] text-[var(--determinex-accent)]" : "border-transparent text-gray-600 hover:text-gray-400"}`}>
              {label}
              {outdated > 0 && <span className="text-amber-500/80 font-mono text-[8px]">{outdated}</span>}
            </button>
          );
        })}
      </div>

      {/* Search + actions */}
      <div className="shrink-0 flex items-center gap-2 px-4 py-2 border-b" style={{ borderColor: "var(--determinex-border)" }}>
        <input value={search} onChange={(e) => setSearch(e.target.value)} placeholder="Search packages..."
          className="flex-1 rounded-lg border border-white/8 bg-black/30 px-3 py-1.5 text-[10px] text-white/70 placeholder:text-gray-700 outline-none focus:border-[var(--determinex-accent)]/30" />
        <button onClick={refresh} className={`text-gray-600 hover:text-gray-400 transition-colors ${refreshing ? "animate-spin text-cyan-400" : ""}`}>
          <RefreshCw size={13} />
        </button>
        {outdatedCount > 0 && (
          <button className="flex items-center gap-1 rounded-lg border border-amber-500/30 bg-amber-950/10 px-2.5 py-1 text-[9px] font-bold text-amber-400 hover:bg-amber-950/20 transition-colors">
            <AlertTriangle size={10} /> Update {outdatedCount}
          </button>
        )}
      </div>

      {/* Dep list */}
      <div className="flex-1 overflow-y-auto no-scrollbar divide-y divide-white/[0.03]">
        {filtered.map((dep) => (
          <div key={dep.name} className="flex items-center gap-3 px-4 py-2.5 hover:bg-white/[0.02] transition-colors group">
            <div className="flex-1 min-w-0">
              <div className="flex items-center gap-2">
                <span className="text-[11px] font-mono text-white/75">{dep.name}</span>
                {dep.dev && <span className="text-[7px] rounded border border-white/8 px-1 py-0.5 text-gray-600">dev</span>}
                {dep.vuln && <span className="text-[7px] rounded border border-red-500/30 bg-red-950/20 px-1 py-0.5 text-red-400">vuln</span>}
              </div>
            </div>
            <div className="flex items-center gap-2 shrink-0">
              <span className="text-[10px] font-mono text-gray-500">{dep.current}</span>
              {dep.outdated ? (
                <div className="flex items-center gap-1.5">
                  <span className="text-[8px] text-amber-400 font-mono">{"->"} {dep.latest}</span>
                  <button className="opacity-0 group-hover:opacity-100 rounded border border-amber-500/30 bg-amber-950/20 px-1.5 py-0.5 text-[8px] text-amber-400 hover:bg-amber-950/40 transition-all">
                    Update
                  </button>
                </div>
              ) : (
                <Check size={11} className="text-emerald-500/50" />
              )}
            </div>
          </div>
        ))}
        {/* Add dep row */}
        <div className="flex items-center gap-2 px-4 py-3 opacity-40 hover:opacity-80 transition-opacity cursor-pointer">
          <Plus size={12} className="text-gray-600" />
          <span className="text-[10px] text-gray-600">Add dependency...</span>
        </div>
      </div>
    </div>
  );
}
