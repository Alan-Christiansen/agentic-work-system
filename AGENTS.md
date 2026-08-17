# Agent Instructions

## Purpose

Build and test a small, provider-neutral project protocol. Prefer demonstrated workflow value over speculative infrastructure.

## Sources of truth

- Repository implementation and technical decisions live here.
- Project purpose, portfolio status, accepted cross-tool decisions, and handoffs live in the Obsidian project home documented in `README.md`.
- Conversation history and provider memory are supporting context only.

## Working rules

- Read `README.md`, `docs/architecture.md`, and `docs/project-contract-v0.1.md` before proposing project-protocol or structural changes.
- Load only the context relevant to the current task.
- Keep reusable machinery free of Alan's personal, career, and venture data.
- Make small, reversible changes and verify them in proportion to risk.
- Preserve unrelated user changes.
- Record accepted architecture changes in `docs/architecture.md` and project-level decisions in the vault.
- End meaningful work with a concise handoff: outcome, files consulted, decisions, changed artifacts, unresolved questions, and next action.

## Explicit exclusions

- Do not use, invoke, extend, vendor, or copy from `claude-obsidian`. It was downloaded for research only.
- Do not build an Obsidian plugin, MCP server, A2A service, or autonomous orchestration layer unless the current milestone explicitly authorizes it.
- Do not place personal or venture source-of-truth data in this repository.
