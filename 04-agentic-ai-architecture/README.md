# Agentic AI Architecture

Use these for study and mock interviews. For every answer, add trade-offs, failure modes, and metrics.

## 1. What makes a system agentic?

**Model answer:** It can decide actions, select tools, maintain state, iterate, and adapt a plan rather than only producing a single response.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 2. What risks grow with agent autonomy?

**Model answer:** Incorrect actions, runaway loops, excess cost, unauthorized tool use, data leakage, inconsistent state, and difficult incident response.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 3. What is planner-executor architecture?

**Model answer:** A planner decomposes goals while executors carry out steps, separating reasoning about work from action execution.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 4. When should you use multiple agents?

**Model answer:** When responsibilities have distinct tools, policies, contexts, owners, or evaluation criteria—not merely because multi-agent is fashionable.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 5. What is a supervisor-agent pattern?

**Model answer:** A supervisor interprets the request, delegates to specialists, tracks progress, and synthesizes results.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 6. How do you prevent infinite loops?

**Model answer:** Maximum steps, explicit stopping conditions, budgets, progress checks, duplicate-action detection, and human escalation.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 7. How do you secure tool-using agents?

**Model answer:** Least privilege, server-side authorization, strict schemas, allowlists, input validation, sandboxing, approvals, and audit logs.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 8. What state should an agent persist?

**Model answer:** Only state required for continuity or personalization, with retention rules; separate transient working memory from durable business records.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 9. How do you evaluate agents?

**Model answer:** Task completion, tool selection, argument accuracy, policy compliance, step efficiency, recovery behavior, latency, cost, and user outcomes.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 10. What is human-in-the-loop design?

**Model answer:** Human review or approval at defined risk points such as external communication, destructive actions, financial commitments, or low-confidence decisions.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?
