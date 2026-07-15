"use client";
import React, { useState, useRef, useEffect } from "react";
import { createPortal } from "react-dom";
import {
  Archive,
  Binary,
  Bot,
  Castle,
  Check,
  CircleDashed,
  CircleDot,
  CloudRain,
  Crosshair,
  FlaskConical,
  Frame,
  Ghost,
  Grid3X3,
  Moon,
  Mountain,
  Orbit,
  RadioTower,
  Rocket,
  Shield,
  Sparkles,
  Sun,
  Telescope,
  TerminalSquare,
  Trees,
  Wrench,
} from "lucide-react";
import { useIterationTheme } from "@/contexts/IterationThemeContext";
import { SKIN_PACKS, type SkinIconKey } from "@/theme/skinPacks";

type SkinIconComponent = React.ComponentType<{
  size?: number;
  strokeWidth?: number;
  className?: string;
}>;

const SKIN_ICONS: Record<SkinIconKey, SkinIconComponent> = {
  binary: Binary,
  orbit: Orbit,
  terminal: TerminalSquare,
  radar: Crosshair,
  grid: Grid3X3,
  lens: CircleDot,
  archive: Archive,
  assistant: Bot,
  terrain: Trees,
  rain: CloudRain,
  shield: Shield,
  cave: Mountain,
  aether: Sparkles,
  frame: Frame,
  wraith: Ghost,
  ring: CircleDashed,
  test: FlaskConical,
  atlas: Telescope,
  signal: RadioTower,
  dungeon: Castle,
  mech: Rocket,
  plainDark: Moon,
  plainLight: Sun,
};

// Note: rocinante uses "orbit", lightcycle uses "grid", trex uses "terrain" — all already in SKIN_ICONS

// Skin groups for visual organization
const SKIN_GROUPS: Array<{ label: string; ids: string[] }> = [
  {
    label: "Industrial",
    ids: ["codefall", "vector", "neon", "strategy", "redlens", "raincity"],
  },
  {
    label: "Exploration",
    ids: ["orbital", "aegis", "terrain", "archive", "cave", "shelter"],
  },
  {
    label: "Signal & Aether",
    ids: ["aether", "signal", "wraith", "frame", "ring", "dungeon", "mech", "atlas", "test"],
  },
  {
    label: "Cinematic",
    ids: ["rocinante", "lightcycle", "trex"],
  },
  {
    label: "Plain",
    ids: ["plaindark", "plainlight"],
  },
];

function ColorSwatch({ color, label }: { color: string; label: string }) {
  return (
    <div
      className="h-3 w-3 rounded-sm border border-white/10 shrink-0"
      style={{ background: color }}
      title={label}
    />
  );
}

export function SkinPickerInline() {
  const { theme, setTheme, allThemes } = useIterationTheme();
  const [startingTheme, setStartingTheme] = useState(theme);
  const allById = allThemes.reduce<Record<string, string>>((acc, t) => ({ ...acc, [t]: t }), {});

  return (
    <div className="space-y-1">
      <div className="mb-3 rounded-xl border border-[var(--determinex-border)]/30 bg-black/30 p-3">
        <div className="text-[9px] font-black uppercase tracking-widest text-[var(--determinex-accent)]">
          Preview mode
        </div>
        <p className="mt-1 text-[10px] leading-relaxed text-white/45">
          Pick a skin to preview it across the IDE. Apply keeps it; Cancel returns to the skin you opened this panel with.
        </p>
        <div className="mt-3 flex gap-2">
          <button
            type="button"
            onClick={() => setStartingTheme(theme)}
            className="rounded-lg border border-emerald-400/25 bg-emerald-950/20 px-3 py-2 text-[9px] font-black uppercase tracking-widest text-emerald-300"
          >
            Apply skin
          </button>
          <button
            type="button"
            onClick={() => setTheme(startingTheme)}
            className="rounded-lg border border-white/10 bg-white/[0.03] px-3 py-2 text-[9px] font-black uppercase tracking-widest text-white/45"
          >
            Cancel preview
          </button>
        </div>
      </div>
      {SKIN_GROUPS.map((group) => {
        const groupThemes = group.ids.filter((id) => allById[id]);
        if (groupThemes.length === 0) return null;
        return (
          <div key={group.label}>
            <div className="px-1 pb-1.5 pt-3">
              <span className="font-mono text-[8px] uppercase tracking-[0.3em] text-white/30">
                {group.label}
              </span>
            </div>
            <div className="grid grid-cols-2 gap-1.5">
              {groupThemes.map((id) => {
                const t = id as keyof typeof SKIN_PACKS;
                const pack = SKIN_PACKS[t];
                if (!pack) return null;
                const Icon = SKIN_ICONS[pack.iconKey] ?? Wrench;
                const active = theme === t;
                return (
                  <button
                    key={t}
                    onClick={() => setTheme(t)}
                    title="Preview this skin"
                    className="group relative flex items-center gap-2.5 rounded-xl border px-3 py-2.5 text-left transition-all"
                    style={{
                      borderColor: active ? pack.colors.accent + "60" : "rgba(255,255,255,0.07)",
                      background: active
                        ? `linear-gradient(135deg, ${pack.colors.accentGlow}, ${pack.colors.panelStrong})`
                        : "rgba(255,255,255,0.02)",
                      boxShadow: active ? `0 0 12px ${pack.colors.accentGlow}` : undefined,
                    }}
                  >
                    <span
                      className="flex h-7 w-7 shrink-0 items-center justify-center rounded-lg border transition-all"
                      style={{
                        color: pack.colors.accent,
                        borderColor: pack.colors.border,
                        background: `linear-gradient(135deg, ${pack.colors.panelStrong}, ${pack.colors.bg})`,
                        boxShadow: active ? `0 0 10px ${pack.colors.accentGlow}` : undefined,
                      }}
                    >
                      <Icon size={14} strokeWidth={1.85} />
                    </span>
                    <span className="min-w-0 flex-1 overflow-hidden">
                      <span className={`block truncate text-[10px] font-bold ${active ? "text-white" : "text-white/55 group-hover:text-white/80"}`}>
                        {pack.label}
                      </span>
                      <span className="block truncate text-[7px] uppercase tracking-wider text-white/20">
                        {pack.cue}
                      </span>
                    </span>
                    {active && (
                      <Check size={12} strokeWidth={2.5} className="shrink-0" style={{ color: pack.colors.accent }} />
                    )}
                  </button>
                );
              })}
            </div>
          </div>
        );
      })}
    </div>
  );
}

export function ThemeSelector({ className }: { className?: string }) {
  const { theme, setTheme, allThemes, themePack } = useIterationTheme();
  const [open, setOpen] = useState(false);
  const [hoveredId, setHoveredId] = useState<string | null>(null);
  const [menuPos, setMenuPos] = useState({ x: 0, y: 0 });
  const btnRef = useRef<HTMLButtonElement>(null);
  const menuRef = useRef<HTMLDivElement>(null);
  const ActiveIcon = SKIN_ICONS[themePack.iconKey] ?? Wrench;

  useEffect(() => {
    if (!open) return;
    const close = (e: MouseEvent) => {
      const target = e.target as Node;
      if (btnRef.current?.contains(target) || menuRef.current?.contains(target)) return;
      setOpen(false);
    };
    document.addEventListener("mousedown", close);
    return () => document.removeEventListener("mousedown", close);
  }, [open]);

  const handleOpen = () => {
    if (!btnRef.current) return;
    const rect = btnRef.current.getBoundingClientRect();
    const menuHeight = Math.min(allThemes.length * 68 + 80, Math.floor(window.innerHeight * 0.82));
    const fitsBelow = rect.bottom + menuHeight < window.innerHeight;
    const rawY = fitsBelow ? rect.top : rect.bottom - menuHeight;
    const y = Math.max(12, Math.min(rawY, window.innerHeight - menuHeight - 12));
    setMenuPos({ x: rect.right + 10, y });
    setOpen((o) => !o);
  };

  const chooseTheme = (t: keyof typeof SKIN_PACKS) => {
    setTheme(t);
    setOpen(false);
  };

  // Build a map of id -> group order for sorted rendering
  const allById = allThemes.reduce<Record<string, (typeof allThemes)[number]>>(
    (acc, t) => ({ ...acc, [t]: t }),
    {}
  );

  return (
    <div className={className}>
      <button
        ref={btnRef}
        onClick={handleOpen}
        data-testid="skin-selector-trigger"
        title={`Switch skin — ${themePack.cue}`}
        className="flex cursor-pointer flex-col items-center gap-1 text-gray-500 transition-colors hover:text-white"
      >
        <span
          className="flex h-7 w-7 items-center justify-center rounded-md border transition-all"
          style={{
            color: themePack.colors.accent,
            borderColor: themePack.colors.border,
            background: `linear-gradient(135deg, ${themePack.colors.panelStrong}, ${themePack.colors.panel})`,
            boxShadow: `0 0 16px ${themePack.colors.accentGlow}`,
          }}
        >
          <ActiveIcon size={15} strokeWidth={1.8} />
        </span>
        <span className="text-[7px] font-bold uppercase leading-none tracking-normal">Skin</span>
      </button>

      {open &&
        typeof document !== "undefined" &&
        createPortal(
          <div
            ref={menuRef}
            onMouseDown={(e) => e.stopPropagation()}
            className="fixed z-[9999] overflow-hidden border backdrop-blur-xl"
            style={{
              left: menuPos.x,
              top: menuPos.y,
              width: 300,
              maxHeight: "calc(100dvh - 24px)",
              borderColor: "var(--determinex-border)",
              borderRadius: "var(--determinex-radius)",
              background: "var(--determinex-panel-glass)",
              boxShadow: "var(--determinex-shell-shadow)",
            }}
          >
            {/* Header */}
            <div className="border-b border-white/10 px-4 py-3">
              <p className="font-mono text-[8px] uppercase tracking-[0.34em] text-white/35">
                Visual Skin Pack
              </p>
              <p className="mt-0.5 text-[10px] text-white/50">
                {allThemes.length} skins · hover to preview
              </p>
            </div>

            <div className="max-h-[min(80dvh,740px)] overflow-y-auto py-1 no-scrollbar">
              {SKIN_GROUPS.map((group) => {
                const groupThemes = group.ids.filter((id) => allById[id]);
                if (groupThemes.length === 0) return null;
                return (
                  <div key={group.label}>
                    <div className="px-4 py-2 border-b border-white/5">
                      <span className="font-mono text-[8px] uppercase tracking-[0.3em] text-white/25">
                        {group.label}
                      </span>
                    </div>
                    {groupThemes.map((id) => {
                      const t = id as keyof typeof SKIN_PACKS;
                      const pack = SKIN_PACKS[t];
                      if (!pack) return null;
                      const Icon = SKIN_ICONS[pack.iconKey] ?? Wrench;
                      const active = theme === t;
                      const hovered = hoveredId === id;
                      return (
                        <button
                          key={t}
                          data-testid={`skin-selector-option-${t}`}
                          onPointerEnter={() => setHoveredId(id)}
                          onPointerLeave={() => setHoveredId(null)}
                          onPointerDownCapture={(e) => {
                            e.preventDefault();
                            e.stopPropagation();
                            chooseTheme(t);
                          }}
                          onClick={(e) => {
                            e.preventDefault();
                            chooseTheme(t);
                          }}
                          className="group flex w-full items-center gap-3 px-4 py-2.5 text-left transition-all"
                          style={{
                            background:
                              active
                                ? `linear-gradient(90deg, ${pack.colors.accentGlow}, transparent)`
                                : hovered
                                  ? `rgba(255,255,255,0.04)`
                                  : undefined,
                          }}
                        >
                          {/* Icon swatch */}
                          <span
                            className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg border transition-all"
                            style={{
                              color: pack.colors.accent,
                              borderColor: pack.colors.border,
                              background: `linear-gradient(135deg, ${pack.colors.panelStrong}, ${pack.colors.bg})`,
                              boxShadow: active || hovered ? `0 0 14px ${pack.colors.accentGlow}` : undefined,
                            }}
                          >
                            <Icon size={16} strokeWidth={1.85} />
                          </span>

                          {/* Label + cue */}
                          <span className="min-w-0 flex-1">
                            <span
                              className={`block truncate text-[10px] font-bold tracking-wide transition-colors ${
                                active ? "text-white" : "text-white/60 group-hover:text-white/85"
                              }`}
                            >
                              {pack.label}
                            </span>
                            <span className="mt-0.5 block truncate text-[8px] uppercase tracking-[0.18em] text-white/25">
                              {pack.cue}
                            </span>
                            {pack.backdropImage ? (
                              <div className="mt-2 h-10 w-24 overflow-hidden rounded-md border border-white/10 opacity-70 transition-all group-hover:opacity-100">
                                {/* eslint-disable-next-line @next/next/no-img-element */}
                                <img
                                  src={pack.backdropImage}
                                  alt={pack.label}
                                  className="h-full w-full object-cover"
                                />
                              </div>
                            ) : (
                              <div className="mt-1.5 flex gap-1">
                                <ColorSwatch color={pack.colors.bg} label="bg" />
                                <ColorSwatch color={pack.colors.accent} label="accent" />
                                <ColorSwatch color={pack.colors.accent2} label="accent2" />
                                <ColorSwatch color={pack.colors.text} label="text" />
                              </div>
                            )}
                          </span>

                          {active && (
                            <Check
                              size={13}
                              strokeWidth={2}
                              className="shrink-0"
                              style={{ color: pack.colors.accent }}
                            />
                          )}
                        </button>
                      );
                    })}
                  </div>
                );
              })}

              {/* Remaining themes not in any group */}
              {allThemes
                .filter((t) => !SKIN_GROUPS.some((g) => g.ids.includes(t)))
                .map((t) => {
                  const pack = SKIN_PACKS[t];
                  if (!pack) return null;
                  const Icon = SKIN_ICONS[pack.iconKey] ?? Wrench;
                  const active = theme === t;
                  return (
                    <button
                      key={t}
                      data-testid={`skin-selector-option-${t}`}
                      onPointerDownCapture={(e) => {
                        e.preventDefault();
                        e.stopPropagation();
                        chooseTheme(t);
                      }}
                      onClick={(e) => {
                        e.preventDefault();
                        chooseTheme(t);
                      }}
                      className="group flex w-full items-center gap-3 px-4 py-2.5 text-left transition-colors hover:bg-white/5"
                      style={{
                        background: active
                          ? `linear-gradient(90deg, ${pack.colors.accentGlow}, transparent)`
                          : undefined,
                      }}
                    >
                      <span
                        className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg border"
                        style={{
                          color: pack.colors.accent,
                          borderColor: pack.colors.border,
                          background: `linear-gradient(135deg, ${pack.colors.panelStrong}, ${pack.colors.bg})`,
                          boxShadow: active ? `0 0 14px ${pack.colors.accentGlow}` : undefined,
                        }}
                      >
                        <Icon size={16} strokeWidth={1.85} />
                      </span>
                      <span className="min-w-0 flex-1">
                        <span className={`block truncate text-[10px] font-bold ${active ? "text-white" : "text-white/55 group-hover:text-white/80"}`}>
                          {pack.label}
                        </span>
                        <span className="mt-0.5 block truncate text-[8px] uppercase tracking-[0.18em] text-white/25">
                          {pack.cue}
                        </span>
                        {pack.backdropImage ? (
                          <div className="mt-2 h-10 w-24 overflow-hidden rounded-md border border-white/10 opacity-70 transition-all group-hover:opacity-100">
                            {/* eslint-disable-next-line @next/next/no-img-element */}
                            <img
                              src={pack.backdropImage}
                              alt={pack.label}
                              className="h-full w-full object-cover"
                            />
                          </div>
                        ) : (
                          <div className="mt-1.5 flex gap-1">
                            <ColorSwatch color={pack.colors.bg} label="bg" />
                            <ColorSwatch color={pack.colors.accent} label="accent" />
                            <ColorSwatch color={pack.colors.accent2} label="accent2" />
                            <ColorSwatch color={pack.colors.text} label="text" />
                          </div>
                        )}
                      </span>
                      {active && <Check size={13} strokeWidth={2} className="shrink-0" style={{ color: pack.colors.accent }} />}
                    </button>
                  );
                })}
            </div>
          </div>,
          document.body
        )}
    </div>
  );
}
