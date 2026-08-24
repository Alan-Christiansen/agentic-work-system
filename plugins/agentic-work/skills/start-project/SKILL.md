---
name: start-project
description: Create a Project Contract v0.3 project directly or promote an explicitly approved Area candidate, preserving existing work and applying profile-specific setup. Use when the user asks to start, initialize, scaffold, or promote a project. Do not use for ordinary work inside an existing initialized project, portfolio classification, or standalone repository creation.
---

# Agentic Work: Start Project

Create one restartable project record and, for software profiles, one linked local implementation repository. Treat the resulting next action as durable state, not authorization to perform it.

## Select the mode

Normalize the request to exactly one mode before loading or changing project data:

- `direct-creation`: create a new project or initialize an existing working folder that is not an Area candidate.
- `area-promotion`: promote one explicitly approved candidate from an underscore-prefixed, folder-matching Area home.

Use the mode already stated when the user clearly says to create a standalone project or promote a named Area candidate. If the invocation does not establish a mode, ask once whether this is direct creation or an approved Area promotion. Do not default, scan for possible candidates, or infer promotion merely because a similar name exists.

For direct creation, read [references/direct-creation.md](references/direct-creation.md). For Area promotion, read [references/area-promotion.md](references/area-promotion.md). Do not load the other mode reference.

## Collect the required intake

Obtain or confirm these values before writing:

- stable internal project name and lowercase kebab-case `project_id`;
- exact project parent and resulting folder path;
- `domain`;
- lifecycle: `planned`, `active`, `blocked`, `paused`, `complete`, `cancelled`, or `archived`;
- `pm_scope`: `managed` or `excluded`;
- `income_role` when managed: `direct`, `enabling`, `none`, or `unknown`;
- `project_profile`: `general`, `software-product`, or `software-tool`;
- objective, observable definition of done, important boundaries, blockers, and one represented next action;
- an approved agent role: primary role, specific expertise to apply, and working approach;
- whether the public name is final or provisional while the internal identity remains stable;
- for Area promotion, the exact Area home and candidate origin;
- for either software profile, repository mode and exact local path.

Ask for missing information in one compact intake when practical. The skill may draft a clearly provisional role brief from approved context, but must obtain explicit approval before writing it. Do not invent public claims, names, locations, classifications, objectives, finish lines, next actions, or a final role.

The role shapes perspective and methods only. It does not grant credentials, tool access, decision rights, or authority beyond the contract and current task.

## Apply the profile

| Profile | Required profile file | Repository requirement |
| --- | --- | --- |
| `general` | none | optional and only when explicitly requested |
| `software-product` | `Product Requirements.md` | required: create an approved stub or link an existing local Git repository |
| `software-tool` | `Technical Brief.md` | required: create an approved stub or link an existing local Git repository |

For either software profile, read [references/repository-setup.md](references/repository-setup.md). “Repository not created yet” is not a successful software-project initialization result.

Use only the matching profile template tree under `assets/project-profiles/`. The software-product profile includes its demonstrated Product Planning scaffold; the software-tool profile includes only its Technical Brief. Do not mix profile files or create an empty profile extension for `general`.

## Preflight and approval

Before any mutation:

1. read the nearest applicable `AGENTS.md` files and the current Area or project records allowed by the selected mode;
2. resolve every project, asset, profile, origin, and repository path exactly;
3. inspect the destination for files, case variants, symlinks, underscore-prefixed or legacy unprefixed home candidates, profile documents, `xPM/`, profile-provided folders, and filename or folder collisions;
4. for an existing repository, complete the read-only Git preflight in the repository reference;
5. identify every file to create, preserve, rename, or edit and every Git operation proposed;
6. present one compact preflight summary containing the mode, identity, profile, complete proposed role brief, exact paths, repository action and role-synchronization effect, promotion effects, provisional values, collisions, and stop boundaries;
7. obtain explicit approval for that exact plan.

If the user changes the path, profile, repository mode, promotion origin, or mutation set after the summary, refresh the affected preflight and approval. Do not treat general permission to start a project as permission to use an unreviewed repository target.

## Instantiate the project

Use the packaged templates under `assets/project/`, replacing every placeholder with approved state. The result contains:

```text
Project Name/
├── _Project Name.md
├── Product Requirements.md  # software-product only
├── Technical Brief.md       # software-tool only
├── Product Planning/        # software-product only
└── xPM/
    ├── Status.md
    ├── Decisions.md
    └── Handoff.md
```

Name the home with one leading underscore followed by the exact parent-folder name. Preserve existing working files. Add the approved `## Agent role` section after `## Tasks`, with non-empty `### Primary role`, `### Expertise to apply`, and `### Working approach` subsections. Never overwrite an underscore-prefixed or legacy unprefixed home candidate, profile document, `xPM` record, repository file, or asset merely because a template exists. Remove template guidance, placeholder decisions, and placeholder prose from the instantiated files. An empty `## Tasks` section is valid; never add an empty local checkbox.
Format generated Markdown with no blank line immediately before or after a heading. Preserve intentional spacing elsewhere and do not alter heading spacing inside fenced examples.

Record provisional public naming visibly while retaining the stable internal folder name, home filename, and `project_id`.

Keep human working material in the domain-meaningful folder that owns it, runtime software assets in the repository, and durable reusable assets in the installation's established asset system. Preserve existing meaningful asset locations; do not relocate or remove them merely because a profile uses another contextual folder. Stop when duplicate names, case collisions, unresolved references, or uncertain ownership could duplicate or lose material.

Do not claim atomic rollback. If an approved write fails after partial creation, stop, preserve the recoverable state, and report exactly what succeeded and failed. Never delete or overwrite material to simulate a clean rollback.

## Synchronize durable state

The project home owns stable identity and canonical lifecycle. `xPM/Status.md` owns the detailed current outcome, blockers, and next action. Synchronize:

- project-home and Status lifecycle;
- project-home `next_action` and Status `## Next action`;
- project-home `blocked_by` and Status `## Blockers`;
- Handoff's recommended next action;
- the applicable local calendar date under the contract's timezone rule;
- project-home `repo` and the repository README backlink when a repository is present.
- project-home `## Agent role` and the exact derived role copy in repository `AGENTS.md` when a repository is present.

Create no accepted Decision entry unless the user actually accepted a choice worth preserving. Do not leave the template's example decision in place.

## Validate and hand off

Before reporting success:

- validate the project home against `assets/schemas/project.schema.json`;
- for promotion, validate the Area home against `assets/schemas/area.schema.json`;
- verify the home has exactly one structural leading underscore and its remaining base name exactly matches the parent folder;
- verify every required file exists and no forbidden profile file was added;
- verify dates, frontmatter values, link targets, lifecycle, blockers, and next actions;
- verify no empty local task placeholder exists;
- verify the complete approved role brief is present, non-empty, and does not imply authority or credentials;
- verify existing working files and meaningful asset locations remain present;
- for promotion, verify the Area, candidate note when present, and project preserve their origin links and do not represent the project as an inactive proposal;
- for software profiles, verify the local Git root, absent index lock, required stub files, Obsidian `repo` path, repository backlink, and exact role parity between the project home and repository `AGENTS.md`; stop and report drift rather than choosing a side;
- inspect the final diffs and Git status, distinguishing intended changes from unrelated pre-existing changes;
- confirm no remote, dependency, commit, publication, deployment, purchase, message, installation, or represented next action was performed.

Replace `xPM/Handoff.md` with the contract's eight-part restart packet. Report created and changed files, preserved existing material, validation results, repository state, unresolved questions, and one concrete project next action. Stop without executing that action.

## Authority and portability boundaries

- Do not choose or change lifecycle, PM scope, income role, profile, objective, definition of done, promotion, public name, agent role, repository path, or accepted decisions without explicit approval.
- Do not create or link a repository until its exact target appears in an approved preflight.
- Do not add dependencies, accounts, remotes, commits, publications, deployments, DNS changes, purchases, messages, or installation changes.
- Do not execute tasks or next actions represented by the Area, candidate, or project.
- Do not expose unrelated context or search sibling projects, Journals, or broad vault content.
- Keep reusable instructions and generated repository guidance provider-neutral and free of private data, secrets, or hard-coded installation paths.
