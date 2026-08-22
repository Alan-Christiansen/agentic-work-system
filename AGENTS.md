# Agent Instructions

## Purpose

Build and test a small, provider-neutral project protocol. Prefer demonstrated workflow value over speculative infrastructure.

## Sources of truth

- Repository implementation and technical decisions live here.
- Area and project purpose, portfolio status, accepted cross-tool decisions, and handoffs live in their Obsidian homes. The Agentic Work System project home is documented in `README.md`.
- Conversation history and provider memory are supporting context only.

## Working rules

- Read `README.md`, `docs/architecture.md`, and the applicable Area or project contract before proposing protocol or structural changes.
- Load only the context relevant to the current task.
- For ordinary PM work, establish one domain and the available-time envelope before recommending actions; do not aggregate domains unless Alan explicitly requests a cross-domain capacity review.
- Before Area or Project recommendations, reread the same-named human home; direct human wording, task markers, headings, additions, and deletions are canonical and must not be replaced or resurrected from `xPM/` or cached conversation state.
- Load a linked `xPM/Notes/AT-*` file only when its Area task is selected, blocked, due, or otherwise needs restart context; do not load optional detail during a simple home-note scan.
- Load a linked `xPM/Notes/PC-*` file only when shaping, comparing, or proposing promotion for that project candidate; do not load candidate detail during a simple home-note scan.
- Treat `xPM/` as agent coordination infrastructure. Keep human working notes, requirements, research, records, drafts, and deliverables outside it.
- Preserve recognized inline task dates, tags, priorities, and recurrence during edits. Treat plugin query views as derived interfaces, never as a second task source of truth.
- During authorized PM ingestion and review, assign `#urgent`, `#soon`, or no urgency tag based on consequences, dates, actionability, dependencies, and current commitments. Keep `#urgent` rare, remove stale urgency, and treat direct human tag edits as authoritative.
- Keep reusable machinery free of Alan's personal, career, and venture data.
- Treat the reusable repository as future-public: do not add secrets, private data, new hard-coded installation paths, or dependencies on one user's vault layout.
- Make small, reversible changes and verify them in proportion to risk.
- Preserve unrelated user changes.
- Record accepted architecture changes in `docs/architecture.md` and project-level decisions in the vault.
- End meaningful work with a concise handoff: outcome, files consulted, decisions, changed artifacts, unresolved questions, and next action.

## Explicit exclusions

- Do not use, invoke, extend, vendor, or copy from `claude-obsidian`. It was downloaded for research only.
- Do not build an Obsidian plugin, MCP server, A2A service, or autonomous orchestration layer unless the current milestone explicitly authorizes it.
- Do not create a public remote, publish a release, or build new-user installation machinery unless a later milestone explicitly authorizes it.
- Do not place personal or venture source-of-truth data in this repository.
