# Area-candidate promotion

Use this mode only when the user explicitly approves promotion of a named candidate from a named Area.

## Context boundary

Read, in order:

1. the Area folder's `AGENTS.md`, when present;
2. the same-named Area home;
3. the candidate's linked `xPM/Notes/PC-*` note when one exists;
4. Area Status and Handoff;
5. Area Decisions only when needed to interpret an accepted promotion or origin rule;
6. the exact proposed project target and applicable packaged resources.

Do not load unrelated Area tasks, sibling candidates, or other projects. A candidate note that remains after deletion from the Area home is non-actionable and cannot authorize promotion.

## Promotion preconditions

Require explicit confirmation of:

- the exact Area and candidate;
- approval to promote now, not merely candidate maturity or readiness;
- project identity, objective, definition of done, classification, profile, and represented next action;
- a project-specific role brief approved for the promoted project rather than copied blindly from the Area;
- whether the Area-home proposal will be replaced with a compact Related Projects link or retained in another explicitly approved form;
- the origin links to preserve.

For a software profile, preflight and approve the required repository before mutating the Area or creating the promoted project. Do not leave the Area showing a completed promotion when repository setup failed.

## Preserve origin and authority

The promoted project must link to:

- the originating Area home;
- the candidate note ID when a candidate note exists;
- the promotion date under the contract's timezone rule.

The Area home must link to the promoted project outside the inactive Proposed Projects representation. The candidate note, when retained, must record the promotion date and promoted-project link without pretending its former maturity activates a second project.

Preserve the Area's lifecycle, blockers, operational tasks, and next action unless the user separately approves a factual synchronization change. Promotion of one candidate does not authorize execution or reprioritization of an Area task.

## Write

After approval:

1. create or link the required repository for a software profile;
2. instantiate the project using the shared scaffold rules;
3. add the approved project-specific role brief and synchronize it to repository `AGENTS.md` when applicable;
4. add the approved Area and candidate origin links to the project;
5. replace or revise the Area proposal exactly as approved;
6. update the candidate note's promotion history when present;
7. synchronize the Area and project handoffs with the same factual promotion outcome;
8. leave both represented operational next actions unexecuted.

If a write fails after a partial promotion, do not remove history or overwrite files to conceal it. Report the exact partial state and the smallest safe recovery action.

## Promotion verification

Verify that:

- the Area remains an Area and the new record is a project;
- the candidate is no longer represented as inactive work;
- Area, candidate, and project links resolve in both directions when the candidate note exists;
- the promotion decision and date are recoverable from files;
- Area lifecycle, blockers, tasks, and next action remain internally synchronized;
- project lifecycle, blockers, and next action remain internally synchronized;
- no repository, external service, or represented next action beyond the approved initialization plan was created or performed.
