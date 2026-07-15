import React, { useState, useEffect, useCallback } from "react";
import {
  Check,
  Zap,
  Plus,
  X,
  ListTodo,
  Code2,
  Terminal as TerminalIcon,
  Brain,
  Sparkles,
  ChevronDown,
} from "lucide-react";
import {
  createTodo,
  toggleTodo as apiToggleTodo,
  deleteTodo as apiDeleteTodo,
  getKnowledgeSuggestions,
} from "@/lib/api";

export const IdeationBoard = ({
  readinessScore,
  setReadinessScore,
  activeThreadId,
  setActiveThreadId,
  threadHistory,
  handlePromote,
  todos,
  setTodos,
}: {
  readinessScore: number;
  setReadinessScore: (val: number) => void;
  activeThreadId: string;
  setActiveThreadId: (id: string) => void;
  threadHistory: { id: string; title: string; updated: string }[];
  handlePromote: (id: string, hist: string) => void;
  todos: Array<{ id: number; text: string; done: boolean }>;
  setTodos: React.Dispatch<
    React.SetStateAction<Array<{ id: number; text: string; done: boolean }>>
  >;
}) => {
  const [newTodo, setNewTodo] = useState("");
  const [brainSuggestions, setBrainSuggestions] = useState<{ text: string; relevance: number }[]>(
    []
  );
  const [brainLoading, setBrainLoading] = useState(false);
  const [showBrain, setShowBrain] = useState(true);

  // Recalculate readiness score automatically when todos change
  useEffect(() => {
    if (todos.length === 0) {
      setReadinessScore(0);
      return;
    }
    const completed = todos.filter((t) => t.done).length;
    let score = Math.floor((completed / todos.length) * 100);
    if (score < 10) score = 10;
    setReadinessScore(score);
  }, [todos, setReadinessScore]);

  // Query brain for contextual suggestions when thread changes
  const fetchBrainSuggestions = useCallback(async () => {
    const thread = threadHistory.find((t) => t.id === activeThreadId);
    if (!thread || !thread.title) return;

    setBrainLoading(true);
    try {
      const result = await getKnowledgeSuggestions(thread.title);
      if (result.suggestions && result.suggestions.length > 0) {
        const existingTexts = new Set(todos.map((t) => t.text.toLowerCase()));
        const filtered = result.suggestions.filter(
          (s: { text: string }) => !existingTexts.has(s.text.toLowerCase())
        );
        setBrainSuggestions(filtered.slice(0, 4));
      } else {
        setBrainSuggestions([]);
      }
    } catch {
      setBrainSuggestions([]);
    } finally {
      setBrainLoading(false);
    }
  }, [activeThreadId, threadHistory, todos]);

  useEffect(() => {
    if (activeThreadId) {
      fetchBrainSuggestions();
    }
  }, [activeThreadId, fetchBrainSuggestions]);

  const handleEscalate = () => {
    setReadinessScore(100);
    setTimeout(() => {
      handlePromote(activeThreadId, "Simulated thread history for compilation.");
    }, 800);
  };

  const toggleTodo = async (id: number) => {
    const todo = todos.find((t) => t.id === id);
    if (!todo) return;
    setTodos(todos.map((t) => (t.id === id ? { ...t, done: !t.done } : t)));
    try {
      await apiToggleTodo(id, !todo.done);
    } catch {
      setTodos(todos.map((t) => (t.id === id ? { ...t, done: todo.done } : t)));
    }
  };

  const addTodo = async (e: React.KeyboardEvent | React.MouseEvent) => {
    if ("key" in e && e.key !== "Enter") return;
    if (!newTodo.trim()) return;
    const text = newTodo.trim();
    const optimisticId = Date.now();
    setTodos([...todos, { id: optimisticId, text: text, done: false }]);
    setNewTodo("");
    try {
      const res = await createTodo(activeThreadId, text);
      if (res?.id)
        setTodos((prev) => prev.map((t) => (t.id === optimisticId ? { ...t, id: res.id } : t)));
    } catch {
      setTodos((prev) => prev.filter((t) => t.id !== optimisticId));
    }
  };

  const adoptSuggestion = async (text: string) => {
    const optimisticId = Date.now();
    setTodos((prev) => [...prev, { id: optimisticId, text, done: false }]);
    setBrainSuggestions((prev) => prev.filter((s) => s.text !== text));
    try {
      const res = await createTodo(activeThreadId, text);
      if (res?.id)
        setTodos((prev) => prev.map((t) => (t.id === optimisticId ? { ...t, id: res.id } : t)));
    } catch {
      setTodos((prev) => prev.filter((t) => t.id !== optimisticId));
    }
  };

  const removeTodo = async (id: number) => {
    const todo = todos.find((t) => t.id === id);
    if (!todo) return;
    setTodos(todos.filter((t) => t.id !== id));
    try {
      await apiDeleteTodo(id);
    } catch {
      setTodos([...todos, todo]);
    }
  };

  return (
    <div className="flex flex-col h-full w-full bg-transparent">
      <div className="px-5 py-4 border-b border-[#30363d] bg-[#0d1117] flex flex-col gap-3">
        <div>
          <span className="text-[12px] font-black uppercase tracking-[0.2em] text-cyan-400 drop-shadow-[0_0_8px_rgba(0,229,255,0.8)] flex items-center gap-2">
            <Code2 size={16} /> Concept Lab
          </span>
          <p className="text-[10px] text-cyan-300/60 mt-1 font-mono leading-relaxed">
            Active cognitive threads injected into matrix state.
          </p>
        </div>

        <div className="w-full">
          <select
            value={activeThreadId}
            onChange={(e) => setActiveThreadId(e.target.value)}
            className="w-full bg-[#010409] text-[11px] text-gray-300 border border-[#30363d] rounded p-2 outline-none focus:border-cyan-500/50 uppercase tracking-widest font-black font-sans"
          >
            {threadHistory.length === 0 && <option value="">AWAITING INJECTION...</option>}
            {threadHistory.map((t) => (
              <option key={t.id} value={t.id}>
                [{t.id.slice(0, 5)}] {t.title}
              </option>
            ))}
          </select>
        </div>
      </div>

      <div className="flex-1 p-5 overflow-y-auto w-full flex flex-col gap-5 no-scrollbar">
        {/* Readiness Gauge */}
        <div className="flex flex-col gap-2 bg-[#0b0f19] p-4 rounded-xl border border-[#30363d] shadow-inner">
          <div className="flex justify-between items-end mb-1">
            <span className="text-[10px] font-black uppercase tracking-widest text-[#CCCCCC]">
              Idea Readiness Engine
            </span>
            <span className="text-sm font-mono font-bold text-cyan-400">{readinessScore}%</span>
          </div>
          <div className="w-full bg-[#010409] h-2.5 rounded-full overflow-hidden border border-[#30363d]/50">
            <div
              className="h-full bg-cyan-500 shadow-[0_0_10px_rgba(0,229,255,0.6)] transition-all duration-500"
              style={{ width: `${readinessScore}%` }}
            />
          </div>
        </div>

        {/* Brain Suggestions Panel */}
        {activeThreadId && (
          <div className="flex flex-col gap-0 bg-gradient-to-b from-[#0d0f1a] to-[#0d1117] border border-purple-500/20 rounded-xl overflow-hidden">
            <button
              onClick={() => setShowBrain(!showBrain)}
              className="flex items-center justify-between w-full px-4 py-3 hover:bg-purple-500/5 transition-colors"
            >
              <span className="text-[10px] font-black uppercase tracking-widest text-purple-400 flex items-center gap-2">
                <Brain size={14} className={brainLoading ? "animate-pulse" : ""} />
                Brain Suggestions
                {brainSuggestions.length > 0 && (
                  <span className="text-[8px] bg-purple-500/20 text-purple-300 px-1.5 py-0.5 rounded-full border border-purple-500/30">
                    {brainSuggestions.length}
                  </span>
                )}
              </span>
              <ChevronDown
                size={12}
                className={`text-gray-500 transition-transform ${showBrain ? "rotate-180" : ""}`}
              />
            </button>

            {showBrain && (
              <div className="px-4 pb-3 flex flex-col gap-1.5">
                {brainLoading ? (
                  <div className="flex items-center gap-2 py-3 justify-center">
                    <Sparkles size={12} className="text-purple-400 animate-spin" />
                    <span className="text-[9px] text-purple-400/60 font-mono">
                      Querying vector brain...
                    </span>
                  </div>
                ) : brainSuggestions.length > 0 ? (
                  brainSuggestions.map((s, i) => (
                    <button
                      key={i}
                      onClick={() => adoptSuggestion(s.text)}
                      className="group flex items-start gap-2 p-2.5 rounded-lg border border-purple-500/10 hover:border-purple-500/40 bg-[#010409]/50 hover:bg-purple-500/5 transition-all text-left"
                    >
                      <Plus
                        size={12}
                        className="shrink-0 mt-0.5 text-purple-500/40 group-hover:text-purple-400 transition-colors"
                      />
                      <span className="text-[10px] text-gray-400 group-hover:text-gray-200 leading-relaxed transition-colors">
                        {s.text}
                      </span>
                    </button>
                  ))
                ) : (
                  <div className="py-2 text-center">
                    <span className="text-[9px] text-gray-600 font-mono italic">
                      No contextual matches in knowledge brain
                    </span>
                  </div>
                )}
              </div>
            )}
          </div>
        )}

        {/* Sculpted To-Do List */}
        <div className="flex flex-col gap-3 flex-1">
          <div className="flex justify-between items-center border-b border-[#30363d] pb-2">
            <span className="text-[10px] font-black uppercase tracking-widest text-gray-500 flex items-center gap-1.5">
              <ListTodo size={14} /> Concept Fruition Steps
            </span>
            <span className="text-[9px] font-mono text-cyan-500">
              {todos.filter((t) => t.done).length} / {todos.length}
            </span>
          </div>

          <div className="flex flex-col gap-2 min-h-[60px]">
            {todos.length === 0 ? (
              <div className="text-[10px] text-gray-500 uppercase font-mono tracking-widest text-center py-6 border border-dashed border-[#30363d] rounded-xl bg-[#010409] flex flex-col items-center justify-center gap-2">
                <TerminalIcon size={14} className="text-gray-600" />
                Awaiting AI Architecture Draft...
              </div>
            ) : (
              todos.map((todo) => (
                <div
                  key={todo.id}
                  className={`group flex items-start gap-3 p-3 rounded-xl border transition-all ${todo.done ? "bg-cyan-900/10 border-cyan-500/30" : "bg-[#0d1117] border-[#30363d] hover:border-cyan-500/50"}`}
                >
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      toggleTodo(todo.id);
                    }}
                    className="mt-0.5 shrink-0"
                  >
                    <div
                      className={`w-4 h-4 rounded border flex items-center justify-center transition-colors ${todo.done ? "bg-cyan-500 border-cyan-400 text-[#010409]" : "border-gray-600 hover:border-cyan-400 text-transparent"}`}
                    >
                      <Check
                        size={12}
                        className={todo.done ? "opacity-100" : "opacity-0"}
                        strokeWidth={3}
                      />
                    </div>
                  </button>
                  <p
                    className={`text-[11px] leading-relaxed flex-1 pt-0.5 ${todo.done ? "text-cyan-400/50 line-through" : "text-gray-300"}`}
                  >
                    {todo.text}
                  </p>
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      removeTodo(todo.id);
                    }}
                    className="text-gray-600 hover:text-red-400 opacity-0 group-hover:opacity-100 transition-opacity p-0.5 shrink-0"
                  >
                    <X size={14} />
                  </button>
                </div>
              ))
            )}
          </div>

          <div className="flex items-center gap-2 mt-2 bg-[#0d1117] border border-[#30363d] rounded-xl p-1.5 focus-within:border-cyan-500/50 transition-colors">
            <input
              type="text"
              value={newTodo}
              onChange={(e) => setNewTodo(e.target.value)}
              onKeyDown={addTodo}
              placeholder="Add a requirement..."
              className="flex-1 bg-transparent px-2 text-xs text-gray-200 outline-none placeholder-gray-600 font-mono"
            />
            <button
              onClick={addTodo}
              className="bg-[#161b22] hover:bg-cyan-900 border border-[#30363d] hover:border-cyan-500 text-gray-400 hover:text-cyan-400 p-1.5 rounded-lg transition-colors"
            >
              <Plus size={14} />
            </button>
          </div>
        </div>

        {/* Action Trigger */}
        <button
          onClick={handleEscalate}
          disabled={readinessScore < 20}
          className={`mt-4 w-full py-4 text-xs font-black uppercase tracking-[0.15em] border rounded-xl transition-all flex justify-center items-center gap-3 group ${readinessScore >= 100 ? "bg-cyan-600 text-white border-cyan-400 shadow-[0_0_20px_rgba(0,229,255,0.4)] hover:bg-cyan-500" : "bg-[#0d1117] text-gray-500 border-[#30363d] hover:text-cyan-400 hover:border-cyan-500/50 shadow-[0_0_15px_rgba(0,0,0,0.5)]"}`}
        >
          <Zap
            size={16}
            className={`${readinessScore >= 100 ? "text-white" : "text-gray-600 group-hover:text-cyan-400"} transition-colors`}
          />
          Escalate to Pack
        </button>
      </div>
    </div>
  );
};
