"""
LLM provider setup — selects Gemini, Groq, or Local (Ollama) based on .env.

Usage
-----
.. code-block:: python

    from demos.shared.llm_setup import get_llm

    llm = get_llm()
    # llm is a langchain_core.language_models.chat_models.BaseChatModel
"""

from __future__ import annotations

import os

from dotenv import load_dotenv
from langchain_core.language_models.chat_models import BaseChatModel

load_dotenv()


def get_llm() -> BaseChatModel:
    """Return a chat model based on the ``LLM_PROVIDER`` env variable.

    Supported providers
    -------------------
    - ``gemini`` → :class:`langchain_google_genai.ChatGoogleGenerativeAI`
    - ``groq``   → :class:`langchain_groq.ChatGroq`
    - ``local``  → :class:`langchain_ollama.ChatOllama`

    Raises
    ------
    ValueError
        If ``LLM_PROVIDER`` is unset or contains an unknown value.
    """
    provider = os.getenv("LLM_PROVIDER", "gemini").lower().strip()

    if provider == "gemini":
        from langchain_google_genai import ChatGoogleGenerativeAI

        return ChatGoogleGenerativeAI(
            model=os.getenv("GEMINI_MODEL", "gemini-2.0-flash"),
            api_key=os.getenv("GEMINI_API_KEY"),
        )

    if provider == "groq":
        from langchain_groq import ChatGroq

        return ChatGroq(
            model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
            api_key=os.getenv("GROQ_API_KEY"),
        )

    if provider == "local":
        from langchain_ollama import ChatOllama

        return ChatOllama(
            model=os.getenv("LOCAL_MODEL", "llama3"),
            base_url=os.getenv("LOCAL_BASE_URL", "http://localhost:11434"),
        )

    msg = f"Unknown LLM_PROVIDER={provider!r}. Expected one of: gemini, groq, local"
    raise ValueError(msg)
