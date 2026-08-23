# Architecture

## Objective

Provide the smallest durable contract that allows humans and heterogeneous AI agents to understand, continue, and review project work.

See [System Architecture](system-architecture.md) for the editable Excalidraw overview.

## System layers

1. **Data:** Area and project definitions, goals, status, decisions, context, and deliverables in their appropriate human-owned locations.
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
3. Area- or project-local `AGENTS.md`, when present
4. Area or project home
5. `xPM/Status.md` and the latest `xPM/Handoff.md`
6. `xPM/Decisions.md` when the task could affect or reopen a prior PM-governance choice
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

## Work contracts

The current v0.2 contract is defined in `project-contract.md`. Its machine-readable project-home schema is `../schemas/project.schema.json`, the copyable minimum scaffold is under `../templates/project/`, and optional requirements profiles are under `../templates/project-profiles/`. Canonical contract and schema filenames remain stable; Git history and release tags preserve superseded versions.

The contract standardizes stable identity, lifecycle status, objective and definition of done, current outcome and next action, blockers, optional repository locations, accepted decisions, handoffs, context loading, and agent authority boundaries. v0.2 adds explicit Agentic PM scope, a small set of project profiles, explicit income relevance, and a project-local assets boundary.

Portfolio eligibility and lifecycle are independent. `pm_scope` determines whether the Agentic PM may use a project in portfolio analysis; `status` continues to describe the project's lifecycle. A missing v0.2 classification is treated as an inventory gap, not permission to load or prioritize the project.

Area Contract v0.1 is defined in `area-contract.md`. Its schema is `../schemas/area.schema.json`, and its scaffold is under `../templates/area/`. Areas represent ongoing responsibilities without a definition of done. The same-named Area home is its human dashboard, containing separate Tasks and Proposed Projects sections.

Projects and Areas remain distinct. An Area task may be scheduled without creating a project. A proposed project remains outside the active portfolio until Alan and the Agentic PM explicitly agree to promote it. Promotion creates a normal project record, preserves a link to the originating Area and Dashboard proposal or PM Note, and applies Project Contract v0.2.

Agentic PM is one reusable capability, not one continuously loaded global manager. Normal PM operation selects a single domain, loads only explicitly managed state within that domain, and sizes recommendations to the time and attention available for that session. Availability is transient input rather than durable Area metadata.

Cross-domain coordination is an optional, explicitly invoked capacity view. It compares compact commitments to help allocate attention among domains, then returns detailed management to the selected domain scope.

The same-named Area or Project home is user-owned plain Markdown and the only required human-facing PM file. Area homes include quick Tasks and free-form Proposed Projects; Project homes include directly editable Tasks and the finishable project definition. Humans can edit these files directly; agents discover changes by rereading them before PM work. Absence is authoritative, so `xPM/`, older conversations, and handoffs cannot resurrect deleted human state.

Task detail uses progressive disclosure. Visible home-note checklists stay one line per task. An optional linked `xPM/Notes/AT-*` file holds restart details only for an Area task that earns them, and agents load it only when needed.

Project-candidate detail follows the same progressive-disclosure pattern without treating candidates as tasks. Human-authored headings and free-form descriptions remain visible under Proposed Projects; optional linked `xPM/Notes/PC-*` files hold derived shaping detail and are loaded only during candidate work.

`xPM/` is a reserved coordination bucket at the bottom of each Area or Project folder. Status, handoff, PM-governance decisions, and earned per-item support live there. Human working files remain at root or in domain-meaningful folders regardless of whether an agent helped create them.

Canonical tasks remain distributed in their relevant same-named human homes so scoped agents receive complete local context. An optional vault-level Tasks-plugin dashboard provides one eagle-eye human view by querying those sources. It may group `#urgent`, `#soon`, and untagged work, but it never owns or duplicates task state.

Optional task-tool features may enhance that surface without becoming a dependency. Inline dates, tags, priorities, recurrence, and query views are allowed, but the source checkbox line remains the portable canonical record and the full workflow must remain legible without the tool.

## Capability separation

The Multi-Agent Project Protocol is foundational. The Agentic PM is one capability built on it. Specialist roles such as marketing, research, implementation, and review also consume the same protocol.

Reusable Agentic Work skills may be distributed through thin host-specific plugin manifests around one shared skill source. The canonical package uses the `agentic-work` namespace and keeps each capability independently invocable, such as `agentic-work:record-checkpoint`. Plugin packaging is an adapter and distribution concern; the underlying project contract, skill procedure, and durable state remain provider-neutral files.

Project creation is provided by the shared `agentic-work:start-project` skill after manual direct creation and Area promotion proved the workflow. It supports explicit direct-creation and approved Area-promotion modes, preserves existing work and origin history, and instantiates only the requirements profile selected by the project.

The skill applies a stricter initialization rule than the v0.2 minimum: a new `software-product` or `software-tool` initialization is incomplete until an approved local stub repository is created or an existing local repository is verified and linked in both directions. General projects do not require a repository. Repository creation remains a reviewed local action; remotes, dependencies, commits, publication, deployment, and installation changes remain separate authority boundaries.

Area creation is provided by the shared `agentic-work:start-area` skill. It creates or initializes one Area Contract v0.1 record for an ongoing responsibility, keeps human tasks separate from inactive project candidates, preserves existing working material, and never adds a definition of done or software-project profile. Correcting a misclassified existing project remains a separate reviewed mutation; the skill does not silently move, convert, or delete project state.

## Future distribution boundary

The reusable repository may be published after personal dogfooding demonstrates sustained value. Public readiness is an architectural constraint, not a current milestone.

- Reusable contracts, schemas, templates, and skills must not depend on private context, venture records, one vault layout, or one absolute local path.
- A user's canonical Area and project records remain in their own Obsidian vault or equivalent document system; they are not bundled into the reusable repository.
- A complete installation currently has two sides: reusable repository and agent-plugin machinery, plus user-owned Obsidian records instantiated from the contracts.
- Future bootstrap tooling may initialize the reusable repository side and the user's Obsidian-side records while preserving that ownership boundary.
- A companion Obsidian plugin may eventually become a thin installation or navigation adapter. It must not become the source of truth or a prerequisite for the plain-file protocol.
- Public documentation, packaging, installation, licensing, remote creation, and release workflows remain deferred until the dogfooded manual workflow stabilizes.

## Deferred architecture

Do not add MCP, A2A, an Obsidian plugin, autonomous scheduling, a large knowledge-ingestion framework, or public-release machinery until a real repeated workflow need justifies it and the milestone explicitly authorizes it.

## Third-party research boundary

The locally downloaded `claude-obsidian` repository informed research only. It is not a dependency or implementation base for this project.
