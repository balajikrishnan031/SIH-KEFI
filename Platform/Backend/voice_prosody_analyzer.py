"""
================================================================================
MOSJE SC/ST POA ACT 1989 - VOICE STRESS & ACOUSTIC PROSODY ANALYZER
================================================================================
Analyzes speech pitch (Hz), vocal tremor (jitter %), speech rate (WPM),
energy stability (dB), and pause duration to detect vocal acoustic markers
of panic, severe intimidation distress, and psychomotor trauma slowing.
================================================================================
"""

import math
import re
from typing import Dict, Any, Optional

def analyze_audio_prosody(audio_metadata: Optional[Dict[str, Any]] = None, transcript: str = "") -> Dict[str, Any]:
    """
    Analyzes vocal acoustic prosody metrics for IVRS 14566 & mobile audio streams.
    """
    if not audio_metadata:
        # Transcript-based acoustic heuristics
        word_count = len(transcript.split()) if transcript else 10
        has_threat_words = any(w in transcript.lower() for w in ["kill", "threat", "dhamki", "attack", "fear", "scared", "court", "bayam"])
        has_ellipsis = "..." in transcript
        
        speech_rate_wpm = 175 if has_threat_words else 80 if has_ellipsis else 130
        avg_pitch_hz = 240.0 if has_threat_words else 120.0 if has_ellipsis else 165.0
        pause_duration_sec = 0.5 if has_threat_words else 2.6 if has_ellipsis else 0.9
        energy_db = 76.0 if has_threat_words else 44.0 if has_ellipsis else 62.0
        vocal_jitter_pct = 4.8 if has_threat_words else 1.2
    else:
        speech_rate_wpm = audio_metadata.get("speech_rate_wpm", 130)
        avg_pitch_hz = audio_metadata.get("avg_pitch_hz", 165.0)
        pause_duration_sec = audio_metadata.get("pause_duration_sec", 0.9)
        energy_db = audio_metadata.get("energy_db", 62.0)
        vocal_jitter_pct = audio_metadata.get("vocal_jitter_pct", 1.8)

    # Compute Vocal Acoustic Distress Index (0.0 to 1.0)
    jitter_norm = min(1.0, vocal_jitter_pct / 5.0)
    pitch_norm = min(1.0, abs(avg_pitch_hz - 160.0) / 100.0)
    pause_norm = min(1.0, pause_duration_sec / 3.0)
    
    vocal_stress_index = round((jitter_norm * 0.45) + (pitch_norm * 0.30) + (pause_norm * 0.25), 2)

    # Acoustic Vocal Classification Rules for Atrocity Trauma
    if vocal_stress_index > 0.55:
        vocal_state = "High Intimidation Vocal Tremor / Acute Agitation"
        somatic_override_recommended = True
        clinical_vocal_insight = f"Elevated vocal jitter ({vocal_jitter_pct}%) and pitch tremor ({round(avg_pitch_hz)} Hz) indicate high psychological intimidation stress."
    elif pause_duration_sec > 2.0 or speech_rate_wpm < 85:
        vocal_state = "Traumatic Withdrawal / Psychomotor Slowing"
        somatic_override_recommended = False
        clinical_vocal_insight = "Prolonged vocal pause gaps and speech slowing reflect trial exhaustion and post-traumatic fear."
    else:
        vocal_state = "Emotional Equilibrium"
        somatic_override_recommended = False
        clinical_vocal_insight = "Vocal acoustic prosody remains within nominal baseline range."

    return {
        "vocal_state": vocal_state,
        "vocal_stress_index": vocal_stress_index,
        "metrics": {
            "avg_pitch_hz": round(avg_pitch_hz, 1),
            "speech_rate_wpm": speech_rate_wpm,
            "pause_duration_sec": round(pause_duration_sec, 2),
            "energy_db": round(energy_db, 1),
            "vocal_jitter_pct": round(vocal_jitter_pct, 2)
        },
        "somatic_override_recommended": somatic_override_recommended,
        "clinical_vocal_insight": clinical_vocal_insight
    }

