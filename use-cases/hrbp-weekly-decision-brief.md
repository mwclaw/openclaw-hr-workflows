# HRBP Weekly Decision Brief

> **HRMC relationship:** Adjacent research related to manager-support workflows, not the current compliance-first MVP.  
> **Evidence level:** Proposed workflow pattern; not production-validated.

### Summary
Designed to create a weekly executive-style brief for HRBPs that highlights people risks, upcoming decisions, manager follow-ups, and unresolved issues across their client group.

### What problem does this solve?
HRBPs sit between executives, managers, employees, People programs, and messy operating reality. Their problem is rarely lack of information. It is fragmentation.

Signals live in 1:1 notes, engagement comments, attrition data, performance cycles, Slack/email, open ER issues, headcount plans, and manager conversations. The HRBP has to manually synthesize all of it into judgment.

### What does this workflow do?
- Pulls agreed inputs into a weekly briefing packet.
- Summarizes key people risks and open loops.
- Highlights decisions due this week.
- Flags manager follow-ups.
- Separates facts, interpretation, and recommended action.
- Creates questions for the HRBP to pressure-test.
- Produces a concise manager/executive-ready version when approved.

### Worker → verifier → human review contract

This proposed workflow uses two deliberately separate roles. Neither may send messages, update an HR system, or make an employment decision.

1. **Brief worker:** turns an approved source packet into a draft using [`../templates/hrbp-weekly-decision-brief.md`](../templates/hrbp-weekly-decision-brief.md). It separates verified facts from interpretation, cites sources, names missing facts, keeps law/regulation, written policy, and operating practice distinct, and names the owner and next question.
2. **Independent verifier:** receives the source packet, draft, and contract—but not the worker's hidden reasoning. It rejects missing sources, unsupported claims, hidden unknowns, absent owners/actions, policy/practice/legal conflation, or weak escalation boundaries. The structural checker can reject incomplete drafts, but a passing structure does not prove factual accuracy.
3. **Human HRBP:** approves, edits, returns, or discards the work. Only a human-approved version may be adapted for a manager or executive audience.

The receipt records the worker output, verifier result, material edits or override rationale, human disposition, and any separately authorized external action. The companion [synthetic retrieval benchmark](../benchmarks/hrbp-retrieval/README.md) tests whether expected source passages are found before drafting begins and publishes failures rather than hiding them.

### Who uses it / who is affected?
- HRBPs / People Business Partners
- People leaders
- Functional executives
- Managers with open talent or org issues
- Employees indirectly affected by better follow-through and decision quality

### What is the real-world impact?
- **More structured judgment under load** — aims to put important signals in one place.
- **More visible follow-up** — makes open loops easier to review.
- **Manager-coaching support** — turns vague concerns into questions for human judgment.
- **Executive-prep support** — organizes inputs before leadership meetings.
- **Clearer boundaries** — distinguishes HR-owned work from manager-owned work.

### What data does it need?
- HRBP notes / action logs
- Talent review outputs
- Performance cycle status
- Engagement survey themes
- Attrition / regrettable loss data
- Open ER or manager-relations issues at appropriate access level
- Headcount / hiring plan changes
- Calendar reminders and prior commitments

### What must stay human-reviewed?
- Any recommendation about a named employee
- Performance, termination, discipline, accommodations, leave, or investigation matters
- Executive-facing summaries
- Sensitive employee relations content
- Anything where data is incomplete or context-dependent

### What would make it demo-ready?
- Use synthetic HRBP notes and fake talent data.
- Generate a one-page weekly brief.
- Show sections: Watchlist, Decisions, Manager Follow-ups, Risks, Recommended Next Moves.
- Include confidence labels and source links.
- End with the HRBP approving/editing the final version.
- Show the worker draft failing at least one verifier gate, then show the corrected draft and human disposition.
