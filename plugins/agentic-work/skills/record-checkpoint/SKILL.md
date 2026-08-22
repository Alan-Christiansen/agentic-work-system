---
name: record-checkpoint
description: Verify a human-created Git commit for an Agentic Work System project and synchronize the linked Obsidian project home, xPM/Status.md, and xPM/Handoff.md with that clean checkpoint. Use when the user says work was committed, asks to record or synchronize a checkpoint, or wants stale uncommitted or awaiting-review state replaced after a reviewed commit. Do not use this skill to create commits, push, deploy, choose new scope, or begin the next task.
---

# Agentic Work: Record Checkpoint

Record a reviewed Git commit as the durable project checkpoint. Treat the companion repository and Obsidian project records as one synchronized state, then stop.

## Preconditions

Require access to:

1. the individual Obsidian project folder;
2. its companion Git repository.

Require the user to have created the commit already. A linked path is informational and does not grant access.

Require repository inspection to remain read-only. Use Git's `--no-optional-locks` global option for every Git command. If the host cannot run Git without optional locks, stop and report the limitation instead of continuing.

## Workflow

### 1. Load the project contract locally

Read, in order:

1. the project folder's `AGENTS.md`, when present;
2. the project home note;
3. `xPM/Status.md`;
4. `xPM/Handoff.md`;
5. `xPM/Decisions.md` only when needed to interpret the next approved action.

Read the repository's `AGENTS.md` and `README.md`. Resolve the companion repository from the project home's `repo` property when the user did not provide it explicitly.

Do not search parent vault folders, sibling projects, Journals, or unrelated repositories.

### 2. Verify the Git checkpoint

From the companion repository:

1. confirm the repository root with `git --no-optional-locks rev-parse --show-toplevel`;
2. resolve the index-lock path with `git --no-optional-locks rev-parse --git-path index.lock` and stop if that path already exists;
3. run `git --no-optional-locks status --porcelain=v1`;
4. require no modified, staged, or untracked files;
5. read the current branch;
6. read the full and short `HEAD` hashes, subject, author date, and change summary, using `git --no-optional-locks` for every command;
7. confirm the resolved index-lock path still does not exist;
8. compare the commit with the reviewed work described by the current Status and Handoff.

If the working tree is not clean, stop and report the exact entries. Do not commit, discard, move, ignore, or otherwise alter them.

If an index lock exists or appears during inspection, stop and report its resolved path. Do not remove, rename, relocate, overwrite, or copy it. Do not use `dist/`, another ignored directory, or any repository location as temporary storage.

If the current commit cannot be connected confidently to the reviewed work, stop and ask the user to identify the intended commit.

### 3. Determine the next action

Use an explicitly approved post-checkpoint action already present in the project records or supplied by the user.

Do not promote an item from `Later`, invent a new milestone, or treat a proposal as approved. When no post-checkpoint action is approved, use:

`Select the next approved project action`

### 4. Synchronize the Obsidian project

Resolve the approved lifecycle value before writing. The project-home `status` is canonical; `xPM/Status.md` frontmatter must mirror it. If the two values conflict, stop unless the user explicitly supplies the approved value. Mirroring an approved value is factual synchronization, not permission to choose a lifecycle change.

Update the project home frontmatter:

- set `updated` to the current calendar date using the project contract's timezone rule;
- preserve or apply the explicitly approved `status`;
- set `next_action` to the same concrete action used in Status;
- set `blocked_by` from the blockers recorded in Status, using `[]` when Status says none. If the blockers cannot be represented confidently as project IDs or named external blockers, stop and report the ambiguity.

Replace outdated state in `xPM/Status.md` so it records:

- frontmatter `status` matching the project home and `updated` using the same local calendar date;
- the accepted commit's short hash and subject;
- that the companion repository is clean;
- the completed reviewed outcome;
- the current active outcome, if one is approved;
- the exact next action;
- unresolved blockers and later work that remain true.

Replace `xPM/Handoff.md` using the project contract's eight sections:

1. task and intended outcome;
2. current state;
3. files consulted;
4. decisions made;
5. artifacts changed;
6. verification performed;
7. unresolved questions or risks;
8. recommended next action.

Include the commit's full or short hash, subject, branch, and clean working-tree result. State that no repository files, ignored artifacts, or Git metadata were changed by this checkpoint-recording task only after validating that claim.

Preserve unresolved risks from the prior handoff when they remain true. Do not edit `xPM/Decisions.md` unless the user separately approved a decision change.

### 5. Validate and stop

Re-read the project home, Status, and Handoff. Confirm:

- all three name the same next action;
- the project-home and Status frontmatter `status` values match the approved lifecycle;
- the project-home `blocked_by` matches the blockers in Status;
- the project-home and Status `updated` values use the same current local date;
- current-state language no longer says the accepted work is uncommitted or awaiting review;
- the commit hash is accurate;
- `git --no-optional-locks status --porcelain=v1` remains empty;
- the resolved index-lock path remains absent;
- no repository, deployment, remote, or decision change occurred.

Report the recorded checkpoint and next action. Do not begin that action.

## Safety boundaries

- Never create or amend a commit.
- Never stage files.
- Never push or create a remote.
- Never deploy or change external services.
- Never clean a dirty working tree.
- Never create, move, delete, rename, overwrite, or copy anything inside the repository, including ignored paths, build output, and `.git` metadata.
- Never remediate a Git lock. Report it and stop.
- Never use the repository as temporary storage.
- Never infer approval for scope, lifecycle, priority, deadline, or decision changes.
- Never expose or search unrelated vault content.
