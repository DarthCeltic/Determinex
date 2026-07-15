"use client";

import { useCallback, useState, useEffect } from "react";
import { invoke as tauriInvoke } from "@tauri-apps/api/core";
import { isTauri, invokeSafe, saveApiKeys, getApiKeyStatus } from "@/lib/api";
import {
  NETWORK_POLICY_COPY,
  type NetworkPolicyMode,
  hasCompletedSetup,
  markSetupCompleted,
  SETUP_RERUN_EVENT,
  storeNetworkPolicy,
  readStoredNetworkPolicy
} from "@/lib/networkPolicy";
import { motion, AnimatePresence } from "framer-motion";
import { Shield, Zap, Cloud, Cpu, Server, Check, ArrowRight, Loader2, HardDrive, AlertTriangle, X, KeyRound } from "lucide-react";

const invoke = async (cmd: string, args?: Record<string, unknown>) => {
  if (isTauri()) {
    return tauriInvoke(cmd, args);
  }
  const result = await invokeSafe(cmd, args);
  if (result !== null) return result;
  // Mocks for dev mode
  if (cmd === "probe_hardware") return { total_vram_mb: 6144, vram_budget_mb: 4144, reserved_vram_mb: 2000, hardware_source: "mock", hardware_fallback: false, recommended_tier: "engineer=qwen2.5-coder:3b-instruct" };
  if (cmd === "ensure_ollama_installed") return { status: "installed (mock)", version: "0.1.27" };
  if (cmd === "pull_required_models") return { models_pulled: [], models_failed: [] };
  return {};
};

type SetupStep =
  | "checking"
  | "probing"
  | "welcome"
  | "providers"
  | "hardware"
  | "installing"
  | "ready"
  | "error";

interface HardwareProbe {
  total_vram_mb?: number | null;
  vram_budget_mb: number;
  reserved_vram_mb?: number;
  hardware_source?: string;
  hardware_fallback?: boolean;
  recommended_tier: string;
}

type SetupApiKeys = {
  openai_key: string;
  anthropic_key: string;
  gemini_key: string;
  groq_key: string;
  deepseek_key: string;
  mistral_key: string;
  openrouter_key: string;
};

export function SetupWizard() {
  const [step, setStep] = useState<SetupStep>("checking");
  const [error, setError] = useState<string | null>(null);
  const [completed, setCompleted] = useState(false);
  const [policy, setPolicy] = useState<NetworkPolicyMode>("cloaked");
  const [hardware, setHardware] = useState<HardwareProbe | null>(null);
  const [recommendedPolicy, setRecommendedPolicy] = useState<NetworkPolicyMode | null>(null);
  const [installPhase, setInstallPhase] = useState<string>("");
  const [apiKeys, setApiKeys] = useState<SetupApiKeys>({
    openai_key: "",
    anthropic_key: "",
    gemini_key: "",
    groq_key: "",
    deepseek_key: "",
    mistral_key: "",
    openrouter_key: "",
  });
  const [openrouterConfigured, setOpenrouterConfigured] = useState<boolean | null>(null);

  useEffect(() => {
    getApiKeyStatus().then((status) => setOpenrouterConfigured(status.openrouter));
  }, []);

  const isNative = isTauri();

  const beginSetupProbe = useCallback(() => {
    setCompleted(false);
    setError(null);
    setPolicy(readStoredNetworkPolicy());

    // Proactively probe hardware to determine the best network policy recommendation
    setStep("probing");
    invoke("probe_hardware")
      .then((res) => {
        const hw = res as HardwareProbe;
        setHardware(hw);
        // Recommend a policy based on VRAM capability
        if (hw.vram_budget_mb < 8000) {
          setRecommendedPolicy("cloaked");
        } else {
          setRecommendedPolicy("offline");
        }
        setStep("welcome");
      })
      .catch((err) => {
        console.error("Hardware probe failed:", err);
        setHardware({ total_vram_mb: null, vram_budget_mb: 4000, reserved_vram_mb: 0, hardware_source: "fallback", hardware_fallback: true, recommended_tier: "Fallback inference budget (4GB)" });
        setRecommendedPolicy("cloaked");
        setStep("welcome");
      });
  }, []);

  useEffect(() => {
    if (hasCompletedSetup()) {
      setCompleted(true);
      return;
    }

    beginSetupProbe();
  }, [beginSetupProbe, isNative]);

  useEffect(() => {
    if (typeof window === "undefined") return;
    const handler = () => beginSetupProbe();
    window.addEventListener(SETUP_RERUN_EVENT, handler);
    return () => window.removeEventListener(SETUP_RERUN_EVENT, handler);
  }, [beginSetupProbe]);

  const handlePolicySelect = async (mode: NetworkPolicyMode) => {
    setPolicy(mode);
    setStep("providers");
  };

  const handleStartInstall = async () => {
    setStep("installing");
    try {
      storeNetworkPolicy(policy);
      await invoke("sync_network_policy", { policy });
      if (Object.values(apiKeys).some((value) => value.trim().length > 0)) {
        setInstallPhase("Saving API keys to the local Config Vault...");
        await saveApiKeys(apiKeys);
      }

      if (policy === "online" || policy === "cloaked") {
        setInstallPhase("Checking for Ollama installation...");
        const ollamaResult = (await invoke("ensure_ollama_installed")) as { status: string; version: string };
        setInstallPhase(`Ollama v${ollamaResult.version} — ${ollamaResult.status}`);

        setInstallPhase("Determining required models for your hardware...");
        const pullResult = (await invoke("pull_required_models")) as {
          models_pulled: string[];
          models_failed: string[];
        };

        if (pullResult.models_failed.length > 0) {
          setError(`Failed to download models: ${pullResult.models_failed.join(", ")}`);
          setStep("error");
          return;
        }

        setInstallPhase("Registering Determinex model swarm with Ollama...");
        await invoke("initialize_system");
      } else {
        setInstallPhase("Configuring IDE for Offline mode...");
        // Still init system, but don't pull models from internet
        await invoke("initialize_system").catch(() => {});
      }

      setStep("ready");
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : String(err));
      setStep("error");
    }
  };

  const finishSetup = () => {
    markSetupCompleted();
    setCompleted(true);
    window.location.reload();
  };

  if (completed || step === "checking") return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-[#0a0a0f]/90 backdrop-blur-md font-sans text-slate-200">
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,rgba(99,102,241,0.15)_0%,rgba(0,0,0,0)_70%)] pointer-events-none" />

      <motion.div
        initial={{ opacity: 0, y: 20, scale: 0.95 }}
        animate={{ opacity: 1, y: 0, scale: 1 }}
        className="relative w-full max-w-4xl max-h-[90vh] overflow-y-auto bg-slate-900/80 border border-indigo-500/20 rounded-2xl shadow-2xl p-8 flex flex-col"
        style={{ boxShadow: "0 25px 50px -12px rgba(0,0,0,0.5), 0 0 0 1px rgba(99,102,241,0.1)" }}
      >
        <div className="flex items-center gap-3 mb-8">
          <div className="w-10 h-10 rounded-lg bg-indigo-500/20 border border-indigo-500/40 flex items-center justify-center">
            <Zap className="w-5 h-5 text-indigo-400" />
          </div>
          <div>
            <h1 className="text-2xl font-bold tracking-tight text-white">Determinex IDE Setup</h1>
            <p className="text-sm text-slate-400">Configure your local workspace and intelligence engine</p>
          </div>
        </div>

        <AnimatePresence mode="wait">
          {step === "probing" && (
            <motion.div key="probing" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="flex flex-col items-center justify-center py-12 gap-4">
              <Loader2 className="w-8 h-8 text-indigo-400 animate-spin" />
              <p className="text-sm text-slate-400">Detecting system capabilities...</p>
            </motion.div>
          )}

          {step === "welcome" && (
            <motion.div key="welcome" initial={{ opacity: 0, x: 20 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0, x: -20 }} className="flex flex-col gap-6">
              <h2 className="text-lg font-semibold text-slate-200">Step 1: Network & Privacy Policy</h2>
              <p className="text-sm text-slate-400">How would you like Determinex to operate? This controls what data leaves your machine.</p>

              <div className="bg-slate-800/50 border border-slate-700/50 rounded-xl p-4 text-xs text-slate-400 leading-relaxed">
                <strong className="text-slate-300">What this setup does:</strong> if <a href="https://ollama.ai" target="_blank" rel="noreferrer" className="text-indigo-400 hover:underline">Ollama</a> isn&apos;t already installed, Determinex downloads and silently installs it for you (no prompts, no terminal), then pulls the model(s) it needs for your hardware. This step needs an internet connection and can take several minutes depending on model size and your connection speed.
              </div>

              {recommendedPolicy && hardware && (
                <div className="bg-indigo-500/10 border border-indigo-500/30 rounded-xl p-4 flex gap-3 text-indigo-200">
                  <Zap className="w-5 h-5 shrink-0 text-indigo-400 mt-0.5" />
                  <div className="text-sm leading-relaxed">
                    <strong>Recommendation:</strong> Based on a {hardware.total_vram_mb ? `${Math.round(hardware.total_vram_mb / 1024 * 10) / 10} GB physical VRAM` : `${Math.round(hardware.vram_budget_mb / 1024 * 10) / 10} GB fallback inference budget`} probe, we recommend <strong>{NETWORK_POLICY_COPY[recommendedPolicy].label}</strong>.
                    {recommendedPolicy === "offline"
                      ? " Your hardware provides ample headroom to run advanced reasoning models locally without slowing down your computer."
                      : " Running advanced models entirely locally on this hardware may severely slow down your computer. We highly recommend Cloaked mode to offload heavy tasks to the cloud while protecting your privacy."}
                  </div>
                </div>
              )}

              <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-2">
                {(Object.entries(NETWORK_POLICY_COPY) as [NetworkPolicyMode, typeof NETWORK_POLICY_COPY[NetworkPolicyMode]][]).map(([mode, info]) => {
                  const isRecommended = mode === recommendedPolicy;
                  return (
                    <button
                      key={mode}
                      onClick={() => handlePolicySelect(mode)}
                      className={`relative flex flex-col items-start p-5 rounded-xl border transition-all group text-left ${
                        isRecommended
                          ? "bg-indigo-900/40 border-indigo-500/60 hover:bg-indigo-900/60 hover:border-indigo-400 shadow-[0_0_15px_rgba(99,102,241,0.1)]"
                          : "border-slate-700/50 bg-slate-800/40 hover:bg-slate-800/80 hover:border-indigo-500/50"
                      }`}
                    >
                      {isRecommended && (
                        <div className="absolute -top-3 left-4 bg-indigo-500 text-white text-[10px] font-bold px-2 py-1 rounded-full uppercase tracking-wider shadow-lg">
                          Recommended
                        </div>
                      )}
                      <div className="flex items-center gap-2 mb-3 mt-1">
                        {mode === "offline" && <Shield className={`w-5 h-5 ${isRecommended ? "text-emerald-300" : "text-emerald-400"}`} />}
                        {mode === "cloaked" && <Server className={`w-5 h-5 ${isRecommended ? "text-indigo-300" : "text-indigo-400"}`} />}
                        {mode === "online" && <Cloud className={`w-5 h-5 ${isRecommended ? "text-sky-300" : "text-sky-400"}`} />}
                        <span className={`font-semibold ${isRecommended ? "text-indigo-100" : "text-white"}`}>{info.label}</span>
                      </div>
                      <p className={`text-sm mb-2 ${isRecommended ? "text-indigo-200/80" : "text-slate-300"}`}>{info.summary}</p>
                      <p className="text-xs text-slate-500 mt-auto">{info.detail}</p>
                    </button>
                  );
                })}
              </div>
            </motion.div>
          )}

          {step === "providers" && (
            <motion.div key="providers" initial={{ opacity: 0, x: 20 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0, x: -20 }} className="flex flex-col gap-6">
              <div>
                <h2 className="text-lg font-semibold text-slate-200">Step 2: API Keys & Model Providers</h2>
                <p className="text-sm text-slate-400 mt-1">
                  Add cloud provider keys now, or leave them blank for local-only setup. Keys are stored by the native Config Vault and can be changed later.
                </p>
              </div>

              {/* OpenRouter — real state, not assumed */}
              {openrouterConfigured ? (
                <div className="rounded-xl border border-green-500/30 bg-green-500/10 p-4 flex gap-3">
                  <Zap className="w-5 h-5 text-green-400 flex-shrink-0 mt-0.5" />
                  <div>
                    <p className="text-sm font-semibold text-green-200 mb-1">
                      OpenRouter — Already Configured ✓
                    </p>
                    <p className="text-xs text-green-300/80 leading-relaxed">
                      An <code className="font-mono bg-black/30 px-1 rounded">openrouter</code> key is already saved.
                      Roles can route through it via <code className="font-mono bg-black/30 px-1 rounded">litellm_config.yaml</code>.
                    </p>
                  </div>
                </div>
              ) : (
                <label className="rounded-xl border border-green-500/30 bg-green-500/10 p-4 flex flex-col gap-2">
                  <span className="flex items-center gap-2 text-xs font-semibold uppercase tracking-wider text-green-200">
                    <Zap className="w-3.5 h-3.5 text-green-400" /> OpenRouter (optional free tier)
                  </span>
                  <p className="text-xs text-green-300/80 leading-relaxed">
                    Add an OpenRouter key to unlock a range of free-tier models with no credit card
                    required. Get one at openrouter.ai/keys.
                  </p>
                  <input
                    type="password"
                    value={apiKeys.openrouter_key}
                    onChange={(event) => setApiKeys((current) => ({ ...current, openrouter_key: event.target.value }))}
                    placeholder={policy === "offline" ? "Skipped in Offline / Local Only" : "Paste OpenRouter key, optional"}
                    disabled={policy === "offline"}
                    className="w-full rounded-lg border border-slate-700 bg-black/30 px-3 py-2 text-sm text-white placeholder:text-slate-600 outline-none focus:border-green-500 disabled:opacity-40"
                  />
                </label>
              )}

              <div>
                <p className="text-xs font-semibold uppercase tracking-wider text-slate-500 mb-3">
                  Optional: Add Paid Provider Keys
                </p>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                {[
                  ["anthropic_key", "Anthropic / Claude"],
                  ["openai_key", "OpenAI / ChatGPT"],
                  ["gemini_key", "Google Gemini"],
                  ["groq_key", "Groq"],
                  ["deepseek_key", "DeepSeek"],
                  ["mistral_key", "Mistral"],
                ].map(([key, label]) => (
                  <label key={key} className="rounded-xl border border-slate-700/50 bg-slate-800/40 p-4 flex flex-col gap-2">
                    <span className="flex items-center gap-2 text-xs font-semibold uppercase tracking-wider text-slate-300">
                      <KeyRound className="w-3.5 h-3.5 text-indigo-400" /> {label}
                    </span>
                    <input
                      type="password"
                      value={apiKeys[key as keyof SetupApiKeys]}
                      onChange={(event) => setApiKeys((current) => ({ ...current, [key]: event.target.value }))}
                      placeholder={policy === "offline" ? "Skipped in Offline / Local Only" : "Paste API key, optional"}
                      disabled={policy === "offline"}
                      className="w-full rounded-lg border border-slate-700 bg-black/30 px-3 py-2 text-sm text-white placeholder:text-slate-600 outline-none focus:border-indigo-500 disabled:opacity-40"
                    />
                  </label>
                ))}
                </div>
              </div>

              <div className="rounded-xl border border-emerald-500/20 bg-emerald-500/10 p-4 text-sm leading-relaxed text-emerald-100/80">
                <strong>Local</strong> means Ollama models run on this machine. <strong>Cloaked</strong> means cloud calls are allowed only through privacy gates that obfuscate identifiers and keep workspace boundaries explicit.
              </div>

              <div className="flex justify-end gap-3 mt-2">
                <button onClick={() => setStep("welcome")} className="px-4 py-2 rounded-lg text-sm font-medium text-slate-400 hover:text-white transition-colors">
                  Back
                </button>
                <button onClick={() => setStep("hardware")} className="px-6 py-2 rounded-lg text-sm font-medium bg-indigo-600 hover:bg-indigo-500 text-white transition-colors flex items-center gap-2">
                  Continue <ArrowRight className="w-4 h-4" />
                </button>
              </div>
            </motion.div>
          )}

          {step === "hardware" && (
            <motion.div key="hardware" initial={{ opacity: 0, x: 20 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0, x: -20 }} className="flex flex-col gap-6">
              <h2 className="text-lg font-semibold text-slate-200">Step 3: Hardware Diagnostics & Startup</h2>

              {!hardware ? (
                <div className="flex flex-col items-center justify-center py-12 gap-4">
                  <Loader2 className="w-8 h-8 text-indigo-400 animate-spin" />
                  <p className="text-sm text-slate-400">Probing system capabilities...</p>
                </div>
              ) : (
                <div className="flex flex-col gap-6">
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div className="p-4 rounded-xl bg-slate-800/50 border border-slate-700/50 flex flex-col gap-1">
                      <div className="flex items-center gap-2 text-slate-400 mb-1">
                        <Cpu className="w-4 h-4" />
                        <span className="text-xs font-semibold uppercase tracking-wider">Physical VRAM</span>
                      </div>
                      <span className="text-2xl font-bold text-white">{hardware.total_vram_mb ? `${Math.round(hardware.total_vram_mb / 1024 * 10) / 10} GB` : "Unknown"}</span>
                      <span className="text-xs text-slate-500">{hardware.hardware_fallback ? "Probe unavailable; using fallback budget" : `Detected by ${hardware.hardware_source ?? "hardware probe"}`}</span>
                    </div>

                    <div className="p-4 rounded-xl bg-slate-800/50 border border-slate-700/50 flex flex-col gap-1">
                      <div className="flex items-center gap-2 text-slate-400 mb-1">
                        <Cpu className="w-4 h-4" />
                        <span className="text-xs font-semibold uppercase tracking-wider">Inference Budget</span>
                      </div>
                      <span className="text-2xl font-bold text-white">{Math.round(hardware.vram_budget_mb / 1024 * 10) / 10} GB</span>
                      <span className="text-xs text-slate-500">{hardware.reserved_vram_mb ? `${Math.round(hardware.reserved_vram_mb / 1024 * 10) / 10} GB reserved for OS/GPU overhead` : "Conservative usable budget"}</span>
                    </div>

                    <div className="p-4 rounded-xl bg-slate-800/50 border border-slate-700/50 flex flex-col gap-1">
                      <div className="flex items-center gap-2 text-slate-400 mb-1">
                        <HardDrive className="w-4 h-4" />
                        <span className="text-xs font-semibold uppercase tracking-wider">Recommended Tier</span>
                      </div>
                      <span className="text-lg font-bold text-white truncate" title={hardware.recommended_tier}>
                        {hardware.recommended_tier.split(" | ")[0].replace("engineer=", "")}
                      </span>
                      <span className="text-xs text-slate-500">Auto-selected loadout</span>
                    </div>
                  </div>

                  {policy === "offline" && (
                    <div className="p-4 rounded-xl bg-amber-500/10 border border-amber-500/20 flex gap-3 text-amber-200/80">
                      <AlertTriangle className="w-5 h-5 shrink-0 text-amber-500" />
                      <div className="text-sm leading-relaxed">
                        You selected <strong>Offline Mode</strong>. Determinex will rely entirely on the hardware shown above, and will skip downloading online models during this setup.
                      </div>
                    </div>
                  )}

                  <div className="rounded-xl border border-slate-700/50 bg-slate-800/30 p-4">
                    <div className="text-xs font-semibold uppercase tracking-wider text-slate-300 mb-2">Setup will run</div>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-2 text-xs text-slate-400">
                      <div className="rounded-lg bg-black/25 border border-white/5 px-3 py-2">Ollama install/start check</div>
                      <div className="rounded-lg bg-black/25 border border-white/5 px-3 py-2">Required local model pull/build</div>
                      <div className="rounded-lg bg-black/25 border border-white/5 px-3 py-2">Role routing and startup validation</div>
                    </div>
                  </div>

                  <div className="flex justify-end gap-3 mt-4">
                    <button onClick={() => setStep("welcome")} className="px-4 py-2 rounded-lg text-sm font-medium text-slate-400 hover:text-white transition-colors">
                      Back
                    </button>
                    <button onClick={handleStartInstall} className="px-6 py-2 rounded-lg text-sm font-medium bg-indigo-600 hover:bg-indigo-500 text-white transition-colors flex items-center gap-2">
                      Start Setup <ArrowRight className="w-4 h-4" />
                    </button>
                  </div>
                </div>
              )}
            </motion.div>
          )}

          {step === "installing" && (
            <motion.div key="installing" initial={{ opacity: 0, scale: 0.95 }} animate={{ opacity: 1, scale: 1 }} className="flex flex-col items-center justify-center py-16 gap-6 text-center">
              <div className="relative">
                <div className="w-16 h-16 rounded-full border-2 border-indigo-500/20 border-t-indigo-500 animate-spin" />
                <div className="absolute inset-0 flex items-center justify-center">
                  <Zap className="w-6 h-6 text-indigo-400 animate-pulse" />
                </div>
              </div>
              <div className="flex flex-col gap-2">
                <h2 className="text-xl font-bold text-white">Configuring Environment</h2>
                <p className="text-sm text-indigo-300 font-mono">{installPhase}</p>
                <p className="text-xs text-slate-500 max-w-md mx-auto mt-2">
                  This may take several minutes if large model weights are being downloaded. Do not close the window.
                </p>
              </div>
            </motion.div>
          )}

          {step === "error" && (
            <motion.div key="error" initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="flex flex-col gap-4 items-center text-center py-8">
              <div className="w-16 h-16 rounded-full bg-red-500/20 flex items-center justify-center mb-2">
                <X className="w-8 h-8 text-red-500" />
              </div>
              <h2 className="text-xl font-bold text-white">Setup Failed</h2>
              <p className="text-sm text-red-400 bg-red-950/50 border border-red-500/30 p-4 rounded-lg max-w-lg font-mono">
                {error}
              </p>
              <button onClick={() => setStep("welcome")} className="mt-6 px-6 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-white">
                Try Again
              </button>
            </motion.div>
          )}

          {step === "ready" && (
            <motion.div key="ready" initial={{ opacity: 0, scale: 0.95 }} animate={{ opacity: 1, scale: 1 }} className="flex flex-col items-center justify-center py-12 gap-6 text-center">
              <div className="w-20 h-20 rounded-full bg-emerald-500/20 flex items-center justify-center mb-2">
                <Check className="w-10 h-10 text-emerald-500" />
              </div>
              <div className="flex flex-col gap-2">
                <h2 className="text-2xl font-bold text-white">System Ready</h2>
                <p className="text-sm text-slate-400">Determinex is fully configured for your environment.</p>
              </div>
              <button onClick={finishSetup} className="mt-4 px-8 py-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold tracking-wide flex items-center gap-2 transition-all hover:scale-105 active:scale-95 shadow-lg shadow-emerald-500/20">
                Launch IDE <ArrowRight className="w-5 h-5" />
              </button>
            </motion.div>
          )}
        </AnimatePresence>
      </motion.div>
    </div>
  );
}
