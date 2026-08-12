#!/usr/bin/env python3
"""Reject structurally incomplete HRBP weekly decision briefs."""
from pathlib import Path
import re, sys
HEADINGS=("## Brief metadata","## Executive readout","## Decision items","## Manager follow-ups","## Watchlist","## Verifier findings","## Human disposition","## Receipt")
FIELDS=("Verified facts","Source references","Interpretation / working hypothesis","Missing facts","Written policy layer","Operating practice layer","Accountable owner","Next question or action","Human review / escalation boundary")
def main():
    if len(sys.argv)!=2: print("usage: check-hrbp-weekly-decision-brief.py BRIEF.md"); return 2
    path=Path(sys.argv[1])
    if not path.is_file(): print(f"FAIL: file not found: {path}"); return 2
    text=path.read_text(); errors=[]
    for heading in HEADINGS:
        if heading not in text: errors.append(f"missing heading: {heading}")
    items=re.split(r"^### Decision item:",text,flags=re.MULTILINE)[1:]
    if not items: errors.append("at least one decision item is required")
    for i,item in enumerate(items,1):
        for field in FIELDS:
            match=re.search(rf"^- {re.escape(field)}:[ \t]*(.*)$",item,re.MULTILINE)
            if not match or not match.group(1).strip(): errors.append(f"decision item {i}: unresolved field '{field}'")
    if "Status: DRAFT — HUMAN REVIEW REQUIRED" not in text: errors.append("brief must remain marked DRAFT — HUMAN REVIEW REQUIRED")
    if errors:
        print("FAIL"); [print(f"- {error}") for error in errors]; return 1
    print(f"PASS: {path}"); print("Structural completeness only; source validation and human judgment remain required."); return 0
if __name__=="__main__": raise SystemExit(main())
