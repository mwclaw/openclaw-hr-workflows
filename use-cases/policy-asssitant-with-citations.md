# Policy Assistant with Citations

### Summary
Answers employee and manager policy questions using approved company documents, shows citations, flags uncertainty, and escalates sensitive cases instead of guessing.

### What problem does this solve?
Employees and managers ask policy questions constantly. HR spends time answering repeat questions, correcting misunderstandings, and translating policy language into practical next steps.

Generic AI is dangerous here because a confident wrong answer can create legal, employee-relations, or trust problems.

### What does this workflow do?
- Searches only approved policy sources.
- Answers in plain English.
- Cites the exact policy section used.
- Gives a practical next step.
- Shows confidence level.
- Refuses or escalates when the question is sensitive, ambiguous, or outside the source material.
- Logs the question, answer, citation, and escalation path.

### Who uses it / who is affected?
- Employees
- Managers
- People Operations
- HRBPs
- Employee Relations
- Legal/compliance reviewers for escalated questions

### What is the real-world impact?
- **Faster answers** — employees get basic guidance without waiting on HR.
- **Better consistency** — answers come from approved source material.
- **Reduced HR volume** — repeat questions become self-serve.
- **Safer AI adoption** — citations, refusals, and escalation rules prevent false certainty.
- **Policy improvement loop** — repeated confusing questions reveal where policies need rewriting.

### What data does it need?
- Approved employee handbook
- Policy library
- Benefits summaries where appropriate
- Location-specific policy variants
- Escalation rules by topic
- HR contact / intake routing map

### What must stay human-reviewed?
- Medical, disability, accommodation, protected leave, harassment, discrimination, retaliation, immigration, pay, discipline, or termination questions
- Questions involving a named employee situation
- Any answer where source documents conflict
- Any answer requiring legal interpretation

### What would make it demo-ready?
- Load a synthetic handbook.
- Ask three questions:
  1. simple PTO question
  2. location-specific leave question
  3. sensitive accommodation/ER question
- Show correct behavior: answer, cite, escalate.
- Show the audit log.
- End with: “The magic is not the answer. The magic is the guardrail.”
