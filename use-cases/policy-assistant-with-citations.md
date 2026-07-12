# Policy Assistant with Citations

> **HRMC relationship:** Related prototype concept for the AI Service Desk; outside the current compliance-first MVP.  
> **Evidence level:** Proposed workflow pattern; not production-validated.

### Summary
Designed to answer employee and manager policy questions using approved company documents, show citations, flag uncertainty, and escalate sensitive cases instead of guessing.

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
- **Potentially faster answers** — basic questions may be answered from approved material.
- **Consistency support** — responses are grounded in approved source material.
- **Potentially lower repetitive volume** — some routine questions may become self-serve.
- **Reduced false-certainty risk** — citations, refusals, and escalation rules make limitations more visible.
- **Policy-improvement signals** — repeated confusing questions may reveal where policies need rewriting.

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
