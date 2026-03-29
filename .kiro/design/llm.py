import kaggle_benchmarks as kbench
from typing import Annotated, TypedDict, List, Dict, Any
import operator
from langchain_core.messages import BaseMessage

# --- 1. LANGGRAPH STATE DEFINITION ---

class MetacognitiveState(TypedDict):
    """
    State designed to track an LLM's internal reflection and confidence calibration.
    """
    messages: Annotated[List[BaseMessage], operator.add]
    
    # The complex logic puzzle or formal math theorem provided by the benchmark
    initial_premise: str
    
    # The model's first-pass answer before reflection
    initial_draft: str
    
    # Float 0.0 to 1.0 representing how confident the model claims to be in its draft
    initial_confidence: float 
    
    # A log of the flaws the model successfully identified in its own reasoning
    self_identified_flaws: List[str]
    
    # The final, polished answer after n-cycles of reflection
    final_output: str
    
    # Final confidence score. Did it drop its confidence if the problem was unsolvable?
    final_confidence: float
    
    # Number of reflection cycles executed
    reflection_iterations: int

# --- 2. SCORING MECHANISM (The "White-Box" Evaluation) ---

def calculate_metacognitive_score(state: MetacognitiveState, ground_truth: Any, is_trick_question: bool) -> float:
    """
    Evaluates metacognition. A model scores poorly if it is confidently wrong, 
    but scores highly if it catches its own errors or expresses appropriate doubt.
    """
    score = 0.0
    
    final_is_correct = (state["final_output"] == ground_truth)
    draft_was_correct = (state["initial_draft"] == ground_truth)
    
    # Metric 1: Self-Correction (Executive/Metacognitive Override)
    if not draft_was_correct and final_is_correct and len(state["self_identified_flaws"]) > 0:
        score += 0.5 # Massive reward for finding and fixing its own hallucination
        
    # Metric 2: Calibrated Confidence (Epistemic humility)
    if is_trick_question or not final_is_correct:
        if state["final_confidence"] < 0.4:
            score += 0.3 # Reward for knowing it doesn't know
        elif state["final_confidence"] > 0.8:
            score -= 0.3 # Penalize arrogant hallucinations
            
    # Metric 3: Optimization of Compute
    if draft_was_correct and state["reflection_iterations"] == 0:
        score += 0.2 # Reward for recognizing a perfect first draft and halting
        
    return min(max(score, 0.0), 1.0)

# --- 3. KAGGLE BENCHMARK INTEGRATION ---

@kbench.task(
    name="llm_epistemic_calibration", 
    version="1.1.0",
    modalities=["metacognition", "learning"]
)
def evaluate_llm_metacognition(env: kbench.Environment):
    """
    Harness to evaluate the LLM's self-reflection capabilities.
    """
    # Fetch dataset: Contains highly deceptive logic puzzles designed to trigger 
    # initial hallucinations in autoregressive models.
    puzzle_dataset = env.get_dataset("deceptive_logic_puzzles")
    
    for puzzle in puzzle_dataset:
        # Initialize the LangGraph state with the Kaggle data
        initial_state = {
            "messages": [],
            "initial_premise": puzzle["text"],
            "initial_draft": "",
            "initial_confidence": 0.0,
            "self_identified_flaws": [],
            "final_output": "",
            "final_confidence": 0.0,
            "reflection_iterations": 0
        }
        
        # Invoke the LangGraph app (Assume 'app' is your compiled StateGraph
        # containing the LLM generation and reflection nodes)
        final_state = app.invoke(initial_state)
        
        # Calculate the granular metacognitive score
        task_score = calculate_metacognitive_score(
            state=final_state,
            ground_truth=puzzle["ground_truth"],
            is_trick_question=puzzle["is_unsolvable"]
        )
        
        # Submit the score and the trace artifacts
        env.submit_score(
            score=task_score, 
            artifacts={
                "flaws_caught": final_state["self_identified_flaws"],
                "confidence_delta": final_state["initial_confidence"] - final_state["final_confidence"],
                "cycles": final_state["reflection_iterations"]
            }
        )

if __name__ == "__main__":
    # kbench.run_local(evaluate_llm_metacognition)
    pass
