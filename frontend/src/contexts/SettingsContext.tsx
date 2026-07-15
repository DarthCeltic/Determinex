"use client";
import React, { createContext, useContext, useState, useEffect, useCallback } from "react";
import {
  getApiKeyStatus,
  getToolRegistry,
  checkOllamaStatus,
  getModelsRegistry,
  invokeSafe,
  getOllamaBaseUrl,
  saveOllamaBaseUrl,
} from "@/lib/api";
import { useErrorToast } from "@/components/ErrorToast";
import {
  readStoredNetworkPolicy,
  storeNetworkPolicy,
  type NetworkPolicyMode,
} from "@/lib/networkPolicy";

// ── Types ────────────────────────────────────────────────────────────────────

interface ToolEntry {
  name: string;
  status: string;
  type: string;
  requires: string | null;
}
export interface ApiKeys {
  openai_key: string;
  anthropic_key: string;
  gemini_key: string;
  groq_key: string;
  deepseek_key: string;
  mistral_key: string;
  openrouter_key: string;
}

interface SettingsContextValue {
  // Modal visibility
  showSettings: boolean;
  setShowSettings: React.Dispatch<React.SetStateAction<boolean>>;

  // Settings tab
  settingsTab: "keys" | "roles" | "diagnostics" | "skin" | "network";
  setSettingsTab: React.Dispatch<React.SetStateAction<"keys" | "roles" | "diagnostics" | "skin" | "network">>;

  // Network policy
  networkPolicy: NetworkPolicyMode;
  setNetworkPolicy: (mode: NetworkPolicyMode) => void;

  // API key state
  keyStatus: Record<string, boolean>;
  apiKeys: ApiKeys;
  setApiKeys: React.Dispatch<React.SetStateAction<ApiKeys>>;

  // Ollama endpoint (not a secret -- a configurable local/remote base URL)
  ollamaBaseUrl: string;
  setOllamaBaseUrl: React.Dispatch<React.SetStateAction<string>>;
  saveOllamaEndpoint: (url: string) => Promise<void>;

  // Tool registry
  toolCatalog: ToolEntry[];
  toolCoverage: string;
  refreshToolRegistry: () => Promise<void>;

  // Service login (connect external provider)
  showServiceLogin: string | null;
  setShowServiceLogin: React.Dispatch<React.SetStateAction<string | null>>;
  serviceKeyInput: string;
  setServiceKeyInput: React.Dispatch<React.SetStateAction<string>>;

  // Diagnostics
  diagnosticResult: string[] | null;
  isDiagnosing: boolean;
  runDiagnostics: () => Promise<void>;
}

const SettingsContext = createContext<SettingsContextValue | null>(null);

export function useSettings(): SettingsContextValue {
  const ctx = useContext(SettingsContext);
  if (!ctx) throw new Error("useSettings must be used inside <SettingsProvider>");
  return ctx;
}

// ── Provider ─────────────────────────────────────────────────────────────────

export function SettingsProvider({ children }: { children: React.ReactNode }) {
  const showError = useErrorToast();
  const [showSettings, setShowSettings] = useState(false);
  const [settingsTab, setSettingsTab] = useState<"keys" | "roles" | "diagnostics" | "skin" | "network">("keys");
  const [networkPolicyState, setNetworkPolicyState] = useState<NetworkPolicyMode>("cloaked");
  const [keyStatus, setKeyStatus] = useState<Record<string, boolean>>({});
  const [apiKeys, setApiKeys] = useState<ApiKeys>({
    openai_key: "",
    anthropic_key: "",
    gemini_key: "",
    groq_key: "",
    deepseek_key: "",
    mistral_key: "",
    openrouter_key: "",
  });
  const [ollamaBaseUrl, setOllamaBaseUrl] = useState<string>("");
  const [toolCatalog, setToolCatalog] = useState<ToolEntry[]>([]);
  const [toolCoverage, setToolCoverage] = useState("0/0");
  const [showServiceLogin, setShowServiceLogin] = useState<string | null>(null);
  const [serviceKeyInput, setServiceKeyInput] = useState("");
  const [diagnosticResult, setDiagnosticResult] = useState<string[] | null>(null);
  const [isDiagnosing, setIsDiagnosing] = useState(false);

  useEffect(() => {
    const policy = readStoredNetworkPolicy();
    setNetworkPolicyState(policy);
    invokeSafe("sync_network_policy", { policy }).catch(console.error);
  }, []);

  const setNetworkPolicy = useCallback((mode: NetworkPolicyMode) => {
    setNetworkPolicyState(mode);
    storeNetworkPolicy(mode);
    invokeSafe("sync_network_policy", { policy: mode }).catch(console.error);
  }, []);

  // Refresh key status + tool registry (called on settings open and after saves).
  const refreshToolRegistry = useCallback(async () => {
    try {
      const reg = await getToolRegistry();
      setToolCatalog(reg.tools || []);
      setToolCoverage(reg.coverage || "0/0");
    } catch {
      /* ignore */
    }
  }, []);

  // Reload when the settings modal opens (mirrors the original useEffect([showSettings])).
  useEffect(() => {
    getApiKeyStatus()
      .then((data) => setKeyStatus(data as unknown as Record<string, boolean>))
      .catch((e) => showError(`Failed to load API key status: ${e}`));
    getOllamaBaseUrl()
      .then((url) => setOllamaBaseUrl(url || ""))
      .catch(() => {});
    refreshToolRegistry();
  }, [showSettings, refreshToolRegistry]);

  const saveOllamaEndpoint = useCallback(async (url: string) => {
    await saveOllamaBaseUrl(url);
    setOllamaBaseUrl(url);
  }, []);

  const runDiagnostics = useCallback(async () => {
    setIsDiagnosing(true);
    setDiagnosticResult(["Running systems check..."]);
    try {
      const dbg: string[] = [];
      const ollama = await checkOllamaStatus(ollamaBaseUrl || undefined);
      if (ollama?.ok) {
        dbg.push(`✓ Ollama online`);
      } else {
        dbg.push(`✗ Ollama offline/error: ${ollama?.error || "Unknown"}`);
      }
      const models = await getModelsRegistry();
      const tiers = models?.tiers?.length || 0;
      dbg.push(tiers > 0 ? `✓ Models registry alive (${tiers} tiers)` : `✗ Models registry empty`);
      const tools = await getToolRegistry();
      const online = tools?.online || 0;
      const total = tools?.total || 0;
      dbg.push(`ℹ Tool registry: ${online}/${total} tools active`);
      const keys = await getApiKeyStatus();
      const total_providers = Object.keys(keys).length;
      const activeKeys = Object.values(keys).filter((v) => v === true).length;
      dbg.push(`ℹ API Keys: ${activeKeys}/${total_providers} configured`);
      setDiagnosticResult(dbg);
    } catch (e) {
      setDiagnosticResult((prev) => [...(prev ?? []), `✗ Diagnostic failure: ${e}`]);
    } finally {
      setIsDiagnosing(false);
    }
  }, [ollamaBaseUrl]);

  return (
    <SettingsContext.Provider
      value={{
        showSettings,
        setShowSettings,
        settingsTab,
        setSettingsTab,
        networkPolicy: networkPolicyState,
        setNetworkPolicy,
        keyStatus,
        apiKeys,
        setApiKeys,
        ollamaBaseUrl,
        setOllamaBaseUrl,
        saveOllamaEndpoint,
        toolCatalog,
        toolCoverage,
        refreshToolRegistry,
        showServiceLogin,
        setShowServiceLogin,
        serviceKeyInput,
        setServiceKeyInput,
        diagnosticResult,
        isDiagnosing,
        runDiagnostics,
      }}
    >
      {children}
    </SettingsContext.Provider>
  );
}
