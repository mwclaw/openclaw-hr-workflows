# HR Workflow Risk Tiers

> **HRMC relationship:** Adjacent governance pattern, not a current product capability.
>
> **Evidence level:** Proposed risk-classification framework; not legal advice or production validation.

## Summary

Not every HR workflow should use the same AI controls.

Low-risk work can move quickly. Sensitive work needs human review, source trails, and clear ownership. High-impact employment decisions should never be delegated to an autonomous agent.

This pattern helps teams sort HR workflows by risk before building automation around them.

## What Problem Does This Solve?

AI demos often treat HR work as one category.

That is wrong.

A lunch-and-learn FAQ, a handbook citation lookup, a leave accommodation question, and a termination recommendation do not carry the same risk. The workflow should change as the stakes change.

## Tier 1: Low-Risk Enablement

Examples:

- summarizing public HR articles
- drafting internal training outlines
- organizing non-sensitive HR project notes
- generating interview-prep questions for HR team learning
- creating synthetic demo scenarios

Controls:

- label AI-generated drafts
- verify important claims before use
- keep real employee data out unless approved
- human owns final wording

Agent role:

- draft
- organize
- summarize
- suggest

## Tier 2: Operational HR Support

Examples:

- policy Q&A with citations
- manager coaching prep
- HRBP weekly decision briefs
- compliance intake routing
- handbook gap spotting
- source-to-packet workflow support

Controls:

- source links required
- missing facts listed
- company policy separated from law/regulation
- operating practice separated from written policy
- accountable HR owner named
- audit trail written

Agent role:

- gather
- compare
- route
- draft questions
- preserve evidence

## Tier 3: Sensitive Employee Matters

Examples:

- accommodations
- protected leave
- employee relations investigations
- harassment or discrimination concerns
- pay equity concerns
- performance issues with legal or protected-class risk

Controls:

- human HR review required
- legal review when appropriate
- access limited to need-to-know users
- source and decision trail preserved
- employee recourse and dignity protected
- no automated final decision

Agent role:

- intake support
- chronology building
- missing-facts checklist
- policy/source retrieval
- draft review packet

## Tier 4: High-Impact Employment Decisions

Examples:

- termination
- discipline
- promotion or demotion decisions
- compensation decisions
- hiring rejection or selection
- investigation findings
- compliance certification

Controls:

- no autonomous decision-making
- named accountable human decision maker
- documented rationale
- legal/HR review where appropriate
- source trail and review packet retained
- bias, privacy, and adverse-impact concerns considered

Agent role:

- support the packet
- surface evidence
- identify gaps
- draft review questions
- record human decisions

Agent must not:

- decide
- approve
- reject
- discipline
- terminate
- certify compliance
- hide uncertainty behind a score

## What Data Does It Need?

Use the least sensitive data that can answer the question.

Preferred order:

1. synthetic examples
2. public sources
3. sanitized internal patterns
4. approved policy documents
5. sensitive employee data only inside an approved environment with access controls

## What Must Stay Human-Reviewed?

Human review is required whenever the workflow touches:

- employment status
- pay
- protected characteristics
- medical or leave facts
- discipline
- investigations
- legal exposure
- employee trust or dignity

## What Would Make This Demo-Ready?

- A sample intake for each tier.
- A visible risk-tier label.
- Required source links.
- Missing-facts output.
- Human owner and review status.
- Audit trail entry.
- Clear refusal behavior for Tier 4 decisions.

The point is not to make HR slower. The point is to keep speed proportional to risk.
