"use client";
import { useState, useEffect } from "react";
import { invokeSafe, isTauri } from "@/lib/api";

export interface BootstrapState {
  isBootstrapping: boolean;
  bootTier: string | null;
  bootError: string | null;
  bootProgress: number;
  dismissBootError: () => void;
}

export function useBootstrap(): BootstrapState {
  const [isBootstrapping, setIsBootstrapping] = useState(true);
  const [bootTier, setBootTier] = useState<string | null>(null);
  const [bootError, setBootError] = useState<string | null>(null);
  const [bootProgress, setBootProgress] = useState(0);

  useEffect(() => {
    if (!isTauri()) {
      setIsBootstrapping(false);
      return;
    }
    // Stages mirror the sequence in ipc_bootstrap.rs:
    //   0→20%  Docker check   (~500ms)
    //   20→45% Ollama verify  (~1s)
    //   45→65% VRAM probe     (~500ms)
    //   65→88% Model checks   (~5-30s)
    //   88→97% Determinex tags   (~1s)
    const stages: [number, number][] = [
      [20, 500],
      [45, 1500],
      [65, 2500],
      [88, 8000],
      [97, 12000],
    ];
    const timers: ReturnType<typeof setTimeout>[] = [];
    stages.forEach(([pct, delay]) => {
      timers.push(setTimeout(() => setBootProgress(pct), delay));
    });
    invokeSafe<{ tier: string }>("initialize_system")
      .then((result) => {
        timers.forEach(clearTimeout);
        if (result) setBootTier(result.tier);
        setBootProgress(100);
        setTimeout(() => setIsBootstrapping(false), 300);
      })
      .catch((err: unknown) => {
        timers.forEach(clearTimeout);
        setBootError(String(err));
        setIsBootstrapping(false);
      });
    return () => timers.forEach(clearTimeout);
  }, []);

  return {
    isBootstrapping,
    bootTier,
    bootError,
    bootProgress,
    dismissBootError: () => setIsBootstrapping(false),
  };
}
