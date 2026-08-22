# Direct creation

Use this mode for a new standalone project or for initializing a pre-existing working folder that is not being promoted from an Area candidate.

## Context boundary

Read only:

1. the applicable parent or project-local `AGENTS.md`, when present;
2. the exact target folder and its shallow file inventory;
3. existing files whose names or references affect the scaffold;
4. the packaged project, profile, schema, and repository resources needed by the selected profile.

Do not run a portfolio inventory or inspect sibling projects merely to choose metadata.

## Preflight

Resolve the parent folder and calculate both `Project Name/` and `Project Name/Project Name.md`. Confirm the folder and home note use the approved stable internal identity even when the eventual public name is provisional.

If the target folder does not exist, plan its creation. If it exists, preserve every working file and inspect only deeply enough to find scaffold, asset, link, or case collisions.

Stop for clarification when:

- the same-named home already exists and may represent an initialized project;
- a generic or differently named file could be the intended project home;
- `xPM/`, `Assets/`, a profile document, or the repository target has conflicting content;
- both `assets/` and `Assets/` exist;
- moving an asset folder would collide by name or break references that cannot be updated confidently;
- the requested folder is an obvious archive or deletion candidate rather than a retained project.

For `software-product` or `software-tool`, finish repository preflight before project writes. Do not create an Obsidian-only software project and defer its implementation home.

## Write

After approval:

1. create the target folder only if absent;
2. preserve existing work in place;
3. create or safely normalize `Assets/`;
4. instantiate the same-named home and `xPM/` records;
5. add only the selected profile document;
6. create or link the approved repository for a software profile and write the two-way links;
7. populate Status and Handoff with factual initialization state and the represented next action.

When normalizing a case-only asset folder on a case-insensitive filesystem, use a uniquely resolved sibling staging name only after confirming it does not exist, complete the two-step rename, update known references, and verify every moved asset. Never merge two asset folders automatically. Do not use a Git repository, ignored directory, or `.git` location as staging.

Do not add a placeholder Decision. If no accepted decision needs a log entry, create only the Decisions frontmatter and `# Decisions` heading.

## Direct-creation verification

Confirm the new project has no Area or candidate origin unless the user explicitly supplied a non-promotion provenance link. Confirm pre-existing files remain byte-for-byte present except for specifically approved reference updates or asset normalization.
