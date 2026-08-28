# LLM and GenAI Architecture

Use these for study and mock interviews. For every answer, add trade-offs, failure modes, and metrics.

## 1. What are core components of an enterprise LLM app?

**Model answer:** Experience layer, orchestration, prompt management, model gateway, retrieval/tools, identity, policy controls, observability, evaluation, and enterprise integrations.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 2. What is a model gateway?

**Model answer:** A stable abstraction over model providers that can handle auth, routing, quotas, retries, policy, logging, cost, and fallback.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 3. Why avoid hard-coding one LLM provider?

**Model answer:** Models change rapidly in quality, price, availability, terms, and capabilities. Abstraction reduces lock-in and enables routing and fallback.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 4. Why is structured output important?

**Model answer:** Schema-constrained output improves validation, downstream automation, integration reliability, and predictable error handling.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 5. When should you use a smaller model?

**Model answer:** For constrained classification, extraction, routing, summarization, or transformation tasks when it meets quality targets at lower latency and cost.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 6. What is production prompt management?

**Model answer:** Treat prompts as versioned assets with ownership, testing, metadata, deployment control, rollback, and evaluation.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 7. How do you reduce LLM latency?

**Model answer:** Smaller models, less context, caching, parallel independent calls, streaming, efficient retrieval, and fewer model hops.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 8. How do you reduce LLM cost?

**Model answer:** Model routing, smaller models, token budgets, caching, context compression, prompt optimization, batching, and deterministic tools where appropriate.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 9. What is context-window management?

**Model answer:** Selecting and compressing only the information needed for the task while avoiding irrelevant memory and overflow.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 10. How do you design model-provider failover?

**Model answer:** Provider adapters, common schemas, bounded retries, health checks, circuit breakers, fallback models, and regression evaluation of fallback behavior.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?
