"""Deterministic intent routing for the public demo's fixed analytics API."""

from __future__ import annotations

from dataclasses import dataclass
import re


MAX_RANKING_LIMIT = 100


@dataclass(frozen=True)
class ChatRoute:
    intent: str | None
    limit: int = 10
    status: str = "supported"
    reason: str = ""


_INTENT_PATTERNS = {
    "monthly_sales": (
        r"\bmonthly\b", r"\bmonth(?:ly)?\s+(?:sales|trend|trends)\b",
        r"\b(?:sales|units)\s+(?:trend|trends)\s+(?:by|over|across)\s+month(?:s)?\b",
        r"\b(?:sales|units) trends?\b",
        r"\b(?:trend|trends)\s+over\s+time\b",
    ),
    "top_stores": (
        r"\btop\b.*\bstores?\b", r"\bbest\b.*\bstores?\b",
        r"\bstores?\b.*\b(?:top|best|performing|performance|rank)\b",
    ),
    "top_products": (
        r"\btop\b.*\b(?:products?|items?)\b", r"\bbest[ -]selling\b",
        r"\b(?:products?|items?)\b.*\b(?:top|best|performing|performance|rank)\b",
    ),
    "category_performance": (
        r"\bcategor(?:y|ies)\b", r"\bcat_id\b",
    ),
    "department_performance": (
        r"\bdepartments?\b", r"\bdept_id\b",
    ),
    "weekday_performance": (
        r"\bweekdays?\b", r"\bday[s]?\s+of\s+(?:the\s+)?week\b",
        r"\b(?:monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b",
    ),
    "summary": (
        r"\bsummary\b", r"\boverview\b", r"\boverall\b",
        r"\b(?:record|fact[ -]?row|row) count\b", r"\bhow many (?:records|rows|fact rows)\b",
        r"\btotal (?:sales|units)\b", r"\baverage sales\b",
    ),
}

_UNSUPPORTED_PATTERNS = (
    r"\brevenue\b", r"\bprofit\b", r"\bcurrency\b", r"\bdollars?\b",
    r"\bcustomer", r"\btransactions?\b", r"\bdaily\b", r"\bper day\b",
    r"\bsales_fact\b", r"\bsales_enriched\b", r"\b(?:select|insert|update|delete|drop)\b",
    r"\b(?:sql|database credentials?|api key|secret)\b",
    r"\b(?:ignore|disregard|forget)\b.{0,50}\b(?:previous|prior|system|instructions?|rules?|prompt)\b",
    r"\b(?:system prompt|reveal|act as|pretend to be|bypass)\b",
)


def _matches(question: str, patterns: tuple[str, ...]) -> bool:
    return any(re.search(pattern, question) for pattern in patterns)


def route_question(question: str) -> ChatRoute:
    """Classify only supported aggregate questions; never interprets SQL."""
    normalized = " ".join(question.casefold().split())
    if _matches(normalized, _UNSUPPORTED_PATTERNS):
        return ChatRoute(
            None,
            status="unsupported",
            reason=(
                "This demo cannot answer questions about revenue, customers, "
                "transactions, daily records, internal data, or instructions to run code. "
                "Sales values in the snapshot are units sold, not currency."
            ),
        )

    intents = [
        intent for intent, patterns in _INTENT_PATTERNS.items()
        if _matches(normalized, patterns)
    ]
    if len(intents) > 1:
        return ChatRoute(
            None,
            status="ambiguous",
            reason="Please ask about one supported topic at a time: summary, monthly sales, stores, products, categories, departments, or weekdays.",
        )
    if not intents:
        return ChatRoute(
            None,
            status="unsupported",
            reason="I could not match that to a supported aggregate. Ask about the sales summary, monthly trend, top stores or products, category or department performance, or weekday performance.",
        )

    intent = intents[0]
    limit = 10
    if intent in {"top_stores", "top_products"}:
        match = re.search(
            r"\btop\s+(\d+)\b|\b(\d+)\s+(?:top|best)\b|\blimit(?:\s+of)?\s+(\d+)\b",
            normalized,
        )
        if match:
            requested = int(next(group for group in match.groups() if group is not None))
            limit = min(max(requested, 1), MAX_RANKING_LIMIT)
    return ChatRoute(intent, limit=limit)
