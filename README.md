# Agentic Work System

A portable, file-first system for coordinating Alan and multiple AI agents across projects without making any provider's conversation history the source of truth.

## Current milestone

Complete an independent review of the initial `agentic-pm` plugin and the personal/public configuration split.

## Boundaries

- Obsidian holds project purpose, status, decisions, planning, and handoffs.
- This repository holds reusable schemas, templates, instructions, tools, tests, and technical documentation.
- Personal, career, and venture context does not belong in this repository.
- The reusable core is being kept suitable for possible future public distribution, but publishing and new-user installation are not current work.
- `claude-obsidian` is research material only. This project does not use, extend, or depend on its code or skills.
- Plugins, MCP, A2A, and autonomous orchestration are deferred until a tested workflow demonstrates a need.

## Local dogfood project home

`/Users/alanc/_Vaults/Studio-Vault/200 - Projects/270 - Tech & Systems/Agentic Work System/Agentic Work System.md`

This path belongs to the current local installation and must not become a required path for other users.

## Start here

1. Read `AGENTS.md`.
2. Read `docs/architecture.md`.
3. Read `docs/project-contract.md` when creating or evaluating project state.
4. Read `docs/area-contract.md` when creating or evaluating managed Area state.
5. Consult the Obsidian project `xPM/Status.md`, `xPM/Decisions.md`, and `xPM/Handoff.md` for agent-maintained state.

## Current artifacts

- `docs/project-contract.md`: current human-readable protocol
- `docs/project-frontmatter-cheat-sheet.md`: quick reference for project fields and accepted values
- `docs/area-contract.md`: current protocol for ongoing responsibilities, Area tasks, and project candidates
- `docs/area-frontmatter-cheat-sheet.md`: quick reference for Area fields and accepted values
- `schemas/project.schema.json`: current machine-readable frontmatter schema
- `schemas/area.schema.json`: current machine-readable Area-home schema
- `templates/project/`: minimum project scaffold
- `templates/area/`: minimum managed-Area scaffold with one same-named human dashboard and an `xPM/` support bucket
- `templates/project-profiles/`: optional requirements profiles for software products and tools
- `plugins/agentic-work/`: shared Claude/Cowork and ChatGPT/Codex plugin source providing namespaced Agentic Work skills
- `plugins/agentic-work/skills/start-area/`: create or initialize an ongoing Area while preserving the Area/Project distinction
- `plugins/agentic-work/skills/start-project/`: directly create a project or promote an approved Area candidate with profile-specific scaffolding and repository setup
- `plugins/agentic-work/skills/record-checkpoint/`: verify a reviewed human-created commit, synchronize the Obsidian project checkpoint, and stop
- `plugins/agentic-pm/`: independently versioned project, Area, and portfolio-management skills
- `plugins/agentic-pm/references/operating-policy.md`: provider-neutral management rules shared by the Agentic PM skills
- `dist/agentic-work.plugin`: uploadable Claude/Cowork plugin package
- `dist/agentic-pm.plugin`: independently uploadable Agentic PM package
- `.agents/plugins/marketplace.json`: repository-local **Spectra Studio** Codex marketplace catalog

The earlier standalone `agentic-work-record-checkpoint` skill is superseded by the plugin capability `agentic-work:record-checkpoint`.
