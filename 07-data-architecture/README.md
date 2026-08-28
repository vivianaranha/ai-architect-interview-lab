# Data Architecture

Use these for study and mock interviews. For every answer, add trade-offs, failure modes, and metrics.

## 1. What data is unique to GenAI systems?

**Model answer:** Prompts, context, embeddings, model outputs, feedback, conversation history, traces, and derived knowledge.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 2. What is AI data lineage?

**Model answer:** Tracking source, transformations, versions, model/prompt usage, and downstream outputs.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 3. How should embeddings be governed?

**Model answer:** As derived data that may encode sensitive information: access control, encryption, retention, deletion, and tenant boundaries still apply.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 4. How do you handle PII in prompts?

**Model answer:** Minimize, redact where possible, enforce purpose limitation, use approved providers, encrypt, and avoid unnecessary logging or retention.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 5. What is a feature store?

**Model answer:** A managed system to create, version, store, and serve ML features consistently for training and inference.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 6. How do you prevent stale data?

**Model answer:** Freshness metadata, source timestamps, cache TTLs, index versions, freshness SLAs, and explicit stale-data behavior.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 7. What is schema evolution?

**Model answer:** Managing data-format changes while preserving compatibility between producers and consumers.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 8. How should conversation history be stored?

**Model answer:** Separate durable records from temporary context, store only what is needed, and apply retention/deletion and access policies.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 9. When should AI query a DB directly?

**Model answer:** Prefer a governed semantic/service layer; tightly controlled read-only analytics may be acceptable with strict schemas and authorization.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 10. Why is metadata important?

**Model answer:** It enables filtering, authorization, provenance, freshness, lineage, ownership, and better retrieval.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?
