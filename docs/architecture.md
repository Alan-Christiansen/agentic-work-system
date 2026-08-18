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
- Project notes point to repositories and external work sites without duplicating their detailed implementation history.
- Files, not conversations, hold accepted state.

## Context path

Load context in this order:

1. Global working preferences
2. Relevant domain context
3. Project home
4. Current task brief or source material
5. Deeper files only when required

## Project contract

The v0.1 contract is defined in `project-contract-v0.1.md`. Its machine-readable project-home schema is `../schemas/project.schema.json`, and the copyable minimum scaffold is under `../templates/project/`.

The contract standardizes stable identity, lifecycle status, objective and definition of done, current outcome and next action, blockers, optional repository locations, accepted decisions, handoffs, context loading, and agent authority boundaries.

## Capability separation

The Multi-Agent Project Protocol is foundational. The Agentic PM is one capability built on it. Specialist roles such as marketing, research, implementation, and review also consume the same protocol.

Reusable Agentic Work skills may be distributed through thin host-specific plugin manifests around one shared skill source. The canonical package uses the `agentic-work` namespace and keeps each capability independently invocable, such as `agentic-work:record-checkpoint`. Plugin packaging is an adapter and distribution concern; the underlying project contract, skill procedure, and durable state remain provider-neutral files.

## Deferred architecture

Do not add MCP, A2A, an Obsidian plugin, autonomous scheduling, or a large knowledge-ingestion framework until a real repeated workflow failure justifies it.

## Third-party research boundary

The locally downloaded `claude-obsidian` repository informed research only. It is not a dependency or implementation base for this project.
