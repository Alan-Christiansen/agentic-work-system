# Area Contract v0.1

## Purpose

This contract defines the minimum durable state required for Alan and the Agentic PM to manage an ongoing responsibility without misrepresenting it as a finishable project.

An Area has no definition of done. It may contain routine responsibilities, bounded tasks, and possible future projects. Only an explicitly approved promotion creates a project under `200 - Projects`.

## Required Area files

Every managed Area using this contract has one same-named home and four supporting notes:

```text
Area Name/
├── Area Name.md
├── Status.md
├── Dashboard.md
├── Decisions.md
└── Handoff.md
```

The canonical templates are under `templates/area/`.

### Area home

The Area home has the same base name as its parent folder. It records:

- the ongoing responsibility;
- what healthy stewardship looks like;
- important boundaries and ownership;
- links to current state and the human-facing Dashboard;
- relevant external work locations.

Do not add a definition of done. An Area is retired only when the responsibility no longer exists or belongs elsewhere.

### Status

`Status.md` records current health, the one maintenance outcome receiving attention, the next concrete action, blockers, and later concerns. `active` Area status means the responsibility exists; it does not mean the Area should consume primary focus every day.

The Area-home `status`, `next_action`, and `blocked_by` fields mirror `Status.md`. The latest Handoff recommendation matches the same next action.

### Dashboard

`Dashboard.md` is the canonical human-first working surface for bounded Area tasks and possible future projects. Alan may write, start, block, complete, drop, delete, rename, or revise its contents directly in Obsidian without invoking an agent.

The Dashboard keeps tasks and proposed projects visibly separate without splitting the human workflow across files:

```markdown
# Dashboard

## Tasks

- [ ] Do the thing

## Proposed Projects

### Possible project
Free-form intent, context, links, and notes written in the human's own language.
```

Every PM session rereads the current Dashboard before recommending work. Saved human wording, markers, headings, additions, and deletions are authoritative rather than conversation memory or older agent records.

#### Tasks

A complete task may be only one line. IDs, dates, rationale, and next-action details are optional. Agents must not ignore or rewrite a quick task merely because metadata is absent.

Keep the checklist visually tight. When a task genuinely needs restart context, generate one support note under `PM Notes/` and add a short link on the task line:

```markdown
- [!] Register with agency [[PM Notes/AT-001 - Register with agency|details]]
```

`AT` means Area Task. Alan does not need to create or manage the ID; the PM assigns it only when generating a support note. Keep sensitive values out of PM Notes.

The Markdown checkbox marker is canonical for task state:

| Marker | Meaning |
| --- | --- |
| `- [ ]` | Open and available for consideration |
| `- [/]` | In progress |
| `- [!]` | Blocked until a named condition changes |
| `- [x]` | Complete |
| `- [-]` | Intentionally dropped |

Do not duplicate task state in a separate field. If older agent text conflicts with the Dashboard marker, the marker wins. Agents must not reopen or rewrite a manually changed task without approval.

A blocked task's linked PM Note records only the minimum useful restart state: blocker, follow-up date or event, resume condition, and next action. Blocking one task does not block the entire Area or authorize activation of a proposed project.

Agents scan the Dashboard Tasks section first and load a linked task PM Note only when the task is selected, blocked, due for follow-up, or otherwise needs restart context.

Plain Markdown remains canonical. Optional task-tool dates, priorities, recurrence, tags, and query views may enhance the source task when they change behavior. Do not require a global task tag or add tags that merely repeat Area or domain location. Plugin views remain derived interfaces, not another source of truth.

#### Proposed Projects

The Dashboard's `## Proposed Projects` section contains possible future projects, not ordinary tasks. Use it when work may need its own objective, definition of done, multi-session state, decisions, handoffs, deliverables, or repository.

Alan may capture a proposed project as a heading followed by any amount of free-form intent, context, links, or notes. No ID, state field, or agent-authored structure is required:

```markdown
### Wood projects website
I want to begin with a landing page, add ecommerce later, and explore a sub-brand name.
```

Merely appearing under Proposed Projects means the idea is inactive. It does not enter the active portfolio or consume project capacity until Alan and the PM explicitly agree to promote it.

When a proposal earns structured shaping, comparison, or promotion preparation, the PM may generate one note under `PM Notes/` and link it beneath the human description:

```markdown
[[PM Notes/PC-001 - Wood projects website|PM notes]]
```

`PC` means Project Candidate. Alan does not need to create or manage the ID. The human-authored Dashboard heading and description remain authoritative for existence and intent. The linked PM Note holds derived analysis such as desired outcome, boundary, maturity, start conditions, and an eventual promoted-project link. Agents load it only when working on that proposal.

Candidate maturity may be tracked inside its PM Note using `captured`, `candidate`, or `ready`. These are PM interpretations, not activation. `ready` never means active; promotion remains an explicit human decision.

### Deletion and useful history

The Dashboard is a working surface, not an append-only ledger. Alan may delete an unneeded task or proposed project directly in Obsidian.

- Delete freely captured material when its history has no practical value.
- Prefer `[-]` for a task or a short Decision when cancellation rationale may prevent repeated evaluation.
- After promotion, retain a compact Dashboard link when origin visibility remains useful, or record the origin in the Project and remove the proposal from the working section.
- Completed tasks may be removed during cleanup when their history no longer helps.

An absent Dashboard item is intentionally absent. Agents must not recreate it from conversation history, an older Handoff, a PM Note, cached context, or provider memory. Derived records reconcile to the Dashboard rather than restoring the item.

Deleting a Dashboard item makes any matching PM Note non-actionable. The note may also be deleted when its history has no practical value; its continued presence never resurrects a task or proposed project.

### Decisions and Handoff

`Decisions.md` records accepted choices that would otherwise be reopened. `Handoff.md` remains a replaceable restart packet for meaningful Area work.

## Area frontmatter

The Area home uses `schemas/area.schema.json`. A compact setup reference is available in `area-frontmatter-cheat-sheet.md`.

### Required properties

| Property | Meaning |
| --- | --- |
| `type` | Always `area` |
| `schema_version` | Area contract version |
| `area_id` | Stable, globally unique lowercase kebab-case identifier, normally prefixed by domain |
| `status` | `active`, `paused`, or `retired` |
| `domain` | Stable vault-aligned domain identifier |
| `pm_scope` | Whether the Agentic PM may load and manage the Area |
| `created` | Quoted local creation date |
| `updated` | Quoted last material state date |
| `next_action` | One concrete maintenance or proposed-project action |
| `blocked_by` | Area, project, or external blockers; `[]` when clear |

`income_role` is required for a managed Area and uses the same values as managed projects: `direct`, `enabling`, `none`, or `unknown`.

Date-only metadata uses `America/New_York` and remains quoted so schema validators receive strings.

## Agentic PM behavior

The Agentic PM is one reusable capability with multiple independent operating scopes. A normal PM session selects exactly one `domain` before loading managed state. Within that domain, the PM may load only Areas and projects explicitly marked `pm_scope: managed`.

`pm_scope: managed` means eligible within the record's own domain. It does not authorize a session to aggregate every managed record across domains. An Area may serve as the practical entry point for its domain, but the required `domain` value is the default scope boundary.

Area IDs must be globally unique even when display names repeat across domains. Prefer IDs such as `spectra-studio-business-admin` and `aef-business-admin` rather than reusing `business-admin`.

At the beginning of action selection, establish a temporary session envelope:

- selected domain;
- time available for this session or planning horizon;
- current energy or attention constraints when relevant;
- hard stops, deadlines, or blockers that materially affect the recommendation;
- working mode when useful: plan, do, review, or stuck rescue.

Time and energy are session inputs, not permanent Area metadata. Do not copy one conversation's availability into the Area home as if it were durable capacity.

Recommendations must fit the stated envelope. Prefer one finishable action; when nothing valuable fits, recommend a bounded preparation, clarification, or maintenance step rather than silently expanding the time budget.

Managed Areas contribute maintenance needs and candidate-project context, but project candidates do not enter the active project portfolio.

During planning, the PM distinguishes:

- active project outcomes;
- necessary Area maintenance;
- inactive project candidates.

The PM recommends one primary focus and at most one secondary maintenance responsibility unless Alan explicitly chooses otherwise. It may capture candidates and recommend promotion without silently starting them.

### Optional cross-domain capacity review

Cross-domain review occurs only when Alan explicitly requests it. It reads compact domain-level commitments and constraints to help allocate Alan's total capacity; it does not become an overarching PM that continuously manages every task and proposal.

A cross-domain review may recommend which domain receives primary attention and explain displacement. Detailed task selection returns to the chosen domain-scoped PM session.

## Promotion to a project

Promotion occurs only after Alan and the Agentic PM agree that now is the right time to start. The promotion workflow:

1. confirms the desired outcome and finish line;
2. creates a same-named project folder under `200 - Projects` using Project Contract v0.2;
3. selects explicit `pm_scope`, `income_role`, and `project_profile` values;
4. links the project home back to the originating Area and PM Note ID when one exists;
5. removes or replaces the Dashboard proposal with a compact link according to the chosen history value;
6. records the accepted promotion decision;
7. synchronizes both Area and project handoffs.

Promotion does not imply `pm_scope: managed`; Alan chooses managed or excluded explicitly.

## Authority boundaries

Only Alan or an explicitly authorized PM workflow may change Area lifecycle, `pm_scope`, `income_role`, promote a proposal, or record a consequential decline. Moving an Area, creating a promoted project, or changing another Area or project remains propose-first unless the current task explicitly authorizes it.

## Pilot acceptance

Area Contract v0.1 is ready for broader use when:

1. one real ongoing responsibility operates from `300 - Areas` as a valid managed Area;
2. a PM session stays inside one selected domain and fits its recommendation to the stated available time;
3. a managed record in another domain remains unloaded during normal operation;
4. a task added or changed directly in the Dashboard is picked up on the next PM read;
5. a real Area task is captured and selected without creating a project;
6. a blocked task preserves its safe resume condition without blocking the entire Area or activating a candidate;
7. an item deleted from the Dashboard remains absent on the next PM read even if a PM Note remains;
8. a real project candidate is captured without entering the active portfolio;
9. one approved candidate is manually promoted while preserving its origin;
10. a fresh agent can reconstruct the distinctions from the saved files.

Do not automate Area or project creation until these manual steps reveal a stable procedure.
