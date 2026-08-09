"use client";
import { useCallback, useEffect, useRef, useState } from "react";
import { LAYOUT_RESTORED_EVENT } from "./panelLayouts";

/**
 * A user-resizable, per-surface, persisted panel width.
 *
 * Ryan, live 2026-07-27: "all of these boxes are locked, they should be able to
 * be moved or changed or deleted or setup however the user wants. this is too
 * locked in."
 *
 * Zone 1's width was a hard-coded className switch -- w-[460px] for Work,
 * w-[760px] for Source Control, w-[400px] for Brain, w-[380px] for everything
 * else -- so the only way to change it was to edit the source.
 *
 * Deliberately NOT react-resizable-panels, despite it already being a
 * dependency: Zone 1 is a framer-motion `motion.div` whose inline `transform`
 * is rewritten every frame during its enter/exit spring, and PanelGroup wants
 * to own the same element's sizing and layout. The dock in this app already
 * solves the identical problem with a pointer-drag plus a localStorage commit
 * on gesture end (see addonDockLiveRef / commitAddonLayout), so this follows
 * that proven idiom instead of introducing a second, conflicting one.
 *
 * Per-key, like the dock is per-addon: widening Source Control to read a diff
 * should not also widen the narrow Proof panel.
 */

const STORAGE_PREFIX = "determinex.panelWidth.";

export interface PanelWidth {
  width: number;
  /** Attach to a drag handle's onPointerDown. */
  startResize: (e: { clientX: number; preventDefault: () => void }) => void;
  resizing: boolean;
}

export function usePanelWidth(
  key: string,
  defaultWidth: number,
  opts: { min?: number; max?: number } = {}
): PanelWidth {
  const min = opts.min ?? 260;
  const max = opts.max ?? 1200;

  const [width, setWidth] = useState(defaultWidth);
  const [resizing, setResizing] = useState(false);

  // The remembered width must also FIT. `max` is a constant with no knowledge of the window, and
  // the panel renders at an inline pixel width with `shrink-0` inside an `overflow-hidden`
  // ancestor -- so a width dragged wide on a large window, or restored from a layout saved on a
  // bigger display, is drawn past the edge and simply cut. No scrollbar appears, and the resize
  // handle rides the panel's right edge, so the one control that could fix it is off-screen too.
  //
  // Reserved space, not the whole window: the rail, the cockpit beside it and the panel's own
  // padding all need room, and a panel allowed to occupy every pixel is a panel that hides the
  // thing it sits next to.
  const RESERVED_PX = 420;
  const fit = useCallback(
    (n: number) => {
      const room =
        typeof window === "undefined" ? max : Math.max(min, window.innerWidth - RESERVED_PX);
      return Math.min(max, room, Math.max(min, n));
    },
    [min, max]
  );
  // Read the stored value in an effect, not in useState's initializer:
  // localStorage is unavailable during SSR, and reading it while rendering
  // would desync the server and client markup.
  useEffect(() => {
    if (typeof window === "undefined") return;
    const read = () => {
      const raw = window.localStorage.getItem(STORAGE_PREFIX + key);
      const n = raw ? Number(raw) : NaN;
      setWidth(fit(Number.isFinite(n) ? n : defaultWidth));
    };
    read();
    // Re-fit when the window changes. Without this a panel sized on a maximised window stays
    // that wide after a restore-down, and the overflow is invisible rather than absent -- the
    // content is drawn, then clipped, so it reads as a rendering bug rather than a size problem.
    // The stored value is deliberately NOT rewritten here: a temporary small window should not
    // permanently shrink a panel the user sized on purpose.
    const onWindowResize = () => setWidth((w) => fit(w));
    window.addEventListener("resize", onWindowResize);
    // Restoring a named layout rewrites these keys underneath us. Without this the
    // stored value would change and the panel would keep its old width until a
    // reload -- a restore that appears to do nothing.
    window.addEventListener(LAYOUT_RESTORED_EVENT, read);
    return () => {
      window.removeEventListener("resize", onWindowResize);
      window.removeEventListener(LAYOUT_RESTORED_EVENT, read);
    };
  }, [key, defaultWidth, min, max, fit]);

  // Keep the live value out of the drag closure so a fast drag can't read a
  // stale width between renders -- same reason the dock keeps a ref.
  //
  // Synced in an effect rather than assigned during render: mutating a ref while
  // rendering is a React purity violation (react-hooks/refs), and under
  // StrictMode's double-render or a future concurrent re-render it can be
  // written from a pass that is then discarded. `onMove` below also writes it
  // directly, which is legal in an event handler and keeps `onUp`'s commit exact
  // even if the last move's effect has not flushed yet.
  const widthRef = useRef(width);
  useEffect(() => {
    widthRef.current = width;
  }, [width]);

  const startResize = useCallback(
    (e: { clientX: number; preventDefault: () => void }) => {
      e.preventDefault();
      const startX = e.clientX;
      const startWidth = widthRef.current;
      setResizing(true);

      const onMove = (ev: PointerEvent) => {
        const next = fit(startWidth + (ev.clientX - startX));
        widthRef.current = next;
        setWidth(next);
      };
      const onUp = () => {
        window.removeEventListener("pointermove", onMove);
        window.removeEventListener("pointerup", onUp);
        setResizing(false);
        // Commit once per gesture, not per frame.
        try {
          window.localStorage.setItem(STORAGE_PREFIX + key, String(widthRef.current));
        } catch {
          /* storage disabled -- the width still applies for this session */
        }
      };
      window.addEventListener("pointermove", onMove);
      window.addEventListener("pointerup", onUp);
    },
    // `min`/`max` are no longer read directly here -- `fit` closes over both and is itself
    // memoised on them, so listing them again is a dependency the linter can prove is dead.
    [key, fit]
  );

  return { width, startResize, resizing };
}

/** Exported for tests and for clearing a stuck width. */
export function panelWidthStorageKey(key: string): string {
  return STORAGE_PREFIX + key;
}
