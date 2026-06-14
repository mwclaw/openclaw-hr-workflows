# Jurisdiction Source Pack Pattern

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

## What a source pack should contain

At minimum:

| Field | Purpose |
|---|---|
| `jurisdiction` | Country, state, province, city, or regulator scope. |
| `source_family` | Plain-English description of the official source family. |
| `official_sources` | Primary government, regulator, agency, or official guidance URLs. |
| `fallback_queries` | Search queries used when a primary source blocks direct fetch or moves. |
| `scan_dimensions` | Topics the workflow checks, such as leave, pay, safety, privacy, or termination. |
| `last_validated` | Date the source pack was last human-checked. |
| `review_boundary` | What the workflow may flag versus what requires HR/legal review. |
| `audit_fields` | Source URL, fetch status, summary, owner, reviewer, decision, timestamp. |

## Example shape

```json
{
  "jurisdiction": "Example Province",
  "source_family": "Official employment standards, human rights, safety, and privacy guidance",
  "official_sources": [
    {
      "name": "Employment standards guide",
      "url": "https://example.gov/employment-standards",
      "why_it_matters": "Primary source for wage, hour, leave, holiday, and termination checks."
    },
    {
      "name": "Human rights commission guidance",
      "url": "https://example.gov/human-rights",
      "why_it_matters": "Source family for discrimination, harassment, accommodation, and complaint handling."
    }
  ],
  "fallback_queries": [
    "site:example.gov employment standards overtime vacation termination",
    "site:example.gov workplace accommodation harassment human rights"
  ],
  "scan_dimensions": [
    "hours and overtime",
    "leaves of absence",
    "termination and notice",
    "human rights and accommodation",
    "employee privacy and monitoring"
  ],
  "review_boundary": "Issue spotting only. Do not certify compliance. Route policy changes to an accountable HR/legal reviewer."
}
```

## Primary source logic

Prefer sources in this order:

1. official government, regulator, agency, or commission source
2. official guidance, code, rule, regulation, or enforcement page
3. cached canonical URL or sitemap/RSS/API entry
4. fallback search query scoped to official domains
5. reputable secondary source only for discovery, not final authority

Secondary sources can help discover a change, but the workflow should still try to tie the issue back to an official source or route it for human review.

## Fallback logic

Fallbacks are not a loophole. They are a reliability pattern.

Use fallback queries when:

- the official page blocks automated fetches
- the page moved
- the source is split across multiple official pages
- the workflow needs to rediscover the current canonical URL

The output should say when a source is fallback-covered instead of directly fetched.

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

## Audit trail should capture

- source pack name and jurisdiction
- official URL or fallback query used
- fetch status and timestamp
- summary generated
- affected policy/process area
- recommended next action
- accountable owner
- human reviewer
- decision and timestamp

## Practical design rule

A source pack should make source discipline easier. If it turns into a black-box compliance answer, the design has failed.

## Boundary

This pattern is informational only. It is not legal advice, not a compliance certification method, and not a substitute for qualified local counsel.