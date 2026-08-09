---
name: Dependency Audit
description: Audit the repository's dependencies for outdated or risky pins and report findings.
engine: codecargo
tools:
  - shell
tools_requiring_approval:
  - shell
inputs:
  - name: severity
    type: string
    required: false
    description: Minimum severity to report (low, moderate, high, critical)
    default: moderate
---

Audit this repository's dependency manifests (package.json, requirements.txt, go.mod, or equivalents).

For each manifest found:

* List dependencies pinned to versions with known advisories at or above {{ severity }} severity
* Flag dependencies more than two major versions behind their latest release
* Note any dependency pinned to a git SHA or floating tag instead of a version

Use the ecosystem's own CLI (npm audit, pip-audit, govulncheck) where available. Summarize findings as a table ordered by severity, and state plainly when a manifest could not be audited and why.
