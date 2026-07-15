import React, { useEffect, useState } from "react";
import { invokeSafe } from "../lib/api";
import { PlayCircle, StopCircle, RefreshCw, Eye, FileText, CheckCircle, XCircle, Clock } from "lucide-react";

export function AgentTrace() {
  const [sessions, setSessions] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [actionError, setActionError] = useState<string | null>(null);

  const fetchSessions = async () => {
    try {
      const res = await invokeSafe<any[]>("list_hive_sessions", {});
      if (res) setSessions(res);
    } catch (e) {
      console.error("Failed to list sessions", e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchSessions();
    const int = setInterval(fetchSessions, 10000);
    return () => clearInterval(int);
  }, []);

  const handleAction = async (action: string, sessionId: string) => {
    setActionError(null);
    try {
      await invokeSafe(`${action}_session`, { payload: { session_id: sessionId } });
      await fetchSessions();
    } catch (e) {
      setActionError(`Failed to ${action} session ${sessionId.substring(0, 8)}: ${e}`);
    }
  };

  return (
    <div className="flex flex-col h-full bg-[#0d1117] text-[#c9d1d9] p-6 overflow-y-auto">
      <div className="flex items-center space-x-3 mb-6 border-b border-[#30363d] pb-4">
        <ActivityIcon className="w-6 h-6 text-emerald-400" />
        <h2 className="text-xl font-semibold text-[#f0f6fc]">Agent Job Queue</h2>
      </div>

      {actionError && (
        <div className="mb-4 px-4 py-2 rounded-lg bg-red-400/10 border border-red-400/30 text-red-300 text-sm">
          {actionError}
        </div>
      )}

      <div className="bg-[#161b22] border border-[#30363d] rounded-lg overflow-hidden">
        <table className="w-full text-left border-collapse">
          <thead>
            <tr className="border-b border-[#30363d] bg-[#21262d] text-[#8b949e] text-sm">
              <th className="px-4 py-3 font-semibold">Job ID</th>
              <th className="px-4 py-3 font-semibold">Status</th>
              <th className="px-4 py-3 font-semibold">Spec / Path</th>
              <th className="px-4 py-3 font-semibold text-right">Controls</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-[#30363d]">
            {loading && sessions.length === 0 ? (
              <tr>
                <td colSpan={4} className="px-4 py-8 text-center text-[#8b949e] italic">
                  Loading jobs...
                </td>
              </tr>
            ) : sessions.length === 0 ? (
              <tr>
                <td colSpan={4} className="px-4 py-8 text-center text-[#8b949e] italic">
                  No active or recent jobs found.
                </td>
              </tr>
            ) : (
              sessions.map((session) => (
                <tr key={session.session_id} className="hover:bg-[#21262d]/50 transition-colors">
                  <td className="px-4 py-3 font-mono text-sm text-blue-400">
                    {session.session_id.substring(0, 8)}...
                  </td>
                  <td className="px-4 py-3">
                    <StatusBadge status={session.status} />
                  </td>
                  <td className="px-4 py-3 text-sm font-mono text-[#8b949e] truncate max-w-[200px]">
                    {session.spec_path || "Anonymous Task"}
                  </td>
                  <td className="px-4 py-3 flex items-center justify-end gap-2">
                    <button
                      title="View Logs (not implemented yet)"
                      disabled
                      className="p-1.5 text-[#8b949e]/40 bg-[#21262d]/40 rounded cursor-not-allowed"
                    >
                      <FileText className="w-4 h-4" />
                    </button>
                    {session.status === "active" ? (
                      <button
                        title="Cancel Job"
                        onClick={() => handleAction("cancel", session.session_id)}
                        className="p-1.5 text-red-400 hover:text-red-300 bg-red-400/10 hover:bg-red-400/20 rounded transition-colors"
                      >
                        <StopCircle className="w-4 h-4" />
                      </button>
                    ) : (
                      <button
                        title="Replay Job (not implemented yet)"
                        disabled
                        className="p-1.5 text-green-400/40 bg-green-400/5 rounded cursor-not-allowed"
                      >
                        <RefreshCw className="w-4 h-4" />
                      </button>
                    )}
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

function StatusBadge({ status }: { status: string }) {
  switch (status.toLowerCase()) {
    case "active":
      return <span className="flex items-center gap-1.5 text-xs text-blue-400 bg-blue-500/10 px-2 py-1 rounded-full w-fit"><Clock className="w-3 h-3 animate-spin" /> In Progress</span>;
    case "completed":
    case "success":
      return <span className="flex items-center gap-1.5 text-xs text-green-400 bg-green-500/10 px-2 py-1 rounded-full w-fit"><CheckCircle className="w-3 h-3" /> Completed</span>;
    case "failed":
    case "error":
      return <span className="flex items-center gap-1.5 text-xs text-red-400 bg-red-500/10 px-2 py-1 rounded-full w-fit"><XCircle className="w-3 h-3" /> Failed</span>;
    default:
      return <span className="flex items-center gap-1.5 text-xs text-gray-400 bg-gray-500/10 px-2 py-1 rounded-full w-fit">{status}</span>;
  }
}

function ActivityIcon(props: any) {
  return <svg {...props} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>;
}
