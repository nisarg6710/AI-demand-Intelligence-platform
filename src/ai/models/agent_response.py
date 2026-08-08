from dataclasses import dataclass, field
from typing import Any

@dataclass
class AgentResponse:
    """
    Standard response object returned by every ai agent.
    """

    success: bool

    agent: str

    tool_used: str | None = None

    output: Any = None

    metadata: dict = field(default_factory=dict)

    error: str | None = None