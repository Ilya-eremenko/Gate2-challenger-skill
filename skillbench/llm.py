from __future__ import annotations

from dataclasses import dataclass
import json
import os
from typing import Protocol
from urllib import error, request


@dataclass(frozen=True)
class LLMCall:
    task: str
    system: str
    user: str
    model: str


class LLMClient(Protocol):
    def complete(self, *, task: str, system: str, user: str, model: str) -> str:
        ...


class FakeLLMClient:
    def __init__(self, responses: dict[str, str]):
        self.responses = responses
        self.calls: list[LLMCall] = []

    def complete(self, *, task: str, system: str, user: str, model: str) -> str:
        self.calls.append(LLMCall(task=task, system=system, user=user, model=model))
        if task not in self.responses:
            raise KeyError(f"No fake response configured for task: {task}")
        return self.responses[task]


class OpenAICompatibleLLMClient:
    def __init__(self, api_key: str | None = None, base_url: str | None = None, timeout: int = 120):
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        self.base_url = (base_url or os.environ.get("OPENAI_BASE_URL") or "https://api.openai.com/v1").rstrip("/")
        self.timeout = timeout
        if not self.api_key:
            raise RuntimeError("OPENAI_API_KEY is required for live LLM runs")

    def complete(self, *, task: str, system: str, user: str, model: str) -> str:
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": 0,
        }
        body = json.dumps(payload).encode("utf-8")
        http_request = request.Request(
            f"{self.base_url}/chat/completions",
            data=body,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with request.urlopen(http_request, timeout=self.timeout) as response:
                response_body = response.read().decode("utf-8")
        except error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"LLM request failed for {task}: {exc.code} {detail}") from exc
        except error.URLError as exc:
            raise RuntimeError(f"LLM request failed for {task}: {exc.reason}") from exc

        data = json.loads(response_body)
        return data["choices"][0]["message"]["content"]
