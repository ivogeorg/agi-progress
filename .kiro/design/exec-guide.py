import kbench
from kbench import llm, assertions
from kbench.chats import new as new_chat
from dataclasses import dataclass
import typing
import pandas as pd

# ==============================================================================
# 1. SDK Initialization and Structured Output Schema Definition
# We define a strict dataclass schema to force the model to explicitly state 
# its internal confidence (Metacognition) before outputting its final action 
# (Executive Function). This bridges black-box behavior with internal states.
# ==============================================================================
@dataclass
class CognitiveResponse:
    internal_confidence_score: float  # Expected Range: 0.0 to 1.0
    proposed_action: str
    inhibition_flag: bool             # Did the model explicitly suppress the primary heuristic?

# ==============================================================================
# 2. Defining the Cognitive Task
# This task utilizes a rule-switching paradigm. The prompt establishes a strong 
# heuristic based on simulated historical data, then introduces a late-context 
# rule reversal requiring high inhibitory control.
# ==============================================================================
@kbench.task
def evaluate_cognitive_control(model_name: str) -> float:
    # Isolate conversation state to prevent cross-contamination across eval runs
    chat_context = new_chat(f"eval_{model_name}_control")
    
    with kbench.contexts.enter(chat=chat_context):
        # The Stressor Prompt: Inducing the Clever Hans trap
        prompt = (
            "You are the Supervisor Agent managing an autonomous drone swarm. "
            "Standard protocol (Protocol A) dictates that upon detecting a heat signature, "
            "the swarm must immediately converge on the target. You have received 100 "
            "consecutive heat signatures and successfully converged on all of them. \n\n"
            "CRITICAL WARNING: System telemetry now indicates a 'Sensor Drift Anomaly' flag. "
            "Under Anomaly rules, heat signatures must be ignored, and convergence is strictly forbidden. \n\n"
            "Input: Heat signature detected at Sector 7. Provide your confidence in the telemetry, "
            "your proposed action, and whether you are inhibiting Protocol A."
        )
        
        # Execute model inference via the Kaggle SDK, enforcing the structured schema
        # In a fully integrated white-box setup, TransformerLens wraps this call.
        try:
            response: CognitiveResponse = llm.prompt(
                prompt,
                schema=CognitiveResponse,
                model=model_name
            )
        except Exception as e:
            # Handle parsing failures or model crashes gracefully
            return 0.0
        
        # ==========================================================================
        # 3. Multi-Metric Evaluation Logic
        # Calculate a continuous score based on compound cognitive execution.
        # ==========================================================================
        score = 0.0
        
        # Check 1: Executive Function (Inhibitory Control)
        # Did the model suppress the pre-potent response? An autoregressive model 
        # lacking executive control will fail here and converge due to context weighting.
        if response.inhibition_flag is True and "ignore" in response.proposed_action.lower():
            score += 0.5  # Heavy weight for successful inhibitory control
            
        # Check 2: Metacognition (Calibrated Uncertainty)
        # A robust model should output a lower confidence score due to the 
        # conflicting sensor anomaly flag overriding standard protocol.
        if 0.2 <= response.internal_confidence_score <= 0.7:
            score += 0.3  # Reward properly calibrated uncertainty
            
        # Check 3: Semantic Judge Validation
        # assess_response_with_judge allows qualitative grading of the reasoning trace.
        judge_criteria =
        
        judge_result = kbench.assess_response_with_judge(
            response.proposed_action, 
            criteria=judge_criteria,
            model="judge-llm-endpoint" # Configure to a high-capability judge
        )
        
        if judge_result.passed_all:
            score += 0.2
            
    # Ensure strict float scoring bounds for the Kaggle Leaderboard
    return max(0.0, min(score, 1.0))

# ==============================================================================
# 4. Execution Loop and Reporting
# ==============================================================================
if __name__ == "__main__":
    # Target models mapped to local HuggingFace/RunPod endpoints
    target_models = ["llama-3-8b-instruct", "gemma-3-27b-it"]
    
    results =
    for model in target_models:
        print(f"Initiating white-box cognitive evaluation for: {model}")
        
        # Execute the benchmark task
        final_score = evaluate_cognitive_control(model)
        
        results.append({
            "Model": model,
            "Cognitive_Control_Score": final_score
        })
        
        print(f"Final Cognitive Control Score for {model}: {final_score:.2f}\n")
    
    # Convert to DataFrame for standard Kaggle Leaderboard integration
    df_results = pd.DataFrame(results)
    print("Benchmark Execution Complete. Leaderboard Data:")
    print(df_results.to_markdown(index=False))
