# Jurisdiction Source Pack Template

Use this template to define the evidence layer for one employment-law jurisdiction. Keep it informational and review-oriented; do not use it to certify compliance.

## Jurisdiction

- **Name:** `[country / state / province / city]`
- **Scope:** `[who or what this source pack covers]`
- **Last validated:** `YYYY-MM-DD`
- **Owner:** `[role, not a named private person]`

## Source family

Plain-English description of the official source family.

Example:

> Official employment standards, human rights, workplace safety, and privacy regulator guidance for this jurisdiction.

## Official sources

| Source | URL | Why it matters | Last checked |
|---|---|---|---|
| Employment standards source | `https://...` | Wage/hour/leave/termination baseline | `YYYY-MM-DD` |
| Human rights source | `https://...` | Accommodation, harassment, discrimination | `YYYY-MM-DD` |
| Safety source | `https://...` | Workplace safety duties and reporting | `YYYY-MM-DD` |
| Privacy source | `https://...` | Employee data, monitoring, retention | `YYYY-MM-DD` |

## Fallback queries

Use fallback queries when official pages move, block automated fetches, or split guidance across multiple pages.

```text
site:official-domain.example employment standards overtime leave termination
site:official-domain.example workplace accommodation harassment discrimination
site:official-domain.example employee privacy monitoring workplace
```

## Scan dimensions

- hours and overtime
- wage/payment rules
- public holidays or paid time off
- leaves of absence
- termination and notice
- human rights and accommodation
- workplace safety
- employee privacy and monitoring
- required notices or policies

## Workflow boundary

The workflow may:

- find likely issue areas
- summarize official source material
- identify possible handbook/policy gaps
- create an implementation item
- draft language for review
- preserve source trail and uncertainty

The workflow must not:

- certify legal compliance
- decide applicability without review
- approve policy changes
- send employee-facing communications without approval
- replace qualified HR/legal/local counsel review

## Audit fields

- source URL or fallback query
- fetch/search status
- summary generated
- affected policy/process area
- owner
- reviewer
- decision
- timestamp

## Notes

`[Any jurisdiction-specific cautions, language issues, local counsel needs, or source quirks.]`
