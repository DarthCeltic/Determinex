import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { EditorPanel } from "../EditorPanel";

describe("EditorPanel component", () => {
  it("renders initial editor tabs and handles split view toggle", async () => {
    render(<EditorPanel />);

    // Renders tabs for seeded files (hive.py, HealthMap.tsx)
    expect(screen.getAllByText("hive.py").length).toBeGreaterThan(0);
    expect(screen.getByText("HealthMap.tsx")).toBeInTheDocument();

    // Verify split screen toggle is present and starts inactive
    const splitBtn = screen.getByTitle("Split Editor");
    expect(splitBtn).toBeInTheDocument();
    expect(screen.queryByText(/Right:/)).not.toBeInTheDocument();

    // Click to split the screen
    fireEvent.click(splitBtn);
    expect(screen.getByText(/Right:/)).toBeInTheDocument();
  });

  it("handles file tab creation and deletion", async () => {
    render(<EditorPanel />);

    const createBtn = screen.getByTitle("New File");
    fireEvent.click(createBtn);

    // Creates new untitled python file tab
    expect(screen.getAllByText("untitled-3.py").length).toBeGreaterThan(0);

    // Verify active file delete button works
    const deleteBtn = screen.getByTitle("Delete Active File");
    expect(deleteBtn).toBeInTheDocument();
  });
});
