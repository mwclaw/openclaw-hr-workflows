# Selected Work

This page is the shortest inspection path through the strongest public work in this repository.

Every item uses synthetic data or reusable operating patterns. Evidence labels distinguish demonstrated prototypes from production claims.

## 1. Accountable compliance workflow

**Evidence label: Current MVP**

Demonstrates a bounded path from source material to an HR-owned review decision:

- separates law or regulation, written policy, and operating practice
- preserves citations and missing facts
- exercises a refusal path
- records human approval points
- leaves a reconstructable audit receipt

[Inspect the evidence packet](../examples/accountable-compliance-workflow-evidence.md) · [Read the use case](../use-cases/compliance-command-center.md)

## 2. HR Decision Packet

**Evidence label: Prototype with a public release**

A cross-platform workflow for turning an incomplete people question into a reviewable packet rather than an unsupported recommendation. The package includes adversarial evaluations, synthetic input and output, templates, and editions for multiple assistant platforms.

[Inspect the skill](../skills/hr-decision-packet/) · [See platform packaging](../skills/hr-decision-packet/PLATFORMS.md)

## 3. Evaluated HRBP retrieval benchmark

**Evidence label: Reproducible synthetic benchmark**

A 25-question retrieval evaluation with a synthetic corpus, executable baseline, machine-readable results, and a failure ledger. It demonstrates the difference between having documents and proving that a workflow can retrieve the right evidence.

[Inspect the benchmark](../benchmarks/hrbp-retrieval/) · [Read the failure ledger](../benchmarks/hrbp-retrieval/FAILURE-LEDGER.md)

## 4. Human judgment learning loop

**Evidence label: Prototype pattern**

Shows how reviewed edits, approvals, rejections, override rationale, and outcomes can improve future work without silently converting one person's judgment into autonomous policy.

[Read the pattern](../patterns/human-judgment-learning-loop.md)

## 5. Retrieval before prior-event answers

**Evidence label: Prototype pattern with a synthetic failure test**

Defines a recall gate for questions that depend on an earlier event. The workflow must retrieve the relevant record, distinguish evidence from inference, and fail visibly when the record is unavailable.

[Read the pattern](../patterns/retrieval-before-prior-event-answers.md)

## 6. Agent workflow continuity and recovery

**Evidence label: Prototype runbook**

Turns platform upgrades and configuration changes into an inspectable reliability exercise covering ownership, queues, memory, restart stability, rollback readiness, and end-to-end operator checks.

[Read the runbook](../runbooks/agent-workflow-continuity-and-recovery.md)

## What is intentionally absent

This portfolio does not publish private application source, real employee or company data, private operational configuration, local paths, credentials, or private provenance records. The value shown here is the reusable workflow design and its testable control structure.
