"""
================================================================================
KEFFI CLINICAL AI BRAIN - EXPANDED WORLD KNOWLEDGE & DIALOGUE ENGINE
================================================================================
Capabilities:
- 10-Therapy Methodology Execution (CBT, DBT, ACT, Somatic, Rogerian, CFT, PST, BA, IPT, REBT)
- Therapeutic Storytelling & Custom Parables (Mindful Metaphors)
- Solution Prediction & Action Plan Generator (Multi-step Resolution Roadmaps)
- Emotional Puzzles & Cognitive Brain Games (Mindfulness Maze, Gratitude Hunt, Word Anchor)
- General Knowledge & World Facts
================================================================================
"""

import json
import re
import random
from typing import Dict, Any, List, Optional

# ==============================================================================
# 1. THERAPEUTIC STORIES & CUSTOM PARABLES (உவமைக் கதைகள்)
# ==============================================================================
KEFFI_THERAPEUTIC_STORIES = {
    "anxiety": {
        "title": "The Oak Tree and the Gale Wind",
        "story": (
            "Once, a mighty oak tree stood on a cliff during a stormy night. The wind howled and demanded the tree bend or break. "
            "The rigid branches fought the wind until one snapped. But the deep roots beneath the earth held firm, anchoring the tree.\n\n"
            "Anxiety is like the gale wind — loud, intense, and demanding. But your core values and inner breath are the deep roots that keep you anchored. "
            "The storm passes, but the roots remain."
        ),
        "moral": "You do not need to fight every thought; focus on anchoring your roots."
    },
    "depression": {
        "title": "The Bamboo in Winter",
        "story": (
            "In the coldest winter, bamboo shoots bend under heavy snow until they lie flat against the ground. "
            "To a passerby, they appear defeated. But underneath the cold soil, the bamboo's underground rhizome system is storing energy for spring. "
            "When the sun returns, the snow melts, and the bamboo snaps back taller than before.\n\n"
            "Resting during a heavy season is not defeat — it is storing energy for your return."
        ),
        "moral": "Exhaustion is a call for deep rest, not a sign of permanent failure."
    },
    "overthinking": {
        "title": "The River and the Pebbles",
        "story": (
            "A traveler stood by a rushing river, trying to catch every pebble rolling along the riverbed. "
            "The faster he reached down, the more exhausted he became, and the river remained full of rocks.\n\n"
            "A wise monk walked by and said: 'Sit on the bank and watch the pebbles roll by. You do not need to pick up every rock that moves.'\n\n"
            "Your thoughts are like the river's pebbles. You can simply sit on the bank and let them pass."
        ),
        "moral": "Observing a thought is not the same as picking it up and carrying it."
    },
    "self_worth": {
        "title": "The Chipped Teacup",
        "story": (
            "In an ancient tea house, there was a handcrafted ceramic teacup with a small chip along its rim. "
            "The potter offered to throw it away, but the tea master refused, saying: 'The chip shows it has lived, held warmth, and served others. It makes it unique.'\n\n"
            "Your flaws and struggles do not lessen your worth — they are part of your human story."
        ),
        "moral": "imperfection does not mean brokenness; you possess inherent value."
    }
}

# ==============================================================================
# 2. EMOTIONAL PUZZLES & COGNITIVE BRAIN GAMES (மனநல புதிர்கள்)
# ==============================================================================
KEFFI_COGNITIVE_PUZZLES = [
    {
        "type": "Word Anchor",
        "title": "🧩 Calming Word Unscramble",
        "puzzle": "Unscramble these 3 calming words to focus your working memory:\n1. E A C E P -> _ _ _ _ _\n2. L L I T S -> _ _ _ _ _\n3. L A X E R -> _ _ _ _ _",
        "answer": "Answers: 1. PEACE  2. STILL  3. RELAX. How did that feel for your focus?"
    },
    {
        "type": "Perspective Reframe",
        "title": "🧩 Perspective Reframe Challenge",
        "puzzle": "Look at this scenario: 'I made a mistake in today's presentation.'\nChallenge: Find 2 hidden silver linings or learning points from this scenario!",
        "answer": "Example Reframes: 1. Now I know exactly what to improve next time. 2. It proved I am willing to step out of my comfort zone."
    },
    {
        "type": "Gratitude Hunt",
        "title": "🧩 10-Second Gratitude Hunt",
        "puzzle": "Name 3 small, simple physical things within arm's reach that you are thankful for right now (e.g. a soft pillow, a warm drink, a working phone).",
        "answer": "Great job! Noticing small physical comforts helps ground the autonomic nervous system."
    }
]

# ==============================================================================
# 3. SOLUTION PREDICTION & ACTION PLANNER
# ==============================================================================
def predict_solution_roadmap(query: str) -> str:
    """Predicts a structured multi-step action plan based on user problem context."""
    q_lower = query.lower()
    
    if any(k in q_lower for k in ["exam", "study", "marks", "fail", "score"]):
        return (
            "🎯 **Predicted 3-Step Exam Pressure Resolution Plan**:\n"
            "1. **De-clutter**: Pick ONE subject chapter for the next 25 minutes.\n"
            "2. **Pomodoro Sprint**: Study 25 minutes, then step away for a 5-minute glass-of-water break.\n"
            "3. **Micro-Test**: Write down 3 key concepts from memory without checking notes."
        )
    elif any(k in q_lower for k in ["sleep", "insomnia", "night", "awake"]):
        return (
            "🎯 **Predicted 3-Step Sleep Hygiene Reset Plan**:\n"
            "1. **Brain Dump**: Write down all racing thoughts on paper to clear working memory.\n"
            "2. **Screen Off**: Place your phone across the room 30 minutes before sleep.\n"
            "3. **Somatic Body Scan**: Progressively tense and release your toes, calves, and shoulders for 2 minutes."
        )
    elif any(k in q_lower for k in ["relationship", "fight", "friend", "family", "misunderstanding"]):
        return (
            "🎯 **Predicted 3-Step Relationship Communication Plan (DBT DEAR MAN)**:\n"
            "1. **Describe**: State the facts calmly without placing blame.\n"
            "2. **Express**: Share how the situation made you feel using 'I' statements.\n"
            "3. **Ask**: Request one specific, reasonable change moving forward."
        )
    else:
        return (
            "🎯 **Predicted 3-Step General Wellness Plan**:\n"
            "1. **Acknowledge**: Validate your current feeling without fighting it.\n"
            "2. **Ground**: Take 3 slow, deep breaths (4-4-4-4 Box Breathing).\n"
            "3. **Micro-Action**: Perform ONE tiny physical self-care action right now."
        )

# ==============================================================================
# 4. INTELLIGENT DIALOGUE PROTOCOL
# ==============================================================================
class KeffiIntelligentDialogueProtocol:
    """
    Analyzes any user input and determines the precise response protocol:
    - THERAPEUTIC_STORY: Inspiring metaphors
    - COGNITIVE_PUZZLE: Brain games & riddles
    - SOLUTION_PREDICTION: Multi-step action roadmaps
    - CLINICAL_THERAPY: 3-tier CBT/DBT counseling
    """
    
    @staticmethod
    def classify_and_reply(user_input: str) -> Dict[str, Any]:
        text = user_input.lower().strip()

        # 1. Therapeutic Story Request
        if any(k in text for k in ["story", "kadhai", "parable", "metaphor", "tale"]):
            if any(k in text for k in ["anxi", "fear", "worry", "panic"]):
                s = KEFFI_THERAPEUTIC_STORIES["anxiety"]
            elif any(k in text for k in ["sad", "depress", "heavy", "cry"]):
                s = KEFFI_THERAPEUTIC_STORIES["depression"]
            elif any(k in text for k in ["overthink", "thought", "racing", "mind"]):
                s = KEFFI_THERAPEUTIC_STORIES["overthinking"]
            else:
                s = KEFFI_THERAPEUTIC_STORIES["self_worth"]

            reply = f"📖 **{s['title']}**\n\n{s['story']}\n\n💡 **Takeaway**: {s['moral']}"
            return {"protocol": "THERAPEUTIC_STORY", "reply": reply, "options": ["Tell me another story 📖", "Give me a puzzle 🧩", "I need an action plan 🎯"]}

        # 2. Puzzle / Brain Game Request
        if any(k in text for k in ["puzzle", "riddle", "game", "brain", "challenge", "unscramble"]):
            pz = random.choice(KEFFI_COGNITIVE_PUZZLES)
            reply = f"{pz['title']}\n\n{pz['puzzle']}\n\n|||HINT||| Take your time, no rush!"
            return {"protocol": "COGNITIVE_PUZZLE", "reply": reply, "options": ["Show puzzle answer 🧩", "Give me an action plan 🎯", "Tell me a story 📖"]}

        # 3. Action Plan / Solution Request
        if any(k in text for k in ["solution", "plan", "roadmap", "steps", "how to solve"]):
            plan = predict_solution_roadmap(text)
            return {"protocol": "SOLUTION_PREDICTION", "reply": plan, "options": ["Give me a puzzle 🧩", "Tell me a story 📖", "I need to vent 💬"]}

        # 4. Default Clinical Counseling
        import keffi_own_clinical_dataset_engine as own_engine
        return own_engine.generate_own_keffi_response(user_input)
