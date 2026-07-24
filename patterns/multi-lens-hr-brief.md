# Multi-Lens HR Brief

> **HRMC relationship:** Adjacent research pattern for pressure-testing HR questions.
>
> **Evidence level:** Proposed workflow pattern; not production-validated.

AI outputs in HR can look clean while still missing the real issue.

The safer pattern is to pressure-test the question before writing the answer. A multi-lens brief makes the reasoning visible: what is known, what is missing, where the risk sits, who owns the decision, and what should stay human-reviewed.

## What problem does this solve?

Many HR workflows fail because the first question is too narrow.

Examples:

- A manager asks for a script, but the real issue is performance ownership.
- A policy question looks simple, but the answer depends on law, policy, practice, and precedent.
- An AI summary sounds confident, but the source quality is weak.
- A workflow prototype works on fake data, but would be risky with real employee records.

The multi-lens brief is designed to slow the work down just enough to avoid false confidence.

## What does this workflow do?

It reviews a topic through several practical lenses before producing a recommendation.

Useful lenses include:

- Practitioner: what would an operator actually do next?
- HRBP judgment: what tradeoffs, incentives, ownership, and precedent issues matter?
- Employee/dignity: what affects fairness, trust, privacy, recourse, or employee experience?
- Legal/policy: what needs policy, compliance, documentation, or legal review?
- Business operator: what is the business problem, cost, constraint, and second-order effect?
- Skeptic: what is overclaimed, under-sourced, risky, or duplicated?
- Economist: compared to what, at what cost, and with what opportunity cost?
- Technical/operator: what data, workflow state, tokens, verifier, and failure modes matter?

Not every brief needs every lens. The point is to use the lenses that expose the real decision.

## Recommended brief structure

1. Actual question
2. Safety boundary
3. Core claims or ideas
4. Lens notes
5. Disagreements and tensions
6. Source status
7. What is worth using
8. Risks / do not do
9. Deployment path
10. Next action

## Source status labels

Use explicit source-strength labels so weak claims do not sound equal to strong ones.

- Confirmed: source-backed or directly observable.
- Plausible: reasonable inference, but not fully proven.
- Weak: thin source, anecdote, unclear provenance, or marketing claim.
- Missing: needed fact not present.
- Contradicted: conflicts with another credible source or known constraint.

## Human-review boundaries

This pattern should not be used to automate sensitive HR decisions.

Keep human review for:

- discipline
- termination
- compensation
- leave and accommodation issues
- protected-class issues
- investigations
- employee relations notes
- performance decisions
- legal or policy interpretation

For demos and prototypes, start with synthetic data, public policies, fake manager notes, and clearly non-production workflows.

## What would make it demo-ready?

A demo-ready version should show:

- the exact question being answered
- the safety boundary
- at least three relevant lenses
- at least one disagreement or tension
- source-strength labels
- a do-not-do boundary
- a concrete next action
- a verifier or review receipt

If those pieces are missing, the workflow is probably just a longer prompt.
