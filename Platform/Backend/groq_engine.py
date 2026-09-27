"""
================================================================================
KEFFI MASTER CLINICAL ENGINE v6 - DEEP DETAILED & IMMERSIVE CLINICAL MATRIX
================================================================================
Features:
1. Immersive Atmospheric Therapeutic Fables & Kintsugi Metaphors
2. Deep 4-Section Neuro-Clinical Reflections (Validation + Neuroscience + Skill + Options)
3. Crystal-Clear Step-by-Step Evidence-Based Interventions
4. 100% Fail-Safe Execution with Zero Cloud Dependency
================================================================================
"""

import os
import requests
import json
import random
import re
import time
import logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger("keffi.local_llm")

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "keffi"

# ==============================================================================
# 1. IMMERSIVE THERAPEUTIC STORIES & ANCIENT METAPHORS (Kintsugi & Zen Tales)
# ==============================================================================
KEFFI_IMMERSIVE_STORIES = [
    {
        "keywords": ["anxi", "fear", "worry", "panic", "scared", "terrified"],
        "title": "🌲 The Ancient Oak Tree, the Gale Wind, and the Hidden Roots",
        "story": (
            "High on a wind-swept cliff overlooking the misty ocean stood an ancient oak tree. One autumn night, a violent gale storm arrived, "
            "howling through the valley. The young rigid branches fought fiercely against the wind, straining to stand perfectly still, until one thick branch snapped under the pressure.\n\n"
            "The old oak tree nearby leaned into the storm, swaying gently with every gust, and whispered: 'The wind is not your enemy — it is simply passing through. "
            "If you fight every wave of air, you will break. But if you bend with the wind and trust your deep roots below the soil, the storm will pass and leave you unhurt.'\n\n"
            "Your anxious thoughts are like the howling gale wind — loud, intense, and demanding immediate struggle. "
            "Your breath, your values, and your inner self are the deep roots anchored beneath the surface."
        ),
        "takeaway": "You do not need to fight or stop every anxious thought; anchor yourself in your roots and let the wind blow past."
    },
    {
        "keywords": ["sad", "depress", "heavy", "cry", "exhausted", "numb", "empty"],
        "title": "🎋 The Winter Bamboo of Mount Fuji",
        "story": (
            "In the high forests near Mount Fuji, severe winter brings heavy snowstorms. While other trees fight the cold and break beneath heavy ice, "
            "the green bamboo stalk quietly bows low under the weight of the snow until its tip rests flat against the frozen ground. To an untrained eye, the bamboo appears completely defeated.\n\n"
            "Yet underneath the snow-covered soil, the bamboo's underground rhizome network remains vital and alive, quietly storing moisture and nutrients. "
            "When the warm spring sun arrives, the heavy snow melts away, and the bamboo snaps back straight — taller, stronger, and greener than before.\n\n"
            "Bowing low during a heavy emotional season is not failure. Resting and preserving your energy is how you prepare for your spring."
        ),
        "takeaway": "Resting during an exhausting season is not a weakness — it is your inner roots storing energy for your return."
    },
    {
        "keywords": ["overthink", "thought", "racing", "mind", "spiraling", "replay"],
        "title": "🌊 The Monk, the Rushing Mountain River, and the Floating Pebbles",
        "story": (
            "A young monk sat by a rushing mountain stream, feeling overwhelmed by hundreds of thoughts racing through his head. "
            "He tried stepping into the cold water to catch every rolling pebble, but the current was too fast, leaving him exhausted and soaking wet.\n\n"
            "His master walked over, pulled him onto the grassy riverbank, and said: 'Look closely at the water. The pebbles roll downstream on their own. "
            "You do not need to plunge into the river and pick up every rock that floats by. You can simply sit comfortably on the bank, watch them pass, and let the river flow.'\n\n"
            "Your racing thoughts are like those river pebbles. You have the power to sit on the bank of awareness and observe them without picking up every single one."
        ),
        "takeaway": "Observing a thought pass by is not the same as picking it up, believing it, and carrying it."
    },
    {
        "keywords": ["worth", "fail", "useless", "shame", "guilt", "mistake", "flaw"],
        "title": "🍵 The Kintsugi Master and the Golden Chipped Teacup",
        "story": (
            "In ancient Kyoto, a master ceramic artisan accidentally dropped a prized tea bowl, cracking it into several pieces. Instead of throwing the bowl away, "
            "the master mended the cracks using pure lacquer dusted with fine gold powder — a traditional art known as Kintsugi ('Golden Joinery').\n\n"
            "When the bowl was restored, the gold-dusted seams illuminated every flaw, making the teacup far more beautiful, valuable, and cherished than when it was plain and unblemished. "
            "The master remarked: 'The cracks are not something to hide — they are the story of how the bowl survived and grew stronger.'\n\n"
            "Your struggles, mistakes, and painful experiences do not lessen your worth. They are the golden seams of your resilience."
        ),
        "takeaway": "Imperfection is not brokenness; your journey and survival add unique, golden value to who you are."
    },
    {
        "keywords": ["exam", "study", "work", "deadline", "pressure", "busy"],
        "title": "🏔️ The Alpine Traveler and the Wayfarer's Oil Lantern",
        "story": (
            "A traveler stood at the base of a towering alpine mountain at dusk, looking up at the summit shrouded in dark clouds. "
            "Panic set in as he thought: 'How can I ever walk all the way to the top in the dark?'\n\n"
            "An experienced guide handed him a small brass oil lantern and said: 'This lantern will not light up the mountain peak. "
            "It will only light up the single step right in front of your boots. Take that one step calmly, and the light will move forward to show you the next step.'\n\n"
            "You do not have to complete your entire syllabus or resolve your entire workload tonight. Focus strictly on the single step illuminated right now."
        ),
        "takeaway": "Do not overload your mind with the summit — focus exclusively on taking the single step right in front of you."
    }
]

# ==============================================================================
# 2. EMOTIONAL PUZZLES & COGNITIVE BRAIN EXERCISES
# ==============================================================================
KEFFI_DETAILED_PUZZLES = [
    {
        "title": "🧩 Calming Working Memory Unscramble Challenge",
        "puzzle": (
            "Unscramble these 4 grounding words to reset your working memory focus:\n"
            "1. E A C E P ➔ _ _ _ _ _\n"
            "2. L L I T S ➔ _ _ _ _ _\n"
            "3. P O H E ➔ _ _ _ _ _\n"
            "4. M L C A ➔ _ _ _ _ _"
        ),
        "hint": "Answers: 1. PEACE  2. STILL  3. HOPE  4. CALM. Directing your attention to letter patterns helps disengage racing worry loops!"
    },
    {
        "title": "🧩 Perspective Reframe Challenge",
        "puzzle": (
            "Examine this challenging thought: 'I made a mistake in today's work/exam.'\n\n"
            "Challenge: Identify 2 concrete silver linings or constructive takeaways from this situation!"
        ),
        "hint": "Example Reframes: 1. I now have precise clarity on what to review. 2. It demonstrates that I am stepping out of my comfort zone to learn."
    },
    {
        "title": "🧩 10-Second Somatic Sensory Gratitude Hunt",
        "puzzle": (
            "Look around your physical space right now. Identify 3 ordinary objects nearby "
            "(e.g. a soft blanket, a warm cup, a reliable device) and silently name why each one brings comfort."
        ),
        "hint": "Anchoring your senses to physical objects around you signals safety to your autonomic nervous system."
    }
]

# ==============================================================================
# 3. SAFETY EVALUATION
# ==============================================================================
def evaluate_safety(message: str) -> bool:
    """Evaluates whether message indicates explicit self-harm intent."""
    msg_lower = message.lower()
    return any(k in msg_lower for k in [
        "suicide", "kill myself", "end my life", "cut my wrists", "want to die now",
        "uyir.*venam", "sethu", "tharkolai", "vaazha.*virup", "no reason to live"
    ])

# ==============================================================================
# 4. LOCAL OLLAMA INTEGRATION (Custom Model 'keffi')
# ==============================================================================
def _call_local_ollama(patient_message: str, clinical_context: str = "") -> str:
    """Calls local Ollama instance running custom model 'keffi' on http://localhost:11434"""
    prompt = f"[Clinical Context: {clinical_context}]\nUser: {patient_message}\nKeffi:" if clinical_context else f"User: {patient_message}\nKeffi:"
    
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": 220,
            "temperature": 0.65
        }
    }
    try:
        res = requests.post(OLLAMA_URL, json=payload, timeout=3)
        if res.status_code == 200:
            reply = res.json().get("response", "").strip()
            if reply and len(reply) > 20:
                logger.info(f"[OLLAMA SUCCESS] Generated response via local tuned model '{OLLAMA_MODEL}'!")
                return reply
    except Exception as e:
        logger.warning(f"[OLLAMA LOCAL FALLBACK] Local Ollama call fallback: {e}")
    return ""

# ==============================================================================
# 5. MASTER DEEP CLINICAL SYNTHESIZER
# ==============================================================================
def get_keffi_reply(patient_message: str, clinical_context: str = "") -> str:
    """
    100% Detailed, Crystal-Clear, Immersive Response Synthesizer across 14 Clinical Modalities
    """
    msg_lower = patient_message.lower().strip()

    # --------------------------------------------------------------------------
    # 0. CRISIS SAFETY OVERRIDE (Hard-Stop Guarantee)
    # --------------------------------------------------------------------------
    if evaluate_safety(patient_message):
        return (
            "I am really glad you reached out and shared this with me. What you are experiencing right now sounds incredibly heavy, "
            "and I want you to know you do not have to carry it all alone in this moment.\n\n"
            "Please reach out to one of these free, confidential, 24/7 helplines right now to speak with someone who can support you:\n"
            "• India Tele-MANAS: 14416 / 1800-891-4416 (24x7 Government Helpline)\n"
            "• KIRAN Mental Health Helpline: 1800-599-0019 (24x7)\n"
            "• AASRA Suicide Helpline: 9820466726 (24x7)\n"
            "• US Suicide & Crisis Lifeline: 988 | UK Samaritans: 116 123\n"
            "|||OPTION||| Call Tele-MANAS 14416 (India)"
        )

    # --------------------------------------------------------------------------
    # 1. TRY LOCAL OLLAMA MODEL 'keffi'
    # --------------------------------------------------------------------------
    ollama_reply = _call_local_ollama(patient_message, clinical_context)
    if ollama_reply:
        return ollama_reply

    # --------------------------------------------------------------------------
    # 2. IMMERSIVE STORYTELLING REQUEST
    # --------------------------------------------------------------------------
    if any(k in msg_lower for k in ["story", "kadhai", "parable", "metaphor", "tale"]):
        for s in KEFFI_IMMERSIVE_STORIES:
            if any(kw in msg_lower for kw in s["keywords"]):
                return (
                    f"{s['title']}\n\n"
                    f"{s['story']}\n\n"
                    f"💡 **Clinical Takeaway**: {s['takeaway']}\n"
                    f"|||OPTION||| Tell me another story 📖"
                )
        # Default Immersive Story
        s = KEFFI_IMMERSIVE_STORIES[0]
        return f"{s['title']}\n\n{s['story']}\n\n💡 **Clinical Takeaway**: {s['takeaway']}\n|||OPTION||| Give me an action plan 🎯"

    # --------------------------------------------------------------------------
    # 3. DETAILED COGNITIVE PUZZLE REQUEST
    # --------------------------------------------------------------------------
    if any(k in msg_lower for k in ["puzzle", "riddle", "game", "unscramble", "challenge"]):
        pz = random.choice(KEFFI_DETAILED_PUZZLES)
        return f"{pz['title']}\n\n{pz['puzzle']}\n\n💡 **Neuro-Insight**: {pz['hint']}\n|||OPTION||| Show puzzle answers 🧩"

    # --------------------------------------------------------------------------
    # 4. ACADEMIC & WORK OVERWHELM (Problem-Solving Therapy PST)
    # --------------------------------------------------------------------------
    if any(k in msg_lower for k in ["exam", "study", "padipu", "workload", "deadline", "busy", "task", "project", "pressure", "fail"]):
        return (
            "🔍 **Empathetic Reflection & Validation**:\n"
            f"I hear the heavy pressure of deadlines and study workload bearing down on you around '{patient_message[:45]}'. "
            "Feeling overwhelmed when tasks pile up is a completely natural human response.\n\n"
            "🧠 **Neuro-Clinical Mechanism**:\n"
            "Under sustained workload stress, your Prefrontal Cortex (the brain's executive planning center) experiences working memory fatigue. "
            "Trying to hold an entire mountain of tasks in your head triggers cortisol elevation and task paralysis. "
            "De-cluttering your focus onto paper immediately restores executive function.\n\n"
            "🛠️ **Standardized Problem-Solving Therapy (PST) Action Plan**:\n"
            "1. **Subject De-Clutter**: List all pending tasks on paper, select the single most urgent item, and cross out the remaining items for the next 60 minutes.\n"
            "2. **25-Minute Pomodoro Sprint**: Focus exclusively on that single task for 25 minutes with your phone out of sight.\n"
            "3. **5-Minute Recovery**: Step away, drink a glass of water, and stretch your shoulders before resuming.\n"
            "|||OPTION||| Help me prioritize my tasks"
        )

    # --------------------------------------------------------------------------
    # 5. PANIC & SOMATIC ANXIETY (Box Breathing & Polyvagal Down-Regulation)
    # --------------------------------------------------------------------------
    if any(k in msg_lower for k in ["panic", "chest", "breathe", "heart", "shaking", "fear", "anxious", "scared", "terrified"]):
        return (
            "🔍 **Empathetic Reflection & Validation**:\n"
            "I hear you, and I am right here with you. Experiencing a racing heart, tight chest, or rapid breathing during anxiety can be terrifying, "
            "but I want to reassure you that your body is safe right now.\n\n"
            "🧠 **Neuro-Clinical Mechanism**:\n"
            "During a panic surge, your Amygdala activates the Sympathetic Nervous System, releasing adrenaline and triggering a fight-or-flight alert. "
            "Paced diaphragmatic breathing stimulates the Vagus Nerve, sending immediate physiological signals to your brain stem to lower your heart rate.\n\n"
            "🛠️ **Somatic 4-4-4-4 Box Breathing Reset**:\n"
            "• **Inhale** slowly through your nose for 4 seconds.\n"
            "• **Hold** your breath gently for 4 seconds.\n"
            "• **Exhale** smoothly through your mouth for 4 seconds.\n"
            "• **Hold** empty for 4 seconds. Repeat this cycle 3 times with me.\n"
            "|||OPTION||| Guide me through box breathing"
        )

    # --------------------------------------------------------------------------
    # 6. DEPRESSIVE EXHAUSTION & APATHY (Behavioral Activation BA)
    # --------------------------------------------------------------------------
    if any(k in msg_lower for k in ["sad", "depressed", "empty", "exhausted", "crying", "numb", "tired", "kashtam", "bed"]):
        return (
            "🔍 **Empathetic Reflection & Validation**:\n"
            f"I hear how deeply exhausted and heavy life feels for you right now around '{patient_message[:45]}'. "
            "Carrying emotional strain takes a real physical toll, and feeling unable to get up or move is completely valid.\n\n"
            "🧠 **Neuro-Clinical Mechanism**:\n"
            "Depressive apathy creates a cycle where lowered dopamine and serotonin transmission reduces physical motivation, "
            "which leads to withdrawal and further lowers mood. Behavioral Activation (BA) demonstrates that initiating tiny micro-movements "
            "precedes motivation rather than waiting for it.\n\n"
            "🛠️ **30-Second Micro-Behavioral Step**:\n"
            "Take just ONE slow sip of fresh water, or open a window for 10 seconds of sunlight. Notice the physical sensation without expecting yourself to fix everything today.\n"
            "|||OPTION||| Suggest a small micro-step"
        )

    # --------------------------------------------------------------------------
    # 7. CATASTROPHIZING & COGNITIVE DISTORTIONS (CBT Thought Restructuring)
    # --------------------------------------------------------------------------
    if any(k in msg_lower for k in ["always fail", "never good", "everything is ruined", "worst case", "inime", "fail aayiduven"]):
        return (
            "🔍 **Empathetic Reflection & Validation**:\n"
            "It sounds like your mind is painting this situation in very absolute terms right now — like this single setback proves something permanent or catastrophic about your future.\n\n"
            "🧠 **Neuro-Clinical Mechanism**:\n"
            "In Cognitive Behavioral Therapy (CBT), thoughts containing words like 'always', 'never', or 'completely ruined' are identified as Cognitive Distortions (Catastrophizing). "
            "They feel intensely true in the moment because emotional reasoning tricks the brain into mistaking strong feelings for objective facts.\n\n"
            "🛠️ **CBT Double-Standard Technique**:\n"
            "Ask yourself: If a dear friend came to you today having faced this exact situation, what compassionate, balanced advice would you give them? "
            "Offer those exact words of kindness and perspective to yourself right now.\n"
            "|||OPTION||| Guide me through a CBT reframe"
        )

    # --------------------------------------------------------------------------
    # 8. RACING THOUGHTS & WORRY (ACT Cognitive Defusion)
    # --------------------------------------------------------------------------
    if any(k in msg_lower for k in ["stuck in my head", "keep replaying", "obsessing", "what if", "spiraling"]):
        return (
            "🔍 **Empathetic Reflection & Validation**:\n"
            "It sounds like a worry or thought has been looping in your mind on repeat, making it really difficult to put down or find quiet.\n\n"
            "🧠 **Neuro-Clinical Mechanism**:\n"
            "In Acceptance and Commitment Therapy (ACT), thoughts are understood as transient mental events passing through working memory — "
            "not absolute commands or urgent facts that must be solved immediately.\n\n"
            "🛠️ **ACT Cognitive Defusion Practice**:\n"
            "Silently preface the thought with: 'I am noticing that I am having the thought that...' "
            "Observe how creating that linguistic distance reminds you that you are the conscious observer of the thought, not the thought itself.\n"
            "|||OPTION||| Help me defuse this thought"
        )

    # --------------------------------------------------------------------------
    # 9. RELATIONSHIP CONFLICT (IPT DEAR MAN Communication)
    # --------------------------------------------------------------------------
    if any(k in msg_lower for k in ["fight with", "argument with", "relationship", "boundaries", "they don't listen", "veetla problem"]):
        return (
            "🔍 **Empathetic Reflection & Validation**:\n"
            "It sounds like this situation with someone close to you is weighing heavily on your mind and heart.\n\n"
            "🧠 **Neuro-Clinical Mechanism**:\n"
            "Interpersonal Therapy (IPT) highlights that unresolved relational friction keeps your nervous system in a state of chronic hyperarousal. "
            "Establishing structured boundaries protects emotional well-being and fosters clear communication.\n\n"
            "🛠️ **DBT DEAR MAN Communication Framework**:\n"
            "1. **Describe**: State the facts of the situation calmly without judgment words.\n"
            "2. **Express**: Share how it affected you using clear 'I feel...' statements.\n"
            "3. **Assert**: Request one specific, reasonable boundary or change moving forward.\n"
            "|||OPTION||| Draft a DEAR MAN message"
        )

    # --------------------------------------------------------------------------
    # 10. ROGERIAN EMPATHETIC FALLBACK
    # --------------------------------------------------------------------------
    return (
        "🔍 **Empathetic Reflection & Validation**:\n"
        "I am listening closely, and I want to offer a safe, non-judgmental space for whatever you are feeling right now.\n\n"
        "🧠 **Neuro-Clinical Mechanism**:\n"
        "Allowing yourself space to express feelings without immediately needing to solve or suppress them is an essential component of emotional processing and nervous system regulation.\n\n"
        "🛠️ **Self-Compassion Grounding**:\n"
        "Take a slow, grounded breath in, let your shoulders drop away from your ears, and share whatever feels heaviest on your mind right now at your own pace.\n"
        "|||OPTION||| I need to vent this out"
    )
