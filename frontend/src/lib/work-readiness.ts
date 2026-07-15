import type { RoleAssignments } from "@/lib/api";

export interface InstalledModel {
  id: string;
  name: string;
  size_gb: number;
  param_size: string;
  is_determinex: boolean;
}

export type WorkReadinessStatus = "unknown" | "checking" | "ready" | "attention" | "offline";

export interface WorkReadiness {
  status: WorkReadinessStatus;
  ready: boolean;
  label: string;
  summary: string;
  details: string[];
  missingRoles: string[];
  checkedAt?: number;
}

const ROLE_LABELS: Record<keyof RoleAssignments, string> = {
  oracle: "Oracle",
  architect: "Architect",
  builder: "Builder",
  monitor: "Monitor",
};

// Each role lists the current post-rename tag first, then the legacy
// pre-rename tag as a fallback -- boxes that haven't re-pulled/re-tagged the
// renamed models yet (the legacy citadel-* tags are still installed
// alongside the new ones on this dev box) still resolve as ready.
const MODEL_ALIASES: Record<string, string[]> = {
  "local/fast": ["qwen2.5-coder:3b-instruct"],
  "local/coder": ["qwen2.5-coder:1.5b-instruct"],
  "local/smart": ["mistral"],
  "determinex/engineer": ["determinex-engineer-v11-dsl", "citadel-engineer-v11-dsl"],
  "determinex/observer": ["determinex-observer-v6-dsl", "citadel-observer-v6-dsl"],
  "determinex/sentinel": ["determinex-sentinel-v5-dsl", "citadel-sentinel-v5-dsl"],
  "determinex/qwen7b": ["qwen2.5-coder:7b-instruct"],
};

export function createWorkReadiness(status: WorkReadinessStatus): WorkReadiness {
  if (status === "checking") {
    return {
      status,
      ready: false,
      label: "Checking",
      summary: "Checking local model readiness...",
      details: [],
      missingRoles: [],
    };
  }
  return {
    status,
    ready: false,
    label: "Unknown",
    summary: "Model readiness has not been checked yet.",
    details: [],
    missingRoles: [],
  };
}

function isCloudModel(modelId: string): boolean {
  return /^(cloud|openai|anthropic|gemini|deepseek)\//.test(modelId);
}

function normalizeModelId(modelId: string): string {
  return modelId.trim().replace(/^ollama\//, "").replace(/:latest$/, "").toLowerCase();
}

function modelMatches(installed: Set<string>, expected: string): boolean {
  const target = normalizeModelId(expected);
  return installed.has(target) || installed.has(`${target}:latest`);
}

function displayModelId(modelId: string): string {
  return modelId.replace(/determinex/gi, "determinex");
}

export function expectedLocalModels(modelId: string): string[] {
  const trimmed = modelId.trim();
  if (!trimmed || isCloudModel(trimmed)) return [];
  if (MODEL_ALIASES[trimmed]) return MODEL_ALIASES[trimmed];
  return [trimmed.replace(/^ollama\//, "")];
}

export function evaluateWorkReadiness(input: {
  ollamaOk: boolean;
  ollamaError?: string;
  roles: RoleAssignments;
  models: InstalledModel[];
}): WorkReadiness {
  if (!input.ollamaOk) {
    return {
      status: "offline",
      ready: false,
      label: "Ollama Offline",
      summary: input.ollamaError || "Ollama is not reachable. Start Ollama before generating specs.",
      details: [],
      missingRoles: Object.keys(input.roles),
      checkedAt: Date.now(),
    };
  }

  const installed = new Set(
    input.models.flatMap((model) => [model.id, model.name]).map((id) => normalizeModelId(id))
  );
  const missing: string[] = [];
  const cloud: string[] = [];
  const details: string[] = [];

  (Object.keys(input.roles) as (keyof RoleAssignments)[]).forEach((role) => {
    const assignment = input.roles[role];
    if (isCloudModel(assignment)) {
      cloud.push(`${ROLE_LABELS[role]} uses ${assignment}`);
      return;
    }

    const expected = expectedLocalModels(assignment);
    const found = expected.some((modelId) => modelMatches(installed, modelId));
    if (found) {
      details.push(`${ROLE_LABELS[role]} -> ${displayModelId(assignment)}`);
    } else {
      missing.push(`${ROLE_LABELS[role]} needs ${expected.map(displayModelId).join(" or ") || displayModelId(assignment)}`);
    }
  });

  if (missing.length > 0) {
    return {
      status: "attention",
      ready: false,
      label: "Attention",
      summary: `Missing local model coverage for ${missing.length} role${missing.length === 1 ? "" : "s"}.`,
      details: missing,
      missingRoles: missing,
      checkedAt: Date.now(),
    };
  }

  if (cloud.length > 0) {
    return {
      status: "attention",
      ready: false,
      label: "Cloud Selected",
      summary: "One or more Hive roles use cloud models. Confirm API keys or switch to local roles before generating.",
      details: cloud,
      missingRoles: cloud,
      checkedAt: Date.now(),
    };
  }

  return {
    status: "ready",
    ready: true,
    label: "Model Ready",
    summary: "All local Hive roles resolve to installed Ollama models.",
    details,
    missingRoles: [],
    checkedAt: Date.now(),
  };
}

export function specGenerationBlockMessage(readiness?: WorkReadiness): string | null {
  if (!readiness || readiness.ready) return null;
  const detailLine = readiness.details.length
    ? `\n\n${readiness.details.slice(0, 3).join("\n")}`
    : "";
  return `I need model readiness fixed before I write the spec. ${readiness.summary}${detailLine}`;
}
