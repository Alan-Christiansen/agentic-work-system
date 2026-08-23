---
# Setup reference: docs/project-frontmatter-cheat-sheet.md
type: project
schema_version: "0.2"
project_id: project-id
# planned | active | blocked | paused | complete | cancelled | archived
status: planned
domain: domain-id
# managed | excluded
pm_scope: excluded
# Required when pm_scope is managed: direct | enabling | none | unknown
# income_role: unknown
# general | software-product | software-tool
project_profile: general
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
next_action: Define the first concrete action
blocked_by: []
---
# Project Name

## Tasks

## About this Project

### Objective
What useful change will this project produce?

### Definition of done
- Describe the observable finish line.

### Boundaries
- State important inclusions, exclusions, and ownership limits.

## Requirements
Add a link to `Product Requirements` or `Technical Brief` when the selected project profile requires one.

## Work locations
Add repository or external-tool links only when they exist.
