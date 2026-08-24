# Direct creation

Use this mode for a new standalone project or for initializing a pre-existing working folder that is not being promoted from an Area candidate.

## Context boundary

Read only:

1. the applicable parent or project-local `AGENTS.md`, when present;
2. the exact target folder and its shallow file inventory;
3. existing files whose names or references affect the scaffold;
4. the packaged project, profile, schema, and repository resources needed by the selected profile.

Do not run a portfolio inventory or inspect sibling projects merely to choose metadata.

An explicitly supplied stewardship Area may be read only far enough to verify its exact home path and any product-direction links the user approved for this project. This is a relationship link, not candidate provenance or promotion. Do not search for a possible Area, infer one from similar naming, or rewrite Area state during direct creation.

## Preflight

Resolve the parent folder and calculate both `Project Name/` and `Project Name/_Project Name.md`. Confirm the folder and home note use the approved stable internal identity even when the eventual public name is provisional. The leading underscore is structural; the remainder of the home base name must exactly match the folder.

If the target folder does not exist, plan its creation. If it exists, preserve every working file and inspect only deeply enough to find scaffold, profile, link, or case collisions.

Stop for clarification when:

- the underscore-prefixed home or a legacy unprefixed home already exists and may represent an initialized project;
- a generic or differently named file could be the intended project home;
- `xPM/`, a profile document or folder, or the repository target has conflicting content;
- a profile-provided folder would collide with existing content or references that cannot be preserved confidently;
- the requested folder is an obvious archive or deletion candidate rather than a retained project.

For `software-product` or `software-tool`, finish repository preflight before project writes. Do not create an Obsidian-only software project and defer its implementation home.

## Write

After approval:

1. create the target folder only if absent;
2. preserve existing work in place;
3. instantiate the underscore-prefixed, folder-matching home and `xPM/` records;
4. write the explicitly approved project-specific role brief;
5. add only the selected profile tree;
6. create or link the approved repository for a software profile, write the two-way links, and synchronize the exact role brief into `AGENTS.md`;
7. when explicitly approved, add a relationship link to the stewardship Area and relevant canonical Area product-direction notes without copying their content or using promotion language;
8. populate Status and Handoff with factual initialization state and the represented next action.

Do not add a placeholder Decision. If no accepted decision needs a log entry, create only the Decisions frontmatter and `# Decisions` heading.

## Direct-creation verification

Confirm the new project has no candidate or promotion origin. When the user supplied a stewardship Area, confirm the link is represented as an ongoing relationship, the Area itself was not mutated, and no Area-owned direction was copied into the project. Confirm pre-existing files remain byte-for-byte present except for specifically approved reference updates.
