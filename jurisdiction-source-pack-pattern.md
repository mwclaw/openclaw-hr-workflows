# Jurisdiction Source Pack Pattern

> **HRMC relationship:** Current compliance-first MVP design pattern.  
> **Evidence level:** Prototype design; exact source configuration and production implementation remain private.  
> **Coverage:** Examples are fictional. HRMC's current product scope is U.S.-first.

## Goal

Define a repeatable way for an HR workflow to monitor jurisdiction-specific employment, privacy, safety, and human-rights sources without pretending the workflow can certify legal compliance.

A jurisdiction source pack is a small, reviewable bundle of official source families, fallback discovery queries, scope notes, and human-review rules for one location.

## Why this matters

HR compliance work often breaks down because source tracking is informal:

- one person follows a newsletter
- another person remembers a law-firm alert
- government pages move or block automated fetches
- policy updates are discussed in email but not connected to implementation work
- the handbook gets changed without a clear source trail

A source pack makes the evidence layer explicit before any model summarizes, drafts, or routes work.

## Public pattern

A source pack should make four things reviewable: jurisdiction scope, authoritative source families, validation status, and the human-review boundary. It should also preserve enough provenance for an accountable reviewer to understand what was checked and what remains uncertain.

The exact field schema, source inventory, fallback configuration, scanning logic, and production thresholds are intentionally not published.

## Primary source logic

Prefer authoritative primary sources. Secondary material may assist discovery, but it should not silently become the final authority. When a controlling source cannot be verified, the workflow should expose that limitation and route the issue for human review.

## Fallback logic

Fallbacks are not a loophole. They are a reliability pattern.

Fallbacks should preserve provenance and disclose when a source was discovered indirectly. Exact discovery queries and recovery logic remain private implementation details.

## What the workflow may do

A workflow using source packs may:

- detect possible changes
- summarize the source in plain English
- identify likely handbook or process gaps
- create a tracker item
- draft language for human review
- route the issue to HR, legal, payroll, benefits, immigration, safety, or people operations
- preserve the source trail and uncertainty

## What must stay human-reviewed

Human review is required before:

- changing handbook or policy language
- sending employee-facing communications
- deciding whether a law applies to a specific employer or worker
- interpreting ambiguous legal requirements
- changing payroll, benefits, leave, immigration, safety, discipline, or termination practices
- representing that the company is compliant

## Audit principle

The review record should preserve source provenance, scope, uncertainty, ownership, human decisions, and timestamps. The private implementation defines the complete audit schema.

## Practical design rule

A source pack should make source discipline easier. If it turns into a black-box compliance answer, the design has failed.

## Boundary

This pattern is informational only. It is not legal advice, not a compliance certification method, and not a substitute for qualified local counsel.
