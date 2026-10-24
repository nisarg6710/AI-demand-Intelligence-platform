"""Deterministic analytics routing and narrow business-question classification."""

from __future__ import annotations

from dataclasses import dataclass
import re


MAX_RANKING_LIMIT = 100


@dataclass(frozen=True)
class ChatRoute:
    intent: str | None
    limit: int = 10
    horizon: int = 1
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
    "forecast_baseline": (
        r"\b(?:forecast|forecasting)\b.{0,60}\b(?:next|coming|future|month|months|sales|units|performance)\b",
        r"\b(?:predict|predicting|prediction|predictions)\b.{0,60}\b(?:next|coming|future|month|months|sales|units|performance)\b",
        r"\b(?:next|coming|future)\b.{0,40}\b(?:forecast|predict|prediction)\b",
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

_SPECIFIC_PERIOD_PATTERNS = (
    r"\b(?:today|yesterday|tomorrow|latest|current(?:ly)?|most recent)\b",
    r"\b(?:last|this|previous|past)\s+(?:calendar\s+)?(?:month|week|day|quarter|year|period)\b",
    r"\bhow much\b.{0,60}\b(?:sell|sold|sales|units)\b",
)

_GENERAL_BUSINESS_PATTERNS = (
    r"\bhow\s+(?:can|could|does|might)\s+(?:this|the)\s+(?:project|platform|system)\s+(?:help|support|benefit)\b",
    r"\bwhat\s+(?:can|does)\s+(?:this|the)\s+(?:project|platform|system)\s+do\b",
    r"\b(?:business|organizational)\s+(?:benefits?|use cases?|value)\b",
    r"\bhow\s+(?:can|could)\s+(?:an organization|the organization|a business|the business|our organization)\b.{0,100}\b(?:benefit|use|apply|adopt|support)\b",
)

_GENERAL_BUSINESS_DATA_TERMS = (
    r"\b(?:sales|units|revenue|profit|forecast|prediction|customer|transaction|store|product|category|department|weekday)\b",
    r"\b(?:current|latest|today|yesterday|historical|history|last month|this month|date range|specific period)\b",
    r"\b(?:data|metric|measurement|number|figure|result|trend|performance|snapshot|sql|database|query)\b",
)


def _matches(question: str, patterns: tuple[str, ...]) -> bool:
    return any(re.search(pattern, question) for pattern in patterns)


def route_question(question: str) -> ChatRoute:
    """Classify only supported aggregate questions; never interprets SQL."""
    normalized = " ".join(question.casefold().split())
    if _matches(normalized, _SPECIFIC_PERIOD_PATTERNS):
        return ChatRoute(
            None,
            status="unsupported",
            reason=(
                "This demo cannot answer current or specific-period measurements. "
                "Ask for a supported aggregate such as the overall summary or monthly trend."
            ),
        )
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
            reason="Please ask about one supported topic at a time: summary, monthly sales, forecast baseline, stores, products, categories, departments, or weekdays.",
        )
    if not intents:
        return ChatRoute(
            None,
            status="unsupported",
            reason="I could not match that to a supported aggregate. Ask about the sales summary, monthly trend, top stores or products, category or department performance, or weekday performance.",
        )

    intent = intents[0]
    limit = 10
    horizon = 1
    if intent in {"top_stores", "top_products"}:
        match = re.search(
            r"\btop\s+(\d+)\b|\b(\d+)\s+(?:top|best)\b|\blimit(?:\s+of)?\s+(\d+)\b",
            normalized,
        )
        if match:
            requested = int(next(group for group in match.groups() if group is not None))
            limit = min(max(requested, 1), MAX_RANKING_LIMIT)
    elif intent == "forecast_baseline":
        match = re.search(
            r"\b(?:next|coming|for|over|horizon(?:\s+of)?)\s+(\d{1,3})\s+months?\b"
            r"|\b(\d{1,3})[- ]month(?:ly)?\s+(?:forecast|prediction)\b"
            r"|\b(?:forecast|predict\w*)\s+(?:for\s+)?(\d{1,3})\s+months?\b",
            normalized,
        )
        if match:
            requested = int(next(group for group in match.groups() if group is not None))
            if not 1 <= requested <= 12:
                return ChatRoute(
                    None,
                    status="unsupported",
                    reason="The public baseline supports forecast horizons from 1 to 12 months.",
                )
            horizon = requested
    return ChatRoute(intent, limit=limit, horizon=horizon)


def is_general_business_question(question: str) -> bool:
    """Match a narrow, data-independent project-capabilities question."""
    if not isinstance(question, str) or len(question) > 1000:
        return False
    normalized = " ".join(question.casefold().split())
    if _matches(normalized, _SPECIFIC_PERIOD_PATTERNS):
        return False
    if _matches(normalized, _UNSUPPORTED_PATTERNS):
        return False
    if _matches(normalized, _GENERAL_BUSINESS_DATA_TERMS):
        return False
    return _matches(normalized, _GENERAL_BUSINESS_PATTERNS)
