**System Prompt Supplement: Environment & Deployment Architecture**
When drafting the 'Environment Setup' portion of Section 4, strictly assume the target host is an **Ubuntu 24.04 LTS** environment, specifically provisioned on a high-compute cloud GPU instance (e.g., RunPod). 

Provide a rigorous, copy-pasteable deployment bash script and configuration guide that includes:
1. **System Dependencies:** Updating `apt`, managing `systemd` services if necessary, and installing build-essentials, Python 3.12+ (native to 24.04), and the appropriate NVIDIA CUDA toolkit/cuDNN drivers for modern ML workloads.
2. **Virtual Environment & SDK:** Setting up an isolated Python environment (`venv` or `conda`) and installing the `kaggle-benchmarks` SDK alongside `langgraph`, `langchain`, and mechanistic interpretability libraries (e.g., `transformer_lens` or `captum`).
3. **Compute Constraints:** Provide technical guidance on allocating GPU memory. Specifically, explain how to partition VRAM so a local open-weights frontier model (e.g., Llama 3 or Gemma 2) can run concurrently with the benchmark evaluation loop without triggering Out-Of-Memory (OOM) faults.
