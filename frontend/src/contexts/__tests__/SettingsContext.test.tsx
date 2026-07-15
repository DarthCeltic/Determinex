import { render, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

import { SettingsProvider } from "../SettingsContext";

const { invokeSafeMock } = vi.hoisted(() => ({
  invokeSafeMock: vi.fn(),
}));

vi.mock("@/lib/api", () => ({
  getApiKeyStatus: vi.fn().mockResolvedValue({}),
  getToolRegistry: vi.fn().mockResolvedValue({ tools: [], coverage: "0/0" }),
  checkOllamaStatus: vi.fn().mockResolvedValue({ ok: false }),
  getModelsRegistry: vi.fn().mockResolvedValue({ tiers: [] }),
  getOllamaBaseUrl: vi.fn().mockResolvedValue(null),
  saveOllamaBaseUrl: vi.fn().mockResolvedValue(undefined),
  invokeSafe: invokeSafeMock,
}));

describe("SettingsProvider", () => {
  beforeEach(() => {
    invokeSafeMock.mockReset();
    invokeSafeMock.mockResolvedValue(null);
  });

  it("syncs network policy through invokeSafe so browser mode does not crash", async () => {
    render(
      <SettingsProvider>
        <div>child</div>
      </SettingsProvider>,
    );

    await waitFor(() => {
      expect(invokeSafeMock).toHaveBeenCalledWith("sync_network_policy", {
        policy: "cloaked",
      });
    });
  });
});
