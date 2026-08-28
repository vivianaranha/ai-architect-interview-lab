# Enterprise Integration

Use these for study and mock interviews. For every answer, add trade-offs, failure modes, and metrics.

## 1. How should agents access enterprise systems?

**Model answer:** Through governed APIs, service layers, or approved tool interfaces rather than uncontrolled direct access.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 2. Why use a tool abstraction layer?

**Model answer:** It decouples agent reasoning from systems and centralizes authorization, validation, retries, logging, and adapters.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 3. How do you safely integrate SaaS systems?

**Model answer:** Supported APIs, delegated identity/service accounts, scoped permissions, rate limits, audit logging, and server-side business rules.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 4. Why does idempotency matter?

**Model answer:** Retries must not create duplicate side effects, especially for writes and transactions.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 5. How do you handle long-running workflows?

**Model answer:** Durable workflow engines, queues, checkpoints, job status APIs, and event-driven continuation.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 6. Where should critical business rules live?

**Model answer:** In deterministic services or policy engines, not only in prompts.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 7. How should agents handle API failure?

**Model answer:** Classify retryability, bounded retries, circuit breakers, preserved task state, safe partial results, and escalation.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 8. What are contract tests?

**Model answer:** Tests verifying integrations conform to expected schemas and behavior so upstream changes are detected early.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 9. How do you propagate enterprise identity?

**Model answer:** Carry authenticated user/service identity to tools and enforce authorization at every boundary; never trust model-generated identity claims.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 10. Why separate read and write tools?

**Model answer:** Writes require stronger scopes, validation, approval, idempotency, auditability, and rollback planning.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?
