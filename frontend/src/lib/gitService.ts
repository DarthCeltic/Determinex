import { invokeSafe } from "./api";

export type GitFileStatus = "modified" | "untracked" | "staged" | "conflicted";

export type GitFile = {
  path: string;
  status: GitFileStatus;
  /** Raw porcelain status code (e.g. "M", "??", "AM"), for real status badges. */
  code: string;
  originalContent?: string;
  currentContent?: string;
};

export type GitBranch = {
  name: string;
  isCurrent: boolean;
};

export interface GitStatusResult {
  branch: string;
  /** The upstream this branch tracks (e.g. "origin/main"), if any. */
  upstream: string | null;
  files: GitFile[];
  ahead: number;
  behind: number;
}

export async function getGitStatus(cwd: string): Promise<GitStatusResult> {
  const res = await invokeSafe<GitStatusResult>("git_status", { cwd });
  if (!res) {
    throw new Error("Tauri git_status returned null");
  }
  return res;
}

export async function stageFile(cwd: string, filePath: string): Promise<void> {
  await invokeSafe("git_stage", { cwd, path: filePath });
}

export async function unstageFile(cwd: string, filePath: string): Promise<void> {
  await invokeSafe("git_unstage", { cwd, path: filePath });
}

export async function stageAll(cwd: string): Promise<void> {
  await invokeSafe("git_stage_all", { cwd });
}

export async function commitChanges(cwd: string, message: string): Promise<void> {
  await invokeSafe("git_commit", { cwd, message });
}

export async function getGitBranches(cwd: string): Promise<GitBranch[]> {
  const branches = await invokeSafe<string[]>("git_list_branches", { cwd });
  if (!branches) {
    return [];
  }
  const currentBranchRes = await getGitStatus(cwd).catch(() => null);
  const currentBranch = currentBranchRes?.branch || "";

  return branches.map((b) => ({ name: b, isCurrent: b === currentBranch }));
}

export async function createGitBranch(cwd: string, name: string): Promise<void> {
  await invokeSafe("git_create_branch", { cwd, name });
}

export async function checkoutBranch(cwd: string, name: string): Promise<void> {
  await invokeSafe("git_checkout_branch", { cwd, name });
}

export async function pushCommits(cwd: string): Promise<void> {
  await invokeSafe("git_push", { cwd });
}

export async function pullCommits(cwd: string): Promise<void> {
  await invokeSafe("git_pull", { cwd });
}
