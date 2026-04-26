# Privacy Boundary Pattern

## Goal
Define what HR data should and should not enter an OpenClaw workflow, and when sensitive handling requires stronger controls or human review.

## Core principle
Use the minimum necessary data.

If a workflow can succeed with less detail, give it less detail.
Do not feed an agent more employee or candidate information than the task actually requires.

## Default rule
Before any HR workflow runs, ask:
- What is the smallest useful input?
- What can be summarized instead of exposed directly?
- What should be redacted?
- Who should be allowed to review the result?

## High-risk data examples
Treat these as high-risk by default:
- Social Security numbers
- home address
- personal phone/email when not needed
- compensation details beyond the task scope
- medical information
- disability or accommodation details
- leave details tied to diagnosis or treatment
- investigation notes
- harassment or retaliation allegations
- protected-class information
- immigration or work authorization documents
- bank, payroll, or tax information

## Safer workflow pattern
Prefer this sequence:
1. classify the task
2. reduce to minimum necessary data
3. redact or summarize high-risk details when possible
4. run the workflow on the reduced context
5. require human review for sensitive outputs
6. retain only what is needed for audit or operational follow-up

## Good example
A handbook policy-check workflow usually does **not** need:
- employee name
- manager name
- full employee history
- compensation records
- medical details

It usually only needs:
- the policy text
- the practical question being asked
- minimal context about the scenario

## Bad example
Feeding a full employee relations file into an agent workflow just to answer a narrow handbook question.

## Data handling guardrails
- do not use real employee PII in public examples or demos
- redact names when identity is not necessary
- do not keep sensitive context longer than needed
- separate demo/test data from real operational data
- restrict reviewer access to people with a legitimate need to know
- log what source material was used without unnecessarily copying sensitive content everywhere

## Retention and deletion questions
Any serious workflow should define:
- what gets stored
- where it is stored
- who can view it
- how long it is retained
- when it is deleted or archived

## Human review triggers
Require human review when the workflow touches:
- leave
- accommodations
- discipline
- termination
- investigations
- protected-class issues
- pay decisions
- legal threats or probable litigation

## Why this matters
A workflow can be operationally clever and still be irresponsible if it ignores privacy boundaries. In HR, bounded data use is not optional. It is part of the design.
