#!/usr/bin/env python3

import json
import subprocess
import sys
from pathlib import Path


def run_git(args, cwd):
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=cwd,
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def main():
    payload = json.load(sys.stdin)
    cwd = payload.get("cwd") or "."
    source = payload.get("source") or ""

    repo_root = run_git(["rev-parse", "--show-toplevel"], cwd)
    if not repo_root:
        return

    repo = Path(repo_root)
    branch = run_git(["branch", "--show-current"], repo_root) or "(detached)"
    status_lines = (run_git(["status", "--porcelain"], repo_root) or "").splitlines()

    tracked = 0
    untracked = 0
    for line in status_lines:
        if line.startswith("??"):
            untracked += 1
        elif line.strip():
            tracked += 1

    reminders = []
    if branch == "main":
        reminders.append("You are on `main`; prefer a scoped branch for substantive work.")
    if tracked or untracked:
        reminders.append(
            f"Working tree is not clean: {tracked} tracked change(s), {untracked} untracked item(s)."
        )

    state_path = repo / ".planning" / "STATE.md"
    if state_path.exists():
        state_text = state_path.read_text()
        if "Replanning required before execution" in state_text:
            reminders.append(
                "Phase 01 is still at a pre-rerun boundary: run fresh discuss + planning before execution."
            )
    if source == "resume":
        reminders.append(
            "This is a resumed session; for load-bearing work, re-check `.planning/SESSION-REENTRY-CHECKLIST.md`."
        )

    if not reminders:
        return

    message = "Repo guardrails:\n- " + "\n- ".join(reminders)
    output = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": message,
        }
    }
    sys.stdout.write(json.dumps(output))


if __name__ == "__main__":
    main()
