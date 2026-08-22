---
name: start-project
description: Create a Project Contract v0.2 project directly or promote an explicitly approved Area candidate, preserving existing work and applying profile-specific setup. Use when the user asks to start, initialize, scaffold, or promote a project. Do not use for ordinary work inside an existing initialized project, portfolio classification, or standalone repository creation.
---

# Agentic Work: Start Project

Create one restartable project record and, for software profiles, one linked local implementation repository. Treat the resulting next action as durable state, not authorization to perform it.

## Select the mode

Normalize the request to exactly one mode before loading or changing project data:

- `direct-creation`: create a new project or initialize an existing working folder that is not an Area candidate.
- `area-promotion`: promote one explicitly approved candidate from a same-named Area home.

Use the mode already stated when the user clearly says to create a standalone project or promote a named Area candidate. If the invocation does not establish a mode, ask once whether this is direct creation or an approved Area promotion. Do not default, scan for possible candidates, or infer promotion merely because a similar name exists.

For direct creation, read [references/direct-creation.md](references/direct-creation.md). For Area promotion, read [references/area-promotion.md](references/area-promotion.md). Do not load the other mode reference.

## Collect the required intake

Obtain or confirm these values before writing:

- stable internal project name and lowercase kebab-case `project_id`;
- exact project parent and resulting same-named folder path;
- `domain`;
- lifecycle: `planned`, `active`, `blocked`, `paused`, `complete`, `cancelled`, or `archived`;
- `pm_scope`: `managed` or `excluded`;
- `income_role` when managed: `direct`, `enabling`, `none`, or `unknown`;
- `project_profile`: `general`, `software-product`, or `software-tool`;
- objective, observable definition of done, important boundaries, blockers, and one represented next action;
- whether the public name is final or provisional while the internal identity remains stable;
- for Area promotion, the exact Area home and candidate origin;
- for either software profile, repository mode and exact local path.

Ask for missing information in one compact intake when practical. Do not invent public claims, names, locations, classifications, objectives, finish lines, or next actions.

## Apply the profile

| Profile | Required profile file | Repository requirement |
| --- | --- | --- |
| `general` | none | optional and only when explicitly requested |
| `software-product` | `Product Requirements.md` | required: create an approved stub or link an existing local Git repository |
| `software-tool` | `Technical Brief.md` | required: create an approved stub or link an existing local Git repository |

For either software profile, read [references/repository-setup.md](references/repository-setup.md). “Repository not created yet” is not a successful software-project initialization result.

Use only the matching profile template under `assets/project-profiles/`. Do not create both profile files or an empty profile file for `general`.

## Preflight and approval

Before any mutation:

1. read the nearest applicable `AGENTS.md` files and the current Area or project records allowed by the selected mode;
2. resolve every project, asset, profile, origin, and repository path exactly;
3. inspect the destination for files, case variants, symlinks, same-named notes, profile documents, `xPM/`, asset folders, and filename or folder collisions;
4. for an existing repository, complete the read-only Git preflight in the repository reference;
5. identify every file to create, preserve, rename, or edit and every Git operation proposed;
6. present one compact preflight summary containing the mode, identity, profile, exact paths, repository action, promotion effects, provisional values, collisions, and stop boundaries;
7. obtain explicit approval for that exact plan.

If the user changes the path, profile, repository mode, promotion origin, or mutation set after the summary, refresh the affected preflight and approval. Do not treat general permission to start a project as permission to use an unreviewed repository target.

## Instantiate the project

Use the packaged templates under `assets/project/`, replacing every placeholder with approved state. The result contains:

```text
Project Name/
├── Project Name.md
├── Product Requirements.md  # software-product only
├── Technical Brief.md       # software-tool only
├── Assets/
└── xPM/
    ├── Status.md
    ├── Decisions.md
    └── Handoff.md
```

Preserve existing working files. Never overwrite a same-named note, profile document, `xPM` record, repository file, or asset merely because a template exists. Remove template guidance, placeholder decisions, and placeholder prose from the instantiated files. An empty `## Tasks` section is valid; never add an empty local checkbox.

Record provisional public naming visibly while retaining the stable internal folder name, home filename, and `project_id`.

Keep project-local working material in `Assets/`, runtime software assets in the repository, and durable reusable assets in the installation's established asset system. Normalize one existing asset location only when the move and all affected references are unambiguous. Stop when multiple asset locations, duplicate names, case collisions, unresolved references, or uncertain ownership could duplicate or lose material.

Do not claim atomic rollback. If an approved write fails after partial creation, stop, preserve the recoverable state, and report exactly what succeeded and failed. Never delete or overwrite material to simulate a clean rollback.

## Synchronize durable state

The project home owns stable identity and canonical lifecycle. `xPM/Status.md` owns the detailed current outcome, blockers, and next action. Synchronize:

- project-home and Status lifecycle;
- project-home `next_action` and Status `## Next action`;
- project-home `blocked_by` and Status `## Blockers`;
- Handoff's recommended next action;
- the applicable local calendar date under the contract's timezone rule;
- project-home `repo` and the repository README backlink when a repository is present.

Create no accepted Decision entry unless the user actually accepted a choice worth preserving. Do not leave the template's example decision in place.

## Validate and hand off

Before reporting success:

- validate the project home against `assets/schemas/project.schema.json`;
- for promotion, validate the Area home against `assets/schemas/area.schema.json`;
- verify the folder and home base names match;
- verify every required file exists and no forbidden profile file was added;
- verify dates, frontmatter values, link targets, lifecycle, blockers, and next actions;
- verify no empty local task placeholder exists;
- verify existing working files and assets remain present;
- for promotion, verify the Area, candidate note when present, and project preserve their origin links and do not represent the project as an inactive proposal;
- for software profiles, verify the local Git root, absent index lock, required stub files, Obsidian `repo` path, and repository backlink;
- inspect the final diffs and Git status, distinguishing intended changes from unrelated pre-existing changes;
- confirm no remote, dependency, commit, publication, deployment, purchase, message, installation, or represented next action was performed.

Replace `xPM/Handoff.md` with the contract's eight-part restart packet. Report created and changed files, preserved existing material, validation results, repository state, unresolved questions, and one concrete project next action. Stop without executing that action.

## Authority and portability boundaries

- Do not choose or change lifecycle, PM scope, income role, profile, objective, definition of done, promotion, public name, repository path, or accepted decisions without explicit approval.
- Do not create or link a repository until its exact target appears in an approved preflight.
- Do not add dependencies, accounts, remotes, commits, publications, deployments, DNS changes, purchases, messages, or installation changes.
- Do not execute tasks or next actions represented by the Area, candidate, or project.
- Do not expose unrelated context or search sibling projects, Journals, or broad vault content.
- Keep reusable instructions and generated repository guidance provider-neutral and free of private data, secrets, or hard-coded installation paths.
