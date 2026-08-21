#!/usr/bin/env python3
"""Fail when repository navigation or local Markdown links drift."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_ROOT_FILES = {
    "LICENSE",
    "PUBLICATION_BOUNDARY.md",
    "README.md",
    "SECURITY.md",
}
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def main() -> int:
    failures: list[str] = []
    root_files = {path.name for path in ROOT.iterdir() if path.is_file()}
    unexpected = sorted(root_files - ALLOWED_ROOT_FILES)
    missing = sorted(ALLOWED_ROOT_FILES - root_files)

    if unexpected:
        failures.append(f"unexpected repository-root files: {', '.join(unexpected)}")
    if missing:
        failures.append(f"missing required repository-root files: {', '.join(missing)}")

    for markdown_file in sorted(ROOT.rglob("*.md")):
        for raw_target in MARKDOWN_LINK.findall(markdown_file.read_text(encoding="utf-8")):
            target = raw_target.split("#", 1)[0].strip()
            if not target or "://" in target or target.startswith(("#", "mailto:")):
                continue
            if not (markdown_file.parent / target).resolve().exists():
                relative_file = markdown_file.relative_to(ROOT)
                failures.append(f"broken local link in {relative_file}: {raw_target}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("PASS: repository root and local Markdown links are organized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
