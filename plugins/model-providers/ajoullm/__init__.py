"""Ajou LLM Gateway provider profile."""

from __future__ import annotations

import json
import logging
import ssl
import urllib.request
from dataclasses import dataclass

from providers import register_provider
from providers.base import ProviderProfile

logger = logging.getLogger(__name__)

_USER_AGENT = "AjouLLM-Agent/1.0"


@dataclass
class AjouLLMProfile(ProviderProfile):
    """AjouLLM Gateway — certifi SSL + User-Agent override for Mindlogic server compat."""

    def fetch_models(self, *, api_key: str | None = None, timeout: float = 8.0) -> list[str] | None:
        url = self.base_url.rstrip("/") + "/models"
        req = urllib.request.Request(url)
        if api_key:
            req.add_header("Authorization", f"Bearer {api_key}")
        req.add_header("Accept", "application/json")
        req.add_header("User-Agent", _USER_AGENT)

        try:
            import certifi
            ctx = ssl.create_default_context(cafile=certifi.where())
        except ImportError:
            ctx = None

        try:
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
                data = json.loads(resp.read().decode())
            items = data if isinstance(data, list) else data.get("data", [])
            return [m["id"] for m in items if isinstance(m, dict) and "id" in m]
        except Exception as exc:
            logger.debug("fetch_models(ajoullm): %s", exc)
            return None


ajoullm = AjouLLMProfile(
    name="ajoullm",
    aliases=("ajou", "factchat"),
    env_vars=("AJOULLM_API_KEY", "FACTCHAT_API_KEY"),
    display_name="Ajou LLM",
    description="Ajou University LLM API Gateway (Mindlogic)",
    signup_url="https://ajoullm.ajou.ac.kr/",
    fallback_models=(
        "claude-sonnet-4-6",
        "gemini-2.5-flash",
        "gpt-5.4-mini",
        "gemini-3.1-pro-preview",
        "gemini-3-flash-preview",
    ),
    base_url="https://factchat-cloud.mindlogic.ai/v1/gateway",
)

register_provider(ajoullm)
