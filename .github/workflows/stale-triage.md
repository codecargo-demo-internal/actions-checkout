---
on:
  schedule:
    - cron: "0 14 * * 1"
  workflow_dispatch:
permissions:
  contents: read
  issues: write
engine: claude
tools:
  github:
    allowed:
      - list_issues
      - add_issue_comment
      - update_issue
---

# Stale issue triage

Review open issues with no activity in the last 60 days.

For each stale issue:

* If it lacks reproduction steps or has been superseded, comment asking whether it is still relevant and apply the `stale` label
* If it is a confirmed bug with clear reproduction steps, comment summarizing the current state and leave it open without the label
* Never close an issue outright — a human makes that call

Post at most ten comments per run.
