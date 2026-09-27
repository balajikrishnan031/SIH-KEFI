"""
================================================================================
KEFI – AI-POWERED VICTIM MENTAL HEALTH & DISTRESS MONITORING SYSTEM
================================================================================
Greek Origin: Kéfi (Κέφι) — Spirit of joy, emotional vitality, passion & inner healing
Expansion: Kinematic Emotion & Forecasting Intervention System (KEFI)
MoSJE SC/ST Prevention of Atrocities Act 1989 (SIH 2026 PS 26094)

Mathematical Model for Dynamic Distress Score (DDS):
DDS = w1*E + w2*V + w3*B + w4*H + w5*C + w6*T

Where:
E = Emotion & Sentiment Indicators (0-100)
V = Voice Stress Indicators (0-100)
B = Behavioral Engagement Changes (missed check-ins) (0-100)
H = Historical Distress Trend Velocity (0-100)
C = Case-Related Risk Factors (court deposition, legal stage) (0-100)
T = Threat & Intimidation Indicators (0-100)

Weights: w1=0.25, w2=0.20, w3=0.15, w4=0.15, w5=0.10, w6=0.15 (Sum = 1.0)
================================================================================
"""

import math
import time
import json
import re
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta

# Configurable Weights for KEFI DDS Formula
KEFI_WEIGHTS = {
    "w1_emotion": 0.25,
    "w2_voice": 0.20,
    "w3_behavior": 0.15,
    "w4_history_trend": 0.15,
    "w5_case_factors": 0.10,
    "w6_threat_intimidation": 0.15
}

CASE_FACTOR_SCORES = {
    "Complaint Registered / FIR": 30.0,
    "Investigation & Charge Sheet": 45.0,
    "Court Trial & Witness Deposition": 85.0,  # Peak pressure stage
    "Compensation & Relief Processing": 35.0,
    "Rehabilitation & Protection": 25.0
}

def calculate_kefi_dynamic_distress_score(
    text_sentiment_score: float,        # 0.0 to 1.0 (Emotion/Sentiment E)
    vocal_stress_index: float,          # 0.0 to 1.0 (Voice Prosody V)
    missed_checkins_count: int = 0,     # Behavior change B (0-4+)
    historical_trend_velocity: float = 0.0, # Velocity H (-20 to +30)
    legal_stage: str = "Court Trial & Witness Deposition", # Case factor C
    threat_intimidation_flag: bool = False, # Threat indicator T
    immediate_safety_status: str = "Safe" # Separate Immediate Safety Check
) -> Dict[str, Any]:
    """
    Computes exact KEFI Dynamic Distress Score (DDS) using multi-signal weighted fusion.
    """
    # 1. E - Emotion & Sentiment (0-100)
    score_E = text_sentiment_score * 100.0
    
    # 2. V - Voice Stress (0-100)
    score_V = vocal_stress_index * 100.0
    
    # 3. B - Behavior Changes (missed check-ins, 0-100)
    score_B = min(100.0, missed_checkins_count * 30.0)
    
    # 4. H - Historical Trend Velocity (0-100)
    score_H = max(0.0, min(100.0, 50.0 + (historical_trend_velocity * 2.5)))
    
    # 5. C - Case-Related Factors (0-100)
    score_C = CASE_FACTOR_SCORES.get(legal_stage, 40.0)
    
    # 6. T - Threat / Intimidation Indicators (0-100)
    score_T = 90.0 if threat_intimidation_flag else 15.0
    
    # Mathematical Weighted Sum: DDS = w1*E + w2*V + w3*B + w4*H + w5*C + w6*T
    w = KEFI_WEIGHTS
    dds = (
        (w["w1_emotion"] * score_E) +
        (w["w2_voice"] * score_V) +
        (w["w3_behavior"] * score_B) +
        (w["w4_history_trend"] * score_H) +
        (w["w5_case_factors"] * score_C) +
        (w["w6_threat_intimidation"] * score_T)
    )
    
    # 3-Level Risk Band Classification (SIH Workflow Standard)
    if dds >= 61.0:
        risk_level = "RED / HIGH DISTRESS"
        risk_band = "⭕ Red (61–100)"
        action_recommendation = "Urgent counselling, crisis support, witness protection & emergency officer dispatch"
    elif dds >= 31.0:
        risk_level = "ORANGE / MODERATE DISTRESS"
        risk_band = "🟠 Orange (31–60)"
        action_recommendation = "Focused check-ins, scheduled counsellor follow-up & legal aid consultation"
    else:
        risk_level = "GREEN-YELLOW / LOW DISTRESS"
        risk_band = "🟢 Green / Yellow (0–30)"
        action_recommendation = "Routine support, self-help tools & automated periodic monitoring via NHAA 14566"
        
    return {
        "system_name": "KEFI",
        "greek_meaning": "Kéfi (Κέφι) — Spirit of joy, emotional vitality, passion & inner healing",
        "acronym_expansion": "Kinematic Emotion & Forecasting Intervention System",
        "dynamic_distress_score": dds,
        "risk_level": risk_level,
        "risk_band": risk_band,
        "action_recommendation": action_recommendation,
        "immediate_safety_status": immediate_safety_status, # Separate safety check
        "formula_weights": w,
        "sub_scores": {
            "E_emotion_sentiment": round(score_E, 1),
            "V_voice_stress": round(score_V, 1),
            "B_behavior_engagement": round(score_B, 1),
            "H_historical_trend": round(score_H, 1),
            "C_case_factors": round(score_C, 1),
            "T_threat_intimidation": round(score_T, 1)
        }
    }


def calculate_sahay_dynamic_distress_score(*args, **kwargs):
    """Wrapper function maintaining backwards compatibility."""
    return calculate_kefi_dynamic_distress_score(*args, **kwargs)

def calculate_dynamic_distress_score(*args, **kwargs):
    """Wrapper function maintaining backwards compatibility."""
    return calculate_kefi_dynamic_distress_score(*args, **kwargs)


def predict_longitudinal_trend(historical_dds_list: List[float], forecast_hours: int = 72) -> Dict[str, Any]:
    """
    Predicts future distress trajectory over 24h, 48h, 72h using time-series linear trend forecasting.
    """
    if not historical_dds_list:
        historical_dds_list = [22.0, 31.0, 43.0, 52.0, 61.0]
        
    n = len(historical_dds_list)
    if n == 1:
        latest = historical_dds_list[0]
        return {
            "historical": historical_dds_list,
            "forecast_24h": latest,
            "forecast_48h": latest,
            "forecast_72h": latest,
            "trajectory": "STABLE",
            "crisis_probability_72h": round(latest / 100.0, 2)
        }
        
    diffs = [historical_dds_list[i] - historical_dds_list[i-1] for i in range(1, n)]
    avg_velocity = sum(diffs) / len(diffs)
    
    latest_score = historical_dds_list[-1]
    f24 = max(0.0, min(100.0, round(latest_score + (avg_velocity * 1), 1)))
    f48 = max(0.0, min(100.0, round(latest_score + (avg_velocity * 2), 1)))
    f72 = max(0.0, min(100.0, round(latest_score + (avg_velocity * 3), 1)))
    
    if avg_velocity > 3.0:
        trajectory = "RAPIDLY ESCALATING"
    elif avg_velocity > 0.5:
        trajectory = "GRADUALLY INCREASING"
    elif avg_velocity < -0.5:
        trajectory = "IMPROVING / RECOVERING"
    else:
        trajectory = "STABLE"
        
    crisis_prob = max(0.0, min(1.0, round((f72 / 100.0) * (1.15 if avg_velocity > 0 else 0.85), 2)))
    
    return {
        "historical": historical_dds_list,
        "forecast_24h": f24,
        "forecast_48h": f48,
        "forecast_72h": f72,
        "distress_velocity": round(avg_velocity, 1),
        "trajectory": trajectory,
        "elevated_risk_prediction": f"Elevated distress risk predicted within next 7 days (72h Forecast: {f72}/100)"
    }

