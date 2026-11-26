import { cleanup, render, screen } from "@testing-library/react";
import { afterAll, afterEach, beforeAll, expect, test, vi } from "vitest";
import { invoke } from "@tauri-apps/api/core";
import { LivenessPopout } from "../LivenessPopout";

// jsdom does not implement modal dialogs. The browser suite exercises the native dialog.
beforeAll(() => {
  Object.defineProperties(HTMLDialogElement.prototype, {
    showModal: {
      configurable: true,
      value(this: HTMLDialogElement) {
        this.open = true;
      },
    },
    close: {
      configurable: true,
      value(this: HTMLDialogElement) {
        this.open = false;
      },
    },
  });
});

afterAll(() => {
  Reflect.deleteProperty(HTMLDialogElement.prototype, "showModal");
  Reflect.deleteProperty(HTMLDialogElement.prototype, "close");
});

afterEach(() => {
  cleanup();
  vi.unstubAllGlobals();
  vi.mocked(invoke).mockReset();
});

test("reports a stopped worker even when its manifest still says in progress", async () => {
  vi.stubGlobal("__TAURI_INTERNALS__", { transformCallback: vi.fn() });
  vi.mocked(invoke)
    .mockResolvedValueOnce({
      ok: true,
      data: [
        {
          session_id: "abc",
          project_name: "Demo",
          status: "in_progress",
          updated_at: "2026-08-01",
        },
      ],
    })
    .mockResolvedValueOnce({ ok: true, data: { process_crashed: true } });
  render(<LivenessPopout onClose={() => {}} />);
  expect(await screen.findByText("Worker stopped")).toBeInTheDocument();
  expect(screen.getByText("2026-08-01")).toBeInTheDocument();
});

test("a failed session lookup stays distinguishable from an empty list", async () => {
  vi.stubGlobal("__TAURI_INTERNALS__", { transformCallback: vi.fn() });
  vi.mocked(invoke).mockRejectedValueOnce(new Error("read failed"));
  render(<LivenessPopout onClose={() => {}} />);
  expect(await screen.findByRole("alert")).toHaveTextContent(
    "Could not read the local session list."
  );
  expect(screen.queryByText("No sessions have a step marked in progress.")).toBeNull();
});
