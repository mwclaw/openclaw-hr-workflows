# Synthetic Demo: Source Signal to HR Case File

> **HRMC relationship:** Current compliance-first MVP pattern.  
> **Evidence level:** Worked synthetic example; not proof of production accuracy or legal reliability.  
> **Coverage:** “Example Province” is fictional and does not represent current HRMC geographic coverage.

This demo uses fictional facts and generic public-source placeholders. It is designed to show the workflow pattern without using real employee data, private company configuration, or legal conclusions.

## Scenario

A fictional employer, **ExampleCo**, operates in more than one jurisdiction. A public employment-law source appears to announce a new requirement that may affect handbook language and manager process.

The workflow should not decide compliance. It should create a reviewable packet for an accountable HR/legal owner.

## Step 1 — Source signal

| Field | Example |
|---|---|
| Source type | Official public agency guidance |
| Jurisdiction | Example Province |
| Topic | Protected leave / handbook language |
| Signal | New or updated guidance may require policy review before an effective date |
| Confidence | Needs human review |
| Boundary | Issue spotting only; do not certify applicability |

## Step 2 — Scoped relevance check

The workflow compares the source signal against the employer footprint.

```json
{
  "employee_jurisdictions": ["Example Province", "Example State"],
  "source_jurisdiction": "Example Province",
  "relevance": "potentially relevant",
  "reason": "The employer has employees in the jurisdiction named by the source signal."
}
```

## Step 3 — Implementation item

```json
{
  "title": "Review handbook language for Example Province protected leave update",
  "owner": "HR operations owner with legal review",
  "status": "needs review",
  "due_date": "YYYY-MM-DD",
  "linked_source": "Official source URL or source-pack entry",
  "implementation_checks": [
    "Confirm employer coverage",
    "Compare current handbook language",
    "Identify manager intake process changes",
    "Determine whether employee notice or training is needed"
  ]
}
```

## Step 4 — Handbook / policy review instruction

The workflow prepares a review prompt, not final policy language.

The implementation uses a bounded review instruction that separates supported observations, missing information, legal-review questions, and operational follow-up. The full instruction and production configuration are intentionally not published.

## Step 5 — Case file packet

```json
{
  "case_file_type": "Policy change implementation",
  "lane": "HR operations",
  "problem_statement": "A public source signal may require a handbook and manager-process review for Example Province employees.",
  "known_facts": [
    "The source signal is tied to Example Province.",
    "ExampleCo has employees in Example Province.",
    "The current handbook contains a generic leave section."
  ],
  "missing_facts": [
    "Whether ExampleCo is covered by the requirement.",
    "Whether current practice already satisfies any part of the requirement.",
    "Whether notice, manager training, or HRIS coding changes are needed."
  ],
  "source_trail": [
    "Jurisdiction source pack entry",
    "Official public source URL",
    "Current handbook leave section",
    "Implementation tracker item"
  ],
  "ai_may_draft": [
    "Plain-English summary",
    "Checklist of policy/process areas to review",
    "Draft redline language clearly labeled for review"
  ],
  "human_owns": [
    "Legal interpretation",
    "Applicability decision",
    "Final handbook language",
    "Employee-facing communications"
  ],
  "next_action": {
    "owner": "HR operations owner",
    "action": "Confirm applicability with legal review and decide whether to update handbook language.",
    "due_date": "YYYY-MM-DD"
  }
}
```

## Step 6 — Approval and audit

Before action, the workflow should capture:

- source reviewed
- human reviewer
- decision made
- edits requested
- final approved action
- timestamp

## What this design demonstrates

This pattern shows how to connect a source signal to practical HR work without converting the system into an autonomous legal decision-maker.

The useful output is not a confident answer. The useful output is a reviewable packet with source trail, uncertainty, owner, and next action.
