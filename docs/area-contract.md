# Area Contract v0.2

## Purpose

This contract defines the minimum durable state required for Alan and the Agentic PM to manage an ongoing responsibility without misrepresenting it as a finishable project.

An Area has no definition of done. It may contain routine responsibilities, bounded tasks, and possible future projects. Only an explicitly approved promotion creates a project under `200 - Projects`.

## Required Area files

Every managed Area using this contract has one underscore-prefixed, folder-matching human dashboard and one PM support folder:

```text
Area Name/
├── _Area Name.md
├── AGENTS.md
├── CLAUDE.md
├── working files and folders...
└── xPM/
    ├── Status.md
    ├── Decisions.md
    ├── Handoff.md
    └── Notes/                 # optional per-item PM support
```

The canonical base templates are under `templates/area/`. Optional approved working-material packs are under `templates/area-packs/`; they extend an Area without changing its contract or frontmatter schema.

### Folder-local bootstrap adapters
`AGENTS.md` is a thin provider-neutral cold-start adapter. It names the exact underscore-prefixed Area home, routes a newly scoped agent through Status and Handoff, makes Decisions conditional, and states the minimum authority boundary. It does not duplicate the Area role, tasks, proposals, definition, status, or handoff.

`CLAUDE.md` contains only `@AGENTS.md`. These adapters make the folder independently restartable when a user grants an LLM only that Area. They are operational loading files, not Area state or schema fields, so Area Contract v0.2 remains current.

### Area home

The Area home is named with one leading underscore followed by the exact parent-folder name: `Area Name/_Area Name.md`. After removing that structural underscore, the base name must equal the folder name exactly. It is the only required human-facing PM file and combines the Area dashboard with its stable definition. It records:

- the ongoing responsibility;
- what healthy stewardship looks like;
- important boundaries and ownership;
- compact tasks and free-form proposed projects;
- an approved agent-role brief defining the perspective, expertise, and working approach agents should apply;
- relevant external work locations.

Do not add a definition of done. An Area is retired only when the responsibility no longer exists or belongs elsewhere.

Human working notes, records, research, documents, and domain-meaningful folders may live beside the Area home. The contract reserves only the underscore-prefixed, folder-matching home and `xPM/`; it does not force working material into a generic Notes folder.
### Optional product-venture pack
An Area that continuously stewards a software product venture may receive the complete `product-venture` pack after its exact files are included in the approved creation plan. The base Area remains the default, and pack selection does not add an `area_profile` or other schema field.

```text
Area Name/
├── Product Direction/
│   ├── Users & Needs.md
│   ├── Feature Landscape.md
│   └── Business & Monetization.md
└── Incubator/
    ├── _Idea Inbox.md
    └── What-Ifs & Future Capabilities.md
```

These notes own durable venture direction that can outlive any one release. The Area home links them through a compact Product direction section. Release projects link to relevant Area notes rather than copying users and needs, the product-wide feature landscape, business and monetization, or speculative ideas. Do not partially instantiate the pack or add it merely because an Area has a product-like name.

### PM support folder

`xPM/` contains agent coordination machinery rather than ordinary working material:

- `xPM/Status.md` records current health, the maintenance outcome receiving attention, next action, blockers, and later concerns;
- `xPM/Decisions.md` records PM-governance choices that could otherwise be reopened;
- `xPM/Handoff.md` is the replaceable restart packet;
- `xPM/Notes/` contains optional per-item agent support created only when earned.

`active` Area status means the responsibility exists; it does not mean the Area should consume primary focus every day.

The Area-home `status`, `next_action`, and `blocked_by` fields mirror `xPM/Status.md`. The latest `xPM/Handoff.md` recommendation matches the same next action.

### Human dashboard

The underscore-prefixed, folder-matching Area home is the canonical human-first working surface for bounded Area tasks and possible future projects. Alan may write, start, block, complete, drop, delete, rename, or revise its contents directly in Obsidian without invoking an agent.
Generated Area Markdown uses tight heading spacing: no blank line immediately before or after a heading. Intentional spacing elsewhere remains untouched, and fenced examples retain their literal formatting.

The Dashboard keeps tasks and proposed projects visibly separate without splitting the human workflow across files:

```markdown
# Area Name

## Tasks

- [ ] Do the thing

## Proposed Projects

### Possible project
Free-form intent, context, links, and notes written in the human's own language.
```

Every PM session rereads the underscore-prefixed, folder-matching Area home before recommending work. Saved human wording, markers, headings, additions, and deletions are authoritative rather than conversation memory or older agent records.

#### Agent role

Every Area home contains a non-empty `## Agent role` section after `## Proposed Projects`, with `### Primary role`, `### Expertise to apply`, and `### Working approach` subsections. The role brief is explicitly approved during intake. It may describe professional perspectives, subject-matter knowledge, evidence standards, and useful methods, but it never grants credentials, tool access, decision rights, or authority beyond this contract and the current task.

Agents may propose a provisional role brief from approved context, but must label it provisional and obtain approval before writing it. Treat the role as durable working guidance: apply it when relevant, keep uncertainty visible, and do not use it to overstate expertise or bypass specialist boundaries.

#### Tasks

A complete task may be only one line. IDs, dates, rationale, and next-action details are optional. Agents must not ignore or rewrite a quick task merely because metadata is absent.

An empty `## Tasks` section is valid. Do not retain an empty checkbox as a capture placeholder in an Area home: task aggregators correctly treat it as a real task and surface a blank result. Add a checkbox only when it names actual work; use the optional vault-level Inbox for unassigned quick capture.

Keep the checklist visually tight. When a task genuinely needs restart context, generate one support note under `xPM/Notes/` and add a short link on the task line:

```markdown
- [!] Register with agency [[xPM/Notes/AT-001 - Register with agency|details]]
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

Do not duplicate task state in a separate field. If older agent text conflicts with the Area-home marker, the marker wins. Agents must not reopen or rewrite a manually changed task without approval.

A blocked task's linked PM Note records only the minimum useful restart state: blocker, follow-up date or event, resume condition, and next action. Blocking one task does not block the entire Area or authorize activation of a proposed project.

Agents scan the Area home's Tasks section first and load a linked task PM Note only when the task is selected, blocked, due for follow-up, or otherwise needs restart context.

Plain Markdown remains canonical. Optional task-tool dates, priorities, recurrence, tags, and query views may enhance the source task when they change behavior. Do not require a global task tag or add tags that merely repeat Area or domain location. Plugin views remain derived interfaces, not another source of truth.

#### Urgency tags

Use only two qualitative urgency tags:

- `#urgent` means delay has an immediate cost and the task needs attention now;
- `#soon` means the task should remain prominent in the near term;
- no urgency tag means normal or backlog work.

The PM assigns and maintains urgency during ingestion and review. It considers real due dates, scheduled actionability, consequences of delay, blockers, dependencies, and current commitments. It removes or downgrades stale urgency and keeps `#urgent` rare. Never require Alan to classify a bare captured task before it is valid.

Dates retain their own meanings: `📅` is a real deadline and `⏳` is when work becomes actionable. A date may influence the PM's urgency judgment but is not replaced by a tag. If both urgency tags are present, `#urgent` wins and the PM removes `#soon` during the next authorized cleanup. Direct human tag edits are authoritative.

An optional vault-level Tasks-plugin dashboard may aggregate canonical tasks from underscore-prefixed, folder-matching Area and Project homes. It is a derived human view: toggling a result updates the source task, and the dashboard never duplicates or becomes canonical task state.

#### Proposed Projects

The Area home's `## Proposed Projects` section contains possible future projects, not ordinary tasks. Use it when work may need its own objective, definition of done, multi-session state, decisions, handoffs, deliverables, or repository.

Alan may capture a proposed project as a heading followed by any amount of free-form intent, context, links, or notes. No ID, state field, or agent-authored structure is required:

```markdown
### Wood projects website
I want to begin with a landing page, add ecommerce later, and explore a sub-brand name.
```

Merely appearing under Proposed Projects means the idea is inactive. It does not enter the active portfolio or consume project capacity until Alan and the PM explicitly agree to promote it.

When a proposal earns structured shaping, comparison, or promotion preparation, the PM may generate one note under `xPM/Notes/` and link it beneath the human description:

```markdown
[[xPM/Notes/PC-001 - Wood projects website|PM notes]]
```

`PC` means Project Candidate. Alan does not need to create or manage the ID. The human-authored Area-home heading and description remain authoritative for existence and intent. The linked PM Note holds derived analysis such as desired outcome, boundary, maturity, start conditions, and an eventual promoted-project link. Agents load it only when working on that proposal.

Candidate maturity may be tracked inside its PM Note using `captured`, `candidate`, or `ready`. These are PM interpretations, not activation. `ready` never means active; promotion remains an explicit human decision.

### Deletion and useful history

The Area home is a working surface, not an append-only ledger. Alan may delete an unneeded task or proposed project directly in Obsidian.

- Delete freely captured material when its history has no practical value.
- Prefer `[-]` for a task or a short Decision when cancellation rationale may prevent repeated evaluation.
- After promotion, retain a compact Area-home link when origin visibility remains useful, or record the origin in the Project and remove the proposal from the working section.
- Completed tasks may be removed during cleanup when their history no longer helps.

An absent Area-home item is intentionally absent. Agents must not recreate it from conversation history, an older Handoff, a PM Note, cached context, or provider memory. Derived records reconcile to the Area home rather than restoring the item.

Deleting an Area-home item makes any matching PM Note non-actionable. The note may also be deleted when its history has no practical value; its continued presence never resurrects a task or proposed project.

### Decisions and Handoff

`xPM/Decisions.md` records accepted PM-governance choices that would otherwise be reopened. `xPM/Handoff.md` remains a replaceable restart packet for meaningful Area work. Substantive business or design decisions may remain with the working material they govern rather than being forced into the PM log.

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
2. creates a project folder under `200 - Projects` with its underscore-prefixed, folder-matching home using Project Contract v0.3;
3. selects explicit `pm_scope`, `income_role`, and `project_profile` values;
4. links the project home back to the originating Area and PM Note ID when one exists;
5. removes or replaces the Area-home proposal with a compact link according to the chosen history value;
6. records the accepted promotion decision;
7. synchronizes both Area and project handoffs.

Promotion does not imply `pm_scope: managed`; Alan chooses managed or excluded explicitly.

## Authority boundaries

Only Alan or an explicitly authorized PM workflow may change Area lifecycle, `pm_scope`, `income_role`, promote a proposal, or record a consequential decline. Moving an Area, creating a promoted project, or changing another Area or project remains propose-first unless the current task explicitly authorizes it.

## v0.2 acceptance

Area Contract v0.2 is ready for broader use when:

1. one real ongoing responsibility operates from `300 - Areas` as a valid managed Area;
2. a PM session stays inside one selected domain and fits its recommendation to the stated available time;
3. a managed record in another domain remains unloaded during normal operation;
4. a task added or changed directly in the underscore-prefixed, folder-matching Area home is picked up on the next PM read;
5. a real Area task is captured and selected without creating a project;
6. a blocked task preserves its safe resume condition without blocking the entire Area or activating a candidate;
7. an item deleted from the Area home remains absent on the next PM read even if a PM Note remains;
8. a real project candidate is captured without entering the active portfolio;
9. one approved candidate is manually promoted while preserving its origin;
10. a fresh agent can reconstruct the distinctions from the saved files.
11. the approved agent-role brief is present, non-empty, and shapes expertise without changing authority.

Do not automate Area or project creation until these manual steps reveal a stable procedure.
