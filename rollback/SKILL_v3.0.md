---
name: max-imp-loop
description: Use when planning, changing, implementing, deploying, validating, or improving consequential work where a wrong choice could create material rework, operational risk, irreversible effects, or uncertain rollback.
---

# MAX_IMP_LOOP

## Overview

Apply version 3.0 to move from a known state to a better verified state without destroying the ability to return. The core rule is: **no material change without a recoverable prior state and a defined restoration test.**

This skill is additive. Higher-priority instructions, safety controls, privacy requirements, tool constraints, and explicit approval gates remain in force. Existing board requirements for independent lenses, dissent, and advisor signatures also remain in force.

**REQUIRED REFERENCE:** For every `FULL` or `GATED` task, read and apply `references/MAX_IMP_LOOP_v3.0.md`. Do not substitute this summary for the full protocol.

## When to Use

Use for architecture, implementation, configuration, migrations, deployments, security work, operational changes, financial systems, consequential documents, evaluations, and optimization where failure would matter.

Use `LIGHT` for low-risk factual or reversible work. Do not bury routine work in ceremony.

## Operating Contract

1. State the objective, success criteria, hard constraints, protected boundaries, and non-goals.
2. Triage as `LIGHT`, `FULL`, or `GATED`.
3. Inspect authoritative current state. Mark unsupported claims `UNKNOWN`.
4. Before a material change, preserve a known-good checkpoint and record restoration plus verification.
5. Evaluate credible alternatives; include `DO-NOTHING` unless clearly inapplicable.
6. Implement the smallest complete increment and preserve unrelated correct behavior.
7. Verify proportionally to the claim, including refusal, restart, replay, security, regression, and recovery paths where relevant.
8. Record failed approaches, invalidated assumptions, and bounded retries.
9. End each cycle with exactly one outcome: `SHIP`, `DO-NOTHING`, `STUCK`, or `ESCALATE`.
10. Stop at any consequential external-action boundary until the user gives explicit approval naming the action.

## Quick Reference

| Tier | Required depth | Action boundary |
|---|---|---|
| `LIGHT` | Ground → act/answer → verify | Proceed only if authorized, reversible, and non-sensitive |
| `FULL` | Complete v3.0 loop | Prepare and verify reversible work |
| `GATED` | Complete v3.0 loop | Stop before irreversible, external, sensitive, financial, destructive, permission-changing, or people-affecting action |

| Outcome | Meaning |
|---|---|
| `SHIP` | Verified, authorized, recoverable, ready for approved destination |
| `DO-NOTHING` | Current state wins on evidence and expected value |
| `STUCK` | Concrete technical or evidentiary blocker |
| `ESCALATE` | Human judgment, authority, access, or consequential tradeoff required |

## Example

For a production configuration change: capture the current version and hash, export the active configuration, prove how restoration works, isolate the candidate change, test expected and refusal paths, inspect the final diff, simulate rollback when risk justifies it, and only then classify the increment. A successful command alone is not `SHIP`.

## Common Mistakes

- Calling a backup a rollback without proving restoration.
- Treating implemented, running, working, verified, and authorized as equivalent.
- Repeating a failed approach without new evidence.
- Declaring a broad objective complete from a narrow test.
- Adding complexity without naming the failure it prevents.
- Treating reviewer agreement as permission to act.

## Red Flags

Stop and correct course when you see: no known-good checkpoint; untested recovery; silent canonical overwrite; production-first testing; “no error” used as proof; repeated equivalent retries; a false load-bearing assumption left in place; or pressure to act beyond authorization.
