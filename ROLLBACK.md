# Rollback from v3.1 Universal to v3.0

## Preserved state

The following v3.0 active files are preserved byte-for-byte from the previous package:

- `rollback/SKILL_v3.0.md`
- `rollback/MAX_IMP_LOOP_v3.0.md`
- `rollback/MANIFEST_v3.0.sha256`

They are renamed so recursive skill scanners do not discover a second active `SKILL.md`.

## Preferred rollback

Restore the complete prior archive:

```text
max-imp-loop-v3.0-skill.zip
```

Verify its SHA-256 against the known prior receipt before installation.

## File-level reconstruction

When the prior archive is unavailable:

1. Preserve the v3.1 installation and its hash as failed-candidate evidence.
2. Copy `rollback/SKILL_v3.0.md` to a clean `max-imp-loop/SKILL.md`.
3. Copy `rollback/MAX_IMP_LOOP_v3.0.md` to `max-imp-loop/references/MAX_IMP_LOOP_v3.0.md`.
4. Restore the remaining v3.0 package files from a verified source or use the prior archive.
5. Run the v3.0 validator and behavioral scenarios.

Do not mix an active v3.0 `SKILL.md` with the v3.1 canonical reference and call the result restored. A partial reconstruction remains `STUCK` until validated.

## Rollback trigger examples

- Target runtimes fail to discover or activate v3.1 materially more often than v3.0.
- Environment adaptation causes excessive ceremony on `LIGHT` tasks.
- The wrapper suppresses authorized execution instead of adapting to it.
- Cross-model evals show worse compliance or higher false-trigger rates.
