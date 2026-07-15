"use client";

import { useMemo, useState } from "react";
import {
  Brain,
  CheckCircle2,
  Code2,
  FileCheck2,
  GitPullRequest,
  Play,
  RotateCcw,
  ShieldCheck,
  Sparkles,
  Terminal,
} from "lucide-react";

type TimelineStatus = "done" | "active" | "queued";

interface TimelineItem {
  title: string;
  detail: string;
  status: TimelineStatus;
}

const DEMO_TIMELINE: TimelineItem[] = [
  {
    title: "Intent captured",
    detail: "User asks Determinex to fix a failing parser edge case.",
    status: "done",
  },
  {
    title: "Files inspected",
    detail: "Repo map highlights parser.ts, parser.test.ts, and package scripts.",
    status: "done",
  },
  {
    title: "DAG generated",
    detail: "Architect creates a two-step plan: reproduce failure, patch parser.",
    status: "done",
  },
  {
    title: "Patch attempted",
    detail: "Builder edits one conditional and adds a regression test.",
    status: "done",
  },
  {
    title: "Compiler output",
    detail: "First pass fails: test expected empty input to return code 0.",
    status: "done",
  },
  {
    title: "Retry reason",
    detail: "Refine loop adds the missing empty-input branch before parsing.",
    status: "active",
  },
  {
    title: "Tests passed",
    detail: "Unit shard is ready to run after the retry patch.",
    status: "queued",
  },
  {
    title: "Diff ready",
    detail: "Changed files will appear in the review rail before apply.",
    status: "queued",
  },
  {
    title: "Training sample captured",
    detail: "Failure plus accepted fix becomes local training data.",
    status: "queued",
  },
];

const PATCH_FILES = [
  {
    path: "src/parser.ts",
    why: "Adds the empty-input guard the failed test exposed.",
    tests: "parser.empty-input, parser.flags",
  },
  {
    path: "src/parser.test.ts",
    why: "Locks the regression so the bug cannot return silently.",
    tests: "parser.empty-input",
  },
];

function statusClass(status: TimelineStatus) {
  if (status === "done") return "border-emerald-500/40 bg-emerald-500/10 text-emerald-300";
  if (status === "active") return "border-cyan-500/50 bg-cyan-500/10 text-cyan-300";
  return "border-white/10 bg-white/[0.03] text-gray-500";
}

export function GoldenLoopWorkbench({
  onOpenPlanner,
  onRunDemo,
}: {
  onOpenPlanner: () => void;
  onRunDemo: () => void;
}) {
  const [objective, setObjective] = useState("");
  const timeline = useMemo(() => DEMO_TIMELINE, []);

  return (
    <div className="flex h-full min-h-0 bg-[#080c10]">
      <div className="flex-1 min-w-0 flex flex-col">
        <div className="border-b border-[#25303a] bg-[#0d1117] px-6 py-5">
          <div className="flex items-start justify-between gap-5">
            <div className="min-w-0">
              <div className="flex items-center gap-2 text-[10px] uppercase tracking-widest text-emerald-400 font-black">
                <Sparkles size={14} /> Golden Loop
              </div>
              <h1 className="mt-2 text-[28px] leading-tight font-black text-white tracking-normal">
                Ask. Watch it prove the patch. Approve the diff.
              </h1>
              <p className="mt-2 max-w-3xl text-[12px] leading-relaxed text-gray-400">
                Determinex turns every build into a visible proof chain: plan, edit, compiler result,
                retry reason, tests, review, and local learning record.
              </p>
            </div>
            <div className="hidden xl:grid grid-cols-3 gap-2 shrink-0">
              {[
                ["Compiler", "ground truth"],
                ["Cloak", "fail-closed"],
                ["Ledger", "learns locally"],
              ].map(([a, b]) => (
                <div key={a} className="w-28 rounded-md bg-white/[0.04] p-2">
                  <div className="text-[10px] font-black text-white">{a}</div>
                  <div className="text-[8px] text-gray-500 font-mono mt-0.5">{b}</div>
                </div>
              ))}
            </div>
          </div>

          <div className="mt-5 flex gap-2">
            <input
              value={objective}
              onChange={(e) => setObjective(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter") onOpenPlanner();
              }}
              placeholder="Describe the change you want Determinex to make..."
              className="flex-1 min-w-0 rounded-lg border border-[#30363d] bg-[#010409] px-3 py-2.5 text-[12px] text-gray-200 outline-none focus:border-emerald-500/60"
            />
            <button
              onClick={onOpenPlanner}
              className="inline-flex items-center gap-2 rounded-lg border border-emerald-500/30 bg-emerald-500/15 px-3 py-2 text-[11px] font-black uppercase tracking-widest text-emerald-300 hover:bg-emerald-500/25"
            >
              <Play size={14} /> Plan
            </button>
            <button
              onClick={onRunDemo}
              className="inline-flex items-center gap-2 rounded-lg border border-cyan-500/25 bg-cyan-500/10 px-3 py-2 text-[11px] font-black uppercase tracking-widest text-cyan-300 hover:bg-cyan-500/20"
            >
              <Terminal size={14} /> Demo
            </button>
          </div>
        </div>

        <div className="grid grid-cols-1 2xl:grid-cols-[minmax(300px,0.8fr)_minmax(520px,1.2fr)] gap-4 p-4 min-h-0 flex-1 overflow-y-auto">
          <div className="min-h-[420px] overflow-hidden rounded-lg border border-[#25303a] bg-[#0d1117]">
            <div className="border-b border-[#25303a] px-4 py-3 flex items-center gap-2">
              <ShieldCheck size={14} className="text-emerald-400" />
              <div>
                <div className="text-[10px] uppercase tracking-widest text-gray-300 font-black">
                  Trust Timeline
                </div>
                <div className="text-[9px] text-gray-600 font-mono">
                  Every run should leave proof.
                </div>
              </div>
            </div>
            <div className="p-4 overflow-y-auto max-h-[560px]">
              <div className="relative">
                <div className="absolute left-[10px] top-2 bottom-2 w-px bg-white/10" />
                {timeline.map((item, i) => (
                  <div key={item.title} className="relative pl-8 pb-4 last:pb-0">
                    <div
                      className={`absolute left-0 top-0 h-5 w-5 rounded-full border flex items-center justify-center ${statusClass(item.status)}`}
                    >
                      {item.status === "done" ? (
                        <CheckCircle2 size={12} />
                      ) : item.status === "active" ? (
                        <RotateCcw size={11} />
                      ) : (
                        <span className="h-1.5 w-1.5 rounded-full bg-current" />
                      )}
                    </div>
                    <div className="text-[11px] font-bold text-gray-200">
                      {i + 1}. {item.title}
                    </div>
                    <div className="mt-1 text-[10px] text-gray-500 leading-relaxed">
                      {item.detail}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>

          <div className="flex min-h-0 flex-col gap-4">
            <div className="overflow-hidden rounded-lg border border-[#25303a] bg-[#0d1117]">
              <div className="border-b border-[#25303a] px-4 py-3 flex items-center gap-2">
                <Brain size={14} className="text-cyan-400" />
                <div>
                  <div className="text-[10px] uppercase tracking-widest text-gray-300 font-black">
                    Refine Loop
                  </div>
                  <div className="text-[9px] text-gray-600 font-mono">
                    The app explains why each retry exists.
                  </div>
                </div>
              </div>
              <div className="grid grid-cols-1 gap-3 p-4 xl:grid-cols-3">
                {[
                  [
                    "Attempt 1",
                    "Compiler failed",
                    "Borrow checker rejected a moved value. Determinex preserved the error and narrowed the fix.",
                  ],
                  [
                    "Attempt 2",
                    "Tests failed",
                    "Compile passed, but the empty-input test exposed a missing branch.",
                  ],
                  [
                    "Attempt 3",
                    "Patch ready",
                    "Retry adds the guard and prepares the diff for review.",
                  ],
                ].map(([a, b, c]) => (
                  <div key={a} className="rounded-md bg-white/[0.04] p-3">
                    <div className="text-[9px] uppercase tracking-widest text-gray-500 font-bold">
                      {a}
                    </div>
                    <div className="mt-1 text-[12px] font-black text-white">{b}</div>
                    <div className="mt-2 text-[10px] text-gray-500 leading-relaxed">{c}</div>
                  </div>
                ))}
              </div>
            </div>

            <div className="min-h-[360px] overflow-hidden rounded-lg border border-[#25303a] bg-[#0d1117]">
              <div className="border-b border-[#25303a] px-4 py-3 flex items-center justify-between gap-3">
                <div className="flex items-center gap-2">
                  <GitPullRequest size={14} className="text-purple-400" />
                  <div>
                    <div className="text-[10px] uppercase tracking-widest text-gray-300 font-black">
                      Patch Review
                    </div>
                    <div className="text-[9px] text-gray-600 font-mono">
                      Approve, reject, retry, or roll back.
                    </div>
                  </div>
                </div>
                <button className="rounded-lg border border-purple-500/30 bg-purple-500/10 px-2.5 py-1.5 text-[9px] font-black uppercase tracking-widest text-purple-300">
                  Review Diff
                </button>
              </div>
              <div className="grid min-h-0 grid-cols-1 gap-4 p-4 xl:grid-cols-[220px_minmax(320px,1fr)]">
                <div className="space-y-2">
                  {PATCH_FILES.map((file) => (
                    <div
                      key={file.path}
                      className="rounded-md bg-white/[0.04] p-3"
                    >
                      <div className="flex items-center gap-2 text-[11px] font-bold text-gray-200">
                        <Code2 size={12} className="text-purple-300" /> {file.path}
                      </div>
                      <div className="mt-2 text-[9px] text-gray-500 leading-relaxed">
                        {file.why}
                      </div>
                      <div className="mt-2 text-[8px] text-emerald-400 font-mono">
                        tests: {file.tests}
                      </div>
                    </div>
                  ))}
                </div>
                <div className="min-w-0 overflow-hidden rounded-md bg-[#010409] ring-1 ring-white/10">
                  <div className="flex items-center justify-between border-b border-white/10 px-3 py-2">
                    <div className="flex items-center gap-2 text-[9px] uppercase tracking-widest text-gray-500 font-bold">
                      <FileCheck2 size={11} /> Diff Preview
                    </div>
                    <div className="text-[8px] text-gray-600 font-mono">demo trace</div>
                  </div>
                  <pre className="max-h-[260px] overflow-auto p-3 text-[10px] leading-relaxed text-gray-400">
                    {`- if (!input) throw new Error("missing input");
+ if (!input) return { ok: true, items: [] };

+ test("empty input returns an empty result", () => {
+   expect(parse("")).toEqual({ ok: true, items: [] });
+ });`}
                  </pre>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
