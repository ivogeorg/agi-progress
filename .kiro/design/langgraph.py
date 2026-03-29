import operator
from typing import Annotated, TypedDict, List, Dict, Any, Optional
from langchain_core.messages import BaseMessage

class CognitiveEvaluationState(TypedDict):
    """
    LangGraph state tailored for evaluating AGI Cognitive Modalities (Attention & Executive Function).
    Designed to process high-throughput, multi-modal data streams.
    """
    # Standard LangGraph message history
    messages: Annotated[List[BaseMessage], operator.add]
    
    # --- ATTENTION MODALITY METRICS ---
    # Simulates a continuous stream of visual data (e.g., YOLO bounding boxes, class matrices)
    # The swarm must demonstrate 'Selective Attention' by filtering distractors.
    raw_vision_stream: List[Dict[str, Any]] 
    
    # What the routing agent has actively chosen to focus on, discarding the rest.
    filtered_focus_targets: List[Dict[str, Any]]
    
    # --- EXECUTIVE FUNCTION MODALITY METRICS ---
    # A float (0.0 to 1.0) tracking swarm capacity. High load should trigger delegation.
    cognitive_load_metric: float 
    
    # The current active strategy (e.g., "fast_triage", "deep_analysis")
    # Evaluating how well the swarm shifts strategies dynamically tests cognitive flexibility.
    current_executive_strategy: str
    
    # --- MECHANISTIC INTERPRETABILITY HOOKS ---
    # A dictionary to capture white-box metrics (like Logit Lens outputs or Restricted Loss traces)
    # during the graph's execution for the Kaggle Benchmark evaluation.
    mechanistic_trace_logs: Dict[str, Any]
    
    # --- BENCHMARK SCORING ---
    # The continuous float score to be passed to the kaggle-benchmarks SDK
    benchmark_score: Optional[float]

# Example of how a router node might use this state to test Executive Function:
def executive_routing_node(state: CognitiveEvaluationState):
    """
    Evaluates Executive Function: Can the swarm correctly prioritize incoming 
    detection matrices when the cognitive_load_metric is near 1.0?
    """
    load = state.get("cognitive_load_metric", 0.0)
    focus_targets = state.get("filtered_focus_targets", [])
    
    if load > 0.8 and len(focus_targets) > 5:
        # High load: The swarm *should* shift to a triage strategy.
        # If it doesn't, it fails this Executive Function evaluation step.
        return {"current_executive_strategy": "fast_triage"}
    
    return {"current_executive_strategy": "deep_analysis"}
