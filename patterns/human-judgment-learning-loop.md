# Human Judgment Learning Loop

## Purpose

AI systems in HR should get better from reviewed human judgment.

They should not silently absorb that judgment into automation.

This pattern describes how to capture learning safely: what the system tried, what a human changed, why it changed, who approved it, and what should never be automated.

## What problem does this solve?

Many agent workflows treat the final output as the valuable artifact.

In HR, the more valuable artifact is often the review path:

- what facts were known
- what was missing
- which sources mattered
- what HR changed
- what legal or policy boundary applied
- what a manager approved or rejected
- what happened later

That review path can improve future work, but only if it is captured with consent, scope, and human accountability.

## Safe learning artifacts

Good HR learning loops preserve:

- the original question or intake
- source links and source-strength labels
- missing facts
- agent draft or recommendation
- human edits
- approval, rejection, or override notes
- rationale for the change
- final action taken
- later outcome or repair note
- "never automate" boundary

## What must not happen

Do not turn one human correction into silent future automation.

Rejected shortcuts:

- "The user fixed it once, so automate it next time."
- "This manager usually approves, so skip review."
- "This case resembles a prior one, so reuse the outcome."
- "The agent observed the workflow, so consent is implied."
- "The answer was accepted, so the policy interpretation is settled."

## Privacy boundary

Broad ambient capture is the wrong default for HR.

Be especially cautious with:

- browser activity
- keystrokes
- meeting behavior
- private prompts
- employee monitoring data
- manager notes
- sensitive employee relations details

If capture is needed, it should have:

- clear scope
- user notice
- retention rules
- access controls
- review visibility
- rollback or correction path
- legal/privacy/security review where appropriate

## Human-review boundaries

The system may learn from:

- explicit edits
- approval notes
- rejection reasons
- override rationale
- source corrections
- outcome notes

The system must not autonomously decide:

- discipline
- termination
- hiring selection or rejection
- promotion or demotion
- compensation
- investigation findings
- compliance certification
- legal or policy interpretation

## Demo-ready version

A good demo should show:

1. Original synthetic HR question.
2. AI-generated packet with sources and missing facts.
3. Human reviewer edit.
4. Reason for the edit.
5. Final approved action.
6. Learning note for future drafts.
7. Boundary: what the system is not allowed to automate next time.

The point is not "the model learned."

The point is "the organization made judgment visible."
