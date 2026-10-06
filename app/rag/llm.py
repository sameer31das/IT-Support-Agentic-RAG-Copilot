from functools import lru_cache

from langchain_cerebras import ChatCerebras

from app.core.config import get_settings


@lru_cache
def get_chat_model() -> ChatCerebras:
    settings = get_settings()
    if not settings.cerebras_api_key:
        raise RuntimeError("CEREBRAS_API_KEY is missing")

    return ChatCerebras(
        model=settings.cerebras_model,
        api_key=settings.cerebras_api_key,
    )