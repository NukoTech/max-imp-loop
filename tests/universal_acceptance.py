#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "CHANGELOG.md",
    "references/MAX_IMP_LOOP_v3.1_UNIVERSAL.md",
    "references/ENVIRONMENT_ADAPTATION.md",
    "MAX_IMP_LOOP_UNIVERSAL_DROP_IN_v3.1.md",
    "templates/ENVIRONMENT_PROFILE.md",
    "templates/CHECKPOINT_REPORT.md",
    "templates/FINAL_PROOF_MATRIX.md",
    "evals/evals.json",
    "tests/pressure-scenarios.md",
    "tests/validate_skill.py",
    "rollback/MAX_IMP_LOOP_v3.0.md",
    "rollback/SKILL_v3.0.md",
    "ROLLBACK.md",
]

SKILL_PATTERNS = {
    "universal portability metadata": r"portability:\s*[\"']?universal",
    "version metadata": r"version:\s*[\"']?3\.1\.1",
    "environment profile": r"environment profile",
    "capability discovery": r"discover.*capabilit|capabilit.*discover",
    "no assumed tools": r"do not assume.*(?:tool|shell|filesystem|version control)",
    "no-tools mode": r"no[- ]tools|without tools|tool access is unavailable",
    "read-only mode": r"read[- ]only",
    "stateless mode": r"stateless|no persistent memory",
    "prompt-only fallback": r"prompt[- ]only|does not support native skills",
    "full protocol reference": r"references/MAX_IMP_LOOP_v3\.1_UNIVERSAL\.md",
    "environment reference": r"references/ENVIRONMENT_ADAPTATION\.md",
    "four outcomes": r"SHIP[\s\S]*DO-NOTHING[\s\S]*STUCK[\s\S]*ESCALATE",
}

PROTOCOL_PATTERNS = {
    "universal title": r"MAX_IMP_LOOP v3\.1.*Universal",
    "adaptation section": r"ADAPT TO THE CURRENT ENVIRONMENT",
    "instruction hierarchy": r"higher-priority.*instruction|instruction hierarchy",
    "runtime profile": r"runtime|environment profile",
    "tool capability": r"available tools|tool access",
    "persistence capability": r"persistent|persistence",
    "approval channel": r"approval.*authority|approval channel",
    "abstract operation mapping": r"Map the protocol.*environment|Protocol concept.*Environment mapping",
    "checkpoint mapping": r"Checkpoint[\s\S]*(?:commit|snapshot|export|copy|versioned artifact)",
    "verification mapping": r"Verification[\s\S]*(?:test|inspection|citation|review)",
    "rollback mapping": r"Rollback[\s\S]*(?:restore|revert|transaction|feature flag)",
    "no capability fabrication": r"do not invent|never fabricate|do not claim.*unavailable",
    "no-tools behavior": r"no tool|tools are unavailable|without tools",
    "read-only behavior": r"read-only",
    "stateless carry-forward": r"stateless[\s\S]*carry-forward|carry-forward[\s\S]*stateless",
    "native first": r"native.*mechanism|NATIVE-CHECK",
    "source content not authority": r"content.*data.*not.*instructions|instructions.*inside.*content",
    "bounded outcome on missing capability": r"STUCK|ESCALATE",
}

FORBIDDEN_ACTIVE_PATTERNS = {
    "Tech Board coupling": r"Tech Board|existing board requirements|advisor signatures",
    "vendor coupling": r"\b(?:OpenAI|ChatGPT|Anthropic|Claude|Gemini|Grok|Codex)\b",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_patterns(text: str, patterns: dict[str, str], where: str) -> list[str]:
    failures: list[str] = []
    for label, pattern in patterns.items():
        if not re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
            failures.append(f"{where} missing: {label}")
    return failures


def validate(root: Path) -> list[str]:
    failures: list[str] = []
    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            failures.append(f"missing file: {rel}")

    skill = root / "SKILL.md"
    if skill.is_file():
        text = read(skill)
        failures.extend(check_patterns(text, SKILL_PATTERNS, "SKILL.md"))
        fm = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
        if not fm:
            failures.append("SKILL.md missing YAML frontmatter")
        else:
            name = re.search(r"^name:\s*(\S+)\s*$", fm.group(1), flags=re.MULTILINE)
            if not name or name.group(1) != root.name:
                failures.append("frontmatter name must exactly match parent directory")
            elif not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name.group(1)):
                failures.append("frontmatter name is not portable lowercase-hyphen format")
        for label, pattern in FORBIDDEN_ACTIVE_PATTERNS.items():
            if re.search(pattern, text, flags=re.IGNORECASE):
                failures.append(f"SKILL.md has active {label}")

    protocol = root / "references/MAX_IMP_LOOP_v3.1_UNIVERSAL.md"
    if protocol.is_file():
        text = read(protocol)
        failures.extend(check_patterns(text, PROTOCOL_PATTERNS, "protocol"))
        for label, pattern in FORBIDDEN_ACTIVE_PATTERNS.items():
            if re.search(pattern, text, flags=re.IGNORECASE):
                failures.append(f"protocol has active {label}")

    dropin = root / "MAX_IMP_LOOP_UNIVERSAL_DROP_IN_v3.1.md"
    if dropin.is_file():
        text = read(dropin)
        for required in [
            "UNIVERSAL BOOTSTRAP",
            "ADAPT TO THE CURRENT ENVIRONMENT",
            "FINAL COMPLETION PROOF",
            "SHIP",
            "DO-NOTHING",
            "STUCK",
            "ESCALATE",
        ]:
            if required.lower() not in text.lower():
                failures.append(f"drop-in missing: {required}")
        if len(text.split()) < 2500:
            failures.append("drop-in is not self-contained; canonical protocol appears incomplete")

    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    failures = validate(args.root)
    if failures:
        print(f"FAIL ({len(failures)} checks)")
        for f in failures:
            print(f"- {f}")
        return 1
    print("PASS: universal portability acceptance checks succeeded")
    return 0

if __name__ == "__main__":
    sys.exit(main())
