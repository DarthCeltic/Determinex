import { renderHook, act } from "@testing-library/react";
import { describe, expect, it, beforeEach } from "vitest";
import { usePanelWidth, panelWidthStorageKey } from "../usePanelWidth";

function drag(startResize: (e: any) => void, from: number, to: number) {
  act(() => startResize({ clientX: from, preventDefault: () => {} }));
  act(() => {
    window.dispatchEvent(new PointerEvent("pointermove", { clientX: to }));
  });
  act(() => {
    window.dispatchEvent(new PointerEvent("pointerup", { clientX: to }));
  });
}

/**
 * Set the viewport explicitly.
 *
 * These tests used to inherit jsdom's 1024px default silently, which was invisible right up until
 * the width started depending on it. A test whose result turns on a value it never names is a
 * test that will one day change meaning without anyone editing it.
 */
function setViewport(px: number) {
  Object.defineProperty(window, "innerWidth", { value: px, configurable: true, writable: true });
}

function resizeWindowTo(px: number) {
  act(() => {
    setViewport(px);
    window.dispatchEvent(new Event("resize"));
  });
}

describe("usePanelWidth", () => {
  beforeEach(() => {
    localStorage.clear();
    // Wide enough that the viewport is not the binding constraint, so the min/max tests below
    // measure min/max rather than accidentally measuring the fit.
    setViewport(2400);
  });

  it("starts at the default when nothing is stored", () => {
    const { result } = renderHook(() => usePanelWidth("zone1.hive", 460));
    expect(result.current.width).toBe(460);
  });

  it("widens as the handle is dragged right", () => {
    const { result } = renderHook(() => usePanelWidth("zone1.hive", 460));
    drag(result.current.startResize, 500, 620);
    expect(result.current.width).toBe(580); // 460 + 120
  });

  it("persists per surface, so one panel's width does not move another's", () => {
    const a = renderHook(() => usePanelWidth("zone1.git", 760));
    drag(a.result.current.startResize, 100, 200);
    expect(localStorage.getItem(panelWidthStorageKey("zone1.git"))).toBe("860");
    // A different surface keeps its own default.
    const b = renderHook(() => usePanelWidth("zone1.proof", 380));
    expect(b.result.current.width).toBe(380);
  });

  it("restores a stored width on mount", () => {
    localStorage.setItem(panelWidthStorageKey("zone1.hive"), "612");
    const { result } = renderHook(() => usePanelWidth("zone1.hive", 460));
    expect(result.current.width).toBe(612);
  });

  it("clamps to min and max, including a corrupt stored value", () => {
    const { result } = renderHook(() => usePanelWidth("zone1.hive", 460, { min: 300, max: 800 }));
    drag(result.current.startResize, 500, 100); // would be 60
    expect(result.current.width).toBe(300);
    drag(result.current.startResize, 100, 2000);
    expect(result.current.width).toBe(800);

    localStorage.setItem(panelWidthStorageKey("zone1.wide"), "99999");
    const restored = renderHook(() => usePanelWidth("zone1.wide", 460, { min: 300, max: 800 }));
    expect(restored.result.current.width).toBe(800);
  });

  it("reports resizing state so the handle can show feedback", () => {
    const { result } = renderHook(() => usePanelWidth("zone1.hive", 460));
    expect(result.current.resizing).toBe(false);
    act(() => result.current.startResize({ clientX: 0, preventDefault: () => {} }));
    expect(result.current.resizing).toBe(true);
    act(() => {
      window.dispatchEvent(new PointerEvent("pointerup", { clientX: 0 }));
    });
    expect(result.current.resizing).toBe(false);
  });

  it("commits once on pointer-up, not on every move", () => {
    const { result } = renderHook(() => usePanelWidth("zone1.hive", 460));
    act(() => result.current.startResize({ clientX: 0, preventDefault: () => {} }));
    act(() => {
      window.dispatchEvent(new PointerEvent("pointermove", { clientX: 50 }));
    });
    // Mid-gesture: applied to the UI but not yet written.
    expect(result.current.width).toBe(510);
    expect(localStorage.getItem(panelWidthStorageKey("zone1.hive"))).toBeNull();
    act(() => {
      window.dispatchEvent(new PointerEvent("pointerup", { clientX: 50 }));
    });
    expect(localStorage.getItem(panelWidthStorageKey("zone1.hive"))).toBe("510");
  });

  // ── the width must also FIT ────────────────────────────────────────────────
  //
  // The panel renders at an inline pixel width with `shrink-0` inside an `overflow-hidden`
  // ancestor. A remembered width wider than the window is therefore drawn past the edge and
  // clipped -- no scrollbar, and the resize handle rides the panel's right edge so the one
  // control that could fix it is off-screen too. Observed live: the Agent Chat Room's prose,
  // agent evidence and combo buttons were all cut mid-line.

  it("never restores a stored width wider than the window can show", () => {
    setViewport(1000);
    localStorage.setItem(panelWidthStorageKey("zone1.hive"), "900");
    const { result } = renderHook(() => usePanelWidth("zone1.hive", 460));
    expect(result.current.width).toBeLessThan(900);
    expect(result.current.width).toBeLessThanOrEqual(1000);
  });

  it("re-fits when the window is made smaller", () => {
    setViewport(2400);
    const { result } = renderHook(() => usePanelWidth("zone1.hive", 460, { min: 300, max: 1200 }));
    drag(result.current.startResize, 0, 700); // 1160, fine at 2400
    expect(result.current.width).toBe(1160);

    resizeWindowTo(900);
    expect(result.current.width).toBeLessThan(1160);
    expect(result.current.width).toBeLessThan(900);
  });

  it("does not let a temporary small window permanently shrink the stored width", () => {
    setViewport(2400);
    const { result } = renderHook(() => usePanelWidth("zone1.hive", 460, { min: 300, max: 1200 }));
    drag(result.current.startResize, 0, 700);
    expect(localStorage.getItem(panelWidthStorageKey("zone1.hive"))).toBe("1160");

    // Shrinking the window adapts what is DISPLAYED; the user's deliberate choice survives.
    resizeWindowTo(900);
    expect(localStorage.getItem(panelWidthStorageKey("zone1.hive"))).toBe("1160");
  });

  it("still honours min when the window is absurdly narrow", () => {
    // A panel narrower than min is unreadable, so min wins over the fit. Clipping is the lesser
    // failure at that point -- there is genuinely no width that both fits and works.
    setViewport(320);
    const { result } = renderHook(() => usePanelWidth("zone1.hive", 460, { min: 300, max: 1200 }));
    expect(result.current.width).toBe(300);
  });
});
