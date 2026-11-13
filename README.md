# max-imp-loop v3.1 Universal Skill Package

Vendor-neutral governance for evidence-guided improvement, verification, recovery, and rollback.

## What is included

- `SKILL.md` — open Agent Skills-compatible discovery and activation instructions.
- `references/MAX_IMP_LOOP_v3.1_UNIVERSAL.md` — complete canonical protocol.
- `references/ENVIRONMENT_ADAPTATION.md` — capability discovery and abstract-to-native mapping.
- `MAX_IMP_LOOP_UNIVERSAL_DROP_IN_v3.1.md` — one-file fallback for any AI interface that accepts instructions but does not support native skills.
- `templates/` — environment profile, checkpoint report, and final proof matrix.
- `evals/` and `tests/` — trigger/output cases, pressure scenarios, and mechanical validation.
- `rollback/` — preserved v3.0 active files, renamed to prevent accidental duplicate skill discovery.
- `references/legacy/` — earlier governance references retained as historical evidence only.
- `MANIFEST.sha256` — package-integrity hashes.

## Universal use modes

### 1. Native skills-compatible runtime

Place the complete `max-imp-loop` directory in a supported user- or project-level skills location. Keep the directory name unchanged so it matches the frontmatter name.

Common cross-runtime project location:

```text
.agents/skills/max-imp-loop/
```

Common cross-runtime user location:

```text
~/.agents/skills/max-imp-loop/
```

The exact discovery path is controlled by the runtime. Verify discovery rather than assuming it.

### 2. Prompt, project, or custom-instruction interface

Paste or attach:

```text
MAX_IMP_LOOP_UNIVERSAL_DROP_IN_v3.1.md
```

This file is self-contained and includes the full protocol.

### 3. File-aware AI without automatic skill discovery

Provide the entire folder and explicitly instruct the AI to read `SKILL.md`. For every `FULL` or `GATED` task it must also read the two active references named in `SKILL.md`.

## Environment adaptation

The skill does not prescribe a particular shell, operating system, source-control product, deployment platform, memory system, or tool name. It first creates an Environment Profile, then maps checkpoints, verification, rollback, records, and approval to mechanisms actually available.

An AI with no tools remains advisory. An AI with read-only access does not claim writes. A stateless AI emits a carry-forward capsule. A runtime without native skill support uses the standalone drop-in.

## Safe upgrade and rollback

Do not overwrite the only known-good installation.

1. Preserve the current installed directory or package hash.
2. Install v3.1 beside or after a timestamped backup.
3. Validate structure and hashes.
4. Test one `LIGHT`, one `FULL`, one `GATED`, one no-tools, and one stateless scenario.
5. Roll back using `ROLLBACK.md` if the new wrapper underperforms.

## Validation

From the package parent directory:

```bash
python3 max-imp-loop/tests/validate_skill.py --skill-dir max-imp-loop
```

Mechanical validation proves package structure, canonical embedding, required governance controls, rollback preservation, and manifest integrity. It does not guarantee that every model will comply under pressure. Use the bundled evals and pressure scenarios across the target models before consequential deployment.

## Honest portability boundary

The package is universal in format and instruction design, not omnipotent. It cannot create tools, permissions, memory, background execution, or authority that a runtime does not provide, and it cannot override higher-priority instructions. Those limitations are surfaced rather than hidden.

**Version:** 3.1.1
**Execution authority:** none
**Adoption status:** candidate until accepted by the governing owner

## Get it

Standalone repo: `https://github.com/NukoTech/max-imp-loop`.

## Contributing

See `CONTRIBUTING.md`. Fork and open a pull request; maintainer review is required.

## License

MIT. Copyright (c) 2026 Nuko Technologies LLC. See `LICENSE`.
