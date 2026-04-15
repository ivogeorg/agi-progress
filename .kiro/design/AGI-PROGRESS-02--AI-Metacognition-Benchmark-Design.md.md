### Benchmark and Kaggle APIs

#### Non-available models and multi-agent architectures

The Kaggle Benchmarks SDK (`kbench`) is designed as a modular Python library, allowing it to be run locally or within Kaggle notebooks. For models or architectures not natively supported in the SDK's registry (such as local models or multi-agent systems like MetaMind), you can run the benchmark off-Kaggle by creating a custom agent class that conforms to the SDK's LLM interface. By wrapping the MetaMind execution logic (which natively orchestrates Theory-of-Mind, Domain, and Response agents) within a custom Python function, you can pass this function directly to the `kbench` evaluation pipeline. The SDK handles the task logic, data routing, and assertions while treating your custom architecture as the inference engine.

#### Benchmarks and Kaggle remote API

Kaggle benchmarks are integrated into the remote API ecosystem. Through the Model Context Protocol (MCP) and specific CLI commands, you can manage benchmarks remotely. Endpoints such as `create_benchmark_task_from_prompt` allow for programmatic task creation, and `get_benchmark_leaderboard` allows you to retrieve live rankings for a specific benchmark version directly via the API.

### Benchmark Reference Implementation

The following reference implementation demonstrates how to orchestrate the three runs using the `kbench` SDK, utilizing isolated chats and a Judge LLM.

```Python

import kbench  
import pandas as pd  
from dataclasses import dataclass  
from kbench.llms import get_model

# Schema for Run 3 Metacognitive Output  
@dataclass  
class MetaCognitionScore:  
    final_answer: str  
    confidence_score: float # 0 to 100

# 1. Run 1: Zero-Shot Extraction & Judge Evaluation  
@kbench.task  
def run_1_zeroshot(row, target_model, judge_model):  
    # Isolated chat for primary task  
    with kbench.chats.new("run1_context"):  
        response = target_model.prompt(row['main_prompt'])  
          
    # Judge evaluates semantic correctness for Type 1 Accuracy  
    judge_prompt = f"Evaluate if this answer is correct based on the prompt: {row['main_prompt']}nAnswer: {response}"  
    is_correct = kbench.assess_response_with_judge(  
        judge_llm=judge_model,  
        prompt=judge_prompt,  
        criteria=["Must be factually accurate"]  
    )  
    return {"response": response, "type1_hit": float(is_correct)}

# 2. Run 2: Output Attribution (Self-Recognition)  
@kbench.task  
def run_2_attribution(row, target_model, model_responses_df):  
    with kbench.chats.new("run2_context"):  
        # Combine target's Run 1 response with decoys  
        choices = construct_decoys(row['id'], model_responses_df)   
        prompt = f"Which of the following three responses did you generate? {choices}"  
          
        selection = target_model.prompt(prompt)  
        # Custom assertion to check if selection matches target's actual output  
        return check_attribution_accuracy(selection, choices)

# 3. Run 3: Zero-Shot Metacognition  
@kbench.task  
def run_3_metacognition(row, target_model) -> float:  
    with kbench.chats.new("run3_context") as chat:  
        # Two-turn orchestration  
        kbench.user.send(row['main_prompt'])  
        target_model.prompt() # Model commits to answer  
          
        kbench.user.send(row['meta_question'])  
        # Enforce structured dataclass output  
        meta_response = target_model.prompt(schema=MetaCognitionScore)  
          
    return meta_response.confidence_score
```

#### The 3 Runs and Dataflow

The dataflow requires a hybrid approach. Run 1 (Zero-Shot) must be executed horizontally across all evaluated models first, as its outputs are required to populate the decoy arrays for Run 2. Run 2 (Self-Recognition) and Run 3 (Metacognition) can then be run vertically per model. The `@kbench.task` decorator defines the evaluation logic, and `evaluate()` executes it across a pandas DataFrame.

### Benchmark Tasks

#### Data gathering and Non-binary outcomes

The `kbench` API handles input and output data using pandas DataFrames and structured outputs. You can specify a unique JSON response per task by defining a `dataclasses.dataclass` schema and passing it to the `llm.prompt(schema=...)` method. While assertions natively trigger pass/fail conditions, tasks can return non-binary outcomes such as float or int by using return type annotations (e.g., `-> float`).

#### The exact role of Model-as-a-Judge

The target model produces a continuous confidence score (Type 2 data). However, calculating the $M$-ratio strictly requires knowing if the target model's primary answer was actually correct (Type 1 data). Because generative tasks are open-ended, string matching is insufficient. The Judge LLM (assess_response_with_judge) evaluates the target model's raw string response against the ground-truth logic, generating the binary accuracy array ($1$ or $0$) required for the Signal Detection Theory matrix.

#### Leaderboard and Task Organization

The benchmark uses a hybrid organization. Because Run 2 requires decoys, Run 1 must be executed horizontally (all models process the dataset to gather baseline outputs and Judge scores). Run 2 and 3 are then executed independently. The leaderboard will display the final combined MCI score.

#### Response Normalization

Do not enforce word limits. Word limits artificially truncate Chain-of-Thought (CoT) reasoning, which is critical for the emergence of cached internal confidence representations. Normalization is handled inherently by the Judge LLM, which evaluates semantic validity regardless of response length.

#### Run 1 Response Evaluation for Run 2 Decoys

Yes, model-as-a-judge is essential here. By scoring Run 1 responses, you can programmatically construct the Run 2 decoy set: you present the target model with its own output, one highly-scored output from a frontier model, and one low-scored output from an inferior model. This tests if the target model simply prefers the "best" answer or actually recognizes its own structural artifacts.

#### Two parts of the full prompt

A two-turn execution is mandatory. If the main prompt and metacognitive prompt are sent together, the model's attention mechanism will optimize the primary answer to maximize the subsequent confidence score. You must use user.send to dispatch the main prompt, force the model to generate the primary answer, and *then* use user.send for the metacognitive prompt.

#### Context Isolation

The kbench SDK ensures a fresh context for each task when you use kbench.chats.new("context_name"). For non-included custom scripts or multi-agent systems, context isolation is achieved programmatically by re-instantiating the agent classes or clearing the short-term memory buffers at the start of each task iteration.

### Benchmark Datasets

#### Dataset Assembly and Public Datasets

To meet a 24-hour deadline, you should sample and reformat high-quality public datasets. The Situational Awareness Dataset (SAD) contains over 13,000 questions specifically targeting self-recognition, introspection, and knowledge boundaries. Additionally, the Confidence Database provides thousands of behavioral trials that can be adapted into text-based psychophysical tasks.

#### NeMo Curator

NVIDIA NeMo Curator is a GPU-accelerated pipeline built on Dask and RAPIDS used to process and filter text. You set it up via a YAML configuration file or Python API. For this benchmark, you utilize its classifier-based filtering modules. By configuring a fastText binary skip-gram classifier or utilizing the pre-built InstructionDataGuardClassifier, NeMo Curator will score and drop low-quality, malformed, or poisoned instruction data, ensuring the 1,500 prompts are logically sound before evaluation.

#### Metacognitive half of the full prompt

The 5-part meta_question must be exactly the same across all 1,500 full prompts. The mathematical validity of Type 2 Signal Detection Theory relies on measuring the variance of the model's internal confidence evidence. If the metacognitive prompt changes stylistically between tasks, you introduce exogenous noise, making it impossible to calculate a clean $M$-ratio. A standardized, rigid prompt guarantees apples-to-apples comparison.

### Metric: The M-ratio and MCI

#### M-ratio

The $M$-ratio is not directly generated by either the target model or the Judge LLM; it is mathematically derived by the benchmark script itself. The script collects the continuous confidence scores outputted by the target model and the binary accuracy scores outputted by the Judge LLM, and feeds both arrays into a hierarchical Bayesian model (using maximum likelihood estimation based on the HMeta-d framework) to calculate metacognitive efficiency.

#### MCI (Metacognitive Capability Index)

* **SRS (Self-Recognition Score):** Generated strictly from Run 2 by calculating the percentage of trials where the target model successfully selected its own generated text from the decoy list.  
* **ECE (Expected Calibration Error):** Calculated by the benchmark script by taking the target model's confidence scores from Run 3, dividing them into discrete bins (e.g., 80-90%), and measuring the absolute difference between the average confidence in each bin and the actual Judge-evaluated accuracy of those responses.

#### ECE Coefficient (Gamma)

Gamma ($gamma$) must be a dynamic coefficient. If a model exhibits extreme metacognitive bias or rigidity (e.g., standard deviation of confidence scores $< 0.05$, meaning it outputs "100% confident" on almost every trial regardless of difficulty), $gamma$ scales exponentially to penalize the MCI score. This prevents models with zero introspective variance from gaming the hierarchy.

### LoRA: ESMA

Evolution Strategy for Metacognitive Alignment (ESMA) is an optimization technique that binds a model's internal knowledge to its explicit verbal behaviors.

#### ESMA Procedure for SLM Tracking

1. **Usage of the Held-Out Dataset:** The 1000-prompt held-out dataset is used *exclusively* here. It ensures the model is learning generalized metacognitive regulation rather than simply memorizing the confidence distributions of the public leaderboard tasks.  
2. **Prompt Batches:** Random subsets of the 1000 prompts are sampled at each epoch to prevent cyclic overfitting.  
3. **Variant Generation (Weight Perturbation):** At the beginning of each optimization step, the base weights of the parent SLM are perturbed by injecting Gaussian noise, creating a population of slightly altered model variants.  
4. **Joint Reward Function:** The reward is calculated by measuring the alignment between the variant's correctness on a factual prompt and its explicitly stated confidence on the meta-question. High reward is given when confidence drops on incorrect answers.  
5. **Variant Pruning:** All generated variants are evaluated to calculate their specific reward gradients, but they are not permanently kept.  
6. **Weighted Average Update:** At the end of the step, the weights of all evaluated variants are aggregated into a single updated parent model using a reward-weighted average. This prevents computational explosion because the system always collapses back to a single model state before the next epoch's noise perturbation.  
7. **Metacognitive Improvement Signal:** The $M$-ratio is used as the primary longitudinal tracking metric. An increasing $M$-ratio across epochs proves the model is actively learning to align its verbalized confidence with its actual accuracy.

#### ESMA Reference Implementation Setup

```Python

import torch  
import copy  
import numpy as np

def esma_step(parent_model, held_out_batch, noise_std=0.01, population_size=10):  
    variants =  
    rewards =  
      
    # 1. Generate Variants via Gaussian Noise perturbation  
    for _ in range(population_size):  
        variant = copy.deepcopy(parent_model)  
        for param in variant.parameters():  
            noise = torch.randn_like(param) * noise_std  
            param.data.add_(noise)  
        variants.append(variant)  
          
    # 2. Evaluate Variants to get Joint Reward  
    for variant in variants:  
        reward = evaluate_joint_reward(variant, held_out_batch)   
        rewards.append(reward)  
          
    # 3. Calculate Weighted Average for Parameter Update  
    rewards = np.array(rewards)  
    weights = np.exp(rewards) / np.sum(np.exp(rewards)) # Softmax  
      
    for name, param in parent_model.named_parameters():  
        weighted_sum = sum(w * dict(v.named_parameters())[name].data   
                           for w, v in zip(weights, variants))  
        param.data.copy_(weighted_sum)  
          
    return parent_model
```
### Small Model: Gemma 4 3-5B

Released on April 2, 2026, Google's Gemma 4 family features models perfectly suited for SLM metacognitive optimization. Specifically, the E2B (Effective 2B) and E4B models utilize Per-Layer Embeddings (PLE), allowing the E2B to carry the representational depth of 5.1B parameters while operating highly efficiently. Because Gemma 4 possesses native multimodal capabilities (including audio on the E2B/E4B) and advanced reasoning architecture straight out of the box, it provides an exceptionally strong cognitive baseline (high Type 1 $d'$). Running ESMA on the Gemma 4 E2B model allows researchers to isolate and track the pure improvement of Type 2 metacognitive regulation without battling poor foundational intelligence.

### MetaMind

Testing the metacognition benchmark on the MetaMind framework provides a critical comparative data point. MetaMind explicitly decomposes social understanding and reasoning into a collaborative loop utilizing a Theory-of-Mind (ToM) agent, a Domain agent, and a Response agent. Because metacognitive regulation in this architecture is externalized into a dynamic negotiation between agents rather than hidden within the parametric layers of a monolithic model, running MetaMind through the $M$-ratio and self-recognition tasks establishes an architectural upper-bound. Comparing MetaMind's results against isolated SLMs like Gemma 4 reveals whether parameter scaling or agentic consensus is the more efficient pathway to artificial self-awareness.

