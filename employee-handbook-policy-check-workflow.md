# Employee Handbook Policy-Check Workflow

## Goal
Use OpenClaw to help review an employee handbook or policy document against a practical HR question.

## Example use cases
- Does the handbook clearly explain attendance expectations?
- Is the leave language consistent across sections?
- Does a manager question require a policy answer or human escalation?
- Are there missing disclaimers, unclear wording, or policy conflicts?

## Workflow
1. Ingest the handbook or policy text.
2. Identify the section most relevant to the question.
3. Extract the exact language that appears to answer it.
4. Summarize the likely answer in plain English.
5. Flag ambiguity, conflict, or missing language.
6. Escalate to a human if the issue involves legal interpretation, employee risk, or unclear policy language.

## Human approval points
- final interpretation for sensitive employee issues
- any recommendation that could affect employment action
- any situation involving leave, accommodation, pay, discipline, or protected class risk

## Audit trail should capture
- source policy section used
- exact language referenced
- summary produced
- ambiguity flagged
- escalation triggered or not

## Guardrails
- do not present output as legal advice
- do not fabricate policy language
- do not answer beyond the actual text
- escalate when policy is unclear or sensitive

## Why this matters
Policy-checking is a good HR agent workflow because it is useful, bounded, explainable, and safer when paired with human review.
