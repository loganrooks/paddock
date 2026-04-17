# Codex Launch Truth Capture

- `label`: lane-02-docs-vs-readiness-crosswalk
- `captured_at`: 2026-04-17T00:11:54-04:00
- `db_path`: /home/rookslog/.codex/state_5.sqlite
- `selection`: worker threads created at or after 2026-04-17T00:11:35-04:00

## Requested Settings
- `model`: gpt-5.4
- `reasoning_effort`: xhigh
- `approval_mode`: never
- `sandbox_policy`: danger-full-access
- `requested_agent`: worker

## Effective Thread Rows

| thread_id | created_at | model | reasoning_effort | approval_mode | sandbox_policy | agent_role | agent_path |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 019d99a3-4c5f-7e20-83c3-c641db88302c | 2026-04-17T00:11:49-04:00 | gpt-5.4 | xhigh | never | danger-full-access | worker | - |

## Assessment
- `model`: matched requested `gpt-5.4` across 1/1 captured rows.
- `reasoning_effort`: matched requested `xhigh` across 1/1 captured rows.
- `approval_mode`: matched requested `never` across 1/1 captured rows.
- `sandbox_policy`: matched requested `danger-full-access` across 1/1 captured rows.
- `requested_agent`: preserved as operator-declared intent only. The current sqlite thread rows do not prove the named agent.
- This artifact records operator-declared requested settings beside effective thread rows. It does not replace reviewer judgment, and missing runtime fields must stay unresolved rather than being inferred.
