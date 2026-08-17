# Agentic Work System

A portable, file-first system for coordinating Alan and multiple AI agents across projects without making any provider's conversation history the source of truth.

## Current milestone

Define and test the v0.1 Multi-Agent Project Protocol. A successful test allows one agent to begin a bounded task, another to continue it, and a third to review it using saved project state.

## Boundaries

- Obsidian holds project purpose, status, decisions, planning, and handoffs.
- This repository holds reusable schemas, templates, instructions, tools, tests, and technical documentation.
- Personal, career, and venture context does not belong in this repository.
- `claude-obsidian` is research material only. This project does not use, extend, or depend on its code or skills.
- Plugins, MCP, A2A, and autonomous orchestration are deferred until a tested workflow demonstrates a need.

## Project home

`/Users/alanc/_Vaults/💭 Studio-Main/200 - Projects/270 - Tech & Systems/Agentic Work System/Agentic Work System.md`

## Start here

1. Read `AGENTS.md`.
2. Read `docs/architecture.md`.
3. Read `docs/project-contract-v0.1.md` when creating or evaluating project state.
4. Consult the Obsidian project `Status.md`, `Decisions.md`, and `Handoff.md` for current state.

## v0.1 artifacts

- `docs/project-contract-v0.1.md`: human-readable protocol
- `schemas/project.schema.json`: machine-readable frontmatter schema
- `templates/project/`: minimum project scaffold
