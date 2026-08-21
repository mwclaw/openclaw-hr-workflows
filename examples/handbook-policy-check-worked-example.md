# Worked Example — Employee Handbook Policy Check

## Scenario
A manager asks whether the employee handbook clearly supports an attendance write-up for repeated tardiness.

## Workflow goal
Use OpenClaw to review the handbook language, summarize what it says, identify gaps, and determine whether the issue should be escalated.

## Step 1 — Ingest source
The workflow reads the employee handbook and identifies the sections related to:
- attendance
- punctuality
- corrective action
- manager responsibilities

## Step 2 — Extract relevant text
The workflow pulls the exact policy language that appears relevant.

Example output:
- Attendance section states employees are expected to report on time for scheduled shifts.
- Corrective action section says repeated policy violations may result in discipline.
- No section defines what number of tardies triggers a write-up.

## Step 3 — Summarize in plain English
Example summary:
- The handbook supports attendance expectations and allows corrective action for repeated violations.
- The handbook does not clearly define a tardiness threshold for formal write-up.
- This means the manager may need HR review before treating the situation as clearly policy-driven.

## Step 4 — Flag ambiguity
The workflow should explicitly note:
- missing threshold definition
- missing manager guidance
- any inconsistent language across sections

## Step 5 — Decide whether to escalate
Because the question involves possible discipline and the handbook language is not fully specific, the workflow should escalate to a human.

## Sample operator-facing result
- **Question:** Does the handbook clearly support an attendance write-up for repeated tardiness?
- **Answer:** Partially. The handbook supports attendance expectations and corrective action, but it does not define a specific tardiness threshold.
- **Source sections used:** Attendance Policy, Corrective Action Policy
- **Risk note:** Discipline-related interpretation should be reviewed by HR before action is taken.
- **Escalation:** Yes

## Why this is a useful example
This shows the difference between:
- a workflow that helps clarify policy
- and a workflow that improperly pretends to make the final discipline call

That distinction is the whole point.
