# HRBP Retrieval Benchmark

> **Evidence level:** Synthetic benchmark. It tests retrieval behavior on a small fictional corpus; it does not establish production accuracy, legal compliance, or fitness for employment decisions.

This benchmark makes retrieval failures visible before an HRBP decision brief is drafted. It deliberately evaluates retrieval separately from answer generation.

## Contents

- `corpus.json` — synthetic, versioned HR source passages
- `questions.json` — 25 questions with expected passage IDs and failure categories
- `run_baseline.py` — dependency-free BM25-style lexical baseline
- `baseline-report.json` — reproducible machine-readable results
- `FAILURE-LEDGER.md` — human-readable failures and bounded next experiments

## Run

```bash
python3 benchmarks/hrbp-retrieval/run_baseline.py
```

The script reports `hit@1`, `hit@5`, mean reciprocal rank, exact expected-passage ranking, and every failed query. A retrieval hit does not mean a generated conclusion is correct. Production use additionally requires authorization, version checks, privacy controls, injection defenses, claim-level citation validation, and qualified human review.

The benchmark should grow only when a real failure class is identified. Add one intervention at a time and retain the before/after report.
