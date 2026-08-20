# Architecture

## Objective

Provide the smallest durable contract that allows humans and heterogeneous AI agents to understand, continue, and review project work.

## System layers

1. **Data:** project definitions, goals, status, decisions, context, and deliverables in their appropriate human-owned locations.
2. **Protocol:** schemas, authority boundaries, handoff conventions, and context-loading rules shared across agents.
3. **Capabilities:** PM, researcher, builder, reviewer, and future specialist skills that consume the protocol.
4. **Adapters:** provider-specific instruction files or tool integrations kept thin and replaceable.
5. **Interfaces:** conversational agents, Obsidian, command-line tools, and an optional future plugin.

## Durable boundaries

- Obsidian is the document and navigation center, not the physical home of every artifact.
- Each meaningful code or reusable-machinery project has its own Git repository.
- Project homes point to repositories and external work sites without duplicating their detailed implementation history.
- Files, not conversations, hold accepted state.

## Context path

Load context in this order:

1. Global working preferences
2. Relevant domain context
3. Project-local `AGENTS.md`, when present
4. Project home
5. `Status.md` and the latest `Handoff.md`
6. `Decisions.md` when the task could affect or reopen a prior choice
7. Current task brief or source material
8. Repository-local instructions when implementation is involved

Load deeper files only when required.

### Personal context source

An installation may provide a personal context Area outside this reusable repository. Keep the machinery and the personal data separate:

- the always-loaded entry point is a compact working profile plus a routing index;
- deeper personal, domain, and career sources load only when their routing condition matches the task;
- project facts remain in project homes rather than being copied into the personal baseline;
- derived profiles declare their authoritative sources and regeneration date;
- private context is never auto-loaded and requires direct relevance plus current-session confirmation;
- durable context discovered during work is proposed back to its canonical source rather than being left only in conversation history.

Prove this loading path manually in real project tasks before adding a skill or other automation.

## Project contract

The current v0.2 contract is defined in `project-contract-v0.2.md`. Its machine-readable project-home schema is `../schemas/project.schema.json`, the copyable minimum scaffold is under `../templates/project/`, and optional requirements profiles are under `../templates/project-profiles/`. The superseded v0.1 contract remains available as a historical reference.

The contract standardizes stable identity, lifecycle status, objective and definition of done, current outcome and next action, blockers, optional repository locations, accepted decisions, handoffs, context loading, and agent authority boundaries. v0.2 adds explicit Agentic PM scope, a small set of project profiles, explicit income relevance, and a project-local assets boundary.

Portfolio eligibility and lifecycle are independent. `pm_scope` determines whether the Agentic PM may use a project in portfolio analysis; `status` continues to describe the project's lifecycle. A missing v0.2 classification is treated as an inventory gap, not permission to load or prioritize the project.

## Capability separation

The Multi-Agent Project Protocol is foundational. The Agentic PM is one capability built on it. Specialist roles such as marketing, research, implementation, and review also consume the same protocol.

Reusable Agentic Work skills may be distributed through thin host-specific plugin manifests around one shared skill source. The canonical package uses the `agentic-work` namespace and keeps each capability independently invocable, such as `agentic-work:record-checkpoint`. Plugin packaging is an adapter and distribution concern; the underlying project contract, skill procedure, and durable state remain provider-neutral files.

Project creation remains a future capability. The v0.2 templates must be proven through manual migration before a scaffolding skill automates them.

## Deferred architecture

Do not add MCP, A2A, an Obsidian plugin, autonomous scheduling, or a large knowledge-ingestion framework until a real repeated workflow failure justifies it.

## Third-party research boundary

The locally downloaded `claude-obsidian` repository informed research only. It is not a dependency or implementation base for this project.
