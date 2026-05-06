"""Ajou LLM Gateway provider profile."""

from providers import register_provider
from providers.base import ProviderProfile

ajoullm = ProviderProfile(
    name="ajoullm",
    aliases=("ajou", "factchat"),
    env_vars=("AJOULLM_API_KEY", "FACTCHAT_API_KEY"),
    display_name="Ajou LLM",
    description="Ajou University LLM API Gateway (Mindlogic)",
    signup_url="https://ajoullm.ajou.ac.kr/",
    fallback_models=(
        "claude-sonnet-4-6",
        "gemini-3.1-pro-preview",
        "gemini-3-flash-preview",
    ),
    base_url="https://factchat-cloud.mindlogic.ai/v1/gateway",
)

register_provider(ajoullm)
