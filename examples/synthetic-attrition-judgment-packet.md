# Synthetic Demo: Attrition Signal to HR Judgment Packet

> **HRMC relationship:** Future-phase People Intelligence research; not part of the current compliance-first MVP.  
> **Evidence level:** Worked synthetic example, not a predictive model or production evaluation.

This demo uses fictional teams and synthetic data. It is designed to show a People Analytics workflow pattern without using real employee, manager, candidate, customer, or company data.

The goal is not to let AI decide what is happening on a team.

The goal is to help HR see where human judgment belongs.

## Scenario

A fictional employer, **ExampleCo**, has three teams in a quarterly people dashboard. One team appears to have elevated two-year turnover.

A basic dashboard might stop at the metric.

A useful HR workflow should turn the signal into a reviewable packet:

```text
source signal -> scoped relevance check -> evidence packet -> HR judgment point -> next action
```

## Step 1 — Synthetic source signal

Dataset: [`examples/data/synthetic-attrition-snapshot.csv`](data/synthetic-attrition-snapshot.csv)

| Team | Headcount | 2-year turnover | Company median | Regretted turnover | Internal mobility | Exit themes |
|---|---:|---:|---:|---:|---:|---|
| Team A | 42 | 29% | 21% | 17% | 5% | manager communication; growth path unclear; workload sustainability |
| Team B | 38 | 18% | 21% | 8% | 13% | commute; role mismatch; compensation |
| Team C | 55 | 22% | 21% | 9% | 11% | career change; manager communication; benefits |

## Step 2 — Relevance check

```json
{
  "signal": "Team A two-year turnover is above the company median",
  "comparison": {
    "team_a_two_year_turnover": "29%",
    "company_median_two_year_turnover": "21%",
    "difference_points": 8,
    "relative_difference": "about 38% higher than median"
  },
  "supporting_context": [
    "Team A has higher regretted turnover than the comparison teams.",
    "Team A has lower internal mobility than the comparison teams.",
    "Exit themes cluster around manager communication, growth path clarity, and workload sustainability."
  ],
  "boundary": "This is a review signal, not a conclusion about a manager or team."
}
```

## Step 3 — Evidence packet

```json
{
  "packet_type": "People analytics review packet",
  "state": "review-ready",
  "problem_statement": "Team A may have a retention risk that is not explained by turnover volume alone.",
  "known_facts": [
    "Team A's two-year turnover is 29% versus a 21% company median.",
    "Team A's regretted turnover rate is 17%, higher than Teams B and C in this synthetic snapshot.",
    "Team A's internal mobility rate is 5%, lower than Teams B and C.",
    "Synthetic exit themes include manager communication, growth path clarity, and workload sustainability."
  ],
  "missing_facts": [
    "Whether the exits are concentrated by role, tenure, location, or manager span.",
    "Whether the team had restructuring, hiring freezes, unusual workload, or leadership changes.",
    "Whether survey comments, skip-level feedback, or promotion data support the same pattern.",
    "Whether the data is statistically meaningful given team size and privacy thresholds."
  ],
  "human_owns": [
    "Interpreting whether the signal reflects leadership, role design, workload, compensation, career pathing, or normal variance.",
    "Deciding whether and how to engage the manager.",
    "Protecting privacy and avoiding over-attribution from small-sample data."
  ]
}
```

## Step 4 — HR judgment point

The useful question is not:

> Which manager is the problem?

The useful question is:

> What would we need to know before making this a manager, role-design, workload, or career-path conversation?

That distinction matters.

People Analytics should create clarity and accountability. It should not turn a metric into a verdict.

## Step 5 — Suggested next action

```json
{
  "owner": "HRBP or People Analytics partner",
  "next_action": "Review Team A trend by role, tenure, and manager span; compare with engagement comments and internal mobility history before recommending action.",
  "review_questions": [
    "Is the turnover concentrated in one role family or tenure band?",
    "Did workload or leadership context change during the period?",
    "Do survey comments or skip-level notes support the exit themes?",
    "Is there a safe way to discuss the pattern without exposing individual exits?"
  ],
  "do_not_do": [
    "Do not label the manager as the cause from this packet alone.",
    "Do not expose individual exit details.",
    "Do not automate employment decisions from the signal."
  ]
}
```

## Step 6 — AI-assist prompt

```text
Using only the synthetic attrition table and the packet fields below, draft a review note for an HRBP.

Separate:
1. what the data shows,
2. what it does not prove,
3. what questions a human should ask next,
4. what should not be automated.

Do not identify a manager as the cause.
Do not recommend discipline, termination, pay action, or employment decisions.
Treat the output as a starting point for HR review.
```

## What this design demonstrates

A useful AI workflow in HR is not the one that produces the most analysis.

It is the one that makes the human judgment point easier to see.

In this example, the metric matters. But the workflow is only useful if it keeps the evidence, uncertainty, owner, and next action visible.

That is the difference between a dashboard and a judgment packet.
