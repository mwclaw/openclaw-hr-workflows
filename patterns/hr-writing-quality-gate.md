# HR Writing Quality Gate

Updated: 2026-05-05

> **HRMC relationship:** Adjacent reusable review pattern, not a current product control.
>
> **Evidence level:** Proposed checklist; not production-validated and not a compliance certification method.

## Purpose

Use this as a lightweight review standard for AI-assisted HR writing.

It is designed for:
- employee-facing policy explanations
- manager guides
- HR FAQs
- performance or feedback drafts
- change-management communications
- People Ops templates
- policy assistant outputs

The goal is not to make every message short.

The goal is to make HR communication clear, accurate, source-backed, human, and safe.

---

## Quality dimensions

### 1. Readability

Use Flesch-Kincaid as a blunt signal.

Targets:
- Employee-facing FAQs / policy explanations: Grade 8-10
- Manager guidance: Grade 9-11
- Executive summaries: Grade 10-12
- Legal/policy quotations: no target, but explain in plain English afterward

Flags:
- Grade 12+: review for simplification
- Grade 14+: rewrite unless legal precision requires it
- Very short sentences only: check for robotic or patronizing tone

Readability is not enough. A simple answer can still be wrong.

### 2. Source accuracy

For any policy, compliance, benefits, leave, performance, pay, or employee-relations answer:
- cite the source document
- cite the section if available
- distinguish policy text from interpretation
- do not invent missing policy details
- flag source conflicts

Required question:
> Is this answer grounded in an approved source?

### 3. Completeness

The answer should address the actual question, not just summarize related policy.

Check:
- Did it answer what the person asked?
- Did it include the relevant eligibility, timing, location, or approval conditions?
- Did it mention the next step?
- Did it say when to contact HR?

### 4. Risk level

Classify the content before finalizing.

Low risk:
- general navigation
- standard FAQ
- where to find a form
- basic policy explanation with clear source

Medium risk:
- manager guidance
- performance feedback drafts
- employee complaints without protected-class indicators
- location-specific policy questions
- compensation process explanations

High risk:
- medical, disability, accommodation, protected leave
- harassment, discrimination, retaliation
- immigration
- pay disputes
- discipline or termination
- investigations
- named employee situations
- conflicting policy sources
- legal interpretation

Rule:
> High-risk content requires human HR/legal review before use.

### 5. Tone

HR writing should be:
- clear
- calm
- respectful
- direct
- non-defensive
- non-robotic
- appropriately warm

Avoid:
- legalistic fog
- false certainty
- moralizing
- corporate filler
- over-apologizing
- therapy-speak when operational clarity is needed

Tone check:
> Would a reasonable employee or manager understand this as helpful, fair, and serious?

### 6. Actionability

The reader should know what to do next.

Every useful HR answer should include one or more of:
- the next step
- owner/contact
- deadline/timing
- required form/system
- what happens after submission
- escalation path

If there is no action, say so clearly.

---

## AI output review checklist

Before using an AI-generated HR draft, check:

1. **Readability:** Is the grade level appropriate for the audience?
2. **Accuracy:** Is it grounded in approved source material?
3. **Completeness:** Did it answer the real question?
4. **Risk:** Does it trigger HR/legal review?
5. **Tone:** Is it clear, respectful, and human?
6. **Actionability:** Does the reader know what to do next?

If any answer is weak, revise or escalate.

---

## Suggested scoring rubric

Score each dimension from 1-5.

### Readability
1 = confusing / overly dense
3 = understandable but could be clearer
5 = plain, crisp, audience-appropriate

### Accuracy
1 = unsupported or likely wrong
3 = mostly grounded but needs source check
5 = source-backed with clear citations

### Completeness
1 = misses the question
3 = partially answers
5 = answers the question and relevant conditions

### Risk handling
1 = ignores risk
3 = flags some risk
5 = correctly classifies and escalates when needed

### Tone
1 = cold, vague, defensive, or robotic
3 = acceptable
5 = clear, respectful, direct, human

### Actionability
1 = no next step
3 = some next step
5 = clear owner/timing/action/escalation

Recommended threshold:
- 24+ total: usable
- 18-23: revise before use
- under 18: do not use
- any high-risk item: human review required regardless of score

---

## Prompt pattern

Use this after generating a draft:

```text
Review this HR draft using the HR Writing Quality Gate.

Assess:
1. Flesch-Kincaid readability / grade level
2. Source accuracy
3. Completeness
4. Risk level
5. Tone
6. Actionability

Then return:
- overall score out of 30
- risk level: low / medium / high
- top 3 issues
- revised draft
- whether human HR/legal review is required
```

---

## Implementation note for HR AI workflows

Flesch-Kincaid should be used as a signal, not a judge.

The system should not auto-approve writing just because it is easy to read.

The quality gate should combine:
- readability
- source grounding
- risk classification
- tone
- actionability
- human review boundaries

That is the difference between AI-generated text and an HR workflow that can be trusted.
