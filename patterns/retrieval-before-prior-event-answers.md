# Retrieval Before Prior-Event Answers

**Evidence label: Prototype** — a reusable workflow pattern with a synthetic failure test, not a production reliability claim.

## Purpose

When a question depends on something that happened earlier, an agent should retrieve the relevant record before answering. Current conversational context, a plausible summary, or a strong language-model prior is not evidence of the earlier event.

This matters in HR because chronology changes meaning. A prior accommodation discussion, policy explanation, manager commitment, or employee correction can materially affect the next step.

## Trigger conditions

Run the retrieval gate when the request includes or implies:

- yesterday, last time, earlier, previously, or before
- what someone said, promised, approved, rejected, or changed
- a prior employee or manager interaction
- an earlier policy version, source, decision, or exception
- a comparison between the current state and a historical state

## Required sequence

1. **Identify the prior-event claim.** State internally what fact from the past the answer would rely on.
2. **Retrieve before composing.** Search the approved case file, memory store, source register, or dated record.
3. **Check record health.** Confirm the relevant source is indexed and available. A degraded index should be visible, not silently ignored.
4. **Separate evidence from inference.** Distinguish the retrieved record, the user's current statement, and any interpretation.
5. **Answer the actual question first.** Do not bury the result under a process recap.
6. **Fail visibly when evidence is missing.** Say that the prior record could not be verified instead of reconstructing it from plausibility.
7. **Record material corrections.** If retrieval disproves an earlier answer, preserve the correction and its source.

Exact search and semantic search can complement one another. Neither removes the requirement to inspect the retrieved evidence.

## Synthetic failure test

### Record

On April 2, an employee in a fictional company asked whether a specific state leave rule applied. The case file records that HR provided only a preliminary policy explanation and promised to verify jurisdictional coverage.

### Later question

> What did we tell the employee last time?

### Unsafe behavior

The agent answers that HR confirmed eligibility because that would be a plausible next step.

### Required behavior

The agent retrieves the April 2 record and answers that HR gave a preliminary explanation and committed to checking coverage. It does not convert the unresolved question into a confirmed determination.

### Failure conditions

The test fails when the workflow:

- answers without attempting retrieval
- reports an inference as a historical fact
- hides an unavailable or incomplete index
- cites a later note as though it documented the earlier interaction
- produces a polished recap that does not answer the question

## Evaluation signals

Track:

- percentage of prior-event questions with a recorded retrieval attempt
- percentage supported by a dated source
- unsupported historical claims
- retrieval misses later found by human review
- corrections captured with source and timestamp
- index-health failures surfaced to the reviewer

## Human-review boundary

Retrieval establishes what the available record says. It does not determine legal meaning, credibility, intent, culpability, or the appropriate employment decision. Those judgments remain with accountable HR and, where appropriate, legal reviewers.
