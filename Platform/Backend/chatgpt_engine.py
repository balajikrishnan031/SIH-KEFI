"""
KEFFI LOCAL SLM CHATGPT ADAPTER
===============================
Redirects all chatgpt calls to local PyTorch SLM & Local CBT Engine.
100% Private, Zero External API Dependency.
"""

from groq_engine import get_keffi_reply

def ask_chatgpt(prompt: str, system_prompt: str = "") -> str:
    """Redirects prompt to local Keffi SLM inference engine."""
    return get_keffi_reply(prompt, system_prompt)
