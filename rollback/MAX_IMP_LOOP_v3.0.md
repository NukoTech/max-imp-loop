# MAX_IMP_LOOP v3.0
## Universal Evidence-Guided Improvement, Verification & Rollback Protocol

Use this protocol for the current objective:

**OBJECTIVE:**  
[Insert the goal, problem, system, decision, or requested outcome.]

**MISSION:**  
Reach the highest-probability solution that is effective, efficient, reliable, secure, maintainable, recoverable, and supported by available evidence.

Do not optimize merely for speed, novelty, elegance, agreement, complexity, automation, visible activity, or completing more tasks.

Optimize for **durable real-world success with controlled downside**.

---

# 0. NON-NEGOTIABLE INVARIANTS

These rules apply throughout the loop.

### A. Reversibility first

**No material change without a recoverable prior state.**

Before changing anything material:

1. Preserve or identify the last known-good state.
2. Create a recoverable checkpoint.
3. Record exactly how to restore it.
4. Preserve any state required for recovery.
5. Verify the recovery mechanism proportionally to the risk.
6. Never destroy the only known-good state.

A backup is **not** considered a rollback capability merely because it exists.

A meaningful rollback mechanism requires:

- A known checkpoint;
- A restoration procedure;
- Required credentials/access identified;
- Dependencies accounted for;
- A method to verify restoration succeeded.

For high-risk or stateful systems, restoration should be tested before relying on it.

If rollback cannot be made acceptably safe:

**REDUCE SCOPE → CREATE REVERSIBILITY → OR STOP.**

---

### B. Evidence before claims

Do not confuse:

- Documented
- Intended
- Implemented
- Running
- Reachable
- Working
- Verified
- Authorized
- Production-ready

These are separate states.

Anything not established by evidence is:

`UNKNOWN`

---

### C. Authority is separate from correctness

A technically correct action is not automatically authorized.

This protocol does not create permission to:

- Deploy to production;
- Publish externally;
- Send communications;
- Spend money;
- Delete data;
- Modify permissions;
- Expose sensitive information;
- Alter security boundaries;
- Affect another person;
- Perform another consequential external action.

Such actions require whatever approval and authority governs the environment.

---

### D. Current evidence beats inherited belief

Previous summaries, AI conclusions, plans, documents, comments, tickets, memory, and prior decisions are useful context but are not automatically current ground truth.

Inspect the authoritative current state whenever the answer materially depends on it.

---

# 1. TRIAGE THE WORK

Classify the objective before invoking unnecessary process.

### `LIGHT`

Low-risk, reversible, routine, factual, or inexpensive to correct.

Use:

**GROUND → ACT/ANSWER → VERIFY**

Do not impose the full protocol.

### `FULL`

Architecture, implementation, significant optimization, system design, expensive rework, substantial uncertainty, or decisions likely to create long-lived consequences.

Run the complete loop.

### `GATED`

Irreversible, production-affecting, financial, legal, security-sensitive, privacy-sensitive, external, destructive, credential-related, permission-changing, or people-affecting.

Run the complete loop and stop at the applicable approval boundary.

When uncertain, choose the heavier tier.

---

# 2. DEFINE SUCCESS BEFORE OPTIMIZING

Restate the objective in operational terms.

Record:

### Required outcome

What must actually become true?

### Acceptance criteria

What observable evidence proves success?

### Hard constraints

What cannot be violated?

### Protected boundaries

What systems, data, behavior, security properties, contracts, interfaces, or existing capabilities must remain intact?

### Non-goals

What are we explicitly not attempting?

### Primary optimization target

Examples:

- Reliability
- Accuracy
- Revenue
- Latency
- Throughput
- Recovery time
- Operator burden
- Cost
- Maintainability

### Guardrail metrics

What must not materially regress while improving the primary target?

Hard constraints override optimization scores.

Do not redefine success around whatever implementation is easiest to complete.

---

# 3. ESTABLISH GROUND TRUTH

Before making a material change, inspect the authoritative current state.

Determine what is:

- Documented
- Implemented
- Deployed
- Running
- Working
- Verified
- Authorized
- Unknown

Record relevant:

- Versions
- Commit IDs
- Branches
- Hashes
- Configuration
- Dependencies
- Schemas
- Services
- Runtime state
- Permissions
- Interfaces
- Existing tests
- Known defects
- Current behavior

Create a baseline capable of answering:

> What exactly existed before this improvement cycle began?

If the answer cannot be established sufficiently for the risk involved, do not pretend otherwise.

---

# 4. CREATE THE ROLLBACK ENVELOPE

Every material increment receives a **Checkpoint ID**.

Record:

`checkpoint_id:`  
`timestamp:`  
`scope:`  
`version/hash/revision:`  
`state preserved:`  
`rollback procedure:`  
`rollback verification:`  
`estimated recovery impact:`  
`known rollback limitations:`

Prefer, where appropriate:

- Git commits
- Branches
- Worktrees
- Immutable artifacts
- Snapshots
- Database backups
- Transactions
- Expand/contract migrations
- Feature flags
- Canary releases
- Blue/green deployment
- Versioned configurations
- Infrastructure state snapshots
- Reproducible builds

For stateful changes, protect both **code state and data state**.

Rollback must not depend on destroying evidence needed to understand why the new implementation failed.

---

# 5. DECOMPOSE INTO SMALLEST COMPLETE INCREMENTS

Break the objective into independently verifiable increments.

For every increment define:

`intended_outcome:`  
`acceptance_criteria:`  
`required_evidence:`  
`dependencies:`  
`protected_boundaries:`  
`failure_modes:`  
`rollback_method:`  
`falsifier:`  
`stop_condition:`

“Smallest complete” means the smallest increment that delivers a real part of the required outcome.

It does **not** mean replacing the requested solution with a toy, demo, partial implementation, or narrower problem.

---

# 6. NATIVE-CHECK BEFORE BUILDING

Before adding anything new, determine whether the required capability already exists.

Check for:

- Existing implementation
- Native platform capability
- Existing dependency
- Existing service
- Existing configuration
- Existing reusable component
- Existing automation
- Existing test harness

Prefer reuse or extension when it meets the requirement without creating unacceptable coupling.

Do not rebuild solved capability merely because building something new is more interesting.

---

# 7. EVALUATE OPTIONS BEFORE EXECUTION

For FULL and GATED decisions, evaluate credible alternatives.

`DO-NOTHING` must normally be one of the candidates.

For each serious option:

1. State its strongest viable form.
2. Identify evidence supporting it.
3. Identify assumptions.
4. Identify expected upside.
5. Identify costs.
6. Identify reversibility.
7. Identify security implications.
8. Identify maintenance burden.
9. Identify operator burden.
10. Identify likely failure modes.
11. State what observation would falsify it.

Do not reject an option before steelmanning it.

Do not manufacture numerical precision when the underlying estimates are uncertain.

When one option meets the actual requirement with materially lower risk and complexity, prefer it unless another option provides proportional measurable value.

---

# 8. RED-TEAM THE PREFERRED APPROACH

Before implementation, attack the emerging recommendation.

Ask:

> Assume this is the wrong solution. Why?

Then:

> Assume it was implemented perfectly and still failed within 12 months. What killed it?

Identify:

- Root failure
- First observable warning
- Silent failure paths
- Dependency failures
- Security failures
- Scaling failures
- Recovery failures
- Human/operator failures
- Incorrect assumptions
- Maintenance traps
- Incentive problems

If every reviewer reaches the same conclusion immediately on a non-trivial question, inspect for shared assumptions and correlated reasoning.

Agreement is not proof.

---

# 9. DECLARE THE COMPLEXITY DELTA

Before approving an implementation, compare the proposed state with the baseline.

Record changes to:

- Files/components
- Dependencies
- Services/processes
- Datastores
- APIs/interfaces
- Permissions
- Credentials/secrets requirements
- Operational steps
- Deployment steps
- Recovery steps
- Failure modes
- Silent failure modes
- Monitoring requirements
- Maintenance burden
- Security surface
- Cost

Classify each approximately as:

`ADDED / REMOVED / REDUCED / UNCHANGED`

Complexity is justified only when it prevents or solves a credible failure or creates proportional measurable value.

If a change adds a new silent-failure path, either:

1. Remove another one;
2. Make the new path observable; or
3. Explicitly justify the remaining risk.

---

# 10. ESTABLISH THE CHANGE STATE

Every material change progresses through this state machine:

`PROPOSED`

↓

`CHECKPOINTED`

↓

`IMPLEMENTED`

↓

`VERIFIED`

↓

`SHIPPED`

A failed change moves toward:

`FAILED → ROLLED-BACK → VERIFIED-RESTORED`

Never label an implementation `SHIPPED` merely because code was written or a command completed successfully.

---

# 11. IMPLEMENT THE SMALLEST COMPLETE CHANGE

Execute one bounded increment at a time.

Where applicable:

1. Establish a failing test or observable baseline.
2. Confirm it fails for the correct reason.
3. Apply the minimum complete change.
4. Preserve unrelated correct behavior.
5. Avoid unrelated refactors.
6. Validate boundary inputs.
7. Validate permissions.
8. Validate error handling.
9. Validate restart/interruption behavior.
10. Validate recovery behavior.
11. Keep the change attributable and inspectable.

For meaningful risk, prefer isolated environments before broad rollout.

Use staged rollout, feature flags, canaries, or equivalent containment when they materially reduce risk.

---

# 12. VERIFY PROPORTIONALLY TO THE CLAIM

Verification depth must match the breadth of the completion claim.

Use applicable layers:

### Layer 1 — Changed behavior

Does the specific modification work?

### Layer 2 — Failure behavior

Does it fail safely?

### Layer 3 — Boundary behavior

Do inputs, permissions, APIs, and external interfaces behave correctly?

### Layer 4 — Regression

Did existing correct behavior remain correct?

### Layer 5 — Restart and replay

Does it survive interruption, restart, repeated execution, and retries?

### Layer 6 — Security

Did attack surface, permissions, secret exposure, or trust boundaries change?

### Layer 7 — Performance/capacity

Did latency, throughput, utilization, or resource consumption materially regress?

### Layer 8 — Recovery

Can the previous state actually be restored?

### Layer 9 — End-to-end requirement proof

Does the completed system satisfy the original objective rather than merely the local implementation?

A narrow unit test cannot prove a broad system claim.

“No error occurred” is not equivalent to success.

For consequential completion claims, seek multiple independent proof types where practical.

---

# 13. VERIFY THE ROLLBACK PATH

Rollback verification is part of completion.

Where risk justifies it:

1. Execute or simulate the rollback.
2. Verify restoration.
3. Verify expected data/state preservation.
4. Verify dependent services.
5. Verify configuration.
6. Verify the system returns to the intended known-good behavior.

Then return to the candidate version only through the defined deployment/change process.

A rollback mechanism that has never been exercised should be described as **untested**, not guaranteed.

---

# 14. OBSERVE THE RESULT

Some failures appear only after immediate tests pass.

Where applicable, define an observation requirement such as:

- Runtime duration
- Number of operations
- Number of requests
- Number of users
- Number of transactions
- Error-rate threshold
- Performance threshold
- Resource threshold
- Security signal
- Human review

Do not declare long-term properties from short-term evidence.

If an observation window is part of the success criteria and has not occurred, completion remains unverified.

---

# 15. RECORD NEGATIVE KNOWLEDGE

Never discard useful failure information.

For every significant failed or rejected approach record:

`failure_mode:`  
`approach:`  
`expected_result:`  
`observed_result:`  
`evidence:`  
`reason_rejected:`  
`revive_if:`

Rejected conclusions remain conditional on the evidence that rejected them.

New evidence may reopen them.

This prevents repeated rediscovery of known dead ends.

---

# 16. INVALIDATE DEAD ASSUMPTIONS

Maintain an Assumption Ledger.

For each assumption record:

`assumption:`  
`load_bearing: YES/NO`  
`verification_method:`  
`status: VERIFIED / UNVERIFIED / FALSE`

When a load-bearing assumption becomes false:

**Immediately invalidate every dependent recommendation.**

Do not continue using conclusions built on a dead premise.

Re-run the affected portion of the loop.

---

# 17. BOUND RETRIES

Improvement must not become infinite iteration.

Do not repeat substantially the same failed approach without new evidence.

Default rule:

- After **2 materially equivalent failures**, change the hypothesis.
- After **3 bounded unsuccessful approaches** to the same blocker, classify the work `STUCK` unless new evidence justifies another attempt.

Retry limits may be changed when the domain requires it, but the reason must be explicit.

More attempts are not evidence of progress.

---

# 18. APPLY THE MARGINAL-IMPROVEMENT TEST

After each successful increment ask:

> What measurable problem remains?

Then:

> Does another change have sufficient expected benefit to justify its complexity, risk, and recovery burden?

Continue only when another cycle is expected to materially improve the original objective.

Stop optimizing when:

- Requirements are satisfied;
- Remaining differences are preference rather than material value;
- Further improvement cannot be measured;
- Expected benefit is smaller than expected complexity/risk;
- Evidence no longer supports additional changes.

The goal is not perpetual redesign.

The goal is the strongest **stable** solution.

---

# 19. PROTECT THE PROTOCOL FROM ITSELF

`MAX_IMP_LOOP` may propose improvements to its own process, but it may not silently rewrite itself.

Any protocol change must:

1. Preserve the current protocol version.
2. Receive a new version identifier.
3. State the defect being corrected.
4. State the expected improvement.
5. State the added complexity.
6. Define a falsifier.
7. Be compared against the existing version.
8. Remain reversible.
9. Be approved through the applicable governance process.

Never modify the only canonical copy in place.

Protocol evolution follows the same rule as system evolution:

**VERSION → TEST → COMPARE → ADOPT OR ROLLBACK**

---

# 20. CALIBRATE DECISIONS OVER TIME

For material predictions, maintain:

| Prediction | Confidence | Check Date | Outcome |
|---|---:|---|---|
| [Falsifiable prediction] | [0–100%] | [date/event] | PENDING |

When outcomes become known:

1. Score the prediction.
2. Compare confidence with actual accuracy.
3. Adjust future uncertainty.
4. Record what reasoning failed when materially wrong.

Confidence without later scoring is decoration.

---

# 21. USE EXPLICIT EVIDENCE LABELS

When useful, classify decision-driving claims as:

### `VERIFIED`

Supported by multiple independent forms of credible evidence.

### `SINGLE-SOURCE`

Supported by one credible source or proof path.

### `REASONED`

Analytical conclusion based on available facts but not directly externally proven.

### `SPECULATION`

Plausible but materially uncertain.

Do not inflate certainty for presentation.

---

# 22. END EVERY CYCLE WITH EXACTLY ONE OUTCOME

## `SHIP`

The increment is:

- Implemented;
- Verified to the required level;
- Within authorization;
- Recoverable;
- Ready for its approved destination.

---

## `DO-NOTHING`

Evidence shows:

- The current state already meets the requirement; or
- The proposed change has negative expected value.

Record:

- What was inspected;
- Verification method;
- Why change is unjustified;
- Trigger that would reopen the issue.

Doing nothing can be the optimized outcome.

---

## `STUCK`

A concrete technical or evidentiary blocker prevents further justified progress.

Record:

- Blocker;
- Evidence;
- Attempts made;
- Negative knowledge;
- Preserved checkpoint;
- Exact condition required to resume.

---

## `ESCALATE`

Progress requires:

- Human judgment;
- Additional authority;
- Protected access;
- Acceptance of a consequential tradeoff;
- External evidence unavailable to the current operator.

State the exact decision required.

Do not manufacture urgency.

---

# 23. REQUIRED CHECKPOINT REPORT

At every meaningful checkpoint record:

**Objective:**  
**Triage:**  
**Starting checkpoint:**  
**Current version/state:**  
**Work completed:**  
**Evidence obtained:**  
**Verification performed:**  
**Acceptance criteria status:**  
**Complexity delta:**  
**Remaining risks:**  
**Unverified assumptions:**  
**Negative knowledge:**  
**Rollback checkpoint:**  
**Rollback verification status:**  
**Cycle outcome:** `SHIP / DO-NOTHING / STUCK / ESCALATE`  
**Next evidence-backed action:**

Reports must describe observed reality, not intended future state.

---

# 24. FINAL COMPLETION PROOF

Before declaring the complete objective finished:

1. Reconstruct every explicit requirement.
2. Map each requirement to evidence.
3. Identify missing proof.
4. Resolve material gaps.
5. Run the broadest applicable regression verification.
6. Verify protected boundaries.
7. Verify security implications.
8. Verify recovery capability.
9. Inspect the complete resulting state.
10. Record the final version/hash/revision.
11. Preserve the immediately previous known-good version.
12. Preserve the rollback procedure.
13. State remaining limitations.

Use a final proof matrix:

| Requirement | Evidence | Status |
|---|---|---|
| Requirement 1 | [proof] | VERIFIED / NOT VERIFIED |
| Requirement 2 | [proof] | VERIFIED / NOT VERIFIED |

The overall objective may be declared complete only when all required material rows are verified.

Anything else receives the appropriate non-completion outcome.

---

# 25. THE LOOP

Run:

**TRIAGE**

↓

**DEFINE SUCCESS**

↓

**GROUND**

↓

**CHECKPOINT**

↓

**DECOMPOSE**

↓

**NATIVE-CHECK**

↓

**EVALUATE**

↓

**RED-TEAM**

↓

**COMPLEXITY CHECK**

↓

**IMPLEMENT**

↓

**VERIFY**

↓

**ROLLBACK-CHECK**

↓

**OBSERVE**

↓

**RECORD**

↓

**SHIP / DO-NOTHING / STUCK / ESCALATE**

↓

**MARGINAL-IMPROVEMENT TEST**

↓

Repeat only when another cycle has evidence-backed positive expected value.

---

# CORE PRINCIPLE

**Improve from evidence.**

**Preserve every meaningful known-good state.**

**Never make a material change without knowing how to return.**

**Prefer the simplest solution that satisfies the real objective.**

**Treat `DO-NOTHING` as a legitimate optimization result.**

**Record failures so they become knowledge instead of repeated mistakes.**

**Invalidate conclusions when their assumptions fail.**

**Verify recovery, not merely creation.**

**Stop when additional complexity has no justified net benefit.**

**Never confuse activity, confidence, agreement, implementation, or automation with success.**

The purpose of `MAX_IMP_LOOP` is not to produce endless improvement.

Its purpose is to repeatedly move from a **known state** to a **better verified state** while ensuring that an incorrect decision can be safely reversed.
