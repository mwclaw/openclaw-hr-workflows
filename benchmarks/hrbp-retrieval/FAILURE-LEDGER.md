# Retrieval Failure Ledger

This ledger is checked against `baseline-report.json`. A failure is useful evidence, not something to hide.

## Baseline result — 2026-08-12

- Answerable questions: 24
- Hit@1: 79.17%
- Hit@5: 100%
- MRR: 0.8958
- Safety/coverage failure: Q25 returned plausible reorganization passages even though the corpus contains no authorized employee-communication answer. Lexical ranking cannot prove answerability and requires a separate abstention/source-coverage gate.

Five additional ranking misses placed an acceptable passage second rather than first:

| Question | Expected passage ranked | Observed issue |
|---|---:|---|
| Q05 — missing facts in Jordan's request | 2 | General accommodation guidance outranked the case note containing the missing facts. |
| Q11 — leave-related calibration concern | 2 | A speak-up note outranked the calibration note because generic concern terms dominated. |
| Q17 — current leave process | 2 | Accommodation guidance outranked the current leave guide; version/current intent was not enforced. |
| Q23 — small demographic-group protection | 2 | The survey source outranked the privacy standard that contains the rule. |
| Q24 — diagnosis-detail question | 2 | The case note outranked the governing accommodation guidance. |

These are not hidden by Hit@5. They identify where field weighting, intent routing, version filtering, or reranking could help. The next experiment should be the abstention/version gate because its failure has greater HR risk than the ranking misses.

## Intervention rules

| Observed failure | Smallest next experiment | Do not assume |
|---|---|---|
| Right document, wrong fragment | Return the parent section | More reasoning restores missing context |
| Exact identifier missed | Add lexical normalization or field weighting | Embeddings are automatically better |
| Vocabulary mismatch | Add semantic retrieval and fuse ranks | Hybrid improves every query |
| Correct passage ranks too low | Add a reranker | Reranking recovers an absent passage |
| Question requires several sources | Decompose into bounded subqueries | One answer proves every subclaim |
| Corpus has no authorized answer | Add abstention/source-coverage gate | Similarity means the answer exists |
| Superseded source outranks current | Add effective-date/version filtering | Recency is safely inferred from prose |

No benchmark result authorizes an employment recommendation. Accommodations, leave, retaliation, performance action, reorganization, and demographic data require appropriate human HR and, where applicable, legal/privacy review.
