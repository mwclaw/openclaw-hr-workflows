# Agent Workflow Continuity and Recovery

**Evidence label: Prototype** — an operational runbook, not a certification of platform reliability or security.

## Purpose

Use this runbook before and after a platform upgrade, agent migration, or material configuration change. It is designed for mature workflows where multiple agents, scheduled jobs, memory indexes, external channels, and private applications must continue working together.

The goal is not merely a successful install command. The goal is continuity that can be observed, tested, and rolled back.

## 1. Establish the change boundary

Record:

- current platform and application versions
- the components included in the change
- the components intentionally excluded
- the active release identifier
- the rollback release and restore procedure
- the person accountable for the change

Keep one known-good rollback immediately available. Do not call a backup sufficient until its integrity and restore path have been tested.

## 2. Validate configuration before repair

- [ ] Parse and validate the current configuration.
- [ ] Identify deprecated fields and legacy state files.
- [ ] Preserve legacy files until their contents and replacement path are understood.
- [ ] Record explicit capacity limits instead of relying on changed defaults.
- [ ] Separate application identity, command-line identity, and service identity when the platform treats them independently.

Run supported diagnostic and repair commands iteratively when each pass can reveal the next migration layer. Record the final clean result, not the number of attempts as a quality claim.

## 3. Prove ownership and routing

- [ ] Every interactive ingress path has one explicit owner.
- [ ] Scheduled work has an accountable agent or execution lane.
- [ ] Hooks do not depend on ambiguous default ownership.
- [ ] A test message reaches the intended owner once.
- [ ] A substantive HR scenario routes to the configured specialist or remains explicitly narrow.

Ambiguous ownership is a continuity defect even when the gateway is technically reachable.

## 4. Verify memory and prior-event retrieval

- [ ] Every intended source reports the expected eligible-file count.
- [ ] The index is not dirty.
- [ ] Keyword and semantic retrieval are available when configured.
- [ ] Embedding identity and dimensions match the current index.
- [ ] A known prior-event record can be retrieved from a fresh session.
- [ ] Missing or degraded retrieval is visible to the operator.

Use the [Retrieval Before Prior-Event Answers](../patterns/retrieval-before-prior-event-answers.md) pattern for the behavioral test.

## 5. Inspect queues and incomplete work

- [ ] Dead-letter queues are enumerated by channel and failure reason.
- [ ] Replay is attempted only when the original payload and ownership are intact.
- [ ] Empty tombstones are distinguished from recoverable events.
- [ ] Interrupted tasks are categorized as active, recoverable, historical, or expired.
- [ ] Cleanup preserves audit evidence when deletion is not necessary for continuity.

Do not invent a recovered action when the system cannot prove what the original payload contained.

## 6. Audit scheduled jobs

- [ ] Enabled and disabled jobs match intent.
- [ ] Agent-run jobs have the intended tool authority.
- [ ] Model overrides are deliberate rather than migration residue.
- [ ] Worker concurrency is explicit and bounded.
- [ ] Command jobs and agent-turn jobs are evaluated according to their different execution models.
- [ ] One representative job completes and delivers through the expected route.

## 7. Test restart stability

After the final restart:

1. Record the service process identity and start time.
2. Wait beyond the previous failure interval or the documented stability window.
3. Confirm the process identity did not change unexpectedly.
4. Inspect recent logs for repeated restart, forced termination, drain, and recovery signals.
5. Confirm active work is not repeatedly interrupted.

A healthy response at one instant does not disprove a restart loop.

## 8. Exercise the operator path

Run one complete, reversible workflow:

1. send a synthetic or non-sensitive request through the real ingress path
2. verify ownership and specialist routing
3. retrieve a known prior record
4. produce the expected bounded artifact or answer
5. deliver it through the expected channel
6. confirm the private application or dashboard remains reachable
7. verify no duplicate event or orphaned task was created

## 9. Create the continuity receipt

Record only non-sensitive evidence:

- date and reviewer
- change scope
- configuration validation result
- ownership and routing result
- memory/index result
- dead-letter and incomplete-task result
- automation audit result
- restart-stability window
- end-to-end operator-path result
- active release and rollback readiness
- unresolved risks, owner, and review date

Do not publish private addresses, tokens, chat identifiers, local paths, private repository names, real HR data, or reconstructable infrastructure details.

## Stop conditions

Do not declare the change complete when:

- ownership remains ambiguous
- the service repeatedly restarts
- memory is dirty or a known record cannot be retrieved
- dead letters with intact payloads have no review owner
- concurrency changed without an explicit decision
- the active release cannot be identified
- the rollback cannot be restored
- an end-to-end operator path has not been exercised
