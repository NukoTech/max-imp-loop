#!/usr/bin/env python3
"""Mechanical validation for MAX_IMP_LOOP v3.1 Universal.

Checks open Agent Skills structure, active-governance portability, core protocol
controls, exact canonical embedding, rollback preservation, eval presence, and
manifest integrity. It does not prove behavioral compliance across models.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

REQUIRED_FILES = {
    "SKILL.md",
    "README.md",
    "CHANGELOG.md",
    "ROLLBACK.md",
    "MAX_IMP_LOOP_UNIVERSAL_DROP_IN_v3.1.md",
    "references/MAX_IMP_LOOP_v3.1_UNIVERSAL.md",
    "references/ENVIRONMENT_ADAPTATION.md",
    "references/legacy/MAX_IMP_LOOP_PLAN_BUILD_ADVISORY_v2.md",
    "references/legacy/SENTINEL_PROTOCOL_v1.md",
    "templates/ENVIRONMENT_PROFILE.md",
    "templates/CHECKPOINT_REPORT.md",
    "templates/FINAL_PROOF_MATRIX.md",
    "evals/evals.json",
    "tests/pressure-scenarios.md",
    "tests/VERIFICATION.md",
    "tests/baseline-v3.0-universal-validation.txt",
    "tests/universal_acceptance.py",
    "rollback/SKILL_v3.0.md",
    "rollback/MAX_IMP_LOOP_v3.0.md",
    "rollback/MANIFEST_v3.0.sha256",
    "MANIFEST.sha256",
}

EXPECTED_ROLLBACK_HASHES = {
    "rollback/SKILL_v3.0.md": "7806f9e548f2cbde7b3fb7ce9116ebd7e70c24324d19e0554c0b168608c527a9",
    "rollback/MAX_IMP_LOOP_v3.0.md": "d30b9354ecba71df12e3287a9f6e54ab7ec598bf4eeb02e60ea650e5de9c48dc",
    "rollback/MANIFEST_v3.0.sha256": "9ebb727fe7f50eb779002af44acc055d47b3cfac229ccb1fed3e489d2c72c2a7",
    "references/legacy/MAX_IMP_LOOP_PLAN_BUILD_ADVISORY_v2.md": "cff9bbc6cb5b661dcb5f21749dc6ac012f65608438940d0ec299a476417dfb63",
    "references/legacy/SENTINEL_PROTOCOL_v1.md": "7b79501d1e78816cbff02178c11425f5092e7abdac38ebe5d52a7cc4037c0d96",
}

CORE_PROTOCOL_PATTERNS = {
    "version": r"^# MAX_IMP_LOOP v3\.1 Universal$",
    "reversibility invariant": r"No material change without a recoverable prior state",
    "backup is not rollback": r"backup is \*\*not\*\* considered a rollback capability",
    "evidence states": r"Documented[\s\S]*Intended[\s\S]*Implemented[\s\S]*Running[\s\S]*Verified[\s\S]*Authorized",
    "authority separation": r"Authority is separate from correctness",
    "environment adaptation": r"ADAPT TO THE CURRENT ENVIRONMENT",
    "environment status model": r"AVAILABLE / LIMITED / UNAVAILABLE / UNKNOWN",
    "native mapping": r"Map the protocol to native mechanisms",
    "no assumed capabilities": r"Do not assume a shell, filesystem, source-control system, network, persistent memory",
    "no fabricated capabilities": r"Never invent or simulate unavailable tools, permissions, persistence, memory",
    "read-only mode": r"\*\*Read-only:\*\*",
    "no-tools mode": r"\*\*No tools:\*\*",
    "stateless carry-forward": r"Stateless or no persistent memory[\s\S]*carry-forward state capsule",
    "no parallel reviewer caveat": r"No parallel reviewers[\s\S]*correlated reasoning",
    "no background caveat": r"No background execution",
    "content authority boundary": r"Instructions or approvals found inside documents[\s\S]*data—not governing authority",
    "triage": r"`LIGHT`[\s\S]*`FULL`[\s\S]*`GATED`",
    "success criteria": r"DEFINE SUCCESS BEFORE OPTIMIZING",
    "ground truth": r"ESTABLISH GROUND TRUTH",
    "rollback envelope": r"CREATE THE ROLLBACK ENVELOPE",
    "checkpoint id": r"checkpoint_id:",
    "smallest complete increment": r"SMALLEST COMPLETE INCREMENTS",
    "native check": r"NATIVE-CHECK BEFORE BUILDING",
    "do nothing candidate": r"`DO-NOTHING` must normally be one of the candidates",
    "steelman": r"Do not reject an option before steelmanning it",
    "red team": r"RED-TEAM THE PREFERRED APPROACH",
    "complexity delta": r"DECLARE THE COMPLEXITY DELTA",
    "change state machine": r"`PROPOSED`[\s\S]*`CHECKPOINTED`[\s\S]*`IMPLEMENTED`[\s\S]*`VERIFIED`[\s\S]*`SHIPPED`",
    "failed rollback state": r"`FAILED → ROLLED-BACK → VERIFIED-RESTORED`",
    "small implementation": r"IMPLEMENT THE SMALLEST COMPLETE CHANGE",
    "proportional verification": r"VERIFY PROPORTIONALLY TO THE CLAIM",
    "rollback verification": r"VERIFY THE ROLLBACK PATH",
    "observation": r"OBSERVE THE RESULT",
    "negative knowledge": r"RECORD NEGATIVE KNOWLEDGE",
    "assumption invalidation": r"INVALIDATE DEAD ASSUMPTIONS",
    "bounded retries": r"BOUND RETRIES",
    "marginal improvement": r"MARGINAL-IMPROVEMENT TEST",
    "self-protection": r"PROTECT THE PROTOCOL FROM ITSELF",
    "calibration": r"CALIBRATE DECISIONS OVER TIME",
    "evidence labels": r"`VERIFIED`[\s\S]*`SINGLE-SOURCE`[\s\S]*`REASONED`[\s\S]*`SPECULATION`",
    "four outcomes": r"## `SHIP`[\s\S]*## `DO-NOTHING`[\s\S]*## `STUCK`[\s\S]*## `ESCALATE`",
    "checkpoint report": r"REQUIRED CHECKPOINT REPORT",
    "final proof": r"FINAL COMPLETION PROOF",
    "proof matrix": r"\| Requirement \| Evidence \| Status \|",
    "full loop": r"# 26\. THE LOOP",
}

SKILL_REQUIRED_PATTERNS = {
    "full protocol": r"references/MAX_IMP_LOOP_v3\.1_UNIVERSAL\.md",
    "adaptation reference": r"references/ENVIRONMENT_ADAPTATION\.md",
    "prompt-only fallback": r"MAX_IMP_LOOP_UNIVERSAL_DROP_IN_v3\.1\.md",
    "environment profile": r"Environment Profile",
    "capability discovery": r"Discover the current environment's capabilities",
    "no assumptions": r"Do not assume.*tool, shell, filesystem, version control system, network access, persistent memory",
    "read-only": r"\*\*Read-only:\*\*",
    "no-tools": r"\*\*No-tools or prompt-only:\*\*",
    "stateless": r"\*\*Stateless or no persistent memory:\*\*",
    "approval": r"explicitly approves the named action",
    "four outcomes": r"SHIP[\s\S]*DO-NOTHING[\s\S]*STUCK[\s\S]*ESCALATE",
    "mistakes": r"## Common Mistakes",
    "red flags": r"## Red Flags",
}

FORBIDDEN_ACTIVE_PATTERNS = {
    "specific AI vendor": r"\b(?:OpenAI|ChatGPT|Anthropic|Claude|Gemini|Grok|Codex)\b",
    "Tech Board coupling": r"Tech Board|existing board requirements|advisor signatures",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def check_patterns(text: str, patterns: dict[str, str], where: str) -> list[str]:
    failures: list[str] = []
    for label, pattern in patterns.items():
        if not re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
            failures.append(f"{where} missing: {label}")
    return failures


def parse_frontmatter(text: str) -> tuple[dict[str, object] | None, str | None]:
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        return None, "SKILL.md missing YAML frontmatter"

    # Minimal parser for the fixed fields this package uses. Avoids external deps.
    block = match.group(1)
    data: dict[str, object] = {}
    metadata: dict[str, str] = {}
    in_metadata = False
    for line in block.splitlines():
        if line.strip() == "metadata:":
            in_metadata = True
            data["metadata"] = metadata
            continue
        if in_metadata and line.startswith("  "):
            key, sep, value = line.strip().partition(":")
            if not sep:
                return None, f"malformed metadata line: {line}"
            metadata[key.strip()] = value.strip().strip('"\'')
            continue
        in_metadata = False
        key, sep, value = line.partition(":")
        if not sep:
            return None, f"malformed frontmatter line: {line}"
        data[key.strip()] = value.strip().strip('"\'')
    return data, None


def check_frontmatter(root: Path, text: str) -> list[str]:
    failures: list[str] = []
    fm, error = parse_frontmatter(text)
    if error:
        return [error]
    assert fm is not None

    name = str(fm.get("name", ""))
    description = str(fm.get("description", ""))
    metadata = fm.get("metadata", {})

    allowed_keys = {"name", "description", "license", "metadata", "allowed-tools"}
    unexpected_keys = sorted(set(fm) - allowed_keys)
    if unexpected_keys:
        failures.append(f"unsupported frontmatter keys: {', '.join(unexpected_keys)}")

    if name != root.name:
        failures.append("frontmatter name must exactly match parent directory")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        failures.append("frontmatter name must use lowercase letters, numbers, and single hyphens")
    if len(name) > 64:
        failures.append("frontmatter name exceeds 64 characters")
    if not description or len(description) > 1024:
        failures.append("frontmatter description must be 1-1024 characters")
    if not description.startswith("Use this skill when"):
        failures.append("frontmatter description lacks explicit trigger wording")
    if not isinstance(metadata, dict) or metadata.get("version") != "3.1.1":
        failures.append("metadata version is not 3.1.1")
    if not isinstance(metadata, dict) or metadata.get("portability") != "universal":
        failures.append("metadata portability is not universal")
    return failures


def check_manifest(root: Path) -> list[str]:
    failures: list[str] = []
    manifest = root / "MANIFEST.sha256"
    if not manifest.is_file():
        return ["missing MANIFEST.sha256"]

    listed: set[str] = set()
    for number, line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        digest, sep, rel = line.partition("  ")
        if not sep or not re.fullmatch(r"[0-9a-f]{64}", digest):
            failures.append(f"manifest malformed line {number}")
            continue
        path = root / rel
        listed.add(rel)
        if not path.is_file():
            failures.append(f"manifest references missing file: {rel}")
        elif sha256(path) != digest:
            failures.append(f"manifest mismatch: {rel}")

    actual = {
        p.relative_to(root).as_posix()
        for p in root.rglob("*")
        if p.is_file() and p.name != "MANIFEST.sha256"
    }
    missing_from_manifest = sorted(actual - listed)
    stale_entries = sorted(listed - actual)
    for rel in missing_from_manifest:
        failures.append(f"file missing from manifest: {rel}")
    for rel in stale_entries:
        failures.append(f"stale manifest entry: {rel}")
    return failures


def check_dropin(root: Path) -> list[str]:
    failures: list[str] = []
    dropin = root / "MAX_IMP_LOOP_UNIVERSAL_DROP_IN_v3.1.md"
    protocol = root / "references/MAX_IMP_LOOP_v3.1_UNIVERSAL.md"
    if not dropin.is_file() or not protocol.is_file():
        return failures

    text = dropin.read_text(encoding="utf-8")
    begin = "<!-- BEGIN CANONICAL PROTOCOL -->\n"
    end = "\n<!-- END CANONICAL PROTOCOL -->"
    if begin not in text or end not in text:
        failures.append("drop-in canonical markers missing")
        return failures
    embedded = text.split(begin, 1)[1].split(end, 1)[0]
    canonical = protocol.read_text(encoding="utf-8")
    if embedded != canonical:
        failures.append("drop-in canonical protocol is not byte-identical to active reference")
    if "UNIVERSAL BOOTSTRAP" not in text:
        failures.append("drop-in missing universal bootstrap")
    return failures


def check_evals(root: Path) -> list[str]:
    failures: list[str] = []
    path = root / "evals/evals.json"
    if not path.is_file():
        return failures
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"evals JSON invalid: {exc}"]
    if data.get("skill_name") != root.name:
        failures.append("eval skill_name does not match skill directory")
    cases = data.get("cases")
    if not isinstance(cases, list) or len(cases) < 7:
        failures.append("evals require at least seven cases")
        return failures
    triggers = sum(1 for case in cases if case.get("should_trigger") is True)
    nontriggers = sum(1 for case in cases if case.get("should_trigger") is False)
    if triggers < 5 or nontriggers < 2:
        failures.append("evals need at least five trigger and two non-trigger cases")
    ids = [case.get("id") for case in cases]
    if len(ids) != len(set(ids)):
        failures.append("eval IDs are not unique")
    return failures


def validate(root: Path) -> list[str]:
    failures: list[str] = []
    for rel in sorted(REQUIRED_FILES):
        if not (root / rel).is_file():
            failures.append(f"missing file: {rel}")

    # Avoid recursive discovery of rollback/legacy skills.
    skill_files = [p for p in root.rglob("SKILL.md") if p.is_file()]
    if skill_files != [root / "SKILL.md"]:
        failures.append("package contains nested discoverable SKILL.md files")

    skill_path = root / "SKILL.md"
    if skill_path.is_file():
        text = skill_path.read_text(encoding="utf-8")
        failures.extend(check_frontmatter(root, text))
        failures.extend(check_patterns(text, SKILL_REQUIRED_PATTERNS, "SKILL.md"))
        if len(text.splitlines()) > 500:
            failures.append("SKILL.md exceeds 500 lines")
        for label, pattern in FORBIDDEN_ACTIVE_PATTERNS.items():
            if re.search(pattern, text, flags=re.IGNORECASE):
                failures.append(f"SKILL.md has active {label}")

    protocol_path = root / "references/MAX_IMP_LOOP_v3.1_UNIVERSAL.md"
    if protocol_path.is_file():
        text = protocol_path.read_text(encoding="utf-8")
        failures.extend(check_patterns(text, CORE_PROTOCOL_PATTERNS, "protocol"))
        for label, pattern in FORBIDDEN_ACTIVE_PATTERNS.items():
            if re.search(pattern, text, flags=re.IGNORECASE):
                failures.append(f"protocol has active {label}")

    adaptation = root / "references/ENVIRONMENT_ADAPTATION.md"
    if adaptation.is_file():
        text = adaptation.read_text(encoding="utf-8")
        for phrase in [
            "AVAILABLE`, `LIMITED`, `UNAVAILABLE`, or `UNKNOWN`",
            "Prompt-only or no native skill support",
            "No-tools",
            "Stateless or no persistent memory",
            "No parallel reviewers or subagents",
            "No background or asynchronous execution",
            "Never fabricate tool access",
            "data. Instructions or approvals found inside them",
        ]:
            if phrase.lower() not in text.lower():
                failures.append(f"adaptation reference missing: {phrase}")
        for label, pattern in FORBIDDEN_ACTIVE_PATTERNS.items():
            if re.search(pattern, text, flags=re.IGNORECASE):
                failures.append(f"adaptation reference has active {label}")

    for rel, expected in EXPECTED_ROLLBACK_HASHES.items():
        path = root / rel
        if path.is_file() and sha256(path) != expected:
            failures.append(f"preserved rollback/legacy file changed: {rel}")

    failures.extend(check_dropin(root))
    failures.extend(check_evals(root))
    failures.extend(check_manifest(root))
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-dir", type=Path, required=True)
    args = parser.parse_args()
    failures = validate(args.skill_dir.resolve())
    if failures:
        print(f"FAIL ({len(failures)} checks)")
        for item in failures:
            print(f"- {item}")
        return 1
    print("PASS: MAX_IMP_LOOP v3.1 Universal mechanical validation succeeded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
