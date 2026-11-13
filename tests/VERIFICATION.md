# Verification Record — v3.1 Universal

## RED baseline

The universal acceptance test was written first and run against v3.0. It failed 20 checks because the active wrapper lacked explicit environment capability discovery, degraded-capability modes, a standalone prompt-only fallback, and contained active Tech Board coupling.

Evidence: `tests/baseline-v3.0-universal-validation.txt`.

## GREEN candidate

The same universal acceptance test was then run against v3.1 and passed.

Evidence: `tests/v3.1-universal-acceptance.txt`.

The full package validator additionally checks open Agent Skills naming/frontmatter constraints, all core loop controls, byte-identical canonical embedding in the standalone drop-in, preserved rollback hashes, eval structure, absence of nested discoverable skills, and `MANIFEST.sha256` integrity.

Run from the skill parent directory:

```bash
python3 max-imp-loop/tests/validate_skill.py --skill-dir max-imp-loop
```

## Behavioral limit

Mechanical validation does not prove that every AI will follow the skill under pressure. Behavioral portability must be measured in each target runtime using `evals/evals.json` and `tests/pressure-scenarios.md`. The package is designed to adapt; it does not manufacture missing tools, permissions, memory, or compliance.
