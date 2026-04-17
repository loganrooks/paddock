#!/usr/bin/env python3

"""Compatibility shim for sessions that cached the old PreToolUse hook.

The PreToolUse Bash hook has been removed from `.codex/hooks.json`. Keep this
file as a no-op until those sessions are restarted or compacted away.
"""

import sys


if __name__ == "__main__":
    sys.exit(0)
