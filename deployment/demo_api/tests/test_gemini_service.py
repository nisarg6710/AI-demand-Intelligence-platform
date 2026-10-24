from types import SimpleNamespace

import pytest

from deployment.demo_api import gemini_service


def _fake_sdk(generate_content, captured):
    class FakeModels:
        def generate_content(self, **kwargs):
            captured["request"] = kwargs
            return generate_content(**kwargs)

    class FakeClient:
        def __init__(self, **kwargs):
            captured["client"] = kwargs
            self.models = FakeModels()

        def close(self):
            captured["closed"] = True

    fake_types = SimpleNamespace(
        HttpOptions=lambda **kwargs: {"http_options": kwargs},
        HttpRetryOptions=lambda **kwargs: {"retry_options": kwargs},
        GenerateContentConfig=lambda **kwargs: {"generation_config": kwargs},
    )
    return SimpleNamespace(Client=FakeClient), fake_types


@pytest.mark.parametrize("configured", [False, True])
def test_missing_gemini_configuration_does_not_load_sdk(monkeypatch, configured):
    if configured:
        monkeypatch.setenv("DEMO_GEMINI_API_KEY", "demo-only-key")
        monkeypatch.delenv("DEMO_GEMINI_MODEL", raising=False)
    else:
        monkeypatch.delenv("DEMO_GEMINI_API_KEY", raising=False)
        monkeypatch.delenv("DEMO_GEMINI_MODEL", raising=False)
    monkeypatch.setattr(
        gemini_service,
        "_load_sdk",
        lambda: pytest.fail("SDK must not load when settings are incomplete"),
    )

    assert gemini_service.answer_general_business_question("How can the project help?") is None


def test_gemini_service_uses_bounded_request_configuration(monkeypatch):
    monkeypatch.setenv("DEMO_GEMINI_API_KEY", "private-demo-key")
    monkeypatch.setenv("DEMO_GEMINI_MODEL", "test-model")
    captured = {}
    fake_genai, fake_types = _fake_sdk(
        lambda **_: SimpleNamespace(text="A concise general answer."), captured
    )
    monkeypatch.setattr(gemini_service, "_load_sdk", lambda: (fake_genai, fake_types))

    result = gemini_service.answer_general_business_question(
        "How can this project help the organization?"
    )

    assert result == "A concise general answer."
    assert captured["client"]["api_key"] == "private-demo-key"
    assert captured["client"]["http_options"]["http_options"]["timeout"] == 12_000
    assert captured["client"]["http_options"]["http_options"]["retry_options"]["retry_options"]["attempts"] == 1
    request = captured["request"]
    assert request["model"] == "test-model"
    assert request["contents"] == "How can this project help the organization?"
    config = request["config"]["generation_config"]
    assert config["max_output_tokens"] == 256
    assert "historical sales analytics" in config["system_instruction"]
    assert captured["closed"] is True


@pytest.mark.parametrize("response_text", [None, "", "   "])
def test_gemini_service_rejects_empty_responses(monkeypatch, response_text):
    monkeypatch.setenv("DEMO_GEMINI_API_KEY", "private-demo-key")
    monkeypatch.setenv("DEMO_GEMINI_MODEL", "test-model")
    fake_genai, fake_types = _fake_sdk(
        lambda **_: SimpleNamespace(text=response_text), {}
    )
    monkeypatch.setattr(gemini_service, "_load_sdk", lambda: (fake_genai, fake_types))

    assert gemini_service.answer_general_business_question("How can it help?") is None


def test_gemini_service_hides_provider_exception_details(monkeypatch, caplog):
    monkeypatch.setenv("DEMO_GEMINI_API_KEY", "private-demo-key")
    monkeypatch.setenv("DEMO_GEMINI_MODEL", "test-model")

    def fail(**_):
        raise RuntimeError("private-demo-key provider traceback details")

    fake_genai, fake_types = _fake_sdk(fail, {})
    monkeypatch.setattr(gemini_service, "_load_sdk", lambda: (fake_genai, fake_types))

    assert gemini_service.answer_general_business_question("How can it help?") is None
    assert "RuntimeError" in caplog.text
    assert "private-demo-key" not in caplog.text
    assert "traceback details" not in caplog.text


def test_gemini_service_rejects_oversized_question_without_sdk(monkeypatch):
    monkeypatch.setenv("DEMO_GEMINI_API_KEY", "private-demo-key")
    monkeypatch.setenv("DEMO_GEMINI_MODEL", "test-model")
    monkeypatch.setattr(
        gemini_service,
        "_load_sdk",
        lambda: pytest.fail("oversized question must not initialize Gemini"),
    )

    question = "x" * (gemini_service.MAX_QUESTION_LENGTH + 1)
    assert gemini_service.answer_general_business_question(question) is None
