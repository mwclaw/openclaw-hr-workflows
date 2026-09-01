#!/usr/bin/env python3
"""Fail closed when a public-tree path or text artifact crosses the repo boundary."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ALLOWED_ROOT_FILES = {
    "LICENSE",
    "PUBLICATION_BOUNDARY.md",
    "README.md",
    "SECURITY.md",
}

ALLOWED_ROOT_DIRECTORIES = {
    ".github",
    "assets",
    "benchmarks",
    "docs",
    "examples",
    "patterns",
    "runbooks",
    "scripts",
    "skills",
    "templates",
    "use-cases",
}

BLOCKED_PATH_PARTS = {
    ".env",
    "backup",
    "backups",
    "credentials",
    "personal-data",
    "private-data",
    "runtime-state",
    "session-data",
}

BLOCKED_SUFFIXES = {
    ".bak",
    ".db",
    ".key",
    ".log",
    ".p12",
    ".pem",
    ".sqlite",
    ".sqlite3",
    ".tar",
    ".zip",
}

TEXT_SUFFIXES = {
    ".csv",
    ".html",
    ".json",
    ".md",
    ".py",
    ".sh",
    ".tsv",
    ".txt",
    ".yaml",
    ".yml",
}

CONTENT_RULES = {
    "macOS home path": re.compile(r"/Users/[A-Za-z0-9._-]+/"),
    "Windows home path": re.compile(r"[A-Za-z]:\\\\Users\\\\[^\\\\\s]+"),
    "private SSH key": re.compile(r"-----BEGIN (?:OPENSSH |RSA |EC )?PRIVATE KEY-----"),
    "GitHub access token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "OpenAI-style secret": re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
    "Telegram bot token": re.compile(r"\b\d{6,12}:[A-Za-z0-9_-]{20,}\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    "private application name": re.compile(r"\bPersonal" + r"\s+HQ\b", re.IGNORECASE),
}


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [ROOT / item.decode() for item in result.stdout.split(b"\0") if item]


def inspect_path(path: Path) -> list[str]:
    relative = path.relative_to(ROOT)
    failures: list[str] = []
    root_name = relative.parts[0]

    if path.is_symlink():
        failures.append(f"symbolic links are not allowed in the public tree: {relative}")

    if len(relative.parts) == 1 and root_name not in ALLOWED_ROOT_FILES:
        failures.append(f"unapproved repository-root file: {relative}")
    elif len(relative.parts) > 1 and root_name not in ALLOWED_ROOT_DIRECTORIES:
        failures.append(f"unapproved top-level directory: {root_name}")

    lowered_parts = {part.lower() for part in relative.parts}
    blocked_parts = sorted(lowered_parts & BLOCKED_PATH_PARTS)
    if blocked_parts:
        failures.append(f"blocked path category in {relative}: {', '.join(blocked_parts)}")

    if path.suffix.lower() in BLOCKED_SUFFIXES:
        failures.append(f"blocked artifact type: {relative}")

    if path.is_file() and path.stat().st_size > 3 * 1024 * 1024:
        failures.append(f"artifact exceeds public review limit (3 MiB): {relative}")

    return failures


def inspect_content(path: Path) -> list[str]:
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return []

    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return [f"text-like artifact is not UTF-8: {path.relative_to(ROOT)}"]

    failures: list[str] = []
    for label, pattern in CONTENT_RULES.items():
        if pattern.search(content):
            failures.append(f"{label} found in {path.relative_to(ROOT)}")
    return failures


def main() -> int:
    failures: list[str] = []
    files = tracked_files()

    for path in files:
        failures.extend(inspect_path(path))
        failures.extend(inspect_content(path))

    if failures:
        for failure in sorted(set(failures)):
            print(f"FAIL: {failure}")
        return 1

    print(f"PASS: {len(files)} tracked artifacts satisfy the public path and semantic boundary")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
