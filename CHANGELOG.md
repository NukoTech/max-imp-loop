# Changelog

## 3.1.1 — 2026-09-14

- Removed the deprecated top-level `compatibility` frontmatter key so the package conforms to the current ChatGPT skill schema.
- Kept the model-agnostic portability contract in the skill body and `metadata.portability` without changing operational behavior.
- Updated mechanical acceptance checks and the package manifest, including previously omitted `agents/openai.yaml` and `assets/icon.svg` integrity entries.

## Rollback target

Use the preserved v3.1.0 team ZIP or the package state immediately before this metadata-only migration.

## 3.1.0 — 2026-09-01

- Removed active coupling to any board, persona, vendor, operating system, shell, or agent framework.
- Added a required Environment Profile and capability-status model.
- Added abstract-to-native mapping for state, checkpoints, implementation, verification, rollback, records, and approval.
- Added explicit modes for native skill loaders, prompt-only interfaces, tool-enabled agents, read-only agents, no-tools agents, stateless agents, and runtimes without parallel or background execution.
- Added a self-contained universal drop-in containing the complete canonical protocol.
- Added carry-forward state requirements when persistent memory is unavailable.
- Added universal trigger/output evals and portability pressure scenarios.
- Preserved v3.0 active files under `rollback/` without a nested discoverable `SKILL.md`.
- Updated validation to enforce open Agent Skills naming/frontmatter constraints, canonical embedding, vendor neutrality of active governance, and manifest integrity.

## Rollback target

Use the files in `rollback/` to reconstruct the v3.0 active layer. The prior v3.0 ZIP remains the strongest whole-package rollback artifact.

## 3.0.0 — 2026-09-01

- Made recoverable prior state a non-negotiable invariant.
- Distinguished backup existence from proven restoration capability.
- Separated documented, intended, implemented, running, working, verified, authorized, and production-ready states.
- Separated technical correctness from execution authority.
- Added `LIGHT`, `FULL`, and `GATED` triage.
- Added explicit success criteria, protected boundaries, non-goals, and guardrail metrics.
- Added rollback envelopes with checkpoint IDs and restoration verification.
- Required `DO-NOTHING` as a normal candidate.
- Added red-team, complexity-delta, and change-state controls.
- Added proportional verification, rollback testing, and observation windows.
- Added negative knowledge, load-bearing assumption invalidation, and bounded retries.
- Added marginal-improvement stopping rules and protocol self-protection.
- Added calibration, evidence labels, four explicit cycle outcomes, checkpoint reports, and final proof matrices.
- Preserved the v2 Tech Board plan/build source and Sentinel Protocol v1 unchanged under `references/legacy/`.

## Rollback target

The preserved predecessor sources are available under `references/legacy/`. Reverting to them is a governance decision; their inclusion does not silently reactivate them.
