# AI Architecture Foundations

Use these for study and mock interviews. For every answer, add trade-offs, failure modes, and metrics.

## 1. What is the primary responsibility of an AI architect?

**Model answer:** Translate business goals into secure, scalable, governed AI systems spanning workflow, data, models, APIs, infrastructure, evaluation, operations, and cost.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 2. How is an AI architect different from an AI engineer?

**Model answer:** An engineer commonly implements components; an architect owns system boundaries, nonfunctional requirements, integration strategy, trade-offs, governance, and evolution.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 3. What should you clarify before proposing architecture?

**Model answer:** Users, business objective, current workflow, success metrics, data, sensitivity, latency, availability, volume, integrations, budget, compliance, and human approval.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 4. Why start with workflow instead of model choice?

**Model answer:** The model is only one component. Starting with workflow prevents technology-first overengineering and reveals whether AI is actually needed.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 5. When should you not use generative AI?

**Model answer:** When deterministic rules, search, SQL, analytics, or traditional ML solve the problem more reliably, cheaply, and explainably.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 6. What are nonfunctional requirements?

**Model answer:** Qualities such as latency, scalability, security, privacy, reliability, availability, explainability, maintainability, and cost.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 7. How do you choose build vs buy vs hybrid?

**Model answer:** Compare differentiation, time-to-value, control, integration, risk, skills, cost, lock-in, governance, and exit strategy.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 8. What does production readiness mean for AI?

**Model answer:** Repeatable deployment, versioning, monitoring, evaluation, security, rollback, data governance, failure handling, cost controls, auditability, and ownership.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 9. Why are AI systems probabilistic architectures?

**Model answer:** Outputs can vary and fail non-deterministically, so validation, confidence handling, human review, guardrails, evaluation, and recovery are architectural requirements.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 10. What artifacts should an AI architect create?

**Model answer:** Context and component diagrams, data flow, trust boundaries, API contracts, model strategy, ADRs, evaluation plan, cost model, deployment topology, and runbook.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?
