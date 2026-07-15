"use client";
import * as React from "react";

import { AiRouteSelect } from "@/components/AiRouteSelect";
import { invokeSafe } from "@/lib/api";

type IdeCommandResponse = {
  command?: string;
  status?: string;
  payload?: Record<string, unknown>;
  notes?: string[];
  source_mutation_authorized?: boolean;
  training_eligible?: boolean;
};

const DEFAULT_IDEA =
  "Write add(a,b). Examples: add(2,3)==5 and add(-1,4)==3.";

function blockedResponse(command: string): IdeCommandResponse {
  return {
    command,
    status: "TAURI_RUST_COMMAND_BRIDGE_BLOCKED_BACKEND_MISSING",
    payload: {},
    notes: ["Tauri runtime or HTTP bridge not available"],
    source_mutation_authorized: false,
    training_eligible: false,
  };
}

export function GovernedIdeaCommandPanel({
  selectedModel = "auto",
  keyStatus = {},
}: {
  selectedModel?: string;
  keyStatus?: Record<string, boolean | undefined>;
}) {
  const [ideaText, setIdeaText] = React.useState(DEFAULT_IDEA);
  const [modelId, setModelId] = React.useState(selectedModel);
  const [optIn, setOptIn] = React.useState(false);
  const [preview, setPreview] = React.useState<IdeCommandResponse | null>(null);
  const [build, setBuild] = React.useState<IdeCommandResponse | null>(null);
  const [loading, setLoading] = React.useState<"preview" | "build" | null>(null);
  const [error, setError] = React.useState<string | null>(null);

  const previewOracle = React.useCallback(async () => {
    setLoading("preview");
    setError(null);
    try {
      const response = await invokeSafe<IdeCommandResponse>("preview_idea_oracle", {
        idea_text: ideaText,
        model_id: modelId,
      });
      setPreview(response ?? blockedResponse("preview_idea_oracle"));
    } catch (e) {
      setError(`Preview failed: ${e}`);
    } finally {
      setLoading(null);
    }
  }, [ideaText, modelId]);

  const buildIdea = React.useCallback(async () => {
    if (!optIn) return;
    setLoading("build");
    setError(null);
    try {
      const response = await invokeSafe<IdeCommandResponse>("build_idea", {
        idea_text: ideaText,
        opt_in: true,
        model_id: modelId,
      });
      setBuild(response ?? blockedResponse("build_idea"));
    } catch (e) {
      setError(`Build failed: ${e}`);
    } finally {
      setLoading(null);
    }
  }, [ideaText, modelId, optIn]);

  const previewPayload = preview?.payload ?? {};
  const buildPayload = build?.payload ?? {};

  return (
    <section
      data-testid="governed-idea-command-panel"
      className="flex h-full min-h-0 flex-col overflow-auto bg-[#0d1117] p-4 text-sm text-gray-200"
    >
      <header className="border-b border-white/10 pb-3">
        <h2 className="text-sm font-semibold uppercase tracking-[0.18em] text-cyan-300">
          Governed Idea Lab
        </h2>
        <p className="mt-1 text-xs text-gray-500">
          Idea to oracle to verified program. Preview is read-only; build requires explicit local-model opt-in.
        </p>
      </header>

      <label className="mt-4 flex flex-col gap-2">
        <span className="text-xs font-semibold uppercase text-gray-500">Idea</span>
        <textarea
          value={ideaText}
          onChange={(event) => setIdeaText(event.target.value)}
          data-testid="governed-idea-text"
          className="min-h-28 resize-y rounded-md border border-white/10 bg-black/40 p-3 font-mono text-xs text-gray-200 outline-none focus:border-cyan-400/60"
        />
      </label>

      <div className="mt-3 grid grid-cols-1 gap-3 md:grid-cols-[1fr_auto]">
        <AiRouteSelect value={modelId} onChange={setModelId} keyStatus={keyStatus} compact />
        <label className="flex items-end gap-2 pb-2 text-xs text-gray-400">
          <input
            type="checkbox"
            checked={optIn}
            onChange={(event) => setOptIn(event.target.checked)}
            data-testid="governed-idea-opt-in"
          />
          Local build opt-in
        </label>
      </div>

      <div className="mt-4 flex flex-wrap gap-2">
        <button
          type="button"
          onClick={() => void previewOracle()}
          disabled={loading !== null}
          data-testid="governed-idea-preview-button"
          className="rounded-md border border-cyan-400/30 bg-cyan-400/10 px-3 py-2 text-xs font-semibold uppercase text-cyan-200 disabled:opacity-50"
        >
          {loading === "preview" ? "Previewing..." : "Preview Oracle"}
        </button>
        <button
          type="button"
          onClick={() => void buildIdea()}
          disabled={!optIn || loading !== null}
          data-testid="governed-idea-build-button"
          className="rounded-md border border-emerald-400/30 bg-emerald-400/10 px-3 py-2 text-xs font-semibold uppercase text-emerald-200 disabled:opacity-40"
        >
          {loading === "build" ? "Building..." : "Build Verified Program"}
        </button>
      </div>

      {error && (
        <div
          data-testid="governed-idea-error"
          className="mt-3 rounded-md border border-red-400/30 bg-red-400/10 px-3 py-2 text-xs text-red-300"
        >
          {error}
        </div>
      )}

      <div className="mt-4 grid grid-cols-1 gap-3 lg:grid-cols-2">
        <article className="rounded-md border border-white/10 bg-black/25 p-3">
          <h3 className="text-xs font-semibold uppercase text-gray-500">Oracle Preview</h3>
          <dl className="mt-2 grid grid-cols-2 gap-1 text-xs">
            <dt className="text-gray-500">Status</dt>
            <dd data-testid="governed-idea-preview-status" className="font-mono">
              {preview?.status ?? "not run"}
            </dd>
            <dt className="text-gray-500">Checks</dt>
            <dd data-testid="governed-idea-preview-checks" className="font-mono">
              {String(previewPayload.n_checks ?? "0")}
            </dd>
            <dt className="text-gray-500">Sound</dt>
            <dd data-testid="governed-idea-preview-sound" className="font-mono">
              {String(previewPayload.oracle_sound ?? "unknown")}
            </dd>
          </dl>
          {typeof previewPayload.oracle_tests === "string" && (
            <pre
              data-testid="governed-idea-oracle-tests"
              className="mt-3 max-h-72 overflow-auto rounded bg-black/50 p-2 text-[11px] text-gray-300"
            >
              {previewPayload.oracle_tests}
            </pre>
          )}
        </article>

        <article className="rounded-md border border-white/10 bg-black/25 p-3">
          <h3 className="text-xs font-semibold uppercase text-gray-500">Build Result</h3>
          <dl className="mt-2 grid grid-cols-2 gap-1 text-xs">
            <dt className="text-gray-500">Status</dt>
            <dd data-testid="governed-idea-build-status" className="font-mono">
              {build?.status ?? "not run"}
            </dd>
            <dt className="text-gray-500">Solved</dt>
            <dd data-testid="governed-idea-build-solved" className="font-mono">
              {String(buildPayload.solved ?? "unknown")}
            </dd>
            <dt className="text-gray-500">Proof</dt>
            <dd data-testid="governed-idea-build-proof" className="font-mono">
              {String(buildPayload.proof ?? "")}
            </dd>
          </dl>
          {typeof buildPayload.program === "string" && buildPayload.program.length > 0 && (
            <pre
              data-testid="governed-idea-program"
              className="mt-3 max-h-72 overflow-auto rounded bg-black/50 p-2 text-[11px] text-gray-300"
            >
              {buildPayload.program}
            </pre>
          )}
        </article>
      </div>

      <footer className="mt-4 border-t border-white/10 pt-3 text-xs text-gray-500">
        Source mutation authorized: false. Training eligible: false. A solved result is temp-only until a separate human-approved apply gate exists.
      </footer>
    </section>
  );
}

export default GovernedIdeaCommandPanel;
