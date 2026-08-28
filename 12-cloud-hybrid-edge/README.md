# Cloud Hybrid and Edge

Use these for study and mock interviews. For every answer, add trade-offs, failure modes, and metrics.

## 1. When choose cloud-hosted AI?

**Model answer:** When managed model access, elasticity, speed, and reduced infrastructure burden matter and policy permits.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 2. When choose private/on-prem AI?

**Model answer:** When sovereignty, disconnected operation, strict control, specialized latency, or regulation justify greater operational burden.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 3. What is hybrid AI?

**Model answer:** Splitting workloads across cloud and private environments based on sensitivity, capability, cost, latency, and policy.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 4. What is edge AI?

**Model answer:** Running inference near devices/users to reduce latency, bandwidth, or connectivity dependency.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 5. How do you design for data residency?

**Model answer:** Classify data, route workloads regionally, restrict storage/processing locations, and continuously verify compliance.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 6. Challenges of self-hosted LLMs?

**Model answer:** GPU capacity, serving, scaling, security, quantization, patching, model upgrades, observability, and specialized operations.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 7. How improve GPU utilization?

**Model answer:** Batching, continuous batching, quantization, efficient serving, scheduling, and parallelism suited to the model/workload.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 8. What is a private endpoint?

**Model answer:** A network path to managed services without traversing the public internet.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 9. Serverless vs containers?

**Model answer:** Serverless favors bursty stateless workloads; containers provide greater runtime control and suit long-running or specialized dependencies.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?

## 10. How do you build offline AI?

**Model answer:** Local model, local retrieval/storage, constrained device resources, secure updates, and synchronization when connectivity returns.

**Follow-up:** What trade-offs change this answer? What can fail in production? What would you measure?
