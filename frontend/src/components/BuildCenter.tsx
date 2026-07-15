"use client";
import { useState } from "react";
import { AlertCircle, Play, FlaskConical, Terminal, Box, Key, Settings2, GitMerge, GitBranch, Archive } from "lucide-react";
import { ProblemsPanel } from "./buildtools/ProblemsPanel";
import { TasksRunner }   from "./buildtools/TasksRunner";
import { TestRunner }    from "./buildtools/TestRunner";
import { OutputPanel }   from "./buildtools/OutputPanel";
import { DependencyManager } from "./buildtools/DependencyManager";
import { EnvManager }    from "./buildtools/EnvManager";
import { BuildConfig }   from "./buildtools/BuildConfig";
import { DiffViewer }    from "./buildtools/DiffViewer";
import { CICDPanel }     from "./buildtools/CICDPanel";
import { ArtifactBrowser } from "./buildtools/ArtifactBrowser";

type ToolId = "problems" | "tasks" | "tests" | "output" | "deps" | "env" | "config" | "diff" | "cicd" | "artifacts";

type Tool = { id: ToolId; label: string; icon: typeof AlertCircle; group: "run" | "project" | "pipeline"; badge?: number };

const TOOLS: Tool[] = [
  { id:"problems",  label:"Problems",     icon:AlertCircle,  group:"run"                },
  { id:"tasks",     label:"Tasks",        icon:Play,         group:"run"                },
  { id:"tests",     label:"Tests",        icon:FlaskConical, group:"run"                },
  { id:"output",    label:"Output",       icon:Terminal,     group:"run"                },
  { id:"deps",      label:"Dependencies", icon:Box,          group:"project"            },
  { id:"env",       label:"Environment",  icon:Key,          group:"project"            },
  { id:"config",    label:"Build Config", icon:Settings2,    group:"project"            },
  { id:"diff",      label:"Diff Viewer",  icon:GitMerge,     group:"pipeline"           },
  { id:"cicd",      label:"CI / CD",      icon:GitBranch,    group:"pipeline"           },
  { id:"artifacts", label:"Artifacts",    icon:Archive,      group:"pipeline"           },
];

const GROUPS: { id: Tool["group"]; label: string }[] = [
  { id:"run",      label:"Run"      },
  { id:"project",  label:"Project"  },
  { id:"pipeline", label:"Pipeline" },
];

const PANELS: Record<ToolId, React.ReactNode> = {
  problems:  <ProblemsPanel />,
  tasks:     <TasksRunner />,
  tests:     <TestRunner />,
  output:    <OutputPanel />,
  deps:      <DependencyManager />,
  env:       <EnvManager />,
  config:    <BuildConfig />,
  diff:      <DiffViewer />,
  cicd:      <CICDPanel />,
  artifacts: <ArtifactBrowser />,
};

type Props = { initialTool?: ToolId };

export function BuildCenter({ initialTool = "problems" }: Props) {
  const [activeTool, setActiveTool] = useState<ToolId>(initialTool);

  return (
    <div className="flex h-full min-h-0 overflow-hidden" style={{ background: "var(--determinex-bg)" }}>
      {/* Left mini-nav */}
      <div
        className="w-44 shrink-0 flex flex-col border-r overflow-y-auto no-scrollbar py-3"
        style={{ borderColor: "var(--determinex-border)", background: "rgba(0,0,0,0.35)" }}
      >
        {GROUPS.map((group, gi) => (
          <div key={group.id} className={gi > 0 ? "mt-2 pt-2 border-t border-white/5" : ""}>
            <div className="px-4 pb-1 text-[7px] uppercase font-black tracking-widest text-gray-700">
              {group.label}
            </div>
            {TOOLS.filter((t) => t.group === group.id).map((tool) => {
              const Icon = tool.icon;
              const isActive = activeTool === tool.id;
              return (
                <button
                  key={tool.id}
                  onClick={() => setActiveTool(tool.id)}
                  className={`relative w-full flex items-center gap-2.5 px-4 py-2 text-left transition-all ${
                    isActive
                      ? "bg-[var(--determinex-accent)]/10 text-[var(--determinex-accent)]"
                      : "text-gray-600 hover:text-gray-400 hover:bg-white/[0.02]"
                  }`}
                >
                  {isActive && (
                    <div className="absolute left-0 top-1 bottom-1 w-0.5 rounded-full bg-[var(--determinex-accent)]" />
                  )}
                  <Icon size={13} className="shrink-0" />
                  <span className="text-[10px] font-semibold truncate">{tool.label}</span>
                  {tool.badge && (
                    <span className={`ml-auto shrink-0 text-[8px] font-black rounded-full w-4 h-4 flex items-center justify-center ${
                      tool.id === "problems" ? "bg-red-500/20 text-red-400" : "bg-[var(--determinex-accent)]/20 text-[var(--determinex-accent)]"
                    }`}>
                      {tool.badge}
                    </span>
                  )}
                </button>
              );
            })}
          </div>
        ))}
      </div>

      {/* Right: active panel */}
      <div className="flex-1 min-w-0 min-h-0 overflow-hidden">
        {PANELS[activeTool]}
      </div>
    </div>
  );
}
