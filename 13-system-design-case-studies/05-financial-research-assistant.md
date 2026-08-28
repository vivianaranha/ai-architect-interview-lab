# Design a Financial Research Assistant

## Interview prompt
Combine filings, market data, internal research, and analyst notes.

## Constraints
- Low tolerance for fabrication
- Time-sensitive data
- Entitlements
- Licensed content

## Strong answer structure
1. Clarify users, workflow, and measurable outcome.
2. Identify systems of record and data ownership.
3. Separate deterministic services from probabilistic components.
4. Define identity, authorization, and trust boundaries.
5. Add retrieval/models/agents only where justified.
6. Define human review for risky actions.
7. Cover evaluation, observability, failure modes, scale, and cost.
8. Explain alternatives and rollout.

## Baseline whiteboard
```mermaid
flowchart LR
 U[User] --> X[Experience]
 X --> O[AI Orchestration]
 O --> M[Model Gateway]
 O --> R[Retrieval]
 O --> T[Enterprise Tool Layer]
 T --> S[Systems of Record]
 R --> K[Knowledge]
 O --> P[Policy and Guardrails]
 O --> E[Evaluation and Observability]
```

## Follow-ups
- Highest-risk failure mode?
- Where is human approval required?
- What would you cache?
- How do you handle model/provider change?
- What launch metrics matter?
