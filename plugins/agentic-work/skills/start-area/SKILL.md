---
name: start-area
description: Create or initialize an Area Contract v0.1 record for an ongoing responsibility without a finish line, preserving existing work and separating Area tasks from inactive project candidates. Use when the user asks to start, create, initialize, or scaffold an Area. Do not use for finishable projects, ordinary work inside an initialized Area, project promotion, or silent conversion or deletion of an existing project.
---

# Agentic Work: Start Area

Create one restartable Area record for ongoing stewardship. Treat its next action as durable state, not authorization to perform it.

## Confirm the work is an Area

An Area represents an ongoing responsibility with a healthy state but no definition of done. It may contain bounded tasks and inactive project candidates.

Use `agentic-work:start-project` instead when the requested outcome is finishable. If an existing project appears to have been misclassified, do not move, rewrite, or delete it through this skill. Pause and present the Area creation plus project cleanup as separate, exact mutations requiring approval.

## Collect the required intake

Obtain or confirm these values before writing:

- stable internal Area name and globally unique lowercase kebab-case `area_id`, normally prefixed by domain;
- exact Area parent and resulting same-named folder path under the installation's Area system;
- `domain`;
- lifecycle: `active`, `paused`, or `retired`;
- `pm_scope`: `managed` or `excluded`;
- `income_role` when managed: `direct`, `enabling`, `none`, or `unknown`;
- ongoing responsibility, observable healthy state, important boundaries, blockers, and one represented next action;
- any initial Area tasks or proposed projects the user wants captured;
- existing working files, asset locations, canonical records, or external work locations that must be preserved or linked.

Ask for missing information in one compact intake when practical. Do not invent names, locations, classifications, responsibilities, healthy-state claims, boundaries, tasks, project candidates, blockers, or next actions. Do not add a definition of done.

`active` means the responsibility exists; it does not mean the Area should consume primary focus every day. `pm_scope: managed` makes the Area eligible only within its own domain and does not authorize cross-domain portfolio loading.

## Preflight and approval

Before any mutation:

1. read the nearest applicable `AGENTS.md` files and the exact target folder when it exists;
2. resolve the Area parent, folder, same-named home, `xPM/` paths, and any working-material paths exactly;
3. inspect the destination for files, case variants, symlinks, same-named notes, generic dashboard notes that could be the intended home, `xPM/`, and filename or folder collisions;
4. preserve existing working files and identify every file to create, preserve, rename, move, or edit;
5. stop when the same-named home may already be an initialized Area, when ownership is uncertain, or when a move or merge could duplicate or lose material;
6. present one compact preflight summary containing the Area identity, classification, exact paths, initial dashboard content, preservation or normalization effects, provisional values, collisions, and stop boundaries;
7. obtain explicit approval for that exact plan.

If the user changes the parent, identity, classification, or mutation set after the summary, refresh the affected preflight and approval.

Do not scan sibling Areas or broad vault content merely to choose metadata. Do not treat approval to create an Area as approval to delete or convert a similarly named project.

## Instantiate the Area

Use the packaged templates under `assets/area/`, replacing every placeholder with approved state. The result contains:

```text
Area Name/
├── Area Name.md
└── xPM/
    ├── Status.md
    ├── Decisions.md
    └── Handoff.md
```

Preserve existing working files. Never overwrite a same-named home or `xPM` record merely because a template exists. Human working notes, research, records, drafts, deliverables, assets, and domain-meaningful folders remain outside `xPM/`.

Keep `## Tasks` and `## Proposed Projects` separate in the Area home. Preserve user wording and task markers exactly when supplied. Empty sections are valid; never add an empty checkbox or a placeholder project idea. Proposed projects remain inactive and outside the active project portfolio.

Do not create `xPM/Notes/` or per-item PM notes during initialization unless approved initial content already earns specific support. Do not add a placeholder Decision. When no accepted PM-governance decision needs a log entry, create only the Decisions frontmatter and `# Decisions` heading.

Do not claim atomic rollback. If an approved write fails after partial creation, stop, preserve recoverable state, and report exactly what succeeded and failed. Never delete or overwrite material to simulate a clean rollback.

## Synchronize durable state

The Area home owns stable identity, lifecycle, human tasks, and project-candidate intent. `xPM/Status.md` owns detailed current health, the maintenance outcome receiving attention, blockers, and next action. Synchronize:

- Area-home and Status lifecycle;
- Area-home `next_action` and Status `## Next action`;
- Area-home `blocked_by` and Status `## Blockers`;
- Handoff's recommended next action;
- the applicable local calendar date under the contract's timezone rule.

Direct human wording, checkbox markers, headings, additions, and deletions in the same-named Area home are authoritative. Derived `xPM` state must not resurrect absent tasks or project candidates.

## Validate and hand off

Before reporting success:

- validate the Area home against `assets/schemas/area.schema.json`;
- verify the folder and home base names match;
- verify the required Area and `xPM` files exist;
- verify no Project profile document, project frontmatter, repository stub, or definition of done was added;
- verify dates, frontmatter values, lifecycle, blockers, and next actions;
- verify no empty local task checkbox or placeholder proposed project remains;
- verify supplied human tasks, proposals, working files, and assets remain present with their wording and markers preserved;
- verify optional PM Notes were not created without earned, approved content;
- inspect the final diffs and Git status, distinguishing intended changes from unrelated pre-existing changes;
- confirm no project promotion, project conversion, dependency, remote, commit, publication, deployment, purchase, message, installation, or represented next action was performed.

Replace `xPM/Handoff.md` with the contract's eight-part restart packet. Report created and changed files, preserved existing material, validation results, unresolved questions, and one concrete Area next action. Stop without executing that action.

## Authority boundaries

- Do not choose or change Area lifecycle, PM scope, income role, responsibility, healthy state, boundaries, blockers, tasks, project candidates, or next action without explicit approval.
- Do not create, promote, convert, move, or delete a project through this skill.
- Do not add a definition of done, `project_profile`, repository, or software requirements profile to an Area.
- Do not execute Area tasks, shape or promote project candidates, or perform the represented next action.
- Do not expose unrelated context or search sibling Areas, projects, Journals, or broad vault content.
- Keep reusable instructions provider-neutral and free of private data, secrets, or hard-coded installation paths.
