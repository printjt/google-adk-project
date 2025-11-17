"""
Custom tools for MindfulAI using Google ADK tool framework.
Implements crisis detection, mood tracking, and resource management as ADK tools.
"""

from typing import Dict, Any, List
from datetime import datetime
from google.adk.tools import FunctionTool
from adk_config import CRISIS_KEYWORDS, SEVERE_KEYWORDS, CRISIS_RESOURCES


# Crisis Detection Tool
def detect_crisis(text: str) -> Dict[str, Any]:
    """
    Analyzes text for crisis indicators and returns risk assessment.

    Args:
        text: User message to analyze

    Returns:
        Dict containing is_crisis, severity_level, matched_keywords, and confidence_score
    """
    text_lower = text.lower()

    # Check for crisis keywords
    matched_crisis = [kw for kw in CRISIS_KEYWORDS if kw in text_lower]
    matched_severe = [kw for kw in SEVERE_KEYWORDS if kw in text_lower]

    # Calculate severity score
    crisis_score = len(matched_crisis) * 1.0
    severe_score = len(matched_severe) * 2.0
    total_score = crisis_score + severe_score

    # Determine severity level
    if total_score >= 3.0:
        severity = "CRITICAL"
        is_crisis = True
    elif total_score >= 1.5:
        severity = "HIGH"
        is_crisis = True
    elif total_score >= 0.5:
        severity = "MODERATE"
        is_crisis = True
    else:
        severity = "LOW"
        is_crisis = False

    return {
        "is_crisis": is_crisis,
        "severity_level": severity,
        "matched_keywords": matched_crisis + matched_severe,
        "confidence_score": min(total_score / 5.0, 1.0),
        "timestamp": datetime.now().isoformat(),
    }


# Mood Tracking Tool State
_mood_history: List[Dict[str, Any]] = []


def log_mood(mood_score: int, emotions: List[str], notes: str = "") -> Dict[str, Any]:
    """
    Logs a mood entry with score, emotions, and optional notes.

    Args:
        mood_score: Numeric mood score (1-10, where 1=very bad, 10=excellent)
        emotions: List of emotion words (e.g., ["anxious", "hopeful"])
        notes: Optional additional context

    Returns:
        Dict containing the logged entry and current trend analysis
    """
    global _mood_history

    entry = {
        "timestamp": datetime.now().isoformat(),
        "mood_score": mood_score,
        "emotions": emotions,
        "notes": notes,
    }

    _mood_history.append(entry)

    # Calculate trend if we have enough data
    trend = _calculate_mood_trend()

    return {"entry": entry, "trend": trend, "total_entries": len(_mood_history)}


def _calculate_mood_trend() -> Dict[str, Any]:
    """Calculates mood trends from recent history."""
    global _mood_history

    if len(_mood_history) < 2:
        return {"status": "insufficient_data"}

    # Get last 7 entries
    recent = _mood_history[-7:]
    scores = [entry["mood_score"] for entry in recent]

    avg_score = sum(scores) / len(scores)

    # Calculate trend direction
    if len(scores) >= 3:
        recent_avg = sum(scores[-3:]) / 3
        older_avg = (
            sum(scores[:-3]) / len(scores[:-3]) if len(scores) > 3 else scores[0]
        )

        if recent_avg > older_avg + 1:
            direction = "improving"
        elif recent_avg < older_avg - 1:
            direction = "declining"
        else:
            direction = "stable"
    else:
        direction = "stable"

    return {
        "status": "calculated",
        "average_score": round(avg_score, 2),
        "direction": direction,
        "entries_analyzed": len(recent),
    }


# Resource Finder Tool
def get_crisis_resources(location: str = "us") -> Dict[str, Any]:
    """
    Retrieves crisis resources based on location.

    Args:
        location: Geographic location (us, international, etc.)

    Returns:
        Dict containing relevant resources with contact information
    """
    location_lower = location.lower()

    # Get resources for location
    if location_lower in CRISIS_RESOURCES:
        resources = CRISIS_RESOURCES[location_lower]
    else:
        # Default to US and international
        resources = {
            **CRISIS_RESOURCES.get("us", {}),
            **CRISIS_RESOURCES.get("international", {}),
        }

    return {
        "location": location,
        "resources": resources,
        "timestamp": datetime.now().isoformat(),
    }


# Coping Strategies Tool
_coping_strategies = {
    "anxiety": [
        "Deep breathing: 4-7-8 technique (inhale 4s, hold 7s, exhale 8s)",
        "Grounding: Name 5 things you see, 4 you hear, 3 you feel, 2 you smell, 1 you taste",
        "Progressive muscle relaxation",
        "Take a short walk or do light stretching",
    ],
    "panic": [
        "Find a safe, quiet space",
        "Focus on slow, deep breaths",
        "Ground yourself physically (feet on floor, hands on solid surface)",
        "Remind yourself: 'This will pass, I am safe'",
    ],
    "depression": [
        "Break tasks into smallest possible steps",
        "Reach out to one person, even just a text",
        "Get outside for 5 minutes if possible",
        "Do one small self-care activity",
    ],
    "stress": [
        "Take a 5-minute break from the stressor",
        "Write down what's bothering you",
        "Do a brief physical activity",
        "Practice mindful breathing",
    ],
    "overwhelm": [
        "Stop and take 3 deep breaths",
        "Make a list, prioritize just one thing",
        "Remove yourself from the situation temporarily if possible",
        "Ask for help with one specific task",
    ],
}


def get_coping_strategies(situation: str) -> Dict[str, Any]:
    """
    Returns evidence-based coping strategies for a specific situation.

    Args:
        situation: The mental health situation (anxiety, panic, depression, stress, overwhelm)

    Returns:
        Dict containing relevant coping strategies
    """
    situation_lower = situation.lower()
    strategies = _coping_strategies.get(situation_lower, _coping_strategies["stress"])

    return {
        "situation": situation,
        "strategies": strategies,
        "note": "These are immediate coping strategies. For ongoing concerns, please consult a mental health professional.",
    }


# Create ADK FunctionTool objects (ADK automatically extracts function signatures and docstrings)
crisis_detection_tool = FunctionTool(detect_crisis)
mood_tracking_tool = FunctionTool(log_mood)
resource_finder_tool = FunctionTool(get_crisis_resources)
coping_strategies_tool = FunctionTool(get_coping_strategies)
