# Publication Boundary

This repository is public. Treat every file here as something an outside reader, employer, vendor, journalist, or competitor could read.

## Public repo purpose

This repo may contain:

- reusable HR workflow patterns
- synthetic examples
- templates
- public-source monitoring concepts
- human-approval and auditability guidance
- privacy and prompt-injection guardrails

It should help people understand safe workflow design without exposing private systems.

## Keep public

Safe material:

- generic architecture patterns
- synthetic company names and fictional scenarios
- official public-source examples
- templates with placeholders
- high-level workflow diagrams
- non-sensitive implementation principles
- disclaimers and human-review boundaries

## Keep private

Do not publish:

- private application source code
- real company configs or employee counts
- customer, employee, candidate, manager, or family data
- local filesystem paths
- private repository names if not already intentionally public
- commit/provenance records meant for private IP/timeline tracking
- screenshots that show private dashboards or personal data
- credentials, tokens, API keys, cookies, webhook URLs, or environment variables
- internal automation details that would expose access patterns
- real handbook text or non-public policy documents
- legal conclusions presented as compliance certification

## Sanitization checklist before public PRs

Before publishing, check:

- [ ] examples are synthetic
- [ ] no real employee, candidate, manager, customer, or family data
- [ ] no private local home-directory paths
- [ ] no private repo names unless intentionally referenced
- [ ] no private app code copied into docs
- [ ] no tokens, API keys, webhook URLs, cookies, or secrets
- [ ] no exact private company configuration
- [ ] no screenshots containing private UI/data
- [ ] legal/compliance outputs are framed as issue spotting and review support
- [ ] human/legal approval boundary is explicit

## Automated enforcement

The repository's quality workflow runs `python3 scripts/check-publication-boundary.py` on every pull request and push to `main`.

The check fails closed on:

- unapproved top-level paths
- common private-state, credential, backup, database, and key-file paths
- oversized artifacts that are difficult to review safely
- local home-directory paths
- common secret and access-token formats
- the explicitly excluded private-application boundary

Automation is a backstop, not authorization to publish. A human reviewer must still assess meaning, context, source rights, employer confidentiality, and whether a collection of individually harmless details could reconstruct a private system.

## Good public wording

Use:

> This pattern helps route source-backed HR work to accountable human review.

Avoid:

> This system determines legal compliance.

Use:

> Draft language for review.

Avoid:

> Automatically update policy.

Use:

> Synthetic demo data.

Avoid:

> Sanitized real employee example.

## Practical rule

If publishing a detail would make it easier to reconstruct a private system, private data model, private timeline, or real operational footprint, keep it out of this repo.
