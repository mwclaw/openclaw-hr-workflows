# Private HR Workflow Readiness and Recovery

**Evidence label: Prototype** — a reusable operational checklist, not a production certification or substitute for security, privacy, or legal review.

## Purpose

Use this runbook before operating a private HR workflow that handles source documents, review packets, policy drafts, or audit evidence. It tests whether access, data handling, recovery, and publication boundaries work together.

Passing the checklist means the controls were observed at a point in time. It does not prove that a system is secure or legally compliant.

## 1. Define the boundary

Write down, in plain language:

- who may reach the workflow
- which network or identity boundary enforces access
- which ports and services should be reachable
- what must never be reachable from the public internet
- which data is allowed in the workflow
- which data and artifacts may be published

Prefer an explicit allowlist. "Private by convention" is not a control.

## 2. Verify private network exposure

- [ ] The application binds only to an approved private interface or loopback behind an approved access proxy.
- [ ] It does not listen on every interface unless a reviewed firewall or proxy policy requires that configuration.
- [ ] Public tunneling, public ingress, and anonymous sharing are disabled.
- [ ] Every registered device or service identity has a current owner and business purpose.
- [ ] Lost, replaced, or abandoned devices are removed promptly.
- [ ] Access rules grant only the people and systems that need the workflow.
- [ ] A negative test confirms that an unapproved origin or network path cannot perform a write.

Record the observed listener, access rule, device review date, and negative-test result without publishing private addresses or identity details.

## 3. Enforce the application request boundary

Network privacy does not replace safe request handling.

- [ ] State-changing routes reject requests from foreign origins.
- [ ] Routes accept only expected methods and content types.
- [ ] Request bodies and uploads have bounded sizes.
- [ ] Uploads are checked by extension, declared type, and file signature where practical.
- [ ] Error responses do not reveal local paths, internal stack traces, or sensitive record content.
- [ ] Responses set appropriate content-type, framing, referrer, and browser-permission headers.
- [ ] Concurrent writes cannot silently overwrite or corrupt the same record.
- [ ] Stale forms or approvals cannot replace a newer decision without a visible conflict.

## 4. Protect HR data at rest

- [ ] The workflow uses the minimum necessary HR data.
- [ ] Sensitive data directories and files are owner- or service-account-only by default.
- [ ] Writes are atomic or otherwise recoverable after interruption.
- [ ] Test fixtures are synthetic and stored separately from operational data.
- [ ] Logs identify actions and sources without copying unnecessary sensitive content.
- [ ] Retention and deletion expectations are documented.
- [ ] Backups are encrypted or protected by equivalent access controls.

## 5. Prove recovery, not just backup creation

A checksum proves archive integrity; a restore drill proves recoverability.

1. Select a recent backup and verify its checksum or integrity marker.
2. Restore into an isolated temporary location, never over the live system.
3. Restore the application, data, and every documented runtime dependency.
4. Parse or validate restored data stores.
5. Reinstall reproducible dependencies from the lockfile or equivalent manifest.
6. Run the restored workflow's contract and smoke tests.
7. Record missing dependencies and update the restore manifest.
8. Remove the temporary restored copy when validation is complete.

The drill fails if it depends on undocumented files from the live system.

## 6. Separate private operation from public evidence

- [ ] Public repositories use a positive allowlist of approved HR artifact paths.
- [ ] Personal, employee, candidate, family, customer, and employer-confidential data are excluded.
- [ ] Private application source, local paths, configuration, telemetry, and provenance logs remain private.
- [ ] A pre-push or pre-publication guard fails closed on unknown paths.
- [ ] Continuous-integration checks inspect the exact proposed public diff.
- [ ] Secret and sensitive-string scans run before publication.
- [ ] Public examples are synthetic and human-review boundaries are explicit.

Review [Publication Boundary](../PUBLICATION_BOUNDARY.md) before every public pull request.

## 7. Run a representative operator path

Exercise one complete, reversible workflow:

1. ingest or select a synthetic source signal
2. create the review packet or case record
3. capture source identity and evidence
4. perform the human approval or refusal step
5. update the implementation or follow-up state
6. reconstruct the audit evidence without relying on the interface
7. restore exact pre-test operational data

Test the refusal path as well as the happy path. A workflow is not ready if it cannot stop safely.

## 8. Create the readiness receipt

Record:

- date and reviewer
- scope and evidence label
- private listener or access-boundary result
- registered-device review result
- request-boundary negative test
- data-permission result
- backup checksum and isolated-restore result
- representative operator-path result
- publication-boundary scan result
- unresolved risks and owner
- next review date

Do not put private addresses, real HR data, credentials, or reconstructable system details in a public receipt.

## Stop conditions

Do not operate or publish when:

- the application is reachable through an unapproved path
- device or service ownership is unknown
- state-changing routes accept untrusted origins
- a backup cannot be restored independently
- test runs cannot restore exact pre-test data
- the public diff includes a private or ambiguous path
- a sensitive workflow lacks accountable human review

## Recommended cadence

- run the short access and health checks after each release
- review devices and access rules monthly, and after personnel or device changes
- perform an isolated restore drill at least quarterly
- test a representative reversible workflow before material process changes
- review every public artifact independently before publication
