# Companion repository setup

Read this reference for `software-product`, `software-tool`, or an explicitly requested repository for `general`.

## Required result by profile

A new software-project initialization succeeds only when:

- the Obsidian project home contains the verified local repository path in `repo`;
- that path resolves to the intended local Git root;
- the repository contains `README.md`, `AGENTS.md`, and `CLAUDE.md`;
- the README points back to the canonical project home;
- `AGENTS.md` contains an exact derived copy of the canonical project's approved `## Agent role` content, marked as synchronized from the project home;
- no detailed project status is duplicated into the repository.

Allow exactly two modes for a required software repository: `create-stub` or `link-existing`. Do not accept `defer`, `later`, a proposed path, or “not created yet” as completion.

## Shared Git safety

Use `git --no-optional-locks` for every Git inspection. Resolve the root and index-lock path; any existing or appearing index lock is a hard stop. Never remove, rename, relocate, overwrite, copy, or remediate a lock.

Do not use the repository, an ignored directory, build output, or `.git` as temporary storage. Never clean, reset, discard, stash, stage, commit, push, fetch, pull, or add or change a remote.

## Create an approved stub

Before creation, show:

- exact parent and repository path;
- approved repository display name;
- initial branch name, defaulting to `main` only when the user did not choose another;
- the files to create;
- the Obsidian home that will link to it;
- the explicit exclusions: dependencies, remotes, commits, publication, and deployment.

Require explicit approval of that plan. Stop on a non-empty target or an unresolved name, case, symlink, or parent collision. An existing non-empty Git repository belongs in `link-existing`, not `create-stub`.

After approval:

1. create the exact directory when absent;
2. initialize local Git with the approved initial branch;
3. instantiate `assets/repository/README.md`, `AGENTS.md`, and `CLAUDE.md` without unresolved placeholders;
4. substitute the approved project role into `AGENTS.md` without changing its wording;
5. confirm the Git root and index-lock path;
6. record the repository path in the project home;
7. verify the README backlink and exact role parity;
8. report the expected untracked stub files accurately.

Do not describe a new uncommitted stub as clean. No initial commit is part of this skill.

## Link an existing repository

Resolve and verify the user-supplied path before any mutation:

1. confirm the Git root with `git --no-optional-locks rev-parse --show-toplevel`;
2. resolve and check the index-lock path;
3. inspect `git --no-optional-locks status --porcelain=v1 --untracked-files=all`, branch, and HEAD when present;
4. stop if the working tree has unrelated changes or the intended repository identity is uncertain;
5. inspect `README.md`, `AGENTS.md`, and `CLAUDE.md` without overwriting them, and compare any existing repository role copy with the canonical project role.

If required files or the project-home backlink are missing, include their creation or minimal edit in the preflight. Preserve all existing repository guidance. `AGENTS.md` remains the provider-neutral authority; `CLAUDE.md` imports it and contains only demonstrated Claude-specific differences.

After approval, write only the planned minimal repository files, backlink, exact role synchronization, and project-home `repo` value. If role wording differs, the project home wins; stop and report drift unless synchronization was part of the approved mutation set. Record `repo_remote` only when an existing verified remote is relevant and the user approves recording it; never create or change the remote.

## Repository templates

Use the packaged files under `assets/repository/` for a new stub. Replace all double-braced placeholders. For an existing repository, treat these templates as minimum content guidance rather than replacement files.

Runtime code and assets stay in the repository. Obsidian holds product intent, lifecycle, PM state, decisions, and handoff. Link the two locations instead of copying their detailed state.
