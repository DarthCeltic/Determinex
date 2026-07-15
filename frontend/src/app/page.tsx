"use client";

import { useState, useEffect, useMemo, type ReactNode } from "react";
import { listen } from "@tauri-apps/api/event";
import Editor, { DiffEditor } from "@monaco-editor/react";
import {
  Folder,
  FolderOpen,
  Zap,
  Plus,
  Settings,
  Check,
  Activity,
  Cpu,
  XOctagon,
  HelpCircle,
  Terminal as TerminalIcon,
  GitPullRequest,
  ChevronRight,
  Gauge,
  Files,
  Database,
  Globe,
  RefreshCw,
  ShieldCheck,
  Code2,
  Eye,
  Brain,
  LayoutGrid,
  GitBranch,
  RefreshCcw,
  Search,
  FileSearch,
  Lock,
  FileCode,
  Package,
  GraduationCap,
  Key,
  Palette,
  X,
} from "lucide-react";
import {
  injectSandboxContext,
  abortOrchestration,
  promoteToGarden,
  unleashThePack,
  getModelsRegistry,
  getFileSystemTree,
  readFileContent,
  getWorkspaceFiles,
  getHealthTelemetry,
  fetchTodos,
  getThreads,
  nativeOrchestratePlan,
  nativeOrchestrateCodegen,
  nativeOrchestrateAudit,
  invokeSafe,
  isTauri,
} from "@/lib/api";
import { useSettings } from "@/contexts/SettingsContext";
import { useAiRouter } from "@/contexts/AiRouterContext";
import { useIterationTheme } from "@/contexts/IterationThemeContext";
import { Panel, PanelGroup, PanelResizeHandle } from "react-resizable-panels";
import "@xterm/xterm/css/xterm.css";

import { FileSystemNode, FileNode } from "@/components/FileSystemNode";
import { IdeationBoard } from "@/components/IdeationBoard";
import { PipelineDashboard } from "@/components/PipelineDashboard";
import { ProjectArchitect } from "@/components/ProjectArchitect";
import { MatrixExecutionDisplay, AgentStatus } from "@/components/MatrixExecutionDisplay";
import { WorkspaceViewer } from "@/components/WorkspaceViewer";
import { SetupWizard } from "@/components/SetupWizard";
import dynamic from "next/dynamic";
import type { PathInfo } from "@/components/ConceptLab";

import { AnimatePresence, motion } from "framer-motion";

const ConceptLab = dynamic(() => import("@/components/ConceptLab").then((m) => m.ConceptLab), {
  ssr: false,
  loading: () => <div className="flex-1 bg-[#010409]" />,
});
const OracleArena = dynamic(() => import("@/components/OracleArena").then((m) => m.OracleArena), { ssr: false, loading: () => <div className="flex-1 bg-[#0d1117]" /> });
const HealthMap = dynamic(() => import("@/components/HealthMap").then((m) => m.HealthMap), { ssr: false, loading: () => <div className="flex-1 bg-[#0d1117]" /> });
const AgentTrace = dynamic(() => import("@/components/AgentTrace").then((m) => m.AgentTrace), { ssr: false, loading: () => <div className="flex-1 bg-[#0d1117]" /> });
const PrivacyCockpit = dynamic(() => import("@/components/PrivacyCockpit").then((m) => m.PrivacyCockpit), { ssr: false, loading: () => <div className="flex-1 bg-[#0d1117]" /> });
const FlywheelFeed = dynamic(() => import("@/components/FlywheelFeed").then((m) => m.FlywheelFeed), { ssr: false, loading: () => <div className="flex-1 bg-[#0d1117]" /> });
const TerminalPanel = dynamic(() => import("@/components/TerminalPanel").then((m) => m.TerminalPanel), { ssr: false, loading: () => <div className="flex-1 bg-[#0d1117]" /> });
const EditorPanel = dynamic(() => import("@/components/EditorPanel").then((m) => m.EditorPanel), { ssr: false, loading: () => <div className="flex-1 bg-[#0d1117]" /> });
const VerifiedSearch = dynamic(() => import("@/components/VerifiedSearch").then((m) => m.VerifiedSearch), { ssr: false, loading: () => <div className="flex-1 bg-[#0d1117]" /> });
const TeacherOverlay = dynamic(() => import("@/components/TeacherOverlay").then((m) => m.TeacherOverlay), { ssr: false });
const TeacherButton = dynamic(() => import("@/components/TeacherOverlay").then((m) => m.TeacherButton), { ssr: false });
const ToolsHub = dynamic(() => import("@/components/ToolsHub").then((m) => m.ToolsHub), { ssr: false, loading: () => <div className="flex-1 bg-[#0d1117]" /> });
const BuildCenter = dynamic(() => import("@/components/BuildCenter").then((m) => m.BuildCenter), { ssr: false, loading: () => <div className="flex-1 bg-[#0d1117]" /> });
const ExecutionWorkspace = dynamic(() => import("@/components/ExecutionWorkspace").then((m) => m.ExecutionWorkspace), { ssr: false, loading: () => <div className="flex-1 bg-[#0d1117]" /> });
const SuccessorRoadmapPanel = dynamic(() => import("@/components/SuccessorRoadmapPanel").then((m) => m.SuccessorRoadmapPanel), { ssr: false, loading: () => <div className="flex-1 bg-[#0d1117]" /> });
const MissionControlPanel = dynamic(() => import("@/components/MissionControlPanel").then((m) => m.MissionControlPanel), { ssr: false, loading: () => <div className="flex-1 bg-[#0d1117]" /> });
const GovernedIdeaCommandPanel = dynamic(() => import("@/components/ide-product-shell/GovernedIdeaCommandPanel").then((m) => m.GovernedIdeaCommandPanel), { ssr: false, loading: () => <div className="flex-1 bg-[#0d1117]" /> });
const StatusBar = dynamic(() => import("@/components/StatusBar").then((m) => m.StatusBar), { ssr: false });
const CommandPalette = dynamic(() => import("@/components/CommandPalette").then((m) => m.CommandPalette), { ssr: false });
const GitPanel = dynamic(() => import("@/components/GitPanel"), { ssr: false, loading: () => <div className="flex-1 bg-[#0d1117]" /> });
const ProjectAuditPanel = dynamic(() => import("@/components/ProjectAuditPanel").then((m) => m.ProjectAuditPanel), { ssr: false, loading: () => <div className="flex-1 bg-[#0d1117]" /> });
const CommandCenter = dynamic(() => import("@/components/CommandCenter").then((m) => m.CommandCenter), { ssr: false, loading: () => <div className="flex-1 bg-[#0d1117]" /> });
const WorkspaceOnboarding = dynamic(() => import("@/components/WorkspaceOnboarding").then((m) => m.WorkspaceOnboarding), { ssr: false });
const ProblemsPanel = dynamic(() => import("@/components/ProblemsPanel").then((m) => m.ProblemsPanel), { ssr: false, loading: () => <div className="flex-1 bg-[#0d1117]" /> });
const DiffReviewPanel = dynamic(() => import("@/components/DiffReviewPanel").then((m) => m.DiffReviewPanel), { ssr: false, loading: () => <div className="flex-1 bg-[#0d1117]" /> });
const FileSearchPanel = dynamic(() => import("@/components/FileSearchPanel").then((m) => m.FileSearchPanel), { ssr: false, loading: () => <div className="flex-1 bg-[#0d1117]" /> });
import type { PaletteCommand } from "@/components/CommandPalette";
import { HiveBuildLoop } from "@/components/HiveBuildLoop";
import { BenchmarkRunner } from "@/components/BenchmarkRunner";
import { PathDetailPanel } from "@/components/PathDetailPanel";
import { DiscoveryProgressView } from "@/components/DiscoveryProgressView";
import { SpecBreakdownView } from "@/components/SpecBreakdownView";
import { ToolsRegistry } from "@/components/ToolsRegistry";
import { MatrixRain } from "@/components/MatrixRain";
import { SkinBackdrop } from "@/components/SkinBackdrop";
import { ProjectLibrary } from "@/components/ProjectLibrary";
// GoldenLoopWorkbench removed —" replaced by ProjectArchitect
import { BrainStage } from "@/components/BrainStage";
import {
  ProjectHub,
  type ProjectHubDestination,
  type ProjectHubProject,
} from "@/components/ProjectHub";
import { ADDONS } from "@/lib/addons";
import { getGitStatus, type GitFile } from "@/lib/gitService";
import { ADDONS_UPDATED_EVENT, readInstalledAddonIds } from "@/lib/addonStorage";
import { NETWORK_POLICY_COPY } from "@/lib/networkPolicy";
import { AiRouteSelect } from "@/components/AiRouteSelect";
import { ModelSelectorDropdown } from "@/components/ModelSelectorDropdown";
import { BootOverlay } from "@/components/modals/BootOverlay";
import { HelpModal } from "@/components/modals/HelpModal";
import { ServiceLoginModal } from "@/components/modals/ServiceLoginModal";
import { SettingsModal } from "@/components/modals/SettingsModal";
import { useBootstrap } from "@/hooks/useBootstrap";
import { useMoaTelemetry } from "@/hooks/useMoaTelemetry";
import { useErrorToast } from "@/components/ErrorToast";
import { getSkinPackStyle } from "@/theme/skinPacks";
export type PrimaryWorkspace =
  | "ideation"
  | "pipeline"
  | "explorer"
  | "git"
  | "hive"
  | "benchmark"
  | "proof"
  | "extensions"
  | "hub"
  | "audit"
  | "command"
  | "none";

type WorkspaceAddon =
  | "terminal"
  | "editor"
  | "health"
  | "search"
  | "trace"
  | "cloak"
  | "flywheel"
  | "build"
  | "execution"
  | "mission"
  | "roadmap"
  | "problems"
  | "review"
  | "idea"
  | "findfiles";

type AddonDockMode = "bottom" | "right";
type AddonDockSize = "compact" | "standard" | "large";

type AddonItem = {
  id: WorkspaceAddon;
  label: string;
  description: string;
  icon: typeof TerminalIcon;
  tone: string;
  panel: ReactNode;
};

type DeterminexUiSnapshot = {
  app: "Determinex";
  activeWorkspace: PrimaryWorkspace;
  activeAddon: WorkspaceAddon | null;
  addonDockOpen: boolean;
  addonDockMode: AddonDockMode;
  addonDockSize: AddonDockSize;
  selectedProjectName: string;
  workspacePath: string;
  hiveSessionId: string | null;
  selectedModel: string;
  networkPolicy: string;
  panels: {
    projectLibrary: boolean;
    settings: boolean;
    help: boolean;
  };
  viewport: {
    width: number;
    height: number;
  };
  timestamp: string;
};

declare global {
  interface Window {
    __DETERMINEX_UI_SNAPSHOT__?: () => DeterminexUiSnapshot;
  }
}

function displayPath(path: string) {
  return path.replace(/Determinex/gi, "Determinex");
}

function displayModelName(name: string) {
  return name.replace(/determinex/gi, "determinex");
}

export default function DeterminexIDE() {
  const showError = useErrorToast();
  const { theme, themePack } = useIterationTheme();
  const skinPackStyle = getSkinPackStyle(themePack);
  const {
    showSettings,
    setShowSettings,
    settingsTab,
    setSettingsTab,
    keyStatus,
    apiKeys,
    setApiKeys,
    toolCatalog,
    toolCoverage,
    showServiceLogin,
    setShowServiceLogin,
    serviceKeyInput,
    setServiceKeyInput,
    diagnosticResult,
    isDiagnosing,
    runDiagnostics,
    networkPolicy,
    setNetworkPolicy,
  } = useSettings();
  const networkPolicyCopy = NETWORK_POLICY_COPY[networkPolicy];
  const nextPrivacyPolicy = networkPolicy === "offline" ? "cloaked" : "offline";

  const [inputVal, setInputVal] = useState("");
  const [activeContexts, setActiveContexts] = useState<string[]>([]);
  const { selectedModel, changeModel: setSelectedModel } = useAiRouter();
  const [modelTiers, setModelTiers] = useState<any[]>([]);
  const [tandemPresets, setTandemPresets] = useState<any[]>([]);

  // Tactical Guidance State
  const [helpModal, setHelpModal] = useState<{ title: string; desc: string } | null>(null);
  const [lastPrompt, setLastPrompt] = useState("");

  // File System State
  const [fileTree, setFileTree] = useState<FileNode[]>([]);
  const [explorerRoot, setExplorerRoot] = useState<string>("C:\\Dev\\Determinex");
  const [gitBranch, setGitBranch] = useState<string>("");
  const [explorerGitFiles, setExplorerGitFiles] = useState<GitFile[]>([]);
  const [explorerGitMeta, setExplorerGitMeta] = useState<{ upstream: string | null; ahead: number; behind: number }>({
    upstream: null,
    ahead: 0,
    behind: 0,
  });

  useEffect(() => {
    if (!explorerRoot) return;
    getFileSystemTree(explorerRoot)
      .then((res) => {
        if (res && res.tree) setFileTree(res.tree);
      })
      .catch((err) => showError(`Could not load file tree: ${err}`));
  }, [explorerRoot]);

  useEffect(() => {
    if (!explorerRoot) {
      setGitBranch("");
      setExplorerGitFiles([]);
      return;
    }
    getGitStatus(explorerRoot)
      .then((res) => {
        setGitBranch(res.branch);
        setExplorerGitFiles(res.files);
        setExplorerGitMeta({ upstream: res.upstream, ahead: res.ahead, behind: res.behind });
      })
      .catch(() => {
        setGitBranch("");
        setExplorerGitFiles([]);
        setExplorerGitMeta({ upstream: null, ahead: 0, behind: 0 });
      });
  }, [explorerRoot]);

  // Absolute-path -> status map for the file explorer tree. git_status returns
  // paths relative to explorerRoot (repo-relative porcelain output); FileNode.path
  // is always absolute (built server-side via to_string_lossy()), so normalize
  // both to forward slashes and join against explorerRoot to key the map the
  // same way FileSystemNode will look it up.
  const explorerGitStatusMap = useMemo(() => {
    const map: Record<string, { status: string; code: string }> = {};
    const rootNorm = explorerRoot.replace(/\\/g, "/").replace(/\/+$/, "");
    for (const file of explorerGitFiles) {
      const relNorm = file.path.replace(/\\/g, "/").replace(/^\/+/, "");
      map[`${rootNorm}/${relNorm}`] = { status: file.status, code: file.code };
    }
    return map;
  }, [explorerGitFiles, explorerRoot]);

  const toggleContext = (filename: string) => {
    setActiveContexts((prev) => {
      if (prev.includes(filename)) return prev.filter((c) => c !== filename);
      return [...prev, filename];
    });
  };

  // Viewport Engine
  const [isMobile, setIsMobile] = useState(false);

  // Workspace States
  const [activeTabs, setActiveTabs] = useState<string[]>([]);
  const [currentTab, setCurrentTab] = useState("");
  const [fileContents, setFileContents] = useState<Record<string, string>>({});

  const handleOpenFile = async (filePath: string) => {
    const fileName = filePath.split("\\").pop()?.split("/").pop() || filePath;
    if (!activeTabs.includes(fileName)) setActiveTabs((prev) => [...prev, fileName]);
    setCurrentTab(fileName);
    try {
      const res = await readFileContent(filePath);
      if (res) setFileContents((prev) => ({ ...prev, [fileName]: res.content }));
    } catch (err) {
      setMatrixLogs((prev) => [...prev, `[ERROR] Could not read file ${fileName}: ${err}`]);
    }
  };

  // Pipeline State
  const [determinexPhase, setDeterminexPhase] = useState<"ideation" | "execution">("ideation");
  const [isExecutingPack, setIsExecutingPack] = useState(false);
  const [readinessScore, setReadinessScore] = useState(0);
  const [todos, setTodos] = useState<{ id: number; text: string; done: boolean }[]>([]);

  // Hardware Bootstrap
  const { isBootstrapping, bootTier, bootError, bootProgress, dismissBootError } = useBootstrap();

  // Pipeline output
  const [retryCount, setRetryCount] = useState(0);
  const [generatedFile, setGeneratedFile] = useState<string | null>(null);
  const [compilerWarning, setCompilerWarning] = useState<string | null>(null);

  // MoA Agent Telemetry
  const [agentStatus, setAgentStatus] = useState<AgentStatus>({
    currentAgent: null,
    isExecuting: false,
    verdict: null,
    confidence: null,
    accepted: null,
    error: null,
  });

  const [showWarRoom, setShowWarRoom] = useState(false);
  const [activeThreadId, setActiveThreadId] = useState("");
  const [threadHistory, setThreadHistory] = useState<
    { id: string; title: string; updated: string }[]
  >([]);
  const [showOnboarding, setShowOnboarding] = useState(true);
  const [activeSidebar, setActiveSidebar] = useState<PrimaryWorkspace>("command");
  const [lastWorkbenchSidebar, setLastWorkbenchSidebar] = useState<PrimaryWorkspace>("command");
  const [activeAddon, setActiveAddon] = useState<WorkspaceAddon | null>(null);
  const [addonDockOpen, setAddonDockOpen] = useState(false);
  const [addonDockMode, setAddonDockMode] = useState<AddonDockMode>("bottom");
  const [addonDockSize, setAddonDockSize] = useState<AddonDockSize>("standard");
  const [showTeacher, setShowTeacher] = useState(false);
  const [showPalette, setShowPalette] = useState(false);
  const [hiveSessionId, setHiveSessionId] = useState<string | null>(null);
  const [hiveAutoRun, setHiveAutoRun] = useState(false);
  const [hiveSpec, setHiveSpec] = useState<string>("");
  const [hiveProjectName, setHiveProjectName] = useState<string>("");
  const [previewedPath, setPreviewedPath] = useState<PathInfo | null>(null);
  const [confirmedPath, setConfirmedPath] = useState<PathInfo | null>(null);
  const [oracleAnsweredCount, setOracleAnsweredCount] = useState(0);
  const [isOracleConsulting, setIsOracleConsulting] = useState(false);
  const [oracleElapsed, setOracleElapsed] = useState(0);
  useEffect(() => {
    if (!isOracleConsulting) {
      setOracleElapsed(0);
      return;
    }
    const id = setInterval(() => setOracleElapsed((s) => s + 1), 1000);
    return () => clearInterval(id);
  }, [isOracleConsulting]);
  const [externalIdea, setExternalIdea] = useState("");
  const [colorHints, setColorHints] = useState<string[]>([]);
  const [showProjectLibrary, setShowProjectLibrary] = useState(false);
  const [hiveAutoRetry, setHiveAutoRetry] = useState(false);
  const [selectedProjectName, setSelectedProjectName] = useState("Determinex");
  const [workspaceView, setWorkspaceView] = useState<"overview" | "files" | "source" | "runs">(
    "overview"
  );

  const handleSidebarLaunch = (
    sidebar: PrimaryWorkspace
  ) => {
    setActiveSidebar(activeSidebar === sidebar ? "none" : sidebar);
  };
  useEffect(() => {
    if (activeSidebar !== "none" && activeSidebar !== "extensions") {
      setLastWorkbenchSidebar(activeSidebar);
    }
  }, [activeSidebar]);

  const handleAddonLaunch = (addon: WorkspaceAddon) => {
    if (addonDockOpen && activeAddon === addon && activeSidebar !== "extensions") {
      setActiveAddon(null);
      setAddonDockOpen(false);
      return;
    }
    if (activeSidebar === "none" || activeSidebar === "extensions") {
      setActiveSidebar(lastWorkbenchSidebar === "none" || lastWorkbenchSidebar === "extensions" ? "hub" : lastWorkbenchSidebar);
    }
    setActiveAddon(addon);
    setAddonDockOpen(true);
  };
  const closeAddon = () => {
    setActiveAddon(null);
    setAddonDockOpen(false);
  };
  const openProjectHub = () => {
    setActiveSidebar("hub");
    setPreviewedPath(null);
  };
  const openWorkspace = (view: "overview" | "files" | "source" | "runs" = "overview") => {
    setWorkspaceView(view);
    setActiveSidebar("explorer");
  };
  const handleProjectHubNavigate = (destination: ProjectHubDestination) => {
    if (destination === "work") {
      setActiveSidebar("hive");
      return;
    }
    if (destination === "workspace") {
      openWorkspace("overview");
      return;
    }
    if (destination === "source") {
      openWorkspace("source");
      return;
    }
    if (destination === "runs") {
      openWorkspace("runs");
      return;
    }
    if (destination === "brain") {
      setActiveSidebar("benchmark");
      return;
    }
    if (destination === "proof") {
      setActiveSidebar("proof");
    }
  };

  useEffect(() => {
    const handleGlobalKeyDown = (e: KeyboardEvent) => {
      if (
        document.activeElement?.tagName === "INPUT" ||
        document.activeElement?.tagName === "TEXTAREA"
      ) {
        return;
      }
      
      if ((e.metaKey || e.ctrlKey) && e.key === "b") {
        e.preventDefault();
        setActiveSidebar((prev) => (prev === "none" ? "explorer" : "none"));
      } else if ((e.metaKey || e.ctrlKey) && (e.key === "j" || e.key === "`")) {
        e.preventDefault();
        handleAddonLaunch("terminal");
      } else if ((e.metaKey || e.ctrlKey) && e.shiftKey && (e.key === "F" || e.key === "f")) {
        e.preventDefault();
        handleAddonLaunch("findfiles");
      } else if ((e.metaKey || e.ctrlKey) && e.key === "1") {
        e.preventDefault();
        setActiveSidebar("hub");
      } else if ((e.metaKey || e.ctrlKey) && e.key === "2") {
        e.preventDefault();
        setActiveSidebar("hive");
      } else if ((e.metaKey || e.ctrlKey) && e.key === "3") {
        e.preventDefault();
        setActiveSidebar("explorer");
      }
    };
    window.addEventListener("keydown", handleGlobalKeyDown);
    return () => window.removeEventListener("keydown", handleGlobalKeyDown);
  }, []);
  const handleProjectSelect = (project: ProjectHubProject) => {
    setSelectedProjectName(project.name);
    if (!project.localPath.startsWith("Choose")) {
      setExplorerRoot(project.localPath);
    }
  };
  const handleResumeProjectSession = (
    sessionId: string,
    projectName: string,
    shouldRetry: boolean
  ) => {
    setHiveSessionId(sessionId);
    setHiveProjectName(projectName || selectedProjectName);
    setHiveAutoRun(false);
    setHiveAutoRetry(shouldRetry);
    setShowProjectLibrary(false);
    setActiveSidebar("hive");
  };

  const [sandboxFiles, setSandboxFiles] = useState<
    { name: string; modified: string; type: string }[]
  >([]);
  const [isDiffMode, setIsDiffMode] = useState(false);
  const [diffData, setDiffData] = useState({
    old: "# Old Implementation",
    new: "# Proposed Agent Scaffold",
  });
  const [matrixLogs, setMatrixLogs] = useState<string[]>([]);
  const statusBarErrorCount = matrixLogs.filter((l) => l.includes("[ERROR]")).length;

  // Telemetry Gauges State
  const [telemetry, setTelemetry] = useState<any>({});

  // Rust telemetry bridge —" via extracted hook
  useMoaTelemetry({
    setMatrixLogs,
    setCompilerWarning,
    setGeneratedFile,
    setRetryCount,
    setAgentStatus,
  });

  // Viewport Lock
  useEffect(() => {
    const handleResize = () => setIsMobile(window.innerWidth < 768);
    handleResize();
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  // Command palette keyboard shortcut
  useEffect(() => {
    const handler = (e: KeyboardEvent) => {
      if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key === "P") {
        e.preventDefault();
        setShowPalette((v) => !v);
      }
      if ((e.ctrlKey || e.metaKey) && e.key === "k") {
        e.preventDefault();
        setShowPalette((v) => !v);
      }
    };
    window.addEventListener("keydown", handler);
    return () => window.removeEventListener("keydown", handler);
  }, []);

  // Session Hydration
  useEffect(() => {
    const savedTabs = localStorage.getItem("activeTabs");
    if (savedTabs) setActiveTabs(JSON.parse(savedTabs));
    else setActiveTabs(["main.py", "page.tsx"]);

    const savedTab = localStorage.getItem("currentTab");
    if (savedTab) setCurrentTab(savedTab);
    else setCurrentTab("main.py");

    const savedCtx = localStorage.getItem("activeContexts");
    if (savedCtx) setActiveContexts(JSON.parse(savedCtx));
    else setActiveContexts(["main.py"]);

    const refreshRegistry = () => {
      getModelsRegistry()
        .then((data) => {
          if (data && data.tiers) {
            let mergedTiers = data.tiers;
            try {
              const installedAddons = readInstalledAddonIds(localStorage);
              const installedLlms = ADDONS.filter(
                (a) => a.category === "llm" && (installedAddons.has(a.id) || a.status === "builtin")
              );

              if (installedLlms.length > 0) {
                const cloudTier = {
                  tier_id: "addons",
                  title: "Providers & Tools",
                  color: "text-violet-400",
                  models: installedLlms.map((a) => ({
                    id: a.id,
                    name: a.name,
                    desc: a.description,
                    context_window: 128000,
                  })),
                };
                mergedTiers = [cloudTier, ...mergedTiers];
              }
            } catch (e) {
              console.error("Failed to parse addons", e);
            }
            setModelTiers(mergedTiers);
            setTandemPresets(data.tandem_presets || []);
          }
        })
        .catch((e) => showError(`Failed to load model registry: ${e}`));

      if (isTauri()) {
        invokeSafe<
          {
            id: string;
            name: string;
            size_gb: number;
            param_size: string;
            quantization: string;
            is_determinex: boolean;
          }[]
        >("get_ollama_models")
          .then((models) => {
            if (!models) return;
            const determinexModels = models.filter((m) => m.is_determinex);
            const otherModels = models.filter((m) => !m.is_determinex);
            const tiers = [];
            if (determinexModels.length > 0) {
              tiers.push({
                tier_id: "determinex",
                title: "Determinex Fine-tuned",
                color: "text-emerald-400",
                models: determinexModels.map((m) => ({
                  id: `ollama/${m.id}`,
                  name: displayModelName(m.name),
                  desc: `${m.param_size} · ${m.quantization} · ${m.size_gb.toFixed(1)}GB`,
                  context_window: 4096,
                })),
              });
            }
            if (otherModels.length > 0) {
              tiers.push({
                tier_id: "local",
                title: "Local (Ollama)",
                color: "text-blue-400",
                models: otherModels.map((m) => ({
                  id: `ollama/${m.id}`,
                  name: displayModelName(m.name),
                  desc: `${m.param_size} · ${m.quantization} · ${m.size_gb.toFixed(1)}GB`,
                  context_window: 4096,
                })),
              });
            }
            if (tiers.length > 0) setModelTiers(tiers);
          })
          .catch((e) => showError(`Failed to load Ollama models: ${e}`));
      }

      getWorkspaceFiles()
        .then((data) => setSandboxFiles(data.files || []))
        .catch((e) => showError(`Failed to load workspace files: ${e}`));
      getThreads()
        .then((data) => {
          const fetched = data.threads || [];
          setThreadHistory(fetched);
          if (activeThreadId === "" && fetched.length > 0) setActiveThreadId(fetched[0].id);
        })
        .catch((e) => showError(`Failed to load threads: ${e}`));
      if (activeThreadId) {
        fetchTodos(activeThreadId)
          .then((data) => setTodos(data.todos || []))
          .catch((e) => showError(`Failed to load todos: ${e}`));
      }
    };

    refreshRegistry();

    const handleAddonsUpdated = () => refreshRegistry();
    window.addEventListener(ADDONS_UPDATED_EVENT, handleAddonsUpdated);
    
    return () => {
      window.removeEventListener(ADDONS_UPDATED_EVENT, handleAddonsUpdated);
    };
  }, []);

  useEffect(() => {
    if (activeThreadId) {
      fetchTodos(activeThreadId)
        .then((data) => setTodos(data.todos || []))
        .catch((e) => showError(`Failed to load todos: ${e}`));
    } else {
      setTodos([]);
    }
  }, [activeThreadId]);

  useEffect(() => {
    if (activeTabs.length > 0) localStorage.setItem("activeTabs", JSON.stringify(activeTabs));
    if (currentTab) localStorage.setItem("currentTab", currentTab);
    if (activeContexts.length > 0)
      localStorage.setItem("activeContexts", JSON.stringify(activeContexts));
  }, [activeTabs, currentTab, activeContexts]);

  // Poll health telemetry —" paused when window is hidden to avoid hammering backend
  useEffect(() => {
    if (!isTauri()) return;
    const poll = () => {
      if (document.visibilityState !== "hidden") {
        getHealthTelemetry()
          .then((res) => setTelemetry(res))
          .catch((e) => showError(`Health telemetry failed: ${e}`));
      }
    };
    const interval = setInterval(poll, 15000);
    return () => clearInterval(interval);
  }, []);

  const handleInject = async (text?: string) => {
    if (isExecutingPack) return;
    const content = text || inputVal.trim();
    if (!content) return;
    if (!text) setInputVal("");
    setMatrixLogs((prev) => [...prev, `[USER] ${content}`]);

    if (isTauri()) {
      const threadId = activeThreadId || `thread-${Date.now()}`;
      setIsExecutingPack(true);
      setDeterminexPhase("execution");
      setRetryCount(0);
      setGeneratedFile(null);
      setCompilerWarning(null);
      setAgentStatus({
        currentAgent: null,
        isExecuting: true,
        verdict: null,
        confidence: null,
        accepted: null,
        error: null,
      });

      try {
        const result = await nativeOrchestratePlan(content, threadId, selectedModel);
        const verdict = result.audit.verdict ?? null;
        const confidence = result.audit.confidence ?? null;
        const accepted = result.accepted ?? false;
        const firstFile: string | null = accepted ? (result.code.files_affected[0] ?? null) : null;
        setGeneratedFile(firstFile);
        if (firstFile) {
          invokeSafe<string>("read_workspace_file", { relativePath: firstFile })
            .then((code) => {
              if (code) setDiffData((d) => ({ ...d, new: code }));
            })
            .catch((e) => showError(`Failed to read generated file: ${e}`));
        }
        setAgentStatus({
          currentAgent: null,
          isExecuting: false,
          verdict,
          confidence,
          accepted,
          error: null,
        });
        setMatrixLogs((prev) => [
          ...prev,
          `[OBSERVER] Verdict: ${verdict} (confidence: ${((confidence ?? 0) * 100).toFixed(0)}%)`,
          accepted
            ? `[DETERMINEX] PASS Pipeline ACCEPTED. Check the Output panel for the generated file.`
            : `[DETERMINEX] FAIL Pipeline REJECTED. Observer audit failed - see issues above.`,
        ]);
        setTimeout(() => {
          getThreads()
            .then((data) => {
              const fetched = data.threads || [];
              setThreadHistory(fetched);
              if (!activeThreadId && fetched.length > 0) setActiveThreadId(fetched[0].id);
            })
            .catch((e) => showError(`Failed to refresh threads: ${e}`));
        }, 1500);
      } catch (e: any) {
        const stage = e?.stage ?? "Unknown";
        const message = e?.message ?? String(e);
        setAgentStatus({
          currentAgent: null,
          isExecuting: false,
          verdict: null,
          confidence: null,
          accepted: null,
          error: { stage, message },
        });
        setMatrixLogs((prev) => [...prev, `[ERROR][${stage}] MoA pipeline aborted: ${message}`]);
      } finally {
        setIsExecutingPack(false);
      }
    } else {
      try {
        await injectSandboxContext(
          content,
          activeThreadId || "default",
          activeContexts,
          selectedModel
        );
        setTimeout(() => {
          getThreads()
            .then((data) => {
              const fetched = data.threads || [];
              setThreadHistory(fetched);
              if (!activeThreadId && fetched.length > 0) setActiveThreadId(fetched[0].id);
            })
            .catch((e) => showError(`Failed to refresh threads: ${e}`));
        }, 3000);
      } catch (e) {
        setMatrixLogs((prev) => [...prev, `[ERROR] Failed to hit backend: ${e}`]);
      }
    }
  };

  const executeAbort = async () => {
    try {
      await abortOrchestration();
      setIsExecutingPack(false);
      setAgentStatus({
        currentAgent: null,
        isExecuting: false,
        verdict: null,
        confidence: null,
        accepted: null,
        error: null,
      });
      setMatrixLogs((prev) => [...prev, `[SYSTEM] ABORT INTERRUPT FIRED. Actor loop draining.`]);
    } catch (e) {
      setMatrixLogs((prev) => [
        ...prev,
        `[SYSTEM] Abort signal sent (channel may already be closed).`,
      ]);
    }
  };

  const handlePromoteToGarden = async (threadId: string, history: string) => {
    try {
      setDeterminexPhase("execution");
      setMatrixLogs((prev) => [
        ...prev,
        `[SYSTEM] Promoting Thread ${threadId} through native MoA pipeline...`,
      ]);
      if (isTauri()) {
        setIsExecutingPack(true);
        setAgentStatus({
          currentAgent: "sentinel",
          isExecuting: true,
          verdict: null,
          confidence: null,
          accepted: null,
          error: null,
        });
        const result = await nativeOrchestratePlan(history, threadId, selectedModel);
        setAgentStatus({
          currentAgent: null,
          isExecuting: false,
          verdict: result.audit.verdict ?? null,
          confidence: result.audit.confidence ?? null,
          accepted: result.accepted ?? false,
          error: null,
        });
        setIsExecutingPack(false);
      } else {
        await promoteToGarden(threadId, history, selectedModel);
      }
    } catch (e) {
      setMatrixLogs((prev) => [...prev, `[ERROR] Failed to promote: ${e}`]);
      setIsExecutingPack(false);
    }
  };

  const handleUnleash = async () => {
    const payload = inputVal.trim();
    if (!payload) return;
    setLastPrompt(payload);
    setInputVal("");
    await handleInject(payload);
  };

  const HelpBtn = ({ title, desc }: { title: string; desc: string }) => (
    <button
      onClick={(e) => {
        e.stopPropagation();
        setHelpModal({ title, desc });
      }}
      className="ml-2 text-cyan-500/50 hover:text-cyan-400 hover:scale-110 transition-all focus:outline-none"
    >
      <HelpCircle size={14} />
    </button>
  );

  // -------------------------------------------------------------
  // COMMAND PALETTE COMMANDS
  // -------------------------------------------------------------
  const paletteCommands: PaletteCommand[] = [
    { id:"go-home",      label:"Go to Home",          description:"Project hub and overview",         category:"Navigation", icon:Globe,         action:() => setActiveSidebar("hub")       },
    { id:"go-work",      label:"Open Work",           description:"Hive sessions and model routing",  category:"Navigation", icon:Zap,           shortcut:"Ctrl+5", action:() => handleSidebarLaunch("hive")      },
    { id:"go-pipeline",  label:"Open Pipeline",       description:"Build pipeline and architect",     category:"Navigation", icon:Activity,      action:() => handleSidebarLaunch("pipeline")  },
    { id:"go-explorer",  label:"Open Workspace",      description:"File explorer and project view",   category:"Navigation", icon:FolderOpen,    action:() => handleSidebarLaunch("explorer")  },
    { id:"go-brain",     label:"Open Brain",          description:"Benchmarks and model telemetry",   category:"Navigation", icon:Brain,         action:() => handleSidebarLaunch("benchmark") },
    { id:"go-terminal",  label:"Attach Terminal",     description:"Attach terminal to the current workspace", category:"Add-ons", icon:TerminalIcon,  shortcut:"Ctrl+`", action:() => handleAddonLaunch("terminal")  },
    { id:"go-editor",    label:"Attach Code Editor",  description:"Attach Monaco editor to the current workspace", category:"Add-ons", icon:Code2,         action:() => handleAddonLaunch("editor")    },
    { id:"go-idea",      label:"Attach Idea Lab",      description:"Attach governed idea to oracle to verified program flow", category:"Add-ons", icon:Zap, action:() => handleAddonLaunch("idea") },
    { id:"go-health",    label:"Attach Health Map",   description:"Attach oracle health and file status", category:"Add-ons", icon:LayoutGrid,    action:() => handleAddonLaunch("health")    },
    { id:"go-search",    label:"Attach Verified Search",description:"Attach oracle-verified search",  category:"Add-ons", icon:Search,        action:() => handleAddonLaunch("search")    },
    { id:"go-findfiles", label:"Find in Files",       description:"Literal, gitignore-aware text search across the workspace", category:"Add-ons", icon:FileSearch, shortcut:"Ctrl+Shift+F", action:() => handleAddonLaunch("findfiles") },
    { id:"go-trace",     label:"Attach Agent Trace",  description:"Attach WAL replay and session history",   category:"Add-ons", icon:GitBranch,     action:() => handleAddonLaunch("trace")     },
    { id:"go-cloak",     label:"Attach Privacy Cockpit",description:"Attach Project Cloak obfuscation map",    category:"Add-ons", icon:Lock,          action:() => handleAddonLaunch("cloak")     },
    { id:"go-flywheel",  label:"Attach Flywheel",     description:"Attach live training corpus feed",        category:"Add-ons", icon:RefreshCcw,    action:() => handleAddonLaunch("flywheel")  },
    { id:"go-mission",   label:"Attach Mission Control",description:"Attach interactive guide, release gates, runbooks, and proof boundaries", category:"Add-ons", icon:GraduationCap, action:() => handleAddonLaunch("mission")   },
    { id:"go-roadmap",   label:"Attach IDE Roadmap",  description:"Attach Determinex successor roadmap and release blockers", category:"Add-ons", icon:ShieldCheck, action:() => handleAddonLaunch("roadmap")   },
    { id:"go-tools",     label:"Open Tools",          description:"Installed tools, model providers, connectors, and attached panes",category:"Navigation",icon:Package,       action:() => setActiveSidebar("extensions")     },
    { id:"go-build",     label:"Attach Build Center", description:"Attach tasks, tests, output, deps, env, CI/CD", category:"Add-ons", icon:Gauge,        action:() => handleAddonLaunch("build")     },
    { id:"go-proof",     label:"Open Proof",          description:"Project verdicts, builds, logs, diffs, and release gates", category:"Navigation", icon:Eye,           action:() => handleSidebarLaunch("proof")     },
    { id:"go-guide",     label:"Open Guide",          description:"Interactive IDE guided tour",       category:"Navigation", icon:GraduationCap, action:() => setShowTeacher(true)            },
    { id:"settings",     label:"Open Settings",       description:"All settings",                     category:"Settings",   icon:Settings,      action:() => { setSettingsTab("keys"); setShowSettings(true); }  },
    { id:"settings-keys",label:"API Keys",            description:"Manage provider credentials",      category:"Settings",   icon:Key,           action:() => { setSettingsTab("keys"); setShowSettings(true); }  },
    { id:"settings-skin",label:"Appearance",          description:"Skin packs and accent color",      category:"Settings",   icon:Palette,       action:() => { setSettingsTab("skin"); setShowSettings(true); }  },
  ];

  const primaryRailItems: {
    id: PrimaryWorkspace;
    testId: string;
    label: string;
    title: string;
    icon: typeof Zap;
    activeClass: string;
    inactiveClass: string;
    onClick: () => void;
  }[] = [
    { id: "hive", testId: "rail-work", label: "Work", title: "Work (Cmd/Ctrl+2)", icon: Zap,
      activeClass: "text-emerald-400 scale-110 drop-shadow-[0_0_8px_rgba(52,211,153,0.8)]",
      inactiveClass: "text-gray-500 hover:text-emerald-400", onClick: () => handleSidebarLaunch("hive") },
    { id: "explorer", testId: "rail-space", label: "Space", title: "Space (Cmd/Ctrl+3)", icon: Folder,
      activeClass: "text-purple-400 scale-110 drop-shadow-[0_0_8px_rgba(168,85,247,0.8)]",
      inactiveClass: "text-gray-500 hover:text-purple-400", onClick: () => openWorkspace("overview") },
    { id: "command", testId: "rail-command", label: "Cmd", title: "Command Center", icon: Activity,
      activeClass: "text-blue-400 scale-110 drop-shadow-[0_0_8px_rgba(59,130,246,0.8)]",
      inactiveClass: "text-gray-500 hover:text-blue-400", onClick: () => handleSidebarLaunch("command") },
    { id: "benchmark", testId: "rail-brain", label: "Brain", title: "Brain", icon: Database,
      activeClass: "text-orange-400 scale-110 drop-shadow-[0_0_8px_rgba(251,146,60,0.8)]",
      inactiveClass: "text-gray-500 hover:text-orange-400", onClick: () => handleProjectHubNavigate("brain") },
    { id: "proof", testId: "rail-proof", label: "Proof", title: "Proof", icon: Eye,
      activeClass: "text-cyan-400 scale-110 drop-shadow-[0_0_8px_rgba(34,211,238,0.8)]",
      inactiveClass: "text-gray-500 hover:text-cyan-400", onClick: () => handleSidebarLaunch("proof") },
    { id: "audit", testId: "rail-audit", label: "Audit", title: "Project Audit Scorecard", icon: ShieldCheck,
      activeClass: "text-red-400 scale-110 drop-shadow-[0_0_8px_rgba(239,68,68,0.8)]",
      inactiveClass: "text-gray-500 hover:text-red-400", onClick: () => handleSidebarLaunch("audit") },
  ];

  const addonItems: AddonItem[] = [
    { id: "terminal", label: "Terminal", description: "Run commands beside the active screen.", icon: TerminalIcon, tone: "text-emerald-400", panel: <TerminalPanel workspacePath={explorerRoot} /> },
    { id: "idea", label: "Idea Lab", description: "Preview sound oracles and build verified programs.", icon: Zap, tone: "text-cyan-400", panel: <GovernedIdeaCommandPanel selectedModel={selectedModel} keyStatus={keyStatus} /> },
    { id: "editor", label: "Code", description: "Inspect generated code and source files.", icon: Code2, tone: "text-blue-400", panel: <EditorPanel /> },
    { id: "search", label: "Verified Search", description: "Find verified snippets and project context.", icon: Search, tone: "text-blue-400", panel: <VerifiedSearch /> },
    { id: "findfiles", label: "Find in Files", description: "Literal, gitignore-aware text search across the workspace.", icon: FileSearch, tone: "text-blue-400", panel: <FileSearchPanel workspacePath={explorerRoot} /> },
    { id: "build", label: "Build", description: "Tasks, tests, problems, output, deps, env, and artifacts.", icon: Gauge, tone: "text-orange-400", panel: <BuildCenter /> },
    { id: "trace", label: "Trace", description: "Worker timeline, WAL replay, and session events.", icon: GitBranch, tone: "text-violet-400", panel: <AgentTrace /> },
    { id: "health", label: "Health", description: "Oracle health, file status, and system readiness.", icon: LayoutGrid, tone: "text-teal-400", panel: <HealthMap /> },
    { id: "cloak", label: "Cloak", description: "Privacy and context-boundary map.", icon: Lock, tone: "text-emerald-400", panel: <PrivacyCockpit /> },
    { id: "flywheel", label: "Flywheel", description: "Training corpus and feedback feed.", icon: RefreshCcw, tone: "text-amber-400", panel: <FlywheelFeed /> },
    { id: "execution", label: "Runtime", description: "Run tasks, agents, and local processes for the active workspace.", icon: Cpu, tone: "text-rose-400", panel: <ExecutionWorkspace /> },
    { id: "mission", label: "Mission", description: "Interactive guide for release gates, proof runbooks, and next actions.", icon: GraduationCap, tone: "text-emerald-400", panel: <MissionControlPanel /> },
    { id: "roadmap", label: "Roadmap", description: "Determinex successor direction, exact blockers, and release locks.", icon: ShieldCheck, tone: "text-cyan-400", panel: <SuccessorRoadmapPanel /> },
    { id: "problems", label: "Problems", description: "Audit blockers and LSP diagnostics.", icon: XOctagon, tone: "text-red-400", panel: <ProblemsPanel /> },
    { id: "review", label: "Review", description: "Review and apply AI-proposed diffs.", icon: GitPullRequest, tone: "text-purple-400", panel: <DiffReviewPanel /> },
  ];
  const selectedAddon = addonItems.find((item) => item.id === activeAddon) ?? null;
  const runtimeAddonIds: WorkspaceAddon[] = ["idea", "mission", "terminal", "editor", "build", "execution", "trace", "search", "findfiles", "health", "roadmap", "problems", "review"];
  const runtimeAddonItems = runtimeAddonIds
    .map((id) => addonItems.find((item) => item.id === id))
    .filter((item): item is AddonItem => Boolean(item));
  const addonHeightClass =
    addonDockSize === "large"
      ? "h-[520px] max-h-[56vh] min-h-[360px]"
      : addonDockSize === "compact"
        ? "h-[240px] max-h-[34vh] min-h-[210px]"
        : "h-[360px] max-h-[46vh] min-h-[290px]";
  const addonWidthClass =
    addonDockSize === "large"
      ? "w-[min(760px,44vw)] min-w-[520px]"
      : addonDockSize === "compact"
        ? "w-[min(420px,30vw)] min-w-[360px]"
        : "w-[min(600px,38vw)] min-w-[440px]";

  useEffect(() => {
    window.__DETERMINEX_UI_SNAPSHOT__ = () => ({
      app: "Determinex",
      activeWorkspace: activeSidebar,
      activeAddon: addonDockOpen ? activeAddon : null,
      addonDockOpen,
      addonDockMode,
      addonDockSize,
      selectedProjectName,
      workspacePath: explorerRoot,
      hiveSessionId,
      selectedModel,
      networkPolicy,
      panels: {
        projectLibrary: showProjectLibrary,
        settings: showSettings,
        help: helpModal !== null,
      },
      viewport: {
        width: window.innerWidth,
        height: window.innerHeight,
      },
      timestamp: new Date().toISOString(),
    });

    return () => {
      delete window.__DETERMINEX_UI_SNAPSHOT__;
    };
  }, [
    activeAddon,
    activeSidebar,
    addonDockOpen,
    addonDockMode,
    addonDockSize,
    explorerRoot,
    hiveSessionId,
    selectedModel,
    networkPolicy,
    selectedProjectName,
    helpModal,
    showProjectLibrary,
    showSettings,
  ]);

  // -------------------------------------------------------------
  // DESKTOP LUXURY VIEW
  // -------------------------------------------------------------
  const renderDesktopView = () => (
    <div
      className="relative z-10 flex h-full w-full overflow-hidden p-4 pb-9 font-sans"
      style={{
        background: `radial-gradient(circle at 16% 12%, ${themePack.colors.accentGlow}, transparent 28%), radial-gradient(circle at 88% 10%, ${themePack.colors.border}, transparent 24%), var(--determinex-bg)`,
        color: "var(--determinex-text)",
      }}
    >
      <SkinBackdrop />

      <div className="flex h-full w-full gap-4 relative z-10 pt-1">
        {/* Activity Bar */}
        <div
          className="flex h-full w-[72px] shrink-0 flex-col items-center border-r pt-6 pb-4 backdrop-blur-3xl z-50 transition-all duration-500 ease-out"
          style={{
            background: "linear-gradient(180deg, var(--determinex-panel-glass) 0%, rgba(0,0,0,0.4) 100%)",
            borderColor: "var(--determinex-border)",
            boxShadow: "10px 0 40px rgba(0,0,0,0.6)",
            borderTopRightRadius: "var(--determinex-radius)",
            borderBottomRightRadius: "var(--determinex-radius)",
          }}
        >
          {/* Logo (fixed top) */}
          <button
            type="button"
            onClick={openProjectHub}
            data-testid="rail-project-hub"
            title="Project Hub (Cmd/Ctrl+1)"
            className={`mb-4 h-12 w-12 shrink-0 overflow-hidden border-2 transition-all duration-500 ${
              activeSidebar === "hub" ? "scale-110 shadow-[0_0_25px_var(--determinex-accent)]" : "hover:scale-105 hover:shadow-[0_0_15px_var(--determinex-accent-glow)]"
            }`}
            style={{ borderColor: "var(--determinex-border)", borderRadius: "var(--determinex-radius)" }}
          >
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img src="/determinex-icon.jpg" alt="Determinex" className="h-full w-full object-cover mix-blend-screen" />
          </button>

          {/* Scrollable nav section */}
          <div className="flex-1 overflow-y-auto no-scrollbar flex flex-col items-center gap-4 w-full py-1">
            {/* Primary panels -- one data-driven list instead of 6 hand-copied
                blocks, so adding/reordering a destination is a one-line change
                and every entry is guaranteed the same interaction pattern. */}
            {primaryRailItems.map(({ id, testId, label, title, icon: Icon, activeClass, inactiveClass, onClick }) => (
              <div
                key={id}
                data-testid={testId}
                onClick={onClick}
                title={title}
                className={`cursor-pointer transition-all flex flex-col items-center gap-1 ${
                  activeSidebar === id ? activeClass : inactiveClass
                }`}
              >
                <Icon size={19} strokeWidth={1.5} />
                <span className="text-[7px] uppercase font-bold leading-none">{label}</span>
              </div>
            ))}

            <div className="w-8 h-px bg-white/10 shrink-0" />

            <button
              type="button"
              onClick={() => {
                setActiveSidebar(activeSidebar === "extensions" ? "hub" : "extensions");
                closeAddon();
              }}
              data-testid="rail-tools"
              className={`cursor-pointer transition-all flex flex-col items-center gap-1 ${activeSidebar === "extensions" ? "text-pink-400 drop-shadow-[0_0_8px_rgba(244,114,182,0.8)] scale-110" : "text-gray-500 hover:text-pink-400"}`}
              title="Tools, providers, extensions, and attached panes"
            >
              <Package size={20} strokeWidth={1.5} />
              <span className="text-[7px] uppercase font-bold tracking-normal leading-none">
                Tools
              </span>
            </button>
          </div>

          {/* Fixed bottom */}
          <div className="flex flex-col items-center gap-4 w-full pb-2 shrink-0">
            <div className="w-8 h-px bg-[#30363d] flex-shrink-0 mb-1" />
            {isExecutingPack && (
              <div
                onClick={executeAbort}
                className="cursor-pointer transition-all flex flex-col items-center gap-1 text-red-500 hover:text-red-400 animate-pulse drop-shadow-[0_0_8px_rgba(239,68,68,0.8)]"
                title="Abort Orchestration"
              >
                <XOctagon size={20} strokeWidth={1.5} />
                <span className="text-[7px] uppercase font-bold tracking-normal leading-none">
                  Abort
                </span>
              </div>
            )}
            <button
              type="button"
              onClick={() => {
                setNetworkPolicy(nextPrivacyPolicy);
                if (nextPrivacyPolicy === "cloaked") handleAddonLaunch("cloak");
              }}
              data-testid="rail-cloak-policy-toggle"
              title={`${networkPolicyCopy.label}: ${networkPolicyCopy.summary}. Click to switch to ${NETWORK_POLICY_COPY[nextPrivacyPolicy].shortLabel}.`}
              className={`flex flex-col items-center gap-1 transition-all ${
                networkPolicy === "offline"
                  ? "text-amber-400 hover:text-emerald-300"
                  : networkPolicy === "cloaked"
                    ? "text-emerald-400 hover:text-amber-300"
                    : "text-cyan-400 hover:text-emerald-300"
              }`}
            >
              <Lock size={20} strokeWidth={1.5} />
              <span className="text-[7px] font-bold uppercase leading-none tracking-normal">
                {networkPolicy === "offline" ? "Local" : "Cloak"}
              </span>
            </button>
            <button
              type="button"
              onClick={() => { setSettingsTab("skin"); setShowSettings(true); }}
              title={`Skin: ${themePack.label ?? "Switch skin"}`}
              className="flex flex-col items-center gap-1 group"
            >
              <span
                className="h-4 w-4 rounded-full border-2 transition-all duration-300 group-hover:scale-125"
                style={{
                  background: themePack.colors.accent,
                  borderColor: themePack.colors.border,
                  boxShadow: `0 0 8px ${themePack.colors.accentGlow}`,
                }}
              />
              <span className="text-[7px] font-bold uppercase leading-none tracking-normal text-gray-600 group-hover:text-gray-400">
                Skin
              </span>
            </button>
            <div
              onClick={() => setShowTeacher(true)}
              className="cursor-pointer flex flex-col items-center gap-1 text-gray-600 hover:text-[var(--determinex-accent)] transition-colors"
              title="Open Guide"
            >
              <GraduationCap size={20} strokeWidth={1.5} />
              <span className="text-[7px] uppercase font-bold tracking-normal leading-none">Guide</span>
            </div>
            {bootTier && (
              <div
                className="w-full px-1 py-1 rounded-lg border border-cyan-500/20 bg-cyan-950/20 flex flex-col items-center gap-0.5"
                title={bootTier}
              >
                <span className="text-[6px] font-mono text-cyan-400/50 uppercase leading-none">
                  {bootTier.match(/engineer=([^\s|]+)/)?.[1]?.split(":")[0] ?? "OK"}
                </span>
              </div>
            )}
          </div>
        </div>

        {/* Zone 1: Left Brain */}
        <AnimatePresence mode="wait">
        {activeSidebar !== "none" && activeSidebar !== "hub" && activeSidebar !== "extensions" && (
          <motion.div
            key={activeSidebar}
            initial={{ opacity: 0, x: -20, scale: 0.98 }}
            animate={{ opacity: 1, x: 0, scale: 1 }}
            exit={{ opacity: 0, x: -20, scale: 0.98 }}
            transition={{ type: "spring", stiffness: 300, damping: 30, mass: 0.75 }}
            className={`${activeSidebar === "hive" ? "w-[460px]" : activeSidebar === "git" ? "w-[760px]" : activeSidebar === "benchmark" ? "w-[400px]" : "w-[380px]"} flex h-full shrink-0 flex-col border backdrop-blur-2xl`}
            style={{
              background: "var(--determinex-panel-glass)",
              borderColor: "var(--determinex-border)",
              borderRadius: "var(--determinex-radius)",
              boxShadow: "0 0 30px rgba(0,0,0,0.6)",
            }}
          >
            <div className="px-5 py-3 border-b border-[#30363d] bg-[#161b22]/50 rounded-t-2xl flex-shrink-0 flex items-center justify-between">
              <span className="text-[11px] uppercase text-gray-300 font-black tracking-widest flex items-center gap-2 drop-shadow-md">
                {activeSidebar === "ideation" && (
                  <>
                    <HelpCircle size={13} className="text-cyan-400" /> Concept Lab
                  </>
                )}
                {activeSidebar === "pipeline" && (
                  <>
                    <Activity size={13} className="text-amber-500" /> Build Pipeline
                  </>
                )}
                {activeSidebar === "explorer" && (
                  <>
                    <Folder size={13} className="text-purple-400" /> Workspace
                  </>
                )}
                {activeSidebar === "git" && (
                  <>
                    <GitPullRequest size={13} className="text-green-400" /> Source
                  </>
                )}
                {activeSidebar === "hive" && (
                  <>
                    <Zap size={13} className="text-emerald-400" /> Work
                  </>
                )}
                {activeSidebar === "benchmark" && (
                  <>
                    <Database size={13} className="text-orange-400" /> Brain
                  </>
                )}
                {activeSidebar === "proof" && (
                  <>
                    <Eye size={13} className="text-cyan-400" /> Proof
                  </>
                )}
                {activeSidebar === "audit" && (
                  <>
                    <ShieldCheck size={13} className="text-red-400" /> Audit
                  </>
                )}
              </span>
              <button
                onClick={() => {
                  setActiveSidebar("none");
                  setPreviewedPath(null);
                }}
                className="text-gray-600 hover:text-gray-300 transition-colors p-1 rounded hover:bg-white/5"
                title="Close panel"
              >
                <span className="text-[14px] leading-none">✕</span>
              </button>
            </div>

            <div className="flex-1 overflow-y-auto no-scrollbar relative flex flex-col">
              {activeSidebar === "ideation" && (
                <IdeationBoard
                  readinessScore={readinessScore}
                  setReadinessScore={setReadinessScore}
                  activeThreadId={activeThreadId || ""}
                  setActiveThreadId={setActiveThreadId}
                  threadHistory={threadHistory}
                  handlePromote={handlePromoteToGarden}
                  todos={todos}
                  setTodos={setTodos}
                />
              )}

              {activeSidebar === "pipeline" && (
                <PipelineDashboard
                  showWarRoom={showWarRoom}
                  setShowWarRoom={setShowWarRoom}
                  lastPrompt={lastPrompt}
                  sessionId={hiveSessionId}
                />
              )}

              {activeSidebar === "explorer" && (
                <div className="flex flex-col h-full">
                  <div className="p-4 bg-purple-950/20 border-b border-[#30363d] relative flex-shrink-0 flex justify-between items-start">
                    <div>
                      <h3 className="text-[10px] uppercase font-bold text-purple-400 mb-2 tracking-widest flex items-center gap-2">
                        Project Map
                      </h3>
                      <p className="text-[10px] text-purple-300/60 leading-relaxed font-mono">
                        Bound files, source state, scan actions, and runs for this project.
                      </p>
                    </div>
                    <button
                      onClick={() => {
                        getFileSystemTree(explorerRoot)
                          .then((res) => {
                            if (res && res.tree) setFileTree(res.tree);
                          })
                          .catch((err) => showError(`Could not load file system: ${err}`));
                      }}
                      className="p-1.5 border border-purple-500/20 bg-purple-900/20 hover:bg-purple-900/60 text-purple-400 rounded-lg transition-colors cursor-pointer"
                      title="Refresh File System"
                    >
                      <RefreshCw size={14} />
                    </button>
                  </div>
                  <div className="grid grid-cols-4 gap-1.5 border-b border-[#30363d] bg-[#010409] p-2">
                    {[
                      ["overview", "Overview", Gauge],
                      ["files", "Files", Files],
                      ["source", "Source", GitPullRequest],
                      ["runs", "Runs", Activity],
                    ].map(([id, label, Icon]) => {
                      const TabIcon = Icon as typeof Gauge;
                      return (
                        <button
                          key={id as string}
                          type="button"
                          data-testid={`workspace-tab-${id as string}`}
                          onClick={() => setWorkspaceView(id as typeof workspaceView)}
                          className={`flex items-center justify-center gap-1 rounded-md border px-1.5 py-1.5 text-[8px] font-black uppercase tracking-widest transition ${
                            workspaceView === id
                              ? "border-purple-400/50 bg-purple-500/15 text-purple-200"
                              : "border-white/10 bg-white/[0.025] text-gray-600 hover:text-gray-300"
                          }`}
                        >
                          <TabIcon size={10} /> {label as string}
                        </button>
                      );
                    })}
                  </div>
                  <div className="flex-1 overflow-y-auto w-full p-4 flex flex-col h-full bg-[#010409]">
                    {workspaceView === "overview" && (
                      <div className="space-y-3">
                        <div className="rounded-lg border border-purple-500/20 bg-purple-950/20 p-3">
                          <div className="text-[10px] font-black uppercase tracking-widest text-purple-300">
                            {selectedProjectName}
                          </div>
                          <div className="mt-2 font-mono text-[10px] text-gray-500">
                            {displayPath(explorerRoot) || "No workspace path bound yet."}
                          </div>
                        </div>
                        {[
                          ["Inspect files", "Browse the project tree and generated output files.", "files"],
                          ["Review source", "See Git remote, branch, dirty state, and staged intent.", "source"],
                          ["Check runs", "Open a run log or jump to the Work tab to start a session.", "runs"],
                        ].map(([title, text, target]) => (
                          <button
                            key={title}
                            type="button"
                            data-testid={`workspace-action-${target as string}`}
                            onClick={() => setWorkspaceView(target as typeof workspaceView)}
                            className="group w-full rounded-lg border border-white/10 bg-white/[0.03] p-3 text-left transition hover:border-purple-400/50 hover:bg-purple-500/10"
                          >
                            <div className="flex items-center justify-between gap-2">
                              <span className="text-[11px] font-black uppercase tracking-widest text-gray-200">
                                {title}
                              </span>
                              <ChevronRight size={12} className="text-gray-600 group-hover:text-purple-300" />
                            </div>
                            <p className="mt-1 text-[10px] leading-relaxed text-gray-500">{text}</p>
                          </button>
                        ))}
                      </div>
                    )}

                    {workspaceView === "files" && (
                      <>
                    {explorerRoot !== "" && (
                      <div
                        onClick={() => setExplorerRoot("")}
                        className="flex items-center gap-1 text-[11px] font-bold text-cyan-400 hover:bg-[#2A2D2E] p-1.5 mb-2 cursor-pointer bg-cyan-950/20 border border-cyan-500/20 rounded"
                      >
                        <span className="mr-1">&lt; Back</span>
                        <span className="text-gray-400 capitalize opacity-70">to Root</span>
                      </div>
                    )}
                    <div
                      onClick={() => setExplorerRoot("")}
                      className="flex items-center gap-1 text-[11px] font-bold text-gray-300 hover:bg-[#2A2D2E] p-1 mb-1 cursor-pointer"
                    >
                      <ChevronRight size={14} className="rotate-90" />{" "}
                      {explorerRoot.split(/[\\/]/).pop() || "Explorer"}
                    </div>
                    {fileTree.length > 0 ? (
                      <div className="flex flex-col gap-1">
                        {fileTree.map((node, i) => (
                          <FileSystemNode
                            key={i}
                            node={node}
                            activeContexts={activeContexts}
                            toggleContext={toggleContext}
                            setExplorerRoot={setExplorerRoot}
                            handleOpenFile={handleOpenFile}
                            gitStatusMap={explorerGitStatusMap}
                            onFsError={(msg) => showError(msg)}
                          />
                        ))}
                      </div>
                    ) : (
                      <div className="text-[10px] text-gray-600 font-mono italic">
                        Scanning system...
                      </div>
                    )}
                    {sandboxFiles.length > 0 && (
                      <div className="mt-4 pt-4 border-t border-[#30363d]">
                        <div className="text-[9px] uppercase font-bold text-purple-400 tracking-widest mb-2 flex items-center gap-1.5">
                          <Code2 size={9} /> Workspace Output
                        </div>
                        {sandboxFiles.map((f, i) => (
                          <div
                            key={i}
                            onClick={() => {
                              setGeneratedFile(f.name);
                              setActiveSidebar("none");
                            }}
                            className="flex items-center justify-between py-1.5 px-2 rounded-lg hover:bg-white/5 cursor-pointer group"
                          >
                            <span className="text-[10px] font-mono text-gray-400 group-hover:text-gray-200 truncate">
                              {f.name}
                            </span>
                            <span className="text-[8px] font-mono text-gray-700 shrink-0 ml-2">
                              {f.modified}
                            </span>
                          </div>
                        ))}
                      </div>
                    )}
                      </>
                    )}

                    {workspaceView === "source" && (
                      <div className="space-y-3">
                        {[
                          ["Provider", "GitHub or local Git"],
                          ["Remote", "Connected remote appears here after read-only scan."],
                          ["Branch", "Current branch and ahead/behind belong here."],
                          ["Mutation", "Source apply stays gated until verified approval."],
                        ].map(([label, text]) => (
                          <div key={label} className="rounded-lg border border-white/10 bg-white/[0.03] p-3">
                            <div className="text-[9px] font-black uppercase tracking-widest text-green-300">
                              {label}
                            </div>
                            <p className="mt-1 text-[10px] leading-relaxed text-gray-500">{text}</p>
                          </div>
                        ))}
                        <button
                          type="button"
                          data-testid="workspace-source-view-runs"
                          onClick={() => setWorkspaceView("runs")}
                          className="w-full rounded-lg border border-green-500/30 bg-green-500/10 px-3 py-2 text-[10px] font-black uppercase tracking-widest text-green-300"
                        >
                          View runs for this source
                        </button>
                      </div>
                    )}

                    {workspaceView === "runs" && (
                      <div className="flex flex-col items-center justify-center h-full gap-3 text-center py-12">
                        <Activity size={24} className="text-gray-700" />
                        <p className="text-[11px] font-mono text-gray-600 leading-relaxed">
                          Build run history lives in <strong className="text-amber-400/70">Work</strong>.<br />
                          Open a hive session to see live output.
                        </p>
                        <button
                          type="button"
                          onClick={() => setActiveSidebar("hive")}
                          className="mt-2 rounded-lg border border-emerald-500/30 bg-emerald-950/20 px-4 py-2 text-[10px] font-black uppercase tracking-widest text-emerald-400 transition-all hover:bg-emerald-900/30"
                        >
                          Go to Work
                        </button>
                      </div>
                    )}
                  </div>
                </div>
              )}

              {activeSidebar === "git" && (
                <GitPanel workspacePath={explorerRoot} />
              )}

              {activeSidebar === "audit" && (
                <ProjectAuditPanel />
              )}

              {activeSidebar === "benchmark" && <BenchmarkRunner />}

              {activeSidebar === "proof" && (
                <div className="flex flex-col gap-3 p-4">
                  <div className={`rounded-xl border p-3 ${
                    agentStatus.verdict && agentStatus.accepted
                      ? "border-emerald-500/25 bg-emerald-950/20"
                      : agentStatus.verdict && !agentStatus.accepted
                        ? "border-red-500/25 bg-red-950/20"
                        : "border-white/8 bg-white/[0.03]"
                  }`}>
                    <div className="text-[9px] uppercase font-bold tracking-widest text-gray-600 mb-1.5">Last Verdict</div>
                    <div className={`text-xl font-black ${
                      agentStatus.verdict && agentStatus.accepted ? "text-emerald-400"
                        : agentStatus.verdict && !agentStatus.accepted ? "text-red-400"
                        : "text-gray-700"
                    }`}>
                      {agentStatus.verdict ?? "No runs yet"}
                    </div>
                    {agentStatus.confidence !== null && agentStatus.confidence !== undefined && (
                      <div className="text-[10px] text-gray-500 mt-0.5">
                        {(agentStatus.confidence * 100).toFixed(0)}% confidence · {retryCount > 0 ? `${retryCount} retries` : "first attempt"}
                      </div>
                    )}
                  </div>

                  {generatedFile && (
                    <div className="rounded-xl border border-purple-500/20 bg-purple-950/20 p-3">
                      <div className="text-[9px] uppercase font-bold tracking-widest text-purple-400 mb-1.5">Last File</div>
                      <div className="text-[11px] font-mono text-gray-300 break-all leading-relaxed">{generatedFile}</div>
                    </div>
                  )}

                  {threadHistory.length > 0 && (
                    <div>
                      <div className="text-[9px] uppercase font-bold tracking-widest text-gray-600 mb-2 mt-1">Session History</div>
                      <div className="flex flex-col gap-1.5">
                        {threadHistory.slice(0, 8).map((t) => (
                          <div
                            key={t.id}
                            onClick={() => {
                              setActiveThreadId(t.id);
                              setActiveSidebar("hive");
                            }}
                            className={`rounded-lg border p-2.5 cursor-pointer transition-colors ${
                              activeThreadId === t.id
                                ? "border-cyan-500/30 bg-cyan-950/20 text-cyan-300"
                                : "border-white/5 bg-white/[0.02] text-gray-500 hover:border-white/10 hover:text-gray-300"
                            }`}
                          >
                            <div className="text-[10px] font-bold truncate">{t.title || "Untitled session"}</div>
                            <div className="flex items-center justify-between mt-0.5">
                              <span className="text-[8px] text-gray-700">{t.updated}</span>
                              <span className="text-[8px] text-gray-600">open →</span>
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}

                  {threadHistory.length === 0 && !agentStatus.verdict && (
                    <div className="text-center py-8">
                      <Eye size={24} className="text-gray-700 mx-auto mb-3" />
                      <p className="text-[11px] text-gray-600 font-mono leading-relaxed">
                        Run a hive session to see proof, logs, diffs, and build output.
                      </p>
                    </div>
                  )}
                </div>
              )}


              {activeSidebar === "hive" && (
                <ConceptLab
                  selectedProjectName={selectedProjectName}
                  projectPath={displayPath(explorerRoot)}
                  selectedModel={selectedModel}
                  onOpenProjectLibrary={() => setShowProjectLibrary(true)}
                  onSpecChange={(s) => {
                    setHiveSpec(s);
                    setHiveProjectName(s.match(/^#\s+(.+)/m)?.[1]?.trim() ?? "");
                  }}
                  onSessionLaunched={(id) => {
                    setHiveSessionId(id);
                    setHiveAutoRun(true);
                    setHiveSpec("");
                    setActiveSidebar("none");
                    setIsOracleConsulting(false);
                  }}
                  onPathPreview={(path) => {
                    setPreviewedPath(path);
                    if (!path) setConfirmedPath(null);
                  }}
                  confirmedPath={confirmedPath}
                  onAnsweredCountChange={setOracleAnsweredCount}
                  onConsultingChange={setIsOracleConsulting}
                  externalIdea={externalIdea}
                  onColorHintsChange={setColorHints}
                />
              )}
            </div>
          </motion.div>
        )}
        </AnimatePresence>

        {/* Zone 2: Center Arena */}
        <AnimatePresence mode="wait">
        {activeSidebar !== "none" && (
        <motion.div
          key={activeSidebar + "-" + (hiveSessionId || "") + "-" + isOracleConsulting + "-" + (previewedPath ? "prev" : "") + (confirmedPath ? "conf" : "") + (hiveSpec ? "spec" : "")}
          initial={{ opacity: 0, scale: 0.98, y: 10 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          exit={{ opacity: 0, scale: 0.98, y: -10 }}
          transition={{ type: "spring", stiffness: 260, damping: 28, mass: 0.85 }}
          className={`relative flex h-full flex-1 overflow-hidden border backdrop-blur-3xl group ${
            addonDockOpen && selectedAddon && addonDockMode === "right" ? "flex-row" : "flex-col"
          }`}
          style={{
            background: "var(--determinex-panel-glass)",
            borderColor: "var(--determinex-border)",
            borderRadius: "var(--determinex-radius)",
            boxShadow: "var(--determinex-shell-shadow)",
          }}
        >
          <button
            onClick={() => setActiveSidebar("none")}
            className="absolute top-4 right-4 z-[100] h-8 w-8 flex items-center justify-center rounded-full bg-black/20 border border-white/10 text-gray-400 opacity-0 group-hover:opacity-100 transition-opacity hover:bg-black/40 hover:text-white"
            title="Close panel to view background"
          >
            <X size={16} />
          </button>

          <div data-testid="workbench-primary-surface" className="relative min-h-0 flex-1 overflow-hidden">
          {hiveSessionId ? (
            <HiveBuildLoop
              sessionId={hiveSessionId}
              projectName={hiveProjectName}
              autoRun={hiveAutoRun}
              autoRetry={hiveAutoRetry}
              onBack={() => {
                setHiveSessionId(null);
                setHiveProjectName("");
                setHiveAutoRun(false);
                setHiveAutoRetry(false);
                setActiveSidebar("hub");
              }}
            />
          ) : activeSidebar === "hive" && isOracleConsulting ? (
            <OracleArena />
          ) : activeSidebar === "hive" && previewedPath ? (
            <PathDetailPanel
              path={previewedPath}
              onChoose={(path) => {
                setConfirmedPath(path);
                setPreviewedPath(null);
              }}
              onBack={() => setPreviewedPath(null)}
              colorOverride={colorHints[0]}
            />
          ) : activeSidebar === "hive" && confirmedPath && !hiveSpec ? (
            <DiscoveryProgressView
              path={confirmedPath}
              answeredCount={oracleAnsweredCount}
              colorOverride={colorHints[0]}
            />
          ) : activeSidebar === "hive" && hiveSpec ? (
            <SpecBreakdownView spec={hiveSpec} path={confirmedPath} />
          ) : activeSidebar === "hive" ? (
            <div className="flex h-full min-h-0 flex-col overflow-hidden">
              <div className="shrink-0 border-b border-white/10 p-6">
                <div className="mb-2 flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-emerald-300">
                  <Zap size={13} /> Work Cockpit
                </div>
                <div className="flex flex-wrap items-start justify-between gap-4">
                  <div>
                    <h2 className="text-3xl font-black leading-tight text-[var(--determinex-text)]" style={{ fontFamily: "var(--determinex-font-display)" }}>
                      Ask. Plan. Build. Prove.
                    </h2>
                    <p className="mt-2 max-w-3xl text-[12px] leading-relaxed text-[var(--determinex-muted)]">
                      The left panel captures the request. This screen shows what will happen next, which tools are attached, and where proof will appear.
                    </p>
                  </div>
                  <div className="rounded-xl border border-white/10 bg-black/35 px-4 py-3 text-right">
                    <div className="text-[9px] font-black uppercase tracking-widest text-gray-600">Workspace</div>
                    <div className="mt-1 max-w-[260px] truncate font-mono text-[10px] text-gray-300">
                      {selectedProjectName}
                    </div>
                  </div>
                </div>
              </div>

              <div className="min-h-0 flex-1 overflow-y-auto p-6 no-scrollbar">
                <div className={`grid gap-4 ${
                  addonDockOpen && addonDockMode === "right" ? "grid-cols-1" : "xl:grid-cols-[1.1fr_0.9fr]"
                }`}>
                  <section className="rounded-2xl border border-white/8 bg-black/30 p-5">
                    <div className="mb-4 flex items-center justify-between gap-3">
                      <div>
                        <div className="text-[9px] font-black uppercase tracking-widest text-gray-600">Run State</div>
                        <div className="mt-1 text-2xl font-black text-white">
                          {hiveSessionId ? "Running" : "Ready"}
                        </div>
                      </div>
                      <span className="rounded-full border border-white/10 bg-white/[0.04] px-3 py-1 text-[9px] font-black uppercase tracking-widest text-gray-500">
                        {agentStatus.verdict ?? "No verdict"}
                      </span>
                    </div>

                    <div className={`grid gap-3 ${
                      addonDockOpen && addonDockMode === "right" ? "grid-cols-2" : "md:grid-cols-4"
                    }`}>
                      {[
                        ["Ask", "Describe the app, fix, or imported repo outcome."],
                        ["Plan", "Oracle turns the request into choices and a spec."],
                        ["Build", "Builder writes code against the chosen plan."],
                        ["Prove", "Compiler, logs, diffs, and verifier output are recorded."],
                      ].map(([label, detail], index) => (
                        <div key={label} className="rounded-xl border border-white/8 bg-white/[0.03] p-3">
                          <div className="mb-2 flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-emerald-300">
                            <span className="flex h-5 w-5 items-center justify-center rounded-full border border-emerald-400/30 bg-emerald-950/30 font-mono text-[9px]">
                              {index + 1}
                            </span>
                            {label}
                          </div>
                          <p className="text-[10px] leading-relaxed text-gray-500">{detail}</p>
                        </div>
                      ))}
                    </div>
                  </section>

                  <section className="rounded-2xl border border-white/8 bg-black/30 p-5">
                    <div className="mb-4 text-[9px] font-black uppercase tracking-widest text-gray-600">
                      Attach What You Need
                    </div>
                    <div className={`grid gap-2 ${
                      addonDockOpen && addonDockMode === "right" ? "grid-cols-1" : "grid-cols-2"
                    }`}>
                      {[
                        ["Terminal", "terminal", TerminalIcon, "Run commands beside this screen"],
                        ["Code", "editor", Code2, "Inspect generated files and source"],
                        ["Build", "build", Gauge, "Watch tasks, tests, and output"],
                        ["Trace", "trace", GitBranch, "Follow worker events and run history"],
                        ["Search", "search", Search, "Find project context"],
                        ["Find in Files", "findfiles", FileSearch, "Literal text search across the workspace"],
                        ["Health", "health", LayoutGrid, "Check oracle and file readiness"],
                      ].map(([label, addon, Icon, detail]) => {
                        const ActionIcon = Icon as typeof TerminalIcon;
                        return (
                          <button
                            key={label as string}
                            type="button"
                            onClick={() => handleAddonLaunch(addon as WorkspaceAddon)}
                            className="group rounded-xl border border-white/8 bg-white/[0.03] p-3 text-left transition hover:border-emerald-400/40 hover:bg-emerald-500/10"
                          >
                            <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-white">
                              <ActionIcon size={13} className="text-emerald-300" /> {label as string}
                            </div>
                            <p className="mt-1 text-[9px] leading-relaxed text-gray-600 group-hover:text-gray-500">
                              {detail as string}
                            </p>
                          </button>
                        );
                      })}
                    </div>
                  </section>
                </div>

                <div className="mt-4 grid gap-4 lg:grid-cols-3">
                  {[
                    ["Current input", inputVal || "Use the left Work panel to describe what to build."],
                    ["Project contract", displayPath(explorerRoot) || "No workspace path bound."],
                    ["Proof boundary", "No release claim until Proof records a verified run."],
                  ].map(([label, value]) => (
                    <div key={label} className="rounded-xl border border-white/8 bg-white/[0.025] p-4">
                      <div className="text-[9px] font-black uppercase tracking-widest text-gray-600">{label}</div>
                      <div className="mt-2 text-[11px] leading-relaxed text-gray-400">{value}</div>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          ) : activeSidebar === "command" ? (
            <div className="flex h-full min-h-0 flex-col overflow-hidden bg-[var(--determinex-bg)]">
              <CommandCenter workspacePath={explorerRoot} />
            </div>
          ) : activeSidebar === "hub" ? (
            <ProjectHub
              selectedProjectName={selectedProjectName}
              onSelectProject={handleProjectSelect}
              onNavigate={handleProjectHubNavigate}
              onOpenLibrary={() => setShowProjectLibrary(true)}
            />
          ) : activeSidebar === "extensions" ? (
            <div className="flex h-full min-h-0 flex-col overflow-hidden">
              <div className="shrink-0 border-b border-white/10 p-6">
                <div className="mb-2 flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-pink-300">
                  <Package size={13} /> Tools Panel
                </div>
                <h2 className="text-3xl font-black leading-tight text-[var(--determinex-text)]" style={{ fontFamily: "var(--determinex-font-display)" }}>
                  Tools, Providers, and Add-ons
                </h2>
                <p className="mt-2 max-w-3xl text-[12px] leading-relaxed text-[var(--determinex-muted)]">
                  Manage installed tools, model providers, connectors, and IDE panes here. Terminal, Code, Build, Trace, Search, and Health attach to the active screen instead of opening as disconnected pages.
                </p>
              </div>
              <div className="min-h-0 flex-1 overflow-hidden">
                <ToolsHub
                  toolCatalog={toolCatalog}
                  toolCoverage={toolCoverage}
                  activeTool={addonDockOpen ? activeAddon : null}
                  onLaunchTool={handleAddonLaunch}
                  onOpenBrain={() => handleProjectHubNavigate("brain")}
                  onShowServiceLogin={(id) => {
                    setShowServiceLogin(id);
                    setServiceKeyInput("");
                  }}
                />
              </div>
            </div>
          ) : activeSidebar === "pipeline" ? (
            <ProjectArchitect
              selectedProjectName={selectedProjectName}
            />
          ) : activeSidebar === "explorer" ? (
            <div className="relative flex h-full min-h-0 flex-col overflow-hidden">
              {/* Ambient bg */}
              <div className="pointer-events-none absolute inset-0 opacity-20">
                <div className="matrix-rain absolute inset-0" />
              </div>
              <div className="relative z-10 flex min-h-0 flex-1 flex-col p-6">
                <div className="border-b border-white/10 pb-5">
                  <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-purple-300 mb-2">
                    <Folder size={13} /> Workspace Stage
                  </div>
                  <h2 className="text-3xl font-black leading-tight text-[var(--determinex-text)]" style={{ fontFamily: "var(--determinex-font-display)" }}>
                    {selectedProjectName}
                  </h2>
                  <p className="mt-2 max-w-2xl font-mono text-[12px] leading-relaxed text-[var(--determinex-muted)]">
                    {displayPath(explorerRoot) || "No workspace path bound yet."}
                  </p>
                </div>

                <div className="grid min-h-0 flex-1 grid-cols-1 gap-5 py-6 xl:grid-cols-2">
                  <div className="rounded-2xl border border-white/10 bg-black/25 p-6">
                    <div className="mb-4 flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-emerald-300">
                      <GitPullRequest size={14} /> Source
                    </div>
                    {gitBranch ? (
                      <div className="space-y-2 font-mono text-[11px] text-gray-300">
                        <div>branch <span className="text-white">{gitBranch}</span></div>
                        <div>upstream <span className="text-white">{explorerGitMeta.upstream ?? "none"}</span></div>
                        {(explorerGitMeta.ahead > 0 || explorerGitMeta.behind > 0) && (
                          <div className="text-amber-300">
                            {explorerGitMeta.ahead > 0 && `${explorerGitMeta.ahead} ahead`}
                            {explorerGitMeta.ahead > 0 && explorerGitMeta.behind > 0 && " · "}
                            {explorerGitMeta.behind > 0 && `${explorerGitMeta.behind} behind`}
                          </div>
                        )}
                        <div>
                          {explorerGitFiles.length > 0
                            ? <span className="text-amber-300">{explorerGitFiles.length} uncommitted change{explorerGitFiles.length === 1 ? "" : "s"}</span>
                            : <span className="text-gray-500">working tree clean</span>}
                        </div>
                      </div>
                    ) : (
                      <p className="text-[11px] text-gray-500">Not a git repository, or status could not be read.</p>
                    )}
                    <button
                      type="button"
                      onClick={() => setActiveSidebar("git")}
                      className="mt-4 rounded-lg border border-emerald-400/25 bg-emerald-950/20 px-3 py-2 text-[10px] font-black uppercase tracking-widest text-emerald-300 transition hover:bg-emerald-900/30"
                    >
                      Open Source Control
                    </button>
                  </div>

                  <div className="rounded-2xl border border-white/10 bg-black/25 p-6">
                    <div className="mb-4 flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-blue-300">
                      <Files size={14} /> Files
                    </div>
                    <p className="font-mono text-[11px] text-gray-300">
                      {fileTree.length > 0
                        ? `${fileTree.length} top-level entr${fileTree.length === 1 ? "y" : "ies"} scanned`
                        : "Scanning workspace..."}
                    </p>
                    <div className="mt-4 flex flex-wrap gap-2">
                      <button
                        type="button"
                        onClick={() => setWorkspaceView("files")}
                        className="rounded-lg border border-blue-400/25 bg-blue-950/20 px-3 py-2 text-[10px] font-black uppercase tracking-widest text-blue-300 transition hover:bg-blue-900/30"
                      >
                        Browse Tree
                      </button>
                      <button
                        type="button"
                        onClick={() => handleAddonLaunch("findfiles")}
                        className="rounded-lg border border-blue-400/25 bg-blue-950/20 px-3 py-2 text-[10px] font-black uppercase tracking-widest text-blue-300 transition hover:bg-blue-900/30"
                      >
                        Find in Files
                      </button>
                    </div>
                  </div>

                  <div className="rounded-2xl border border-white/10 bg-black/25 p-6">
                    <div className="mb-4 flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-amber-300">
                      <Activity size={14} /> Runs
                    </div>
                    <p className="text-[11px] text-gray-500">
                      {hiveSessionId ? `Active session: ${hiveSessionId}` : "No active Hive session. Start one from Work."}
                    </p>
                    <button
                      type="button"
                      onClick={() => handleSidebarLaunch("hive")}
                      className="mt-4 rounded-lg border border-amber-400/25 bg-amber-950/20 px-3 py-2 text-[10px] font-black uppercase tracking-widest text-amber-300 transition hover:bg-amber-900/30"
                    >
                      Go to Work
                    </button>
                  </div>

                  <div className="rounded-2xl border border-white/10 bg-black/25 p-6">
                    <div className="mb-4 flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-purple-300">
                      <Gauge size={14} /> Quick Attach
                    </div>
                    <p className="text-[11px] text-gray-500">
                      Attach a tool beside this screen instead of switching away from it.
                    </p>
                    <div className="mt-4 flex flex-wrap gap-2">
                      <button
                        type="button"
                        onClick={() => handleAddonLaunch("terminal")}
                        className="rounded-lg border border-purple-400/25 bg-purple-950/20 px-3 py-2 text-[10px] font-black uppercase tracking-widest text-purple-300 transition hover:bg-purple-900/30"
                      >
                        Terminal
                      </button>
                      <button
                        type="button"
                        onClick={() => handleAddonLaunch("editor")}
                        className="rounded-lg border border-purple-400/25 bg-purple-950/20 px-3 py-2 text-[10px] font-black uppercase tracking-widest text-purple-300 transition hover:bg-purple-900/30"
                      >
                        Code
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>

          ) : activeSidebar === "benchmark" ? (
            <BrainStage
              selectedModel={selectedModel}
              modelTiers={modelTiers}
              tandemPresets={tandemPresets}
              onSelectModel={(id) => setSelectedModel(id)}
              matrixLogs={matrixLogs}
              onOpenModelSlots={() => {
                setSettingsTab("roles");
                setShowSettings(true);
              }}
            />
          ) : activeSidebar === "proof" ? (
            <div className="flex flex-col h-full overflow-hidden">
              {/* Header */}
              <div className="border-b shrink-0 p-6" style={{ borderColor: "var(--determinex-border)" }}>
                <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-cyan-400 mb-2">
                  <Eye size={13} /> Project Proof
                </div>
                <h2 className="text-2xl font-black text-white" style={{ fontFamily: "var(--determinex-font-display)" }}>
                  {selectedProjectName} Proof
                </h2>
                <p className="mt-1 text-[12px] leading-relaxed" style={{ color: "var(--determinex-muted)" }}>
                  Project-scoped run history, build output, trace logs, code diffs, verifier results, and release gates. Empty states explain exactly what proof is missing.
                </p>
                <div className="mt-4 flex flex-wrap gap-2">
                  <button
                    type="button"
                    onClick={() => setShowProjectLibrary(true)}
                    className="rounded-lg border border-cyan-400/25 bg-cyan-950/20 px-3 py-2 text-[10px] font-black uppercase tracking-widest text-cyan-300 transition-all hover:bg-cyan-900/30"
                  >
                    Session Library
                  </button>
                  <button
                    type="button"
                    onClick={() => handleAddonLaunch("build")}
                    className="rounded-lg border border-orange-400/25 bg-orange-950/20 px-3 py-2 text-[10px] font-black uppercase tracking-widest text-orange-300 transition-all hover:bg-orange-900/30"
                  >
                    Builds
                  </button>
                  <button
                    type="button"
                    onClick={() => handleAddonLaunch("trace")}
                    className="rounded-lg border border-violet-400/25 bg-violet-950/20 px-3 py-2 text-[10px] font-black uppercase tracking-widest text-violet-300 transition-all hover:bg-violet-900/30"
                  >
                    Trace
                  </button>
                  <button
                    type="button"
                    onClick={() => handleAddonLaunch("editor")}
                    className="rounded-lg border border-blue-400/25 bg-blue-950/20 px-3 py-2 text-[10px] font-black uppercase tracking-widest text-blue-300 transition-all hover:bg-blue-900/30"
                  >
                    Diffs
                  </button>
                  <button
                    type="button"
                    onClick={() => handleAddonLaunch("health")}
                    className="rounded-lg border border-teal-400/25 bg-teal-950/20 px-3 py-2 text-[10px] font-black uppercase tracking-widest text-teal-300 transition-all hover:bg-teal-900/30"
                  >
                    Gates
                  </button>
                </div>
              </div>

              <div className="flex-1 overflow-y-auto p-6 no-scrollbar">
                {/* Main verdict card */}
                <div className="grid grid-cols-1 gap-4 lg:grid-cols-2 mb-6">
                  <div className={`rounded-2xl border p-5 ${
                    agentStatus.verdict && agentStatus.accepted
                      ? "border-emerald-500/25 bg-emerald-950/15"
                      : agentStatus.verdict && !agentStatus.accepted
                        ? "border-red-500/25 bg-red-950/15"
                        : "border-white/8 bg-white/[0.03]"
                  }`}>
                    <div className="text-[9px] uppercase font-bold tracking-widest text-gray-500 mb-2">Oracle Verdict</div>
                    <div className={`text-4xl font-black mb-2 ${
                      agentStatus.verdict && agentStatus.accepted ? "text-emerald-400"
                        : agentStatus.verdict && !agentStatus.accepted ? "text-red-400"
                        : "text-gray-700"
                    }`}>
                      {agentStatus.verdict ?? "-"}
                    </div>
                    {agentStatus.confidence !== null && agentStatus.confidence !== undefined ? (
                      <div className="space-y-1">
                        <div className="flex items-center justify-between text-[10px] text-gray-500">
                          <span>Confidence</span>
                          <span className="font-mono font-bold text-white">{(agentStatus.confidence * 100).toFixed(0)}%</span>
                        </div>
                        <div className="h-1.5 rounded-full bg-white/5 overflow-hidden">
                          <div
                            className={`h-full rounded-full transition-all ${agentStatus.accepted ? "bg-emerald-400" : "bg-red-400"}`}
                            style={{ width: `${(agentStatus.confidence * 100).toFixed(0)}%` }}
                          />
                        </div>
                      </div>
                    ) : (
                      <p className="text-[11px] text-gray-600 font-mono">No pipeline run yet. Go to Work, describe your change, then orchestrate.</p>
                    )}
                  </div>

                  <div className="rounded-2xl border border-white/8 bg-white/[0.03] p-5">
                    <div className="text-[9px] uppercase font-bold tracking-widest text-gray-500 mb-2">Pipeline State</div>
                    <div className="space-y-2 mt-3">
                      {[
                        { label: "Generated file", value: generatedFile ?? "-", color: generatedFile ? "text-purple-300" : "text-gray-700" },
                        { label: "Retry count", value: retryCount > 0 ? String(retryCount) : "-", color: retryCount > 0 ? "text-amber-400" : "text-gray-700" },
                        { label: "Accepted", value: agentStatus.accepted === true ? "Yes" : agentStatus.accepted === false ? "No" : "-", color: agentStatus.accepted === true ? "text-emerald-400" : agentStatus.accepted === false ? "text-red-400" : "text-gray-700" },
                        { label: "Error", value: agentStatus.error ? `${agentStatus.error.stage}: ${agentStatus.error.message.slice(0, 60)}` : "-", color: agentStatus.error ? "text-red-400" : "text-gray-700" },
                      ].map(({ label, value, color }) => (
                        <div key={label} className="flex items-start justify-between gap-3">
                          <span className="text-[10px] text-gray-600 shrink-0">{label}</span>
                          <span className={`text-[10px] font-mono font-bold text-right truncate ${color}`}>{value}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>

                {/* Compiler warning */}
                {compilerWarning && (
                  <div className="mb-4 flex items-start gap-2 rounded-xl border border-amber-500/30 bg-amber-950/20 px-4 py-3">
                    <span className="text-amber-400 text-[10px] font-black uppercase tracking-widest shrink-0 mt-px">Compiler</span>
                    <span className="text-[10px] text-amber-300/80 font-mono leading-relaxed">{compilerWarning}</span>
                  </div>
                )}

                {/* Log tail */}
                {matrixLogs.length > 0 && (
                  <div className="rounded-2xl border border-white/8 bg-black/40 overflow-hidden mb-4">
                    <div className="px-4 py-2.5 border-b border-white/5 flex items-center justify-between">
                      <span className="text-[9px] uppercase font-bold tracking-widest text-gray-500">Session Log</span>
                      <span className="text-[8px] font-mono text-gray-700">{matrixLogs.length} lines</span>
                    </div>
                    <div className="p-4 font-mono text-[10px] leading-relaxed space-y-0.5 max-h-48 overflow-y-auto no-scrollbar">
                      {matrixLogs.slice(-20).map((line, i) => (
                        <div
                          key={i}
                          className={
                            line.includes("[ERROR]") ? "text-red-400"
                              : line.includes("[OBSERVER]") ? "text-violet-400"
                                : line.includes("[DETERMINEX]") ? "text-cyan-400"
                                  : line.includes("[USER]") ? "text-emerald-400"
                                    : "text-gray-600"
                          }
                        >
                          {line}
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Empty state */}
                {matrixLogs.length === 0 && !agentStatus.verdict && (
                  <div className="flex flex-col items-center justify-center py-16 text-center">
                    <div className="h-16 w-16 rounded-2xl border border-white/8 bg-white/[0.03] flex items-center justify-center mb-4">
                      <Eye size={28} className="text-gray-700" />
                    </div>
                    <p className="text-[13px] font-bold text-gray-600">No evidence yet</p>
                    <p className="mt-2 text-[11px] text-gray-700 font-mono leading-relaxed max-w-xs">
                      Open Work, describe a change, and run the Hive. Oracle verdicts, file diffs, and compiler results will appear here.
                    </p>
                    <button
                      onClick={() => setActiveSidebar("hive")}
                      className="mt-6 rounded-xl border border-emerald-500/30 bg-emerald-950/20 px-5 py-2.5 text-[10px] font-black uppercase tracking-widest text-emerald-400 transition-all hover:bg-emerald-900/30"
                    >
                      Go to Work
                    </button>
                  </div>
                )}
              </div>
            </div>
          ) : activeSidebar ? (
            <div className="flex flex-col items-center justify-center h-full gap-3 text-center opacity-40">
              <p className="text-[12px] font-mono text-gray-600">Select a panel from the rail to begin.</p>
              <button onClick={() => setActiveSidebar("none")} className="text-[10px] uppercase font-bold text-gray-500 hover:text-white">Close</button>
            </div>
          ) : null}
          </div>

          <AnimatePresence mode="wait">
            {addonDockOpen && selectedAddon && (
              <motion.div
                key={`${selectedAddon.id}-${addonDockMode}`}
                data-testid="workspace-addon-drawer"
                initial={addonDockMode === "right" ? { opacity: 0, x: 24 } : { opacity: 0, y: 24 }}
                animate={{ opacity: 1, x: 0, y: 0 }}
                exit={addonDockMode === "right" ? { opacity: 0, x: 24 } : { opacity: 0, y: 24 }}
                transition={{ type: "spring", stiffness: 280, damping: 28, mass: 0.8 }}
                className={`flex shrink-0 flex-col overflow-hidden backdrop-blur-3xl ${
                  addonDockMode === "right"
                    ? `${addonWidthClass} h-full border-l border-white/10`
                    : `${addonHeightClass} w-full border-t border-white/10`
                }`}
                style={{
                  background: "linear-gradient(180deg, rgba(3,7,18,0.94) 0%, rgba(1,4,9,0.98) 100%)",
                  boxShadow: addonDockMode === "right"
                    ? "-14px 0 34px rgba(0,0,0,0.35)"
                    : "0 -14px 34px rgba(0,0,0,0.35)",
                }}
              >
                <div className="flex shrink-0 flex-wrap items-center justify-between gap-3 border-b border-white/10 px-4 py-3">
                  <div className="flex min-w-0 items-center gap-3">
                    {(() => {
                      const SelectedAddonIcon = selectedAddon.icon;
                      return <SelectedAddonIcon size={17} className={selectedAddon.tone} />;
                    })()}
                    <div className="min-w-0">
                      <div className="truncate text-[11px] font-black uppercase tracking-widest text-white">
                        {selectedAddon.label}
                      </div>
                      <div className="mt-0.5 truncate text-[9px] font-mono text-gray-600">
                        {selectedAddon.description}
                      </div>
                    </div>
                  </div>
                  <div className="flex min-w-0 items-center justify-end gap-2">
                    <div className="flex rounded-lg border border-white/8 bg-white/[0.03] p-1">
                      {(["bottom", "right"] as const).map((mode) => (
                        <button
                          key={mode}
                          type="button"
                          onClick={() => setAddonDockMode(mode)}
                          className={`rounded-md px-2 py-1 text-[8px] font-black uppercase tracking-widest transition ${
                            addonDockMode === mode ? "bg-white/10 text-white" : "text-gray-600 hover:text-gray-300"
                          }`}
                        >
                          {mode}
                        </button>
                      ))}
                    </div>
                    <div className="flex rounded-lg border border-white/8 bg-white/[0.03] p-1">
                      {(["compact", "standard", "large"] as const).map((size) => (
                        <button
                          key={size}
                          type="button"
                          onClick={() => setAddonDockSize(size)}
                          className={`rounded-md px-2 py-1 text-[8px] font-black uppercase tracking-widest transition ${
                            addonDockSize === size ? "bg-white/10 text-white" : "text-gray-600 hover:text-gray-300"
                          }`}
                        >
                          {size === "standard" ? "std" : size}
                        </button>
                      ))}
                    </div>
                    <div
                      className="flex max-w-[min(560px,42vw)] overflow-x-auto rounded-lg border border-white/8 bg-white/[0.03] p-1"
                      aria-label="Switch attached tool"
                    >
                      {runtimeAddonItems.map((item) => {
                        const AddonIcon = item.icon;
                        const isActive = item.id === selectedAddon.id;
                        return (
                          <button
                            key={item.id}
                            type="button"
                            data-testid={`addon-switch-${item.id}`}
                            aria-label={`Show ${item.label}`}
                            title={item.label}
                            onClick={() => {
                              setActiveAddon(item.id);
                              setAddonDockOpen(true);
                            }}
                            className={`flex h-8 min-w-8 items-center justify-center rounded-md border px-2 transition-all ${
                              isActive
                                ? "border-[var(--determinex-accent)]/60 bg-[var(--determinex-accent)]/15 text-white"
                                : "border-transparent text-gray-600 hover:border-white/10 hover:bg-white/[0.04] hover:text-gray-300"
                            }`}
                          >
                            <AddonIcon size={14} className={isActive ? item.tone : undefined} />
                            <span className="sr-only">{item.label}</span>
                          </button>
                        );
                      })}
                    </div>
                    <button
                      type="button"
                      onClick={closeAddon}
                      className="ml-1 flex h-8 w-8 items-center justify-center rounded-lg border border-white/10 bg-white/[0.03] text-gray-500 transition-all hover:border-red-400/30 hover:text-red-300"
                      title="Close add-on"
                    >
                      <X size={14} />
                    </button>
                  </div>
                </div>
                <div className="min-h-0 flex-1 overflow-auto">
                  {selectedAddon.panel}
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </motion.div>
        )}
        </AnimatePresence>

      </div>

      <AnimatePresence>
        {showProjectLibrary && (
          <motion.div
            key="project-library-modal"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="absolute inset-0 z-50 flex items-center justify-center bg-black/70 p-6 backdrop-blur-sm"
          >
            <motion.div
              initial={{ opacity: 0, y: 24, scale: 0.98 }}
              animate={{ opacity: 1, y: 0, scale: 1 }}
              exit={{ opacity: 0, y: 24, scale: 0.98 }}
              transition={{ type: "spring", stiffness: 280, damping: 28, mass: 0.85 }}
              className="h-[78vh] w-full max-w-5xl overflow-hidden rounded-2xl border border-white/10 shadow-2xl"
            >
              <ProjectLibrary
                onResume={handleResumeProjectSession}
                onClose={() => setShowProjectLibrary(false)}
              />
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Teacher overlay */}
      <TeacherOverlay
        open={showTeacher}
        onClose={() => setShowTeacher(false)}
        activeSidebar={activeSidebar}
        activeAddon={addonDockOpen ? activeAddon : null}
      />

      {!showTeacher && (
        <div className="absolute bottom-14 right-6 z-50 flex items-center gap-2 rounded-2xl border border-[var(--determinex-border)] bg-black/70 px-3 py-2 shadow-[0_0_24px_var(--determinex-accent-glow)] backdrop-blur-xl">
          <div className="hidden max-w-[220px] text-[10px] leading-snug text-gray-500 lg:block">
            Guide can explain this screen, the next build step, and what proof means.
          </div>
          <TeacherButton onClick={() => setShowTeacher(true)} />
        </div>
      )}

      {/* Command palette */}
      <CommandPalette
        open={showPalette}
        onClose={() => setShowPalette(false)}
        commands={paletteCommands}
      />

      {/* Status bar — fixed bottom */}
      <StatusBar
        activeSidebar={activeSidebar}
        selectedModel={selectedModel}
        gitBranch={gitBranch}
        oracleAccepted={agentStatus.accepted}
        oracleVerdict={agentStatus.verdict}
        errorCount={statusBarErrorCount}
        keyStatus={keyStatus}
        onChangeModel={setSelectedModel}
        onClickErrors={() => handleAddonLaunch("problems")}
        onClickModel={() => { setSettingsTab("roles"); setShowSettings(true); }}
        onTogglePanel={() => {
          if (addonDockOpen) closeAddon();
          else handleAddonLaunch(activeAddon ?? "terminal");
        }}
      />
    </div>
  );

  // -------------------------------------------------------------
  // MOBILE EXECUTIVE DASHBOARD
  // -------------------------------------------------------------
  const renderMobileView = () => (
    <div
      className="flex h-full w-full flex-col"
      style={{
        background: `radial-gradient(circle at 18% 0%, ${themePack.colors.accentGlow}, transparent 32%), var(--determinex-bg)`,
        color: "var(--determinex-text)",
      }}
    >
      <header
        className="shrink-0 border-b px-4 py-3"
        style={{
          background: "var(--determinex-panel-glass)",
          borderColor: "var(--determinex-border)",
        }}
      >
        <div className="flex items-center justify-between gap-3">
          <div className="min-w-0">
            <div className="text-[10px] font-black uppercase tracking-widest text-emerald-400">
              Determinex
            </div>
            <div className="truncate text-[13px] font-bold text-white">
              Verified build cockpit
            </div>
          </div>
          <button
            onClick={() => setShowSettings(true)}
            className="rounded-lg border border-[#30363d] bg-[#111821] p-2 text-gray-400"
            title="Settings"
          >
            <Settings size={16} />
          </button>
        </div>
      </header>

      <main className="min-h-0 flex-1 space-y-3 overflow-y-auto p-4">
        <section className="space-y-2 border-b border-[#25303a] pb-3">
          <div>
            <div className="flex items-center gap-2 text-[10px] font-black uppercase tracking-widest text-cyan-300">
              <ShieldCheck size={13} /> Proof loop
            </div>
            <h1 className="mt-2 text-[22px] font-black leading-tight text-white">
              Ask for the change. Keep the proof visible.
            </h1>
            <p className="mt-2 text-[12px] leading-relaxed text-gray-500">
              Objective, verifier state, review state, and proof links stay in one path.
            </p>
          </div>

          <textarea
            value={inputVal}
            onChange={(e) => setInputVal(e.target.value)}
            disabled={isExecutingPack}
            placeholder="Describe the repo change..."
            className="min-h-24 w-full resize-none rounded-lg border border-[#30363d] bg-[#010409] px-3 py-3 text-[13px] text-gray-100 outline-none focus:border-cyan-500/50"
          />

          <AiRouteSelect
            value={selectedModel}
            onChange={setSelectedModel}
            keyStatus={keyStatus}
            compact
          />

          <div className="grid grid-cols-2 gap-2">
            <button
              onClick={() =>
                setInputVal(
                  "Demo: fix an empty-input parser bug, prove it with tests, and show the review diff."
                )
              }
              className="rounded-lg border border-[#30363d] bg-[#111821] px-3 py-2.5 text-[11px] font-black uppercase tracking-widest text-cyan-300"
            >
              Load Demo
            </button>
            <button
              onClick={handleUnleash}
              disabled={isExecutingPack || inputVal.trim().length === 0}
              className={`rounded-lg border px-3 py-2.5 text-[11px] font-black uppercase tracking-widest ${
                isExecutingPack || inputVal.trim().length === 0
                  ? "border-[#30363d] bg-[#0d1117] text-gray-600"
                  : "border-emerald-500/35 bg-emerald-500/15 text-emerald-300"
              }`}
            >
              {isExecutingPack ? "Running" : "Orchestrate"}
            </button>
          </div>
        </section>

        <section className="grid grid-cols-1 gap-2">
          {[
            ["Oracle", "Compiler/test truth is the source of authority.", "emerald"],
            ["Approval", "Source mutation stays gated until a verified diff is approved.", "purple"],
            ["Ledger", "Proof reports stay separate from release readiness.", "cyan"],
          ].map(([label, detail, tone]) => (
            <div
              key={label}
              className="rounded-lg border border-[#25303a] bg-[#0d1117] px-3 py-2.5"
            >
              <div
                className={`text-[10px] font-black uppercase tracking-widest ${
                  tone === "emerald"
                    ? "text-emerald-300"
                    : tone === "purple"
                      ? "text-purple-300"
                      : "text-cyan-300"
                }`}
              >
                {label}
              </div>
              <div className="mt-1 text-[11px] leading-snug text-gray-500">{detail}</div>
            </div>
          ))}
        </section>

        <section className="rounded-lg border border-[#25303a] bg-[#0d1117]">
          <div className="flex items-center justify-between border-b border-[#25303a] px-3 py-2">
            <span className="text-[10px] font-black uppercase tracking-widest text-gray-400">
              Activity
            </span>
            <button
              onClick={() => setIsDiffMode(!isDiffMode)}
              className="text-[10px] font-bold uppercase tracking-widest text-cyan-300"
            >
              {isDiffMode ? "Log" : "Diff"}
            </button>
          </div>
          {isDiffMode ? (
            <div className="h-56">
              <DiffEditor
                height="100%"
                language="python"
                theme="vs-dark"
                original={diffData.old}
                modified={diffData.new}
                options={{
                  minimap: { enabled: false },
                  wordWrap: "on",
                  fontSize: 10,
                  disableLayerHinting: true,
                }}
              />
            </div>
          ) : (
            <div className="min-h-32 px-3 py-3 font-mono text-[10px] leading-relaxed text-emerald-400/80">
              {matrixLogs.length > 0 ? (
                matrixLogs.slice(-12).map((log, i) => <div key={i}>{log}</div>)
              ) : (
                <div className="text-gray-600">No active run yet.</div>
              )}
            </div>
          )}
        </section>

        <nav className="grid grid-cols-2 gap-2 pb-2">
          <a
            href="/proof-center/"
            className="rounded-lg border border-[#30363d] bg-[#111821] px-3 py-3 text-center text-[11px] font-black uppercase tracking-widest text-gray-300"
          >
            Proof Center
          </a>
          <button
            onClick={() => handleSidebarLaunch("benchmark")}
            className="rounded-lg border border-[#30363d] bg-[#111821] px-3 py-3 text-[11px] font-black uppercase tracking-widest text-gray-300"
          >
            Brain & Forge
          </button>
        </nav>
      </main>
    </div>
  );

  return (
    <div
      data-determinex-skin={theme}
      style={{
        ...skinPackStyle,
        background: "var(--determinex-bg)",
        color: "var(--determinex-text)",
      }}
      className="relative flex h-[100dvh] w-full overflow-hidden font-sans"
    >
      <SetupWizard />

      <div className="flex h-[100dvh] w-full relative z-10 bg-transparent">
        {isMobile ? renderMobileView() : renderDesktopView()}
      </div>

      <SettingsModal />

      <ServiceLoginModal />

      <AnimatePresence>
        {showOnboarding && (
          <WorkspaceOnboarding workspacePath={explorerRoot} onClose={() => setShowOnboarding(false)} />
        )}
        {isBootstrapping && (
          <BootOverlay
            bootError={bootError}
            bootProgress={bootProgress}
            onDismiss={dismissBootError}
          />
        )}
      </AnimatePresence>

      <HelpModal helpModal={helpModal} onClose={() => setHelpModal(null)} />
    </div>
  );
}
