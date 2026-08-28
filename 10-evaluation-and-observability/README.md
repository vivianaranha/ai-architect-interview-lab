# Evaluation and Observability

Use these for study and mock interviews. For every answer, add trade-offs, failure modes, and metrics.

## 1. Evaluation vs observability?

**Model answer:** Evaluation asks whether behavior is good enough; observability explains what happened operationally and why.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 2. What should be logged?

**Model answer:** Model/version, latency, tokens, retrieval IDs, tool calls, errors, policy outcomes, eval signals, correlation IDs, while minimizing sensitive content.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 3. What are offline evaluations?

**Model answer:** Repeatable tests against curated representative datasets before release and during regression testing.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 4. What are online evaluations?

**Model answer:** Production signals such as user feedback, task success, acceptance, escalation, abandonment, and sampled human review.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 5. How do you evaluate hallucination?

**Model answer:** Check claims against authoritative sources, measure unsupported statements, verify citations, and use human review in high-risk domains.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 6. What is an evaluation dataset?

**Model answer:** Representative inputs paired with expected outputs, references, or scoring criteria.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 7. Why use golden cases?

**Model answer:** Stable regression checks catch behavior changes across prompts, models, retrieval, and code.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 8. What is agent traceability?

**Model answer:** Recording model decisions, tool calls, policy checks, inputs, outputs, and state transitions.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 9. What operational metrics matter?

**Model answer:** Latency, availability, errors, token cost, model failures, tool failures, retrieval failures, queue depth, and timeouts.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 10. How do you detect quality drift?

**Model answer:** Trend evaluation metrics, sample production interactions, compare versions, and alert on statistically or operationally meaningful degradation.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?
