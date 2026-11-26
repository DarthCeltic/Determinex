"use client";

import { useEffect, useRef, useState } from "react";
import { getHiveSessionStatus, isTauri, listHiveSessions } from "@/lib/api";

type SessionActivity = {
  id: string;
  project: string;
  updated: string;
  status: string;
};

async function readActivity(): Promise<SessionActivity[]> {
  const sessions = await listHiveSessions();
  return Promise.all(
    sessions
      .filter((s) => s.status === "in_progress")
      .map(async (s) => {
        let status: string;
        try {
          const details = await getHiveSessionStatus(s.session_id);
          status = details.process_crashed === true ? "Worker stopped" : "Step marked in progress";
        } catch {
          status = "Worker status unavailable";
        }
        return { id: s.session_id, project: s.project_name, updated: s.updated_at, status };
      })
  );
}

export function LivenessPopout({ onClose }: { onClose: () => void }) {
  const dialog = useRef<HTMLDialogElement>(null);
  const [activity, setActivity] = useState<SessionActivity[] | null>(null);
  const [error, setError] = useState("");
  const [refresh, setRefresh] = useState(0);
  const native = isTauri();

  useEffect(() => {
    const element = dialog.current;
    element?.showModal();
    return () => element?.close();
  }, []);

  useEffect(() => {
    if (!native) return;
    let current = true;
    readActivity().then(
      (rows) => {
        if (current) {
          setActivity(rows);
          setError("");
        }
      },
      () => {
        if (current) setError("Could not read the local session list.");
      }
    );
    return () => {
      current = false;
    };
  }, [native, refresh]);

  return (
    <dialog
      ref={dialog}
      aria-labelledby="liveness-title"
      onCancel={onClose}
      className="fixed inset-0 m-auto max-h-[75vh] w-[min(32rem,90vw)] overflow-auto rounded-xl border border-[var(--dtx-code-border)] bg-[var(--dtx-code-panel)] p-5 text-gray-200 backdrop:bg-black/70"
    >
      <header className="mb-4 flex items-center justify-between gap-4">
        <h2 id="liveness-title" className="font-bold">
          Hive session activity
        </h2>
        <button type="button" className="rounded border px-2 py-1" onClick={onClose}>
          Close
        </button>
      </header>
      {!native ? (
        <p>Open the desktop app to check local workers.</p>
      ) : (
        <>
          <button
            type="button"
            className="mb-3 rounded border px-2 py-1"
            onClick={() => {
              setActivity(null);
              setError("");
              setRefresh((value) => value + 1);
            }}
          >
            Refresh
          </button>
          {error ? (
            <p role="alert">{error}</p>
          ) : activity === null ? (
            <p role="status">Checking sessions…</p>
          ) : activity.length === 0 ? (
            <p>No sessions have a step marked in progress.</p>
          ) : (
            <ul className="space-y-3">
              {activity.map((s) => (
                <li key={s.id}>
                  <strong>{s.project}</strong>
                  <p>{s.status}</p>
                  {s.updated && (
                    <p>
                      Last session update <time>{s.updated}</time>
                    </p>
                  )}
                </li>
              ))}
            </ul>
          )}
        </>
      )}
    </dialog>
  );
}
