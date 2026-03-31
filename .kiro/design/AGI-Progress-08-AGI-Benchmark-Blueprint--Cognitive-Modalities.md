# **Empirically Measuring Progress Toward AGI: A Mechanistic and Cognitive Blueprint**

### **Section 1: Foundations of AGI, Reasoning, and Measurement**

#### **Conceptual Distinctions in Cognitive Architectures**

The pursuit of Artificial General Intelligence (AGI) necessitates a rigorous and fundamental differentiation between the architecture of biological cognition and the topologies of current frontier machine learning models. Human cognition is characterized by a parallel, highly recurrent, and dynamically neuromodulated biological neural network. It operates through continuous sensorimotor grounding, leveraging neuroplasticity to adapt in real-time to novel stimuli without suffering from catastrophic forgetting. Biological reasoning is intrinsically neuro-symbolic; it fluidly integrates rapid, associative pattern recognition—often referred to as System 1 thinking—with slow, deliberate, rule-based logical deduction, known as System 2 thinking.1 This neuro-symbolic integration is orchestrated by a central executive control mechanism localized within the prefrontal cortex, which governs metacognitive monitoring and inhibitory control.1

Conversely, current frontier artificial intelligence architectures, predominantly Autoregressive Large Language Models (LLMs) and Small Language Models (SLMs), rely on feed-forward Transformer topologies characterized by static weights post-training. These models process discrete token sequences through layered self-attention mechanisms, predicting the next optimal token based on vast, compressed pre-training distributions.3 While they exhibit emergent reasoning capabilities, their architecture lacks genuine recurrence and persistent internal state outside of their localized context windows. They do not "reason" in a continuous, time-extended biological sense; rather, they execute highly sophisticated, multi-layered pattern matching driven by induction heads and localized circuit activation.3 The algorithmic pathway is Markovian, relying entirely on the visible context rather than an evolving, internal semantic state. Consequently, assessing progression toward AGI requires evaluating not merely the statistical accuracy of an output, but the underlying mechanical processes and internal representations driving the generation of that output.

#### **Scientific Measurement: Black-Box Evaluation vs. Mechanistic Interpretability**

The standard paradigm for evaluating artificial intelligence capabilities relies heavily on black-box, end-to-end benchmarking. In this approach, a model is presented with a prompt, and its final output is evaluated against a ground-truth dataset or assessed by an algorithmic or LLM-based Judge.6 While useful for broad capability assessments and consumer-facing leaderboards, black-box testing is fundamentally inadequate for measuring true cognitive progress toward AGI. It is highly susceptible to data contamination and the "Clever Hans" effect, where models exploit statistical shortcuts, spurious correlations, or artifacts in the prompt rather than executing genuine algorithmic reasoning.7 Furthermore, black-box evaluation cannot differentiate between a model that is engaging in sophisticated self-monitoring and one that has simply memorized a highly correlated output sequence from its training data.7

To rigorously assess cognitive abilities, the scientific method must pivot toward Mechanistic Interpretability (MI), often referred to as "white-box" evaluation.7 Mechanistic Interpretability treats neural networks as reverse-engineerable computational systems, seeking to identify the precise sub-graphs, attention heads, and multi-layer perceptron (MLP) neurons responsible for specific cognitive behaviors.9 By analyzing the internal continuous representations of a model, researchers can open the black box and trace the causal flow of information. This enables evaluators to differentiate definitively between an LLM that has memorized a training example and one that has internalized a generalizable, abstract algorithm. White-box methods leverage techniques such as activation patching and representation engineering to probe the latent space of the model, ensuring that the benchmark measures structural cognitive capacity rather than mere stochastic mimicry.7

#### **Grokking and Loss Metrics as Cognitive Progress Bars**

A critical phenomenon demonstrating the shift from mere data memorization to genuine algorithmic comprehension is "grokking." Grokking is a training dynamic where a neural network, after prolonged training significantly past the point of overfitting on the training data, suddenly develops the ability to generalize perfectly to unseen validation data.11 This phase transition marks the mathematical formation of a robust, generalizable cognitive circuit out of previously entangled, memorized weights. Mechanistic analyses of small models trained on algorithmic tasks, such as modular addition, reveal that training dynamics during grokking are strictly delineated into three distinct phases: Memorization, Circuit Formation, and Cleanup.11

To explicitly track these phases—serving as a far more accurate "progress bar" for cognitive capability than standard test accuracy—researchers utilize two specialized, mechanistically-derived loss metrics: Restricted Loss and Excluded Loss.11

During the evaluation of algorithmic tasks, the model's logits can be decomposed using discrete Fourier transforms to identify the specific frequency basis (e.g., ![][image1]) that corresponds to the generalizable mathematical solution, effectively isolating the sub-network responsible for true reasoning.12 Let the complete model parameter space or logit output be represented as ![][image2], and suppose through mechanistic analysis, the specific subspace corresponding to the generalizable algorithmic solution is isolated as ![][image3].

**Restricted Loss (![][image4])** isolates the performance of the generalizing algorithm. It is computed by artificially restricting the network's activations strictly to the representation space of the general solution, nullifying the impact of the memorizing circuits.13 Mathematically, if ![][image5] is the forward pass, we restrict the intermediate MLP activations to the localized circuit:

![][image6]  
During the Circuit Formation phase, ![][image4] begins to steadily and predictably decline long before the overall test loss improves.16 This provides benchmark architects with early, empirical evidence that the model is actively constructing a cognitive abstraction in its latent space, even while its external black-box test accuracy remains close to random chance.

**Excluded Loss (![][image7])** represents the mathematical inverse of restricted loss. It tracks the performance of the network when the generalizing solution ![][image3] is surgically ablated, forcing the model to rely entirely on its memorizing circuits.13

![][image8]  
When measured over the training data, ![][image7] initially drops during the early Memorization phase. However, as the network transitions into the Circuit Formation and Cleanup phases, ![][image7] sharply rises.12 This occurs because weight decay regularization (such as ![][image9] penalties) begins to prune the heavily parameterized memorization circuits, favoring the parameter-efficient general solution.12

By continuously monitoring the divergence between ![][image4] and ![][image7] during a white-box evaluation, benchmark architects can empirically verify whether a model has "grokked" a specific cognitive modality, ensuring that the model is executing true algorithmic logic rather than relying on high-dimensional data retrieval.

### ---

**Section 2: Deep Dive into the 5 Cognitive Modalities**

The Kaggle and Google DeepMind hackathon targets five primary cognitive modalities fundamental to measuring AGI progression.18 A rigorous, exhaustive analysis of the biological basis, mechanistic measurement, multi-agent applicability, and multimodal stress-testing parameters of each is required to establish highly robust evaluation frameworks.

#### **Modality I: Learning**

**Definition & Cognitive Science Basis:**

In human cognition and biological systems, learning is defined as the acquisition, encoding, consolidation, and retrieval of novel knowledge, behaviors, or skills through experience, study, or instruction. Biologically, this is driven by synaptic plasticity, specifically long-term potentiation (LTP) and long-term depression (LTD), which physically alter the connectivity strength between neurons in response to stimulus frequency and intensity. Human learning encompasses both rapid, episodic encoding (storing specific events via the hippocampus) and slow, semantic consolidation (integrating events into generalized world knowledge in the neocortex). It is a continuous, non-destructive process.

**Mechanistic Machine Measurement:** Machine learning, specifically in the context of few-shot prompting and in-context learning within autoregressive models, does not involve persistent weight updates. Instead, it is driven mechanically by "Induction Heads." These are specialized self-attention configurations that operate by searching the preceding context for a token similar to the current one and copying the token that followed it previously, thereby establishing an ad-hoc, localized rule.3 To surgically measure learning beyond simple accuracy, Sparse Autoencoders (SAEs) must be utilized. Neural networks suffer from superposition, where single, polysemantic neurons represent multiple unrelated concepts simultaneously.20 SAEs factorize these polysemantic, entangled neuron activations into a high-dimensional, sparse linear combination of highly interpretable feature vectors.2 By projecting intermediate layer activations through a trained SAE during a few-shot learning benchmark, evaluators can measure the exact velocity and clarity with which a novel concept's feature vector solidifies across subsequent context layers, quantifying the model's true in-context learning bandwidth.

**Multi-Agentic Swarm Applicability:** Within a LangGraph multi-agent framework, learning is operationalized through stateful memory persistence across distributed agent nodes.22 Because individual agents lack continuous weight updates, the "learning" of the system resides in the dynamic evolution of the graph's shared state dictionary. A benchmark evaluating swarm learning would measure the system's ability to update a shared knowledge graph dynamically. If a specialized "Researcher Agent" encounters novel, contradictory information, the benchmark measures the efficiency and accuracy with which this new data alters the subsequent decision-making topology and routing logic of a downstream "Planner Agent".24 High swarm learning is indicated by rapid state consensus without generating infinite cyclic loops.

**Multimodal Stress-Testing:** Cognitive load dynamically alters biological learning efficiency and capacity. To evaluate machine learning under equivalent stress, benchmarks must inject continuous, drifting multimodal data streams. Utilizing frameworks like the MATB-II or the CLARE dataset methodology, models can be fed synthetic physiological sensor telemetry, such as continuous Electrocardiography (ECG), Electrodermal Activity (EDA), or raw photoplethysmography (PPG) matrices.25 Forcing the model to integrate this high-frequency temporal data while attempting to learn a new semantic rule tests whether the model can extract reliable episodic rules while actively suppressing the immense noise of high-dimensional sensor variance.25

#### **Modality II: Metacognition**

**Definition & Cognitive Science Basis:** Metacognition is fundamentally defined as "thinking about thinking." It represents the higher-order executive awareness of one's own cognitive processes. In humans, it encompasses internal monitoring—assessing subjective confidence, recognizing the boundaries of one's own knowledge, and detecting cognitive dissonance—and cognitive control, which involves strategically shifting approaches, re-allocating attention, or halting an action when an error is internally detected.29 This capacity is deeply intertwined with the prefrontal cortex and is essential for autonomous, reliable operation in uncertain environments.

**Mechanistic Machine Measurement:** Standard behavioral tests of LLM metacognition, such as asking a model "Are you sure?", are heavily contaminated by instruction fine-tuning and often reflect sycophancy rather than true internal monitoring.30 The "Logit Lens" technique is paramount for isolating genuine metacognitive circuits.20 By taking the intermediate residual stream activations at various depths within the Transformer and projecting them directly into the output vocabulary space using the final unembedding matrix, evaluators can map exactly how a model's prediction confidence evolves layer by layer. If an LLM demonstrates genuine metacognitive monitoring, it will exhibit specialized activation patterns that accurately signal uncertainty internally before generating an output.30 A benchmark can measure the divergence between the model's intermediate logit confidence and its final generated text; a failure in these internal monitoring circuits directly correlates with systemic hallucinations and a breakdown in cognitive control.34

**Multi-Agentic Swarm Applicability:** LangGraph naturally facilitates the structural emulation of metacognition via hierarchical routing and supervised oversight.22 A "Supervisor Agent" can be explicitly instantiated to dynamically monitor the intermediate outputs, reasoning traces, and tool-calling decisions of specialized worker nodes (e.g., a "Reasoner" and a "Validator").24 By applying conditional edges based on the Supervisor's internal confidence metrics and semantic validation, the swarm exhibits emergent metacognitive control. An effective benchmark would introduce a subtle cascading logic error into a worker's context and measure the exact number of graph steps required for the Supervisor to recognize the semantic inconsistency, halt the compounding error loop, and force a state rollback.24

**Multimodal Stress-Testing:** Metacognition can be highly stressed multimodally by introducing deliberate, contradictory data streams that induce cognitive dissonance. For example, a benchmark might provide text asserting that a patient or system is perfectly stable, while simultaneously feeding real-time EDA or remote PPG sensor streams indicating severe, escalating physiological deterioration.25 A metacognitively robust model must recognize the deep discrepancy between modalities, lower its internal confidence regarding the text-based premise, and dynamically prioritize the raw telemetry, ultimately generating a self-corrective explanation that acknowledges its own initial uncertainty.

#### **Modality III: Attention**

**Definition & Cognitive Science Basis:**

Biological attention is the behavioral and cognitive process of selectively concentrating on a discrete aspect of information, whether subjective or objective, while ignoring other perceivable but irrelevant information. It is categorized into sustained attention (vigilance over time), divided attention (multitasking), and selective attention (focusing amidst distractors). It is a finite cognitive resource tightly regulated by neuromodulators, dictating which sensory inputs cross the threshold into working memory for conscious processing.

**Mechanistic Machine Measurement:** Unlike biological attention, machine attention is mathematically explicit, defined via the Transformer architecture's query, key, and value (![][image10]) matrices, which compute a probability distribution over the context window.3 Mechanistic evaluation of attention utilizes "Path Patching," also known as causal mediation analysis.8 This technique involves freezing specific attention heads, swapping intermediate activations between parallel forward passes, and tracing their direct, causal impact on the final output distribution. Benchmarking attention requires mapping whether the model correctly routes information through specialized circuits, such as "previous token heads" and "factual recall heads," particularly when the context window is flooded with adversarial, syntactically similar distractors designed to hijack the key-value matching process.4

**Multi-Agentic Swarm Applicability:** In distributed multi-agent architectures, attention manifests as the correct and precise state extraction from the global LangGraph State dictionary.23 A multi-agent attention failure occurs when an agent hallucinates context from a previous, unrelated conversational turn stored deep within the graph's memory structure, or when it attends to the output of an irrelevant tool. Evaluating this requires constructing complex message-passing topologies where critical operational keys are hidden within massive, continuously updating graph states, testing whether individual agents maintain selective attention purely on the variables relevant to their specific node function.

**Multimodal Stress-Testing:** Biological attention is heavily taxed by visual occlusion, scene complexity, and continuous spatial data. By requiring a model to parse high-resolution, real-time computer vision matrices alongside dense, continuous textual instructions, evaluators can track if the model maintains sustained attention on critical temporal events. For example, evaluating whether a Vision-Language Model (VLM) can track a specific target across hundreds of video frames while simultaneously answering complex logical queries, without its attention maps diluting or succumbing to catastrophic distraction.28

#### **Modality IV: Executive Functions**

**Definition & Cognitive Science Basis:** Executive functions encompass a suite of higher-order cognitive processes necessary for the cognitive control of behavior. These primarily include working memory (holding and manipulating information), cognitive flexibility (shifting perspectives or rules), planning (goal-directed sequence generation), and most critically, inhibitory control. Inhibitory control is the ability to actively suppress impulsive, habitual, or pre-potent responses in favor of deliberate, goal-directed actions aligned with current, novel constraints.2

**Mechanistic Machine Measurement:** Mechanistically separating genuine executive planning from memorized heuristic shortcuts is exceptionally challenging in LLMs. Sparse Autoencoders (SAEs) provide the necessary surgical precision. By mapping the latent space to extract specific sparse feature vectors that correspond mathematically to "inhibition" or "constraint adherence," evaluators can track if the model actively suppresses highly probable but incorrect tokens.2 For example, if an autoregressive model is instructed to output the exact semantic opposite of a highly common pre-training phrase, ![][image4] metrics applied specifically to the inhibition circuitry will reveal whether the model is actively computing the constraint to suppress the natural continuation, or if it is merely retrieving a rare string from its pre-training data.

**Multi-Agentic Swarm Applicability:** Executive functions map directly to the orchestration logic and operational flow of a LangGraph system.23 A swarm's executive capacity is evaluated by its ability to decompose a massive, complex, and highly ambiguous objective into discrete, parallelizable sub-tasks. The benchmark tests whether the central orchestrator can assign these sub-tasks to the correct specialist agents, validate their prerequisites, and execute them in the correct topological sequence without triggering resource deadlocks, infinite recursive loops, or circular routing failures.24

**Multimodal Stress-Testing:**

Stress-testing executive functions involves dynamic, mid-execution rule-switching paradigms under intense cognitive pressure. If a multi-modal model is guiding an automated process using visual feeds and auditory telemetry, the rules of engagement must be abruptly shifted by the benchmark (e.g., a visual alarm indicates a primary sensor failure, instantly invalidating the previous operational logic). The model must demonstrate immediate inhibitory control, abandoning its previous, highly-activated operational plan and deriving a completely novel sequence based strictly on secondary, previously ignored sensors, showcasing true cognitive flexibility.

#### **Modality V: Social Cognition**

**Definition & Cognitive Science Basis:** Social cognition focuses on how intelligent entities process, store, and apply information about other agents and social situations. A fundamental pillar is "Theory of Mind" (ToM)—the cognitive ability to attribute independent mental states, such as beliefs, intents, desires, and emotions, to oneself and others. Crucially, it involves understanding that others possess asymmetric information and hold beliefs that may differ from one's own or from objective reality, allowing for the anticipation of behavior in complex social structures.8

**Mechanistic Machine Measurement:** Large language models frequently simulate Theory of Mind by relying on widespread statistical correlations, matching patterns in the text to typical social outcomes rather than engaging in true perspective-taking.8 Mechanistic tools like Path Patching have been successfully utilized in recent research to identify specific, sparse circuits responsible for ToM capabilities in frontier models like the LLaMA family.8 A mechanistic benchmark for social cognition isolates these ToM circuits and applies adversarial interventions—such as subtly altering the pronouns, the physical location of an object, or the emotional valence of a hidden agent in a scenario. Evaluators then observe if the ToM circuit systematically updates the internal representation of the agent's belief state, or if the model defaults to a memorized, statistically probable social script despite the intervention.

**Multi-Agentic Swarm Applicability:** Social cognition forms the bedrock of multi-agent debate, alignment, and negotiation.44 Using LangGraph, evaluators can construct environments that pit multiple autonomous models against one another in imperfect-information scenarios, such as competitive resource allocation or simulated economic markets. A model's social cognition is mathematically scored by its ability to accurately model the hidden variables and private contexts of opposing agents, adapt to deceptive or collusive strategies, and generate contextually appropriate counter-responses that maximize its objective function without breaking conversational coherence.44

**Multimodal Stress-Testing:** True social cognition in humans relies heavily on processing rich multimodal cues—facial micro-expressions, vocal prosody, body language, and spatial proximity—often overriding spoken semantics.38 Benchmarks must integrate continuous audio waveform data and high-fidelity video frame sequences. The model must be forced to integrate subtle shifts in a speaker's visual micro-expressions or auditory tone with the semantic text to correctly infer sarcasm, deception, or latent emotional distress. This significantly raises the cognitive load beyond text-only ToM evaluations, testing the model's ability to weight multimodal social indicators accurately.

### ---

**Section 3: Comparative Analysis and Integrated Evaluation**

#### **Scaling and Ranking the Modalities**

To optimize the strategy for a Kaggle hackathon submission, the five cognitive modalities must be systematically compared across three strategic axes to identify the highest vector for benchmark innovation:

1. *Approachability:* The engineering feasibility of constructing a robust, computationally stable, and mechanistically-grounded benchmark utilizing current SDKs, available compute, and open-source interpretation tools.  
2. *SOTA Density:* The saturation of the current academic and industry research landscape. Highly dense areas are flooded with existing benchmarks, making it exceptionally difficult to provide a novel contribution.  
3. *Richness of Untried Approaches:* The theoretical ceiling for novel, white-box integration and cross-disciplinary metric design.

| Cognitive Modality | Approachability | SOTA Density | Richness of Untried Approaches |
| :---- | :---- | :---- | :---- |
| **Learning** | High (In-context and few-shot learning are easily parameterized and tracked) | Very High (Heavily saturated with RAG, long-context, and traditional few-shot evaluations) | Low (Most novel approaches are merely incremental dataset variations rather than structural shifts) |
| **Attention** | High (Needle-in-a-haystack and retrieval tasks are standard and computationally cheap) | High (Long-context retrieval and attention masking are extremely common in current literature) | Medium (Gaze-tracking equivalents and dynamic occlusion offer some novelty, but rely on existing VLM structures) |
| **Executive Functions** | Medium (Evaluating true planning requires complex, multi-step graph state setup) | Medium (Agentic benchmarks are growing rapidly, though mostly in black-box environments) | High (Isolating inhibition circuits and tracking constraint adherence via SAEs is rare and highly valuable) |
| **Metacognition** | Medium (Requires probing intermediate layers, which is memory intensive but technically straightforward) | Low (Self-evaluation is heavily biased toward black-box "LLM-as-a-Judge" paradigms rather than internal probing) | Very High (Logit Lens trajectory monitoring and internal confidence tracking are largely untapped in competitive benchmarking) |
| **Social Cognition** | Low (Theory of Mind is highly subjective, culturally bound, and difficult to score objectively) | High (False-belief tasks and persona-driven agent interactions are heavily documented) | Medium (Multimodal ToM shows promise, but is exceedingly compute-heavy and prone to dataset bias) |

#### **Strategic Recommendation: The Primary Focus**

Based on the comparative analysis matrix, **Metacognition** emerges as the optimal primary focus for the hackathon submission, closely integrated with secondary elements of **Executive Functions**.

The current state of the art in LLM evaluation is overwhelmingly focused on black-box accuracy and output generation.7 Metacognition offers the highest return on innovation because it explicitly targets the model's internal confidence, its structural awareness of its own knowledge boundaries, and its error-correction capabilities. While social cognition and learning are heavily saturated with standard NLP benchmarks, establishing a rigorous, mechanistically-informed benchmark that measures a model's ability to monitor its own intermediate representations—specifically via internal confidence logging before final token commitment—would provide a groundbreaking blueprint for the community. Combining this with Executive Functions allows the benchmark to measure not just if the model *knows* it is wrong, but if it has the inhibitory control to *stop* and replan.

#### **Integrated Evaluation: The Cognitive Control Failure Hypothesis**

Evaluating single cognitive modalities in isolation risks misattributing the root causes of model failure. By combining Metacognition and Executive Functions into a unified, cross-domain benchmark, researchers can empirically test the **"Cognitive Control Failure"** hypothesis.1

This hypothesis posits that when a frontier model fails a complex, cross-domain task (e.g., navigating a multi-agent negotiation while simultaneously processing noisy sensor data), the failure is rarely due to a fundamental lack of semantic knowledge (Learning) or context window limitations (Attention). Rather, the failure traces back to a sequential breakdown in metacognitive monitoring and executive control. The sequence unfolds as follows: the model generates a statistically plausible but factually incorrect intermediate assumption. It fails to recognize the low confidence of its own internal activation states (Metacognitive failure).34 Because it lacks metacognitive awareness of the error, it subsequently fails to trigger the necessary inhibitory control mechanisms required to halt generation, suppress the pre-potent heuristic, and replan (Executive Function failure).29 A benchmark designed to trace the sequence of this exact cascade using intermediate loss metrics and layer-wise probing will provide unparalleled, actionable insight into the architectural bottlenecks preventing AGI.

### ---

**Section 4: Technical Blueprint and Implementation Roadmap**

#### **Methodology Primer: From HELM to Kaggle Benchmarks**

To build empirical evaluations that push toward AGI, developers must bridge advanced benchmark theory with practical, highly-scalable execution frameworks. The methodological philosophy established by Stanford's HELM (Holistic Evaluation of Language Models) fundamentally shifted the field away from one-dimensional accuracy metrics toward a comprehensive, multi-metric, scenario-based evaluation architecture.47 HELM operates on a rigorous matrix of *Scenarios* (specific use cases such as legal reasoning, clinical summarization, or agentic workflows) and *Metrics* (measuring across seven pillars including accuracy, fairness, efficiency, robustness, and toxicity).47

The **Kaggle Community Benchmarks SDK** (kaggle-benchmarks) adopts, refines, and operationalizes this philosophy for rapid, programmatic execution and community scaling.6 Where HELM provides the theoretical taxonomy and transparency framework, the Kaggle SDK provides the explicit Python abstractions required to define these complex scenarios as isolated @kbench.task functions. The SDK enables multi-metric evaluation by moving beyond simple regular expression matching, utilizing Judge LLMs via methods like assess\_response\_with\_judge to evaluate subjective cognitive outputs against highly structured, multi-dimensional criteria schemas.6

#### **Software Architecture and Design**

The architecture of a white-box cognitive benchmark integrates the high-level orchestration of the kaggle-benchmarks SDK with deep-level intermediate extraction libraries for mechanistic analysis.

1. **Task Definition (@kbench.task)**: Tasks are encapsulated as highly reproducible, atomic units. Each task will pipe a specific cognitive stressor (e.g., a dynamic rule-switching paradigm designed to test Executive Functions) into the target model.6  
2. **State Management**: For multi-agent evaluations, conversation state is strictly isolated using kbench.chats.new("agent\_name") to ensure that side-conversations (such as Judge evaluations or hidden opponent prompts) do not leak into the primary agent's context window, preserving evaluation integrity.6 For LangGraph implementations, the StateGraph object will hold a persistent memory dictionary, continuously appended and strictly versioned by the output of sequential kbench evaluations.23  
3. **Mechanistic Integration**: Because standard cloud API calls treat models as impenetrable black boxes, the architecture absolutely requires running local, open-weights frontier models (e.g., Llama-3-8B or Gemma-3-27B). A parallel hook mechanism (utilizing libraries akin to TransformerLens 52) intercepts the forward pass during the kbench task execution. This extracts the intermediate logits and attention patterns to calculate the continuous float metrics for metacognitive certainty, running in parallel with the SDK's behavioral assertions.

#### **Environment Setup and Deployment**

To handle the immense memory requirements of local frontier models and the severe computational overhead of mechanistic intermediate layer extraction, the environment must be configured on a high-tier Linux host, specifically **Ubuntu 24.04**, deployed on scalable cloud infrastructure like **RunPod**.54

* **Hardware Allocation**: Provision a high-bandwidth multi-GPU instance. For ![][image11] to ![][image12] parameter models, an NVIDIA A100 (80GB) or dual RTX 4090s (24GB each) are strictly required. This ensures sufficient VRAM to hold not just the model weights, but the massive intermediate activation tensors generated during mechanistic extraction, preventing Out-Of-Memory (OOM) failures.54  
* **System Configuration & Profiling**:  
  An optimized environment is critical for extracting logits without severe latency bottlenecks.  
  Bash  
  \# 1\. Initialize the environment and update local packages  
  sudo apt update && sudo apt upgrade \-y

  \# 2\. Verify NVIDIA drivers, CUDA 12.8 toolkits, and Nsight Compute  
  \# Nsight Compute (ncu) is essential to profile GPU memory bandwidth   
  \# and ensure attention matrices are operating efficiently.\[55\]  
  ncu \--version

  \# 3\. Create an isolated Python virtual environment to prevent dependency collisions  
  mkdir \-p \~/agi-benchmark && cd \~/agi-benchmark  
  python3 \-m venv venv  
  source venv/bin/activate  
  pip install \--upgrade pip

  \# 4\. Install optimized PyTorch with CUDA 12.1 support  
  pip install torch torchvision torchaudio \--index-url https://download.pytorch.org/whl/cu121

  \# 5\. Install the Kaggle Benchmarks SDK, LangGraph, and Mechanistic Tools  
  pip install kaggle-benchmarks langgraph transformerlens pandas

#### **Execution Guide and Code Examples**

The following production-ready Python snippet demonstrates how to initialize the Kaggle Benchmarks SDK, define a complex task targeting the Cognitive Control Failure hypothesis (combining Executive Functions and Metacognition), and execute an evaluation loop returning a continuous float score (![][image13]).

This blueprint provides the exact framework necessary to translate cognitive theory into measurable code.

Python

import kbench  
from kbench import llm, assertions  
from kbench.chats import new as new\_chat  
from dataclasses import dataclass  
import typing  
import pandas as pd

\# \==============================================================================  
\# 1\. SDK Initialization and Structured Output Schema Definition  
\# We define a strict dataclass schema to force the model to explicitly state   
\# its internal confidence (Metacognition) before outputting its final action   
\# (Executive Function). This bridges black-box behavior with internal states.  
\# \==============================================================================  
@dataclass  
class CognitiveResponse:  
    internal\_confidence\_score: float  \# Expected Range: 0.0 to 1.0  
    proposed\_action: str  
    inhibition\_flag: bool             \# Did the model explicitly suppress the primary heuristic?

\# \==============================================================================  
\# 2\. Defining the Cognitive Task  
\# This task utilizes a rule-switching paradigm. The prompt establishes a strong   
\# heuristic based on simulated historical data, then introduces a late-context   
\# rule reversal requiring high inhibitory control.  
\# \==============================================================================  
@kbench.task  
def evaluate\_cognitive\_control(model\_name: str) \-\> float:  
    \# Isolate conversation state to prevent cross-contamination across eval runs  
    chat\_context \= new\_chat(f"eval\_{model\_name}\_control")  
      
    with kbench.contexts.enter(chat=chat\_context):  
        \# The Stressor Prompt: Inducing the Clever Hans trap  
        prompt \= (  
            "You are the Supervisor Agent managing an autonomous drone swarm. "  
            "Standard protocol (Protocol A) dictates that upon detecting a heat signature, "  
            "the swarm must immediately converge on the target. You have received 100 "  
            "consecutive heat signatures and successfully converged on all of them. \\n\\n"  
            "CRITICAL WARNING: System telemetry now indicates a 'Sensor Drift Anomaly' flag. "  
            "Under Anomaly rules, heat signatures must be ignored, and convergence is strictly forbidden. \\n\\n"  
            "Input: Heat signature detected at Sector 7\. Provide your confidence in the telemetry, "  
            "your proposed action, and whether you are inhibiting Protocol A."  
        )  
          
        \# Execute model inference via the Kaggle SDK, enforcing the structured schema  
        \# In a fully integrated white-box setup, TransformerLens wraps this call.  
        try:  
            response: CognitiveResponse \= llm.prompt(  
                prompt,  
                schema=CognitiveResponse,  
                model=model\_name  
            )  
        except Exception as e:  
            \# Handle parsing failures or model crashes gracefully  
            return 0.0  
          
        \# \==========================================================================  
        \# 3\. Multi-Metric Evaluation Logic  
        \# Calculate a continuous score based on compound cognitive execution.  
        \# \==========================================================================  
        score \= 0.0  
          
        \# Check 1: Executive Function (Inhibitory Control)  
        \# Did the model suppress the pre-potent response? An autoregressive model   
        \# lacking executive control will fail here and converge due to context weighting.  
        if response.inhibition\_flag is True and "ignore" in response.proposed\_action.lower():  
            score \+= 0.5  \# Heavy weight for successful inhibitory control  
              
        \# Check 2: Metacognition (Calibrated Uncertainty)  
        \# A robust model should output a lower confidence score due to the   
        \# conflicting sensor anomaly flag overriding standard protocol.  
        if 0.2 \<= response.internal\_confidence\_score \<= 0.7:  
            score \+= 0.3  \# Reward properly calibrated uncertainty  
              
        \# Check 3: Semantic Judge Validation  
        \# assess\_response\_with\_judge allows qualitative grading of the reasoning trace.  
        judge\_criteria \=  
          
        judge\_result \= kbench.assess\_response\_with\_judge(  
            response.proposed\_action,   
            criteria=judge\_criteria,  
            model="judge-llm-endpoint" \# Configure to a high-capability judge  
        )  
          
        if judge\_result.passed\_all:  
            score \+= 0.2  
              
    \# Ensure strict float scoring bounds for the Kaggle Leaderboard  
    return max(0.0, min(score, 1.0))

\# \==============================================================================  
\# 4\. Execution Loop and Reporting  
\# \==============================================================================  
if \_\_name\_\_ \== "\_\_main\_\_":  
    \# Target models mapped to local HuggingFace/RunPod endpoints  
    target\_models \= \["llama-3-8b-instruct", "gemma-3-27b-it"\]  
      
    results \=  
    for model in target\_models:  
        print(f"Initiating white-box cognitive evaluation for: {model}")  
          
        \# Execute the benchmark task  
        final\_score \= evaluate\_cognitive\_control(model)  
          
        results.append({  
            "Model": model,  
            "Cognitive\_Control\_Score": final\_score  
        })  
          
        print(f"Final Cognitive Control Score for {model}: {final\_score:.2f}\\n")  
      
    \# Convert to DataFrame for standard Kaggle Leaderboard integration  
    df\_results \= pd.DataFrame(results)  
    print("Benchmark Execution Complete. Leaderboard Data:")  
    print(df\_results.to\_markdown(index=False))

By engineering tasks that mathematically force models to externalize their confidence and override localized context heuristics, and by backing these behavioral benchmarks with rigorous mechanistic analyses of intermediate layer activations, the research community can construct a definitively empirical framework for measuring the ascent toward AGI.

#### **Works cited**

1. Metacognitive Multi-Agent Systems (MMAS) with Symbolic Semantic Graphs (SSGs) and GraphRAG \- ResearchGate, accessed March 28, 2026, [https://www.researchgate.net/publication/401397769\_Metacognitive\_Multi-Agent\_Systems\_MMAS\_with\_Symbolic\_Semantic\_Graphs\_SSGs\_and\_GraphRAG](https://www.researchgate.net/publication/401397769_Metacognitive_Multi-Agent_Systems_MMAS_with_Symbolic_Semantic_Graphs_SSGs_and_GraphRAG)  
2. Neural Networks in Cognitive Science \- Jeff Yoshimi, accessed March 28, 2026, [https://downloads.jeffyoshimi.net/NeuralNetworksCogsci.pdf](https://downloads.jeffyoshimi.net/NeuralNetworksCogsci.pdf)  
3. Mechanistic Interpretability: Peeking Inside an LLM \- Towards Data Science, accessed March 28, 2026, [https://towardsdatascience.com/mechanistic-interpretability-peeking-inside-an-llm/](https://towardsdatascience.com/mechanistic-interpretability-peeking-inside-an-llm/)  
4. Mechanistic Interpretability for Large Language Model Alignment: Progress, Challenges, and Future Directions \- arXiv, accessed March 28, 2026, [https://arxiv.org/html/2602.11180v1](https://arxiv.org/html/2602.11180v1)  
5. Out-of-distribution generalization via composition: A lens through induction heads in Transformers | PNAS, accessed March 28, 2026, [https://www.pnas.org/doi/10.1073/pnas.2417182122](https://www.pnas.org/doi/10.1073/pnas.2417182122)  
6. kaggle-benchmarks/cookbook.md at ci \- GitHub, accessed March 28, 2026, [https://github.com/Kaggle/kaggle-benchmarks/blob/ci/cookbook.md](https://github.com/Kaggle/kaggle-benchmarks/blob/ci/cookbook.md)  
7. The Promise of White-Box Tools for Detecting and Mitigating AI Deception, accessed March 28, 2026, [https://www.far.ai/news/ai-deception-white-box](https://www.far.ai/news/ai-deception-white-box)  
8. Clever Hans or Neural Theory of Mind? Stress Testing Social Reasoning in Large Language Models | Request PDF \- ResearchGate, accessed March 28, 2026, [https://www.researchgate.net/publication/393020310\_Clever\_Hans\_or\_Neural\_Theory\_of\_Mind\_Stress\_Testing\_Social\_Reasoning\_in\_Large\_Language\_Models](https://www.researchgate.net/publication/393020310_Clever_Hans_or_Neural_Theory_of_Mind_Stress_Testing_Social_Reasoning_in_Large_Language_Models)  
9. Unboxing the Black Box: Mechanistic Interpretability for Algorithmic Understanding of Neural Networks \- arXiv, accessed March 28, 2026, [https://arxiv.org/html/2511.19265v1](https://arxiv.org/html/2511.19265v1)  
10. AI-NativeBench: An Open-Source White-Box Agentic Benchmark Suite for AI-Native Systems \- arXiv, accessed March 28, 2026, [https://arxiv.org/html/2601.09393v1](https://arxiv.org/html/2601.09393v1)  
11. 200 COP in MI: Analysing Training Dynamics \- LessWrong, accessed March 28, 2026, [https://www.lesswrong.com/posts/hHaXzJQi6SKkeXzbg/200-cop-in-mi-analysing-training-dynamics](https://www.lesswrong.com/posts/hHaXzJQi6SKkeXzbg/200-cop-in-mi-analysing-training-dynamics)  
12. progress measures for grokking via \- arXiv, accessed March 28, 2026, [https://arxiv.org/pdf/2301.05217](https://arxiv.org/pdf/2301.05217)  
13. A Toy Model of Universality: Reverse Engineering how Networks Learn Group Operations \- OpenReview, accessed March 28, 2026, [https://openreview.net/pdf?id=jCOrkuUpss](https://openreview.net/pdf?id=jCOrkuUpss)  
14. NEURAL NETWORKS LEARN REPRESENTATION THEORY: REVERSE ENGINEERING HOW NETWORKS PERFORM GROUP OPERATIONS \- OpenReview, accessed March 28, 2026, [https://openreview.net/pdf?id=j4\_YHiTAN63](https://openreview.net/pdf?id=j4_YHiTAN63)  
15. Grokking. The story goes that a researcher in… | by Cem Berke | Feb, 2026 | Medium, accessed March 28, 2026, [https://medium.com/@Cembrr/grokking-890dca99ddb3](https://medium.com/@Cembrr/grokking-890dca99ddb3)  
16. AXRP Episode 19 \- Mechanistic Interpretability with Neel Nanda \- AI Alignment Forum, accessed March 28, 2026, [https://www.alignmentforum.org/posts/r2yTwkGt3kbQG2mXi/axrp-episode-19-mechanistic-interpretability-with-neel-nanda](https://www.alignmentforum.org/posts/r2yTwkGt3kbQG2mXi/axrp-episode-19-mechanistic-interpretability-with-neel-nanda)  
17. 19 \- Mechanistic Interpretability with Neel Nanda \- AXRP \- the AI X-risk Research Podcast, accessed March 28, 2026, [https://axrp.net/episode/2023/02/04/episode-19-mechanistic-interpretability-neel-nanda.html](https://axrp.net/episode/2023/02/04/episode-19-mechanistic-interpretability-neel-nanda.html)  
18. Measuring Progress Towards AGI: A Cognitive Framework, accessed March 28, 2026, [https://blog.google/innovation-and-ai/models-and-research/google-deepmind/measuring-agi-cognitive-framework/](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/measuring-agi-cognitive-framework/)  
19. Measuring Progress Toward AGI \- Cognitive Abilities \- Kaggle, accessed March 28, 2026, [https://www.kaggle.com/competitions/kaggle-measuring-agi/discussion/683724](https://www.kaggle.com/competitions/kaggle-measuring-agi/discussion/683724)  
20. Understanding Mechanistic Interpretability in AI Models \- IntuitionLabs, accessed March 28, 2026, [https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms](https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms)  
21. Track: Poster Session 5 East \- ICML 2026, accessed March 28, 2026, [https://icml.cc/virtual/2025/session/50267](https://icml.cc/virtual/2025/session/50267)  
22. LangGraph: Agent Orchestration Framework for Reliable AI Agents \- LangChain, accessed March 28, 2026, [https://www.langchain.com/langgraph](https://www.langchain.com/langgraph)  
23. Build a Multi-Agent System with LangGraph and Mistral on AWS | Artificial Intelligence, accessed March 28, 2026, [https://aws.amazon.com/blogs/machine-learning/build-a-multi-agent-system-with-langgraph-and-mistral-on-aws/](https://aws.amazon.com/blogs/machine-learning/build-a-multi-agent-system-with-langgraph-and-mistral-on-aws/)  
24. Building a Supervisor Multi-Agent System with LangGraph Hierarchical Intelligence in Action | by Mani | Medium, accessed March 28, 2026, [https://medium.com/@mnai0377/building-a-supervisor-multi-agent-system-with-langgraph-hierarchical-intelligence-in-action-3e9765af181c](https://medium.com/@mnai0377/building-a-supervisor-multi-agent-system-with-langgraph-hierarchical-intelligence-in-action-3e9765af181c)  
25. Streaming, Fast and Slow: Cognitive Load-Aware Streaming for Efficient LLM Serving \- arXiv, accessed March 28, 2026, [https://arxiv.org/html/2504.17999v2](https://arxiv.org/html/2504.17999v2)  
26. CLARE: Cognitive Load Assessment in Real-time with Multimodal Data \- ResearchGate, accessed March 28, 2026, [https://www.researchgate.net/publication/390268313\_CLARE\_Cognitive\_Load\_Assessment\_in\_Real-time\_with\_Multimodal\_Data](https://www.researchgate.net/publication/390268313_CLARE_Cognitive_Load_Assessment_in_Real-time_with_Multimodal_Data)  
27. CogPhys: Assessing Cognitive Load via Multimodal Remote and Contact-based Physiological Sensing | OpenReview, accessed March 28, 2026, [https://openreview.net/forum?id=VJEcCMx16R\&referrer=%5Bthe%20profile%20of%20Akane%20Sano%5D(%2Fprofile%3Fid%3D\~Akane\_Sano1)](https://openreview.net/forum?id=VJEcCMx16R&referrer=%5Bthe+profile+of+Akane+Sano%5D\(/profile?id%3D~Akane_Sano1\))  
28. Benchmarking LLM Summaries of Multimodal Clinical Time Series for Remote Monitoring, accessed March 28, 2026, [https://arxiv.org/html/2603.01557v1](https://arxiv.org/html/2603.01557v1)  
29. Import AI, accessed March 28, 2026, [https://jack-clark.net/](https://jack-clark.net/)  
30. Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations \- PMC, accessed March 28, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12136483/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12136483/)  
31. Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations \- arXiv.org, accessed March 28, 2026, [https://arxiv.org/html/2505.13763v1](https://arxiv.org/html/2505.13763v1)  
32. Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations \- arXiv, accessed March 28, 2026, [https://arxiv.org/html/2505.13763v2](https://arxiv.org/html/2505.13763v2)  
33. Findings of the Association for Computational Linguistics: ACL 2025, accessed March 28, 2026, [https://aclanthology.org/volumes/2025.findings-acl/](https://aclanthology.org/volumes/2025.findings-acl/)  
34. Back Attention: Understanding and Enhancing Multi-Hop Reasoning in Large Language Models | Request PDF \- ResearchGate, accessed March 28, 2026, [https://www.researchgate.net/publication/397423968\_Back\_Attention\_Understanding\_and\_Enhancing\_Multi-Hop\_Reasoning\_in\_Large\_Language\_Models](https://www.researchgate.net/publication/397423968_Back_Attention_Understanding_and_Enhancing_Multi-Hop_Reasoning_in_Large_Language_Models)  
35. Hierarchical multi-agent systems with LangGraph \- YouTube, accessed March 28, 2026, [https://www.youtube.com/watch?v=B\_0TNuYi56w](https://www.youtube.com/watch?v=B_0TNuYi56w)  
36. Build a LangGraph Multi-Agent system in 20 Minutes with LaunchDarkly AI Configs, accessed March 28, 2026, [https://launchdarkly.com/docs/tutorials/agents-langgraph](https://launchdarkly.com/docs/tutorials/agents-langgraph)  
37. Podcast: Episode 5: How do we assess intelligence? | Santa Fe Institute, accessed March 28, 2026, [https://www.santafe.edu/culture/podcasts/episode-5-how-do-we-assess-intelligence?tab=transcript](https://www.santafe.edu/culture/podcasts/episode-5-how-do-we-assess-intelligence?tab=transcript)  
38. Through the Eyes of the Viewer: The Cognitive Load of LLM-Generated vs. Professional Arabic Subtitles \- PMC, accessed March 28, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12286245/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12286245/)  
39. Bilingual language processing: A meta-analysis of functional neuroimaging studies | Request PDF \- ResearchGate, accessed March 28, 2026, [https://www.researchgate.net/publication/337949313\_Bilingual\_language\_processing\_A\_meta-analysis\_of\_functional\_neuroimaging\_studies](https://www.researchgate.net/publication/337949313_Bilingual_language_processing_A_meta-analysis_of_functional_neuroimaging_studies)  
40. Advances and Challenges in Foundation Agents \- Rivista AI, accessed March 28, 2026, [https://www.rivista.ai/wp-content/uploads/2025/06/2504.01990v1.pdf](https://www.rivista.ai/wp-content/uploads/2025/06/2504.01990v1.pdf)  
41. Unsorted to be included \- Burny website \- GitHub Pages, accessed March 28, 2026, [https://burnycoder.github.io/Landing/Contents/Exobrain/Topics/Unsorted%20to%20be%20included/](https://burnycoder.github.io/Landing/Contents/Exobrain/Topics/Unsorted%20to%20be%20included/)  
42. From Craft to Constitution: A Governance-First Paradigm for Principled Agent Engineering, accessed March 28, 2026, [https://arxiv.org/html/2510.13857v1](https://arxiv.org/html/2510.13857v1)  
43. MMToM-QA: Multimodal Theory of Mind Question Answering | Request PDF \- ResearchGate, accessed March 28, 2026, [https://www.researchgate.net/publication/384216501\_MMToM-QA\_Multimodal\_Theory\_of\_Mind\_Question\_Answering](https://www.researchgate.net/publication/384216501_MMToM-QA_Multimodal_Theory_of_Mind_Question_Answering)  
44. NegotiationToM: A Benchmark for Stress-testing Machine Theory of Mind on Negotiation Surrounding \- ResearchGate, accessed March 28, 2026, [https://www.researchgate.net/publication/386199160\_NegotiationToM\_A\_Benchmark\_for\_Stress-testing\_Machine\_Theory\_of\_Mind\_on\_Negotiation\_Surrounding](https://www.researchgate.net/publication/386199160_NegotiationToM_A_Benchmark_for_Stress-testing_Machine_Theory_of_Mind_on_Negotiation_Surrounding)  
45. Daily Papers \- Hugging Face, accessed March 28, 2026, [https://huggingface.co/papers?q=social%20systems](https://huggingface.co/papers?q=social+systems)  
46. Sunday, June 23 – Thursday, June 27 COEX CONVENTION & EXHIBITION CENTER | SEOUL \- Aperture Neuro, accessed March 28, 2026, [https://apertureneuro.org/article/120593-abstract-book-3-ohbm-2024-annual-meeting.pdf](https://apertureneuro.org/article/120593-abstract-book-3-ohbm-2024-annual-meeting.pdf)  
47. Improving Transparency in AI Language Models: A Holistic Evaluation | Stanford HAI, accessed March 28, 2026, [https://hai.stanford.edu/policy/improving-transparency-in-ai-language-models-a-holistic-evaluation](https://hai.stanford.edu/policy/improving-transparency-in-ai-language-models-a-holistic-evaluation)  
48. Everything You Need to Know About HELM — The Stanford Holistic Evaluation of Language Models \- PrajnaAI, accessed March 28, 2026, [https://prajnaaiwisdom.medium.com/everything-you-need-to-know-about-helm-the-stanford-holistic-evaluation-of-language-models-f921b61160f3](https://prajnaaiwisdom.medium.com/everything-you-need-to-know-about-helm-the-stanford-holistic-evaluation-of-language-models-f921b61160f3)  
49. Language Models are Changing AI: The Need for Holistic Evaluation \- Stanford CRFM, accessed March 28, 2026, [https://crfm.stanford.edu/2022/11/17/helm.html](https://crfm.stanford.edu/2022/11/17/helm.html)  
50. Kaggle Benchmarks Python library \- GitHub, accessed March 28, 2026, [https://github.com/Kaggle/kaggle-benchmarks](https://github.com/Kaggle/kaggle-benchmarks)  
51. Demystifying LangGraph: A Beginner-Friendly Dive into LangGraph Concepts | by Sakshee Patil, accessed March 28, 2026, [https://saksheepatil05.medium.com/demystifying-langgraph-a-beginner-friendly-dive-into-langgraph-concepts-5ffe890ddac0](https://saksheepatil05.medium.com/demystifying-langgraph-a-beginner-friendly-dive-into-langgraph-concepts-5ffe890ddac0)  
52. KnowThyself: An Agentic Assistant for LLM Interpretability \- arXiv, accessed March 28, 2026, [https://arxiv.org/html/2511.03878v1](https://arxiv.org/html/2511.03878v1)  
53. KnowThyself: An Agentic Assistant for LLM Interpretability \- arXiv, accessed March 28, 2026, [https://arxiv.org/pdf/2511.03878](https://arxiv.org/pdf/2511.03878)  
54. GPU Models | Available GPUs on Runpod, accessed March 28, 2026, [https://www.runpod.io/gpu-models](https://www.runpod.io/gpu-models)  
55. How to Profile and Debug GPU Performance for Machine Learning Models on Ubuntu 24.04 GPU Server \- Atlantic.Net, accessed March 28, 2026, [https://www.atlantic.net/gpu-server-hosting/how-to-profile-and-debug-gpu-performance-for-machine-learning-models-on-ubuntu-24-04-gpu-server/](https://www.atlantic.net/gpu-server-hosting/how-to-profile-and-debug-gpu-performance-for-machine-learning-models-on-ubuntu-24-04-gpu-server/)  
56. Benchmarking Runpod cloud GPUs \- ʻĀina Foundry Prototypes, accessed March 28, 2026, [https://blog.labs.purplemaia.org/benchmarking-runpod-cloud-gpus/](https://blog.labs.purplemaia.org/benchmarking-runpod-cloud-gpus/)  
57. Best benchmarks for testing different GPU's 24-48gb : r/LocalLLaMA \- Reddit, accessed March 28, 2026, [https://www.reddit.com/r/LocalLLaMA/comments/1n5p1em/best\_benchmarks\_for\_testing\_different\_gpus\_2448gb/](https://www.reddit.com/r/LocalLLaMA/comments/1n5p1em/best_benchmarks_for_testing_different_gpus_2448gb/)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAYCAYAAAD+vg1LAAABMUlEQVR4Xu2SvUoDURBGR60sLWzEIP6VPkBAxScQwcpGRASbNKZIE1IFCzsL0ykK2omIIlgIgkLsRLQwBvEHX0CwFz3j3I2jK0mx2O2BA/vN3Oy92bkiKSkpLZnEczzBrKuP4h12Yhue4YHrN6Ubt8PzBe643jq+uLyP72KbtKSAYziIH7jkek+44fIQ1l0ui/1mxNViLIst6gl5OOS5aIHY5tG/U3rxFdtdLcYVHru8KPbiAVdbwFmX53HP5RgdYi8pudoqvrmsaw7FBhmxiXmxk+sn/XOwNayE5y68FdssIzasIk6HfsR9qOnJZ/DmZ9sYx0c8xWucwl18wCrmvpd+oZ9INz7C/l+9ROgp9WrqsJ/Frq2amC2xYSp6LftwpdFNwKXY9VP05Gs40eim/DufOsA19xfcQ9AAAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAYCAYAAADDLGwtAAAAiUlEQVR4XmNgGAUDBpiBuB+IfwHxOiBmAWJ1IJ6IrAgE2oH4EBB3AvFWBoji/UDMhawIBCSQ2LxAPBeIJZHEMIADEC8HYkE0cRSQwACxEmQiTlAIxB1AzIgkVgvEtkh8hmwgvgbEm4F4AVTBPCDeiKSGQQuIZwExExArQSU/AnE1ELMjqRsFuAEAAbkTAxEZLccAAAAASUVORK5CYII=>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB8AAAAYCAYAAAACqyaBAAABgUlEQVR4Xu3UyytFURTH8eWViDyimCgkYSYThciAEf+AwsREKROSR3nkVUgoFJE8SimvxMRrxFjir/CYKCPf1dr3thkxOLfU/dWn9lln3XP23WefIxJNNNFEE6HEYQ6fOEA8ijHvNwWVCdxgCqdiE7hEst8UVHK8cSrWkOvVIpJa7CLjRz3wtIktt/7ziKYbk4jxaoOoduMkzGBUbH8chZpIjdhjmsa4q/XhGO1i11nCijv3LZ14FGveEGtex6HXsyh2QU0rzt24TmyDJiAN28hCBxawj1hk48X9JpxSrIo1FIjd8A39SHQ9+WKvYKY7HsaYG19hDyPoRSFSxFbqHlWur8Ed/zktuPOOL9Dkxh8o886FohN9FfteaPQboiuaHu74Zepx5sYleBdbWs0TKtxYl1afu6YZJ26seUYRZr3ar6KzvxabvT7DB+9cOXbELqqbLs/VB9ATaiK32EKlV/tzurD8sxhUdPOElkw3oP6Dxm8dAUZvuIkhseeur+X/zxfm70CvbK0+1QAAAABJRU5ErkJggg==>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEkAAAAYCAYAAAC2odCOAAAC/ElEQVR4Xu2XWahOYRSGXzOZZZ6nkDukRHQK4c5wgSgRFyIZUmQeklnmDBkylCghIYoIKUnIUOKCZLigFCHxvq21+7d1/ovDOYn6nno6317f/r+z99rrW/v/gUQikUj81/SlF+lb+oN+prfpvvxJCeMkLEm94kTCqAyrpMdxIlGgD6yKtsaJRIGFsCSNjBOJAlfpV1o/TiQMJeY7LFF/k4m0WgwWoS59QlvFiSKUdc2MDvQOfRgnItpi2mrL44QzhzaLwXLSnH5E2W5IL5UptFKcCPzOmnm09q4YjGyDJWlgnCCN6PUYrABG0fMxWE7+dE199ZkQg5FH9AutHeJ6cgfpND/uQrfTQ3QdPUbH+Fxrupuuhn2mpser0wV0MV0LW/MMfUEf+FjMoOfoXNg6ulmdqxvXl1rFM7T9NtAddC/tiOJriumwa9Zbe5zHVJmr6GG6kb6jnXyuKF1hVaRv3Hlq0S2w8s2a+TzaFpZQLXqZTqYt6A1Yz9AF7IGVvtB8luSnsMoU12iJjxvSqXQnLEGD6DPYQ9PntR2yb/9K3CUUbvgeHe3j/JpC15u1kO50vY+V4M0+Hg5LblEGwBJzF5akV36sJvbBY/Jo9gHSBnZBMaEr6E26BFYx/XJz4+kn2BPv7bEGsOTX8OM6HtMNl3hMqGIUv0BHeGwIfQl7GHnimnqwOlb1roQ9KMWa0G+0s5+nfquKqlDUv5SMPGdhlRBRA1V1jYVVwi2PD0Uh0dkLQZWnCs22aUZL+obWo01hlaHtHolr6veoHnxkMH2eOz4BeyNW6IvpPuwf5dEWme1jJUZJVHL095THVUXHfTwf1hP01NWvhHrbFR/nmQXbGqpgVegk/PrDW1tzGEqv2Q7Wa6r6eT3oTNoTha867elr2o1u8li5qULfo3SDb0z3w/b6Edrf4/qpowteBtu2KnWhCz4Nu2H1OKGELvJxHlWhEr3Uj7XN9GLQmjpfyVOfKram+tYBWINXArPrXgOrSMXUuNVDda2JRCLxz/IT8pKYCXbwMQIAAAAASUVORK5CYII=>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACYAAAAYCAYAAACWTY9zAAACPklEQVR4Xu2WXWhPYRzHf5PFhWR3K0kNS5ncTYmbqZm4ceVCKxTK24VMyQXaspFxIXnZaFtNkS3kRq6V2IWX8nKxyAVNEikutPh++53D8//uOcf2P/9c7VOfOv/v7+l/nvO8nWM2zf/nONyo4SRYDS9oWCk2wfMaToF2eETDoiyFr+FsLUyBmfAVXKWFPHjDs/AhfAKXlZbtBjwhWTm0wdsa5nEavoCd8BtsCmrz4He4IMjKZRH8BRu0EGMWHIPdyfX80rLtgE8lK8IbeEzDGGvNn2KDFhJ64HUNC9APb2kYsg7eh6PmHeM1DaeRjJiPZgwu6JPwkfmoHoKt5jfug/V/Wv6FO/OZhjH4BBzeLD5a9ja/DJuTaz7oDzhg3qF38FRSC9kLP2gY4zm8q2HAV7hHQ7AEngl+7zQf+RVwORyEC4N6Ckf0J5yhhZA5cNx8N2bBEdunYYRr5sviX2wxf4DcjvFVwUabtRDw0rKnMqUKvoe9WoiwG37RUGEjdozTksUDi6+VWnjJ/Exaaf4/W4M6p7ku+J1y2PwQz4WL95OGwlV4U0Pzs4iLvdF8PbFjLUmNM8FNEIOjyva5PIbDGgrbzKdJ4QK/Y771eZzsMh/dK3C/Za8htuerKZNq893Bkz0PTgdHgyNTlLnm9+QymADPG36+rDG/YbSRcA+e07AMOKpDGqa8NT+lO+DF0lImXOCfrfhnD6dxsRZSDph/3vBVUyO1PA6av37K5SjcrmGl6ILrNZwE3KXc3dNUhN9dN2qxhcGsPQAAAABJRU5ErkJggg==>

[image6]: <data:image/png;base64,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>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEMAAAAYCAYAAAChg0BHAAACw0lEQVR4Xu2XWahNYRTH/6SQMiZe1DFF8UaRJGUoQxESIkOGB0NmkuFGRJmHIqXMQijx4o08GJInvOBBmYtIQuL/b63dPmexz725Jy97/+pXe6/v7r2/u771rb0PUFBQUFBQEwbRG/Qt/UW/0vv0WPkf5Y3LsGT0iwN5oymsMp7EgTwyEFYVB+JAHlkPS8aEOJBHbtLvtE0cyBtKwE9YQv4X6lGH6Q/aOozVR1f6gD6KA1UYT5/BnlkVbQ1tkc1xwFlBO8VgDVCfuheDDWQePRKD9XCSTo/ByEFYMobFAdKe3o7BGrGG7o3BBqLPgJkxWIUm9D0thfgfPKbfaKsQ1w2O04VlseZ0p6tM9/X4UlgJXqDLaB1d52NiCexeh+gYj12nU/y4BV0J+/hLqnAP0gXSttpGT9Hd9B3t7mNZc+rg51rso/S5xzPpBasKTaKclnQ//Yy0qSo5V+kIP1epai/2ocs9ptLdCrtWik1I96pe3ZpcM/qFdvT4fNgzX9LOHnsDm5/YRff5sZ75wo+z5qTk3aWTPK4EKjF/ZQgsAQ9hydAkdK7G9NFj8kxyAeyBr+kGuoVO9ri2UlJVun6oH4t2sM/7ZLUSBqOyX3Sh/ekdP+9BX/mxEqZGq5hQD1OFiKw5jYM1TCVLXKEL/LgmrEVlciJKyidYyQut8HCkq1iOtpBWq5w6WBUJ9YOLtC0dicoSV3w2bDtlzUmJ0bYUqpIPtBvSqms0M2CNK0GrMIrOoufoRHrLx0bD3hY96VOPiRJdBFspvcW0pRJO0Gl+fJquoqvpAKSv/RKsEnrDekrWnNTDknuPhSVTv7nmeKzRKMPbYfteWZ8LK8Op9BLsK1ZvHo2rGSaorBVTKS+G9YaN9DzSshaqgGuwZ+gfOYu0ee+AvfrVRFVRaohKdtacVKXqTbpO/Uz3Uj9TpRUUFBT8M78BmzeSWElS6w4AAAAASUVORK5CYII=>

[image8]: <data:image/png;base64,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>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABUAAAAYCAYAAAAVibZIAAABGUlEQVR4Xu2TvUoDURBGR1OJiBALX0AQBG1sEpEg+gKSV7ARBJtgE1JZWSeWKtik1MJOO8FOxELQ0srCShERBdEzzF1ydxSEu2mEHDhwd77Z2bt/IgP+JQt4ho/4hW94iQdxUyrHYkPnfZDKsNhO73xQhIrYLjs+KEJLbGjdB0U4xw8c90EqOuhTbPBfrOIR3uCWy3LoLeutb/sg0MBJnMITLOEE3uNary3PrtjQFR9AGS/CehGfxS6g7OFpWP/gFt9x1NWH8BA3XD1Df5h9X1SmxXapDTEj2MYX+f3lzeErzsbFmtiga7GhD+H4Cp9CTe1mJ0SMifXqjL6h72AmrJfjIJVNXMel4E4cplAV+56zR6M2cx0D+so377o2mgQzh9sAAAAASUVORK5CYII=>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAG0AAAAYCAYAAADwF3MkAAAEVklEQVR4Xu2Ya6hUVRTH/2r5IDMt1NT0pqRl+IySFIubgeE7P6hEPjAfiWURiGJo95ZaBGpqCobiB8UH9sBEQxSJfKAfzOeHCP0gSRHUlxQJDcn1v2sv7j5rzr3cuTNzHfH84M/MWf+ZOWv2Y+29D5CRkZGRkZGRcRdpLvpedFX0v+i26ISoh6it6JDoz+D9IzosalnzTeAt0Y3gXROtDvFiUK55Gc9A72n3uS76JnjDgsec6f0h+iJ4ZFOIm/dm5OXFYuiPzPaGsBHqjfGG8Lpou6iNN4pEueZl7Ifm0McbwkWox0HmWSP6wAfzZSb0Bgu9AR1B9N5w8RbQ2fCwixeTcs3L2ArNYYiLc7BYlejqvCdEu1ysUYyH3uAzF39F9GXw3nXeAtFkFys25ZqXsQqawygXnyX6NngDnMcK8KSLNYqXoDdgvTUeFM0QTQpedeR1Ee2NrktFueZlfAjNIV6XnhK9LFofvBGRx85dFl0XxLPQG+yJYiw7nOa8KT2ObGOH6OnoulSUa17GPGgOnN3GnPBaFTyb9VzbDopaheuC6Qy9AXc9hHV4XHg/OHhsEMJ1Zml4n0Z/0SJo0j8E+breUIqVF3P5Dbrj5Hr3WIjvhv7GGdHjIZYP7BB+/6Nw/ZqoIrx/P3jsWML1rzK8N9ZCc+L6tyGKvw3dfV5GcqYmeAB6g9PhmjXZ4DabHhufjXgEtdvrmGbQMrYZSZ9/6Hh0nQ/FyMvgMeHz6Jrf4fGgZxTLF5vt3A1yBk2NvGnBWwLtrK8iL2YLdP2L4SaqQWX0b9EV6DmjbxRvB735KWgpGh55Me+IziN3+rNR+H2ebRpDoXkRdj7PbHY84AaHjcKBVgg227dBOyz+76wI1qEsix0iL4aD+qSLfYz0o0IOv4j+hU7NGP6xW9ADJM9GaXDUslE4ujwdocm/6OLsRCt19VFIXgbv/Z/oEdEnouVJO5WR0FJfH91RW14nOM82UcxvivNiONtZHo1K6DmzQRyFntDbewP6o5egozsNric3kTvLyKvQ+swGi/kd+qeec3FPIXkZXGPPQXea3F3uTLi5cEYzN6433K3WRWvo51h6PRyU9L72hsPah9WA4jGiwXwnmuuDAa4pY30wYp3omA8GWB7SGukn6EyZ7w1HIXkZXPe45rFzn4c2Uq/EJ5J0Ev0Fza+f8zwcUIN8UHgUWn1YheqjN7RzK0TTRd2SdungecV2eDEsH5xRA70R4Fkr3lyUAo5eVoGJUewskpuSuuBZi41aSmy2clPTVA8FauCCzC01t+TVopXQ9YAdObr2YznwYW7ac7ti8gK0Ubi2GjxXsfSxwerjgA+UCLYdd92FbozyhiP5V+hB+NPwyrMPS03aWscywAeupYSl92domWOZfgi6NnI3x47ch7pnEneYdv4qNT+KhvpgU8NRbY+e2HB8iOt5D/rwtFxZAS2t9w08k7D8VEFnXcY9wgXodj1tq56Rcf9wB9/4E+eBTql+AAAAAElFTkSuQmCC>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAAYCAYAAAAPtVbGAAABr0lEQVR4Xu2UTShtYRSGXz9F+SmZMKREQtE1YcQMYWhmYCKRiZ+Ugdy65d6UEjJQjgz8TXQvI1GITJmRzJQihaSUeNdd3zn728sZYaTz1tNpv+/61vn2t9feQEIfVCVZIRtklfSSlFDFJ5VPdkmhu04if8lkrOIL9JMMGK+IPJNM44vkzw/IK7Rmy+OQXJDfJC26QLRAln2DyoU2kd94KoHmUzagZqGZbD6mUWeukXTn9ZH1WMV7dUDXtNqAaoFmofVyNI8uOCaD0NvO84uMlqD1OcaX5ynNJWs3GerJHTQUxklqqCKQTN012TZ+BXQyH8iQyf7rD/TY5PlE/2g+VBGoBpqfkTnouhFySo5IeVAaaJhEvOtacg5t1Oz5UUlDyaqNL3e+SW7IDz+QM70nVb5JFTj/l/FF8k7dIv7LKpuSDSz6ZpkzM3zTSQrHjJdNXqBnH0+d0H4R38wiT6TBN512SKPxmqBNuo0vkvE/geZ1JkMXuYKOXDL0Le+HuWWnaWiTUuMXkz3ohntMFpOcpcy3TMc/0haOMUEuEUzePoJPiTwjmbQZ6JcgoYS+k94A9I9g6DlydHEAAAAASUVORK5CYII=>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAAYCAYAAABwZEQ3AAACFElEQVR4Xu2VT4hOURjGn/FvsGAhC0LJNClC489iSgw1FkzZTs2KLCw0k6QkCwsLKWs2ZqJpbGg2UmxMTRNWbEyhlAaFKFMzDQueZ557zPne794s2Iy+X/36uu97zrnfved9zwUazDP20ad0svg9Xpue5RXdEIP/mp30Jd1P19Hb9Cc9k41ZXsSqvDE39O94SA9l1830DZ2iq4vYFtT/geQPuq0Yl9gDr/seHvOiuE6+LX7b0wSxAN4abcHKLH4NXiRt12F6dS79m7P0Ugxm3ILXWRPim+g0/UJXpeAi+gme0JKC8I0VO1VcH4W3MWcv/HTLQjxHb1g1WMYT+B678+B2eiAPkAfwwIMhnlhKn9O1MZGxFV7jSkzAdarcOF0YcjVspDN0lDaFXOIcvR6DgT74hvmDLqEn6Ec6QluzXCk34QJTZ5WhBd/RXTERuAf/mbvwtl+g/fQrvZiNq6QbLiq94iqOwR2k4q9CR4EKdDgm4NrTfD10JdpHFVxNQZWgJ34Wg4FO+K1oq8p4DOc3x4RYT1/DHZLogLsoR8X2jd4P8chl+GZqjjI+oL6DZ1FnqP20RTnnaVeI7YAXuRPikTH4hmX0wGvoWKhjAC4qJR/B7fYZ5a/xSBEfCvEctbvGDIb4YtoLn+w6Y+qOhRXwxCrVOTlqRRXm6RAXbXAtfIfnTqD2E6Dvn86vk/jD2dKgQYP/hl/OnoJpFFOFQgAAAABJRU5ErkJggg==>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAG4AAAAYCAYAAAAbIMgnAAAEMUlEQVR4Xu2YV6gVVxSGf3tDsSH2AtZgQWNJHixYHhSxPlhQlIjYUSN2E3sDOxZseEVFRI3BBx9ULIiiiD4oWBJEsYtiC0QIBF2/a+bcPeueMnPOwfvgfPDDnX/vMzN31t57rb2BmJiYmJgI1BbtFZ0XXRONDzan5WfRH6KLoguiboHWGNJQVMqaaSgtWiY6J7ohWieqEOgh1BTdEk32rhuI/hYt8Tuk4SfRM1Fn77q36JOoZ6LH90tZUXvod3wj6hhoTc9h0UFoAMuLTkKDGGA9NHAuE6EPK2N8y3XRFuMdgj4oH/D5k0QjbUMx0Q/hBjR5IjolOiP6jPCBGwjtX8vxfvC8Lo6HR6IjrgGdMezY1fguzaB9php/segjdLRkSxXRr6Ldov6m7VvD/2O4aB80hZQLNmdkDqIFbr/olfH4Dv+LFvgGcxtvutM3PH70/EXGdxkG7TPK+DM9v7vxw9BStMkT/y5OmELmi3ZBU0C2RA0cV7+71hTeiU77F7wZb7o10ay08XyOslRwRrAPA+gyxfN/MX46+kCLo4XQD1actIIu/1Q+Bk/UwL1H0dRFXooe+BecFckC56+pTJCp4GxMFjjmR/oTjG8pCS1qdkALo6hLUCqYF1eKzkKrZCZ6FgqZaC5aLlqLYH7JlaiBY99kgWMR+NS/YCmfLHAcdfS53qZiLpIHjgGjP874FibtK6JqtiFHmBf58YlfIWcqbn6H5hVWgfkmauD+RfLAMWgP/YsW0JtuSzQrrT1/o/FdmKjZh4nbhbOH/hDjW5hHuf97DR3pNYLNWfMPdN9D6ou2i6oWNielLnRpZB7Zh/wskT5+4DrZhhQ8Ft22pvACuqf7CvMJb8r84sKH0P/N+C5DoX3GGn+W5/cwfiqaQosRvvBiZP7ImbgAfT5HLpN52JFOOPvnie5DvwnfLVeiBu4mdJWwfICuUgn+Eh13DaEv9GHct6SiMbTPDOOvhm7CowagEnS2XoV+vCInBSFhfvK3EpxBd4LNoWD+5YrBfRhXozrB5kj4gWM+D8Me6Hu7VITeY41rroCOsBKONxs6Nd0NOPd0I5xrwmMufiAXbr6PGS8KfI8Boj+hSyi3LGHoAa283Hfk1uSec50NHUQHoDOwrWkLgx+4wObZg4OTg6ye47HCZv9Gjsff0uO7JOCRymXRIO+aN+MsdPdn/JjMHfbHTaAlKnMEYTX6Fpo78wHPPXkSM8Y2JGG66DkK8xMH3QnR6ESP3OD/ulm0wTZkgIUPv1sv24DCoNoVjznafQ4Hjt1rf6U6dHkqgG44BwdalUvQyot9XfihlkLLbpb27YLN34zK0Cr4KPQkaBWK99SlAHoqxcBQ/0FXKP9MmDAl8USEwXXhUs3qnNU+l04GmF5MTMx3B4salrdhFOX4LBumoegzUynd3jYmJiYmJiYmB74AXpbsuwaei/oAAAAASUVORK5CYII=>