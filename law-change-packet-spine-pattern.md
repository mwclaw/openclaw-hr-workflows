# Law Change Packet Spine Pattern

> **HRMC relationship:** Current compliance-first MVP design pattern.  
> **Evidence level:** Prototype workflow; production reliability has not been validated.  
> **Disclosure boundary:** Public material shows the operating principle, not the private data model, complete state machine, or production orchestration.

## Goal

Turn a detected HR law or policy-source change into one accountable, source-backed work item instead of a set of disconnected dashboards, queues, drafts, and audit notes.

The pattern is simple:

```text
one law/change = one canonical case = one packet spine = one visible next action
```

## Why this matters

HR compliance workflows often break down after the first signal appears:

- the source alert lives in one place
- the applicability analysis lives somewhere else
- the policy draft is detached from the source
- the implementation tracker becomes a separate queue
- audit evidence is collected late or not at all
- multiple teams see different versions of the same work

That fragmentation makes AI-assisted HR work look more complete than it is. A packet spine keeps every artifact attached to the same source-backed case until a human reviewer closes or archives it.

## When to use this pattern

Use this when a public source, vendor alert, policy review, handbook scan, or internal compliance intake suggests that an HR obligation may have changed.

Good examples:

| Scenario | Why a packet spine helps |
|---|---|
| State employment-law update | Keeps source, jurisdiction, applicability, owner, policy impact, and deadline together. |
| New agency guidance | Separates monitoring from implementation until a human decides the guidance applies. |
| Handbook review gap | Connects a draft redline to the source and review decision that caused it. |
| Payroll/timekeeping rule change | Keeps legal review, system/process updates, notices, and audit proof under one case. |
| Safety or leave-policy change | Prevents training, policy, and manager-communication work from becoming separate uncontrolled queues. |

## Core workflow

```text
1. Source signal detected
   ↓
2. Canonical law-change case created
   ↓
3. Review packet built
   ↓
4. Human/legal review decision recorded
   ↓
5. Policy, redline, implementation, and communication artifacts linked
   ↓
6. Audit proof retained
   ↓
7. Case closed, archived, or kept on watch
```

The visible product should show the operator one clear next action, not five parallel places to check.

## Canonical case

The canonical case is the durable work item that connects the source signal, affected scope, accountable owner, review decision, implementation work, and evidence. Exact fields and the private data model are intentionally not published.

## Review packet

The review packet is not the final answer. It is the structured packet that lets a qualified human decide what happens next.

A useful packet includes:

- plain-English summary of what changed
- source trail and publication date
- affected jurisdictions or employee populations
- known facts and assumptions
- missing facts
- preliminary risk areas
- owner and consults
- recommended disposition: archive, watch, build implementation work, or escalate
- explicit human/legal approval boundary

## Stage principle

The private workflow distinguishes early signals, watch items, human/legal review, implementation, and closure with evidence. The exact state machine and transition rules remain private.

## Artifact nesting rule

Policy drafts, redlines, tracker items, communications, and audit notes should not become independent active queues. They are artifacts under the canonical case.

Bad shape:

```text
source alerts queue
packet queue
implementation queue
redline queue
audit queue
```

Better shape: one canonical case with related review and implementation artifacts attached to it. The operator should not need to reconcile competing queues for the same change.

The operator should be able to ask: “What is the next action on this law change?” and get one answer.

## AI boundaries

AI can help by:

- summarizing public-source material
- identifying likely impacted policy/process areas
- drafting a review packet
- extracting missing facts
- comparing source language to draft policy language
- preparing checklists for accountable owners
- organizing audit evidence

AI should not:

- decide legal applicability by itself
- certify compliance
- approve policy changes
- send employee-facing communications without review
- make or recommend sensitive employment decisions as final outcomes
- hide uncertainty, missing facts, or source limitations

## Human approval points

Pause for qualified human review before:

- legal interpretation
- deciding that an obligation applies or does not apply
- approving handbook, policy, or process changes
- changing pay, leave, benefits, accommodations, discipline, termination, safety, immigration, or protected-class practices
- sending employee-facing communications
- closing a case as complete

## Demonstration boundary

A safe demo can use synthetic facts and public-source-style placeholders:

A safe demonstration may show a fictional source signal becoming a reviewable case, followed by a human disposition and linked implementation evidence. It should not expose the production state model, orchestration, source configuration, prompts, or private data schema.

Do not demo this pattern with real employee PII, private company configurations, confidential policy text, or legal conclusions presented as certification.

## Design checks

A packet-spine workflow is working when:

- every active law-change signal has one canonical case
- every implementation item links back to a packet or recorded review decision
- every policy/redline artifact links back to the source-backed case
- proposed or non-final changes stay in watch status unless a human creates work
- final/effective changes do not skip packet review
- completion requires audit proof
- the operator can see one next action per case

## Practical rule

If a new page, queue, agent, or dashboard makes the same law change appear as separate pieces of work, it is probably weakening the workflow. Attach the artifact to the packet spine instead.

## Boundary

This pattern is informational only. It is not legal advice, a compliance certification method, or a recommendation to automate sensitive HR decisions.
