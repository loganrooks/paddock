#!/usr/bin/env python3

import json
import re
import sys


DENY_PATTERNS = [
    (r"\bgit\s+reset\s+--hard\b", "Blocked destructive git reset."),
    (r"\bgit\s+checkout\s+--\b", "Blocked destructive git checkout restore."),
    (r"\bgit\s+restore\b.*\s--\s", "Blocked broad git restore against tracked files."),
    (r"\bgit\s+clean\b.*-[^- \n]*f[^ \n]*d", "Blocked destructive git clean."),
    (r"\brm\s+-rf\s+(\.|\*|/|~|--no-preserve-root|/\*|\./)", "Blocked destructive rm -rf command."),
    (r"\bfind\s+\.\s+.*-delete\b", "Blocked broad find -delete command."),
]


def main():
    payload = json.load(sys.stdin)
    command = (((payload.get("tool_input") or {}).get("command")) or "").strip()

    if not command:
        return

    for pattern, reason in DENY_PATTERNS:
        if re.search(pattern, command):
            output = {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": reason,
                }
            }
            sys.stdout.write(json.dumps(output))
            return


if __name__ == "__main__":
    main()
