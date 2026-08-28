# Model Selection and Routing

Use these for study and mock interviews. For every answer, add trade-offs, failure modes, and metrics.

## 1. How do you select an enterprise LLM?

**Model answer:** Evaluate task quality, latency, context, tool use, structured output, safety, deployment constraints, residency, cost, vendor terms, and operations.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 2. What is model routing?

**Model answer:** Selecting models based on task, complexity, risk, latency, quality, or cost.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 3. What is cascade routing?

**Model answer:** Try a smaller/cheaper model first and escalate to a stronger model when confidence or validation fails.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 4. Should every task use the largest model?

**Model answer:** No. Use the smallest model that reliably satisfies the task requirements.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 5. How do you benchmark models fairly?

**Model answer:** Same representative dataset, comparable prompts and interfaces, and measurement of quality, latency, reliability, safety, and cost.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 6. Where does traditional ML still fit?

**Model answer:** Structured prediction, forecasting, anomaly detection, ranking, and classification where conventional models may be more efficient and controllable.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 7. When would you use a local model?

**Model answer:** Privacy, offline operation, data residency, predictable cost, low latency, customization, or control requirements.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 8. What is model fallback?

**Model answer:** Switching to an alternate model when the primary fails, is unavailable, rate-limited, too slow, or fails validation.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 9. What is model version risk?

**Model answer:** Behavior can change across versions; use regression suites, monitoring, version pinning where possible, and rollback.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 10. What belongs in a model scorecard?

**Model answer:** Accuracy, structured-output reliability, hallucination, safety, latency, cost, tool use, robustness, context performance, and availability.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?
