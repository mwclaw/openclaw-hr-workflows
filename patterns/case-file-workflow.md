# Case File Workflow Pattern

## Goal

Turn a messy HR issue into a short, reviewable case file before anyone acts.

A case file is not a chatbot transcript and not a final decision. It is a structured packet that keeps facts, sources, risk, owner, decision line, next action, and audit trail in one place.

## Why this matters

Many HR situations fail because context is scattered:

- a manager gives partial facts
- the policy answer is unclear
- legal exposure is possible but not named
- the owner is implied instead of assigned
- the AI draft looks polished but hides uncertainty
- implementation work gets disconnected from the source issue

The case-file pattern makes the next human review easier instead of making the workflow look falsely automatic.

## Good use cases

| Lane | Use when | Example output |
|---|---|---|
| HRBP | A manager, team, or leader issue needs judgment and escalation discipline. | Risk read, talking points, options, next HRBP move. |
| HR specialist | A leave, pay, immigration, employee relations, benefits, safety, or policy question needs source-backed review. | Issue summary, source trail, missing facts, review boundary. |
| HR operations | A policy or legal change needs implementation work. | Owner, due date, HRIS/payroll/training/notice checklist. |

## What a case file should contain

| Section | Purpose |
|---|---|
| Problem statement | One plain-English sentence describing the issue. |
| Lane | HRBP, specialist, HR ops, legal/compliance, payroll, benefits, safety, immigration, or other owner lane. |
| Known facts | Facts currently supported by source material or intake. |
| Claims / assumptions | Things asserted but not yet verified. |
| Missing facts | Information needed before a decision. |
| Source trail | Policies, handbook sections, public sources, prior approvals, or internal references used. |
| Risk areas | Pay, leave, protected class, accommodation, privacy, safety, immigration, discipline, termination, retaliation, or other sensitive area. |
| AI may draft | Narrow drafting/summarizing work allowed before review. |
| Human owns | Decision, approval, legal interpretation, employee-facing action, or escalation. |
| Recommendation options | Possible next steps, preferably with tradeoffs. |
| Next action | The immediate action, owner, and due date. |
| Audit note | Who reviewed what and when. |

## Example shape

```json
{
  "case_file_type": "Policy change implementation",
  "lane": "HR operations",
  "problem_statement": "A new public source indicates a policy update may be needed before an effective date.",
  "known_facts": [
    "The source change appears to affect one or more employee jurisdictions.",
    "The current handbook section may not address the new requirement."
  ],
  "missing_facts": [
    "Whether the employer is covered by the requirement.",
    "Whether current practice already satisfies part of the requirement.",
    "Who owns employee notice and manager training."
  ],
  "source_trail": [
    "Official public source URL",
    "Current handbook section",
    "Implementation tracker item"
  ],
  "ai_may_draft": [
    "Plain-English summary",
    "Checklist of affected policy/process areas",
    "Draft language for review"
  ],
  "human_owns": [
    "Legal interpretation",
    "Policy approval",
    "Employee-facing communication",
    "Final implementation decision"
  ],
  "next_action": {
    "owner": "Accountable HR owner",
    "action": "Review source, confirm applicability, and decide whether to update policy language.",
    "due_date": "YYYY-MM-DD"
  }
}
```

## Workflow chain

A case file can connect several HR workflow surfaces:

```text
source signal
→ scoped relevance check
→ implementation item
→ handbook or policy redline
→ draft language for review
→ human/legal approval
→ completion evidence
```

The important part is that each step stays connected to the same source trail and owner.

## AI boundaries

AI can help by:

- summarizing source material
- extracting relevant policy sections
- identifying missing facts
- drafting options for review
- creating checklists
- comparing versions
- preparing a brief for the accountable owner

AI should not:

- decide discipline, termination, pay, leave, accommodation, immigration, safety, or protected-class outcomes
- approve handbook or policy changes
- certify legal compliance
- send sensitive employee-facing communication without review
- hide uncertainty or source limitations

## Human approval points

Pause for human review before:

- legal interpretation
- policy approval
- employee-facing communication
- changes to pay, leave, benefits, immigration, safety, discipline, or termination practices
- any action involving protected class, harassment, retaliation, accommodation, or investigation issues

## Demo-ready version

A safe demo should use synthetic facts and show:

1. intake of a generic issue
2. source or policy section attached
3. missing facts surfaced
4. draft recommendation clearly labeled for review
5. accountable owner named
6. human approval checkpoint
7. audit note

## Practical design rule

If the packet does not make the next human review easier, cut it or reshape it.

## Boundary

This pattern is informational only. It is not legal advice and is not a recommendation to automate sensitive employment decisions.