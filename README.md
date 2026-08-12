# OpenClaw HR

Practical workflow patterns for using OpenClaw in HR.

Built by [Mike Winkler](https://mikewinkleradvisory.com/about), an AI in HR expert and HR advisor with 16 years in HR, including 10 as an HRBP. These public materials show workflow design, failure tests, and human-review boundaries; they do not represent production client outcomes.

- [Printable AI in HR Workflow Review Worksheet](https://mikewinkleradvisory.com/resources/ai-in-hr-workflow-review)
- [HR Mission Control case study](https://mikewinkleradvisory.com/work/hr-mission-control)
- [Mike Winkler Advisory](https://mikewinkleradvisory.com)

## Important disclaimer
This repository is informational only.

It is not legal advice.
It is not a production-ready compliance framework.
It is not intended for autonomous employment decisions.
It does not treat employee handbooks as executable law or certify that a policy is compliant.

Any sensitive use case involving discipline, termination, pay, leave, accommodations, investigations, protected-class issues, or legal exposure should require human HR and, where appropriate, legal review.

Handbook and policy workflows should preserve three separate layers: applicable law/regulation, written company policy, and actual operating practice. The useful work is spotting tension between those layers, not pretending AI can own the interpretation.

## What this is
A small public repo for operator-grade HR workflow patterns built around OpenClaw.

## Professional case study

This repository documents selected public artifacts from a broader HR applied-AI project built by an HR practitioner.

The work demonstrates how I:

- translate real HR operating problems into bounded AI workflows
- design human approval, citation, privacy, and auditability controls
- separate legal information, company policy, and operating practice
- turn early concepts into reusable patterns, runbooks, and demonstrations
- define where automation must stop and qualified human judgment must begin

Only non-sensitive patterns and synthetic examples belong here. Product internals, private data, proprietary implementation details, and commercial research are intentionally excluded.

The clearest current-MVP example is the [Compliance Command Center](use-cases/compliance-command-center.md).

### See the workflow in two minutes

Start with the [Accountable Compliance Workflow Evidence Packet](examples/accountable-compliance-workflow-evidence.md). It connects the public architecture, a worked synthetic case, a refusal test, human approval points, and the audit receipt into one inspection path.

The packet is intentionally evidence of workflow design and bounded prototype behavior—not a claim of production accuracy, legal reliability, or autonomous decision-making.

## Evidence labels

Public artifacts use these labels so design work is not confused with production capability:

- **Current MVP** — part of HRMC's compliance-first prototype scope
- **Prototype** — demonstrated in a bounded or synthetic setting, not production-validated
- **Future research** — a possible later HRMC capability
- **Adjacent research** — related professional work, not a current HRMC feature

## Current focus
- human approval patterns
- policy Q&A guardrails
- employee handbook policy-check workflows
- compliance and auditability patterns
- policy interpretation support across law, written policy, and operating practice
- privacy-aware workflow design
- AI workload governance
- human-judgment learning loops without silent automation
- evaluated retrieval with visible failure reporting

## Design principles
- auditable
- human-in-the-loop
- privacy-aware
- useful before impressive
- bounded rather than autonomous

## What this is not
- generic AI hype
- private client work
- legal advice
- autonomous decision-making for sensitive HR situations
- compliance certification or autonomous handbook redlining; any prototype draft remains subject to qualified human and legal review
- a recommendation to use real employee PII in examples or demos

## Intended audience
- HR operators
- People Ops leaders
- HRBPs
- builders exploring agent workflows in HR

## Why this exists
Most AI-in-HR discussion stays too abstract. This repo is meant to document practical workflow patterns that can survive operational reality.

## Current contents
- HR agent design principles
- Employee handbook policy-check workflow
- Human approval pattern
- Policy Q&A guardrails
- Handbook policy-check worked example
- HR writing quality gate for source-backed, risk-aware review
- Multi-lens HR brief pattern for pressure-testing claims, sources, and review boundaries
- HR workflow risk tiers for proportional controls and human-review boundaries
- Runbooks for repeatable, human-reviewed OpenClaw-HR workflows
- Private-workflow readiness and recovery checks for access, request, backup, and publication boundaries
- HRBP brief worker → independent verifier → human review contract
- 25-question synthetic HRBP retrieval benchmark with reproducible baseline metrics and documented failures

## Usage boundary
These materials are best treated as early patterns and design notes. They should not be treated as a substitute for legal review, information security review, privacy review, or production implementation standards.

## Flagship use cases

Public-facing use cases use a law-style explainer format: plain-English problem, affected users, real-world impact, data needed, human-review boundaries, and demo path.

- [Compliance Command Center](use-cases/compliance-command-center.md)
- [HRBP Weekly Decision Brief](use-cases/hrbp-weekly-decision-brief.md)
- [HR Workflow Risk Tiers](use-cases/hr-workflow-risk-tiers.md)
- [Policy Assistant with Citations](use-cases/policy-assistant-with-citations.md)
- [AI Workload Governance Review](use-cases/ai-workload-governance-review.md)

## Runbooks

- [Weekly HR Artifact Graduation](runbooks/weekly-hr-artifact-graduation.md)
- [Private HR Workflow Readiness and Recovery](runbooks/private-hr-workflow-readiness.md)

## Reusable use-case page structure

Use this structure for every new workflow:

1. Summary
2. What problem does this solve?
3. What does this workflow do?
4. Who uses it / who is affected?
5. What is the real-world impact?
6. What data does it need?
7. What must stay human-reviewed?
8. What would make it demo-ready?
