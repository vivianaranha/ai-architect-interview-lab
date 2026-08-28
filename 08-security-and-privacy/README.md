# Security and Privacy

Use these for study and mock interviews. For every answer, add trade-offs, failure modes, and metrics.

## 1. What is prompt injection?

**Model answer:** An attack where untrusted content attempts to manipulate model behavior or override intended instructions.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 2. How do you defend against prompt injection?

**Model answer:** Treat content as untrusted, isolate instructions, restrict tools, enforce auth server-side, validate outputs, and use least privilege.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 3. What is indirect prompt injection?

**Model answer:** Malicious instructions hidden in documents, websites, email, or tool output that an AI later consumes.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 4. Why are guardrails not authorization?

**Model answer:** Guardrails influence model output; authorization deterministically controls data and actions.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 5. What is least privilege for agents?

**Model answer:** Each agent receives only the minimum tools, scopes, data, and actions required.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 6. How should secrets be managed?

**Model answer:** Secrets manager or managed identity; never expose credentials to prompts, model context, logs, or source code.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 7. How do you reduce data exfiltration risk?

**Model answer:** Context minimization, ACLs, restricted outbound tools, DLP, output review for sensitive flows, logging, and approvals.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 8. What belongs in an AI threat model?

**Model answer:** Assets, actors, trust boundaries, data flows, prompt risks, tool risks, identity, exfiltration, supply chain, abuse cases, and incident controls.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 9. How do you secure vector stores?

**Model answer:** Encryption, network controls, identity, metadata ACL filters, auditing, backups, retention, and deletion propagation.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 10. What is an agent kill switch?

**Model answer:** A control to immediately disable risky agent actions or specific tools during an incident.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?
