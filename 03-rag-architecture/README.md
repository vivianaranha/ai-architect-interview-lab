# RAG Architecture

Use these for study and mock interviews. For every answer, add trade-offs, failure modes, and metrics.

## 1. Why use RAG?

**Model answer:** To ground answers in private, current, or large knowledge sources, improve provenance, and support citations.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 2. What are the main RAG stages?

**Model answer:** Ingestion, parsing, normalization, chunking, metadata, embedding, indexing, query transformation, retrieval, reranking, context assembly, generation, evaluation.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 3. How do you choose chunking?

**Model answer:** Base it on document semantics and retrieval tasks, then compare approaches using a retrieval evaluation set.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 4. What is hybrid search?

**Model answer:** Combining semantic vector retrieval with lexical search such as BM25 to improve recall for both meaning and exact terms.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 5. Why use reranking?

**Model answer:** Initial retrieval optimizes recall and speed; reranking improves precision among candidate passages.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 6. How do you enforce document permissions?

**Model answer:** Apply identity-aware ACL filters before content enters model context. Authorization must not rely on model behavior.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 7. How do you evaluate RAG?

**Model answer:** Retrieval recall/precision, answer correctness, faithfulness, citation quality, task success, latency, and cost.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 8. What causes poor RAG answers?

**Model answer:** Bad parsing, weak chunking, stale indexes, poor metadata, low recall, irrelevant retrieval, too much context, ambiguity, or weak prompting.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 9. What is query rewriting?

**Model answer:** Transforming user language into retrieval-oriented queries that improve recall or add missing domain terminology.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 10. How do you keep RAG current?

**Model answer:** Incremental ingestion, source-change detection, versioning, deletion propagation, timestamps, and event- or schedule-driven reindexing.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?
