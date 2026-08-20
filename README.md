# Agentic Work System

A portable, file-first system for coordinating Alan and multiple AI agents across projects without making any provider's conversation history the source of truth.

## Current milestone

Prepare the project system for portfolio management by defining and testing Project Contract v0.2, then inventorying the existing `200 - Projects` portfolio without moving or deleting material.

## Boundaries

- Obsidian holds project purpose, status, decisions, planning, and handoffs.
- This repository holds reusable schemas, templates, instructions, tools, tests, and technical documentation.
- Personal, career, and venture context does not belong in this repository.
- `claude-obsidian` is research material only. This project does not use, extend, or depend on its code or skills.
- Plugins, MCP, A2A, and autonomous orchestration are deferred until a tested workflow demonstrates a need.

## Project home

`/Users/alanc/_Vaults/Studio-Vault/200 - Projects/270 - Tech & Systems/Agentic Work System/Agentic Work System.md`

## Start here

1. Read `AGENTS.md`.
2. Read `docs/architecture.md`.
3. Read `docs/project-contract-v0.2.md` when creating or evaluating project state.
4. Consult the Obsidian project `Status.md`, `Decisions.md`, and `Handoff.md` for current state.

## Current artifacts

- `docs/project-contract-v0.2.md`: current human-readable protocol
- `docs/project-contract-v0.1.md`: superseded contract retained for reference
- `schemas/project.schema.json`: current machine-readable frontmatter schema
- `schemas/project-v0.1.schema.json`: preserved v0.1 frontmatter schema
- `templates/project/`: minimum project scaffold
- `templates/project-profiles/`: optional requirements profiles for software products and tools
- `plugins/agentic-work/`: shared Claude/Cowork and ChatGPT/Codex plugin source providing namespaced Agentic Work skills
- `plugins/agentic-work/skills/record-checkpoint/`: verify a reviewed human-created commit, synchronize the Obsidian project checkpoint, and stop
- `dist/agentic-work.plugin`: uploadable Claude/Cowork plugin package
- `.agents/plugins/marketplace.json`: repository-local Codex marketplace catalog

The earlier standalone `agentic-work-record-checkpoint` skill is superseded by the plugin capability `agentic-work:record-checkpoint`.
