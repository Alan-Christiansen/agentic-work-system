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

## Initial project contract

The v0.1 contract will define:

- stable project identity;
- lifecycle status;
- objective and definition of done;
- current outcome and next action;
- dependencies and blockers;
- optional repository and external-tool locations;
- accepted decisions;
- task briefs and handoffs;
- agent authority boundaries.

## Capability separation

The Multi-Agent Project Protocol is foundational. The Agentic PM is one capability built on it. Specialist roles such as marketing, research, implementation, and review also consume the same protocol.

## Deferred architecture

Do not add MCP, A2A, an Obsidian plugin, autonomous scheduling, or a large knowledge-ingestion framework until a real repeated workflow failure justifies it.

## Third-party research boundary

The locally downloaded `claude-obsidian` repository informed research only. It is not a dependency or implementation base for this project.
