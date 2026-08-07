---
name: Repo Stats
description: Get basic repository stats
engine: codecargo
tools:
  - shell
inputs:
  - name: count
    type: number
    required: false
    description: Quantity of longest workflows
    default: 3
---

In this repository, create a list of the {{ count }} longest github actions workflows based on the number of lines in the file.

Then state basic information about the most recent merge into the main branch, including a brief description, files that were updated, when the change was merged, and who approved the merge.

Use the GitHub CLI or other CLI tools where possible to reduce token usage.
