# Scalability Reliability and Cost

Use these for study and mock interviews. For every answer, add trade-offs, failure modes, and metrics.

## 1. How do you scale LLM applications?

**Model answer:** Stateless services, horizontal scaling, queues, caching, rate limits, efficient retrieval, quotas, and workload-aware routing.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 2. What is backpressure?

**Model answer:** Slowing, rejecting, or queueing work so downstream dependencies are not overloaded.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 3. What is a circuit breaker?

**Model answer:** Temporarily stopping calls to an unhealthy dependency to avoid cascading failure.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 4. What is graceful degradation?

**Model answer:** Preserving partial functionality or fallback behavior when models, retrieval, or integrations fail.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 5. What can be cached?

**Model answer:** Embeddings, stable retrieval, deterministic tool responses, prompt fragments, and safe repeated answers subject to freshness requirements.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 6. How do you estimate AI cost?

**Model answer:** Tokens, embedding/indexing, search, compute, storage, networking, observability, human review, and third-party integrations.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 7. Why use agent budgets?

**Model answer:** Caps on steps, tools, latency, or spend prevent runaway autonomous behavior.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 8. What is rate limiting?

**Model answer:** Controlling request volume per user, tenant, model, or dependency to protect reliability and cost.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 9. How do you design multi-region AI?

**Model answer:** Regional stateless services, data residency, model availability, index replication, failover, and defined consistency.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 10. How do you handle provider outages?

**Model answer:** Bounded retries, circuit breakers, fallback providers/models, cached or degraded behavior, clear messaging, and alerts.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?
