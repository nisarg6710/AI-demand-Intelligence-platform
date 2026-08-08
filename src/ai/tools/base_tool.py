from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    """
    Base class for all tools used by AI agents.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique tool name."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Tool description."""
        pass

    @abstractmethod
    def execute(self, *args, **kwargs) -> dict[str, Any]:
        """
        Execute the tool.

        Returns
        -------
        {
            "success": bool,
            "data": Any,
            "metadata": dict,
            "error": str | None
        }
        """
        pass

    def success(self, data, metadata=None):

        return {
            "success": True,
            "data": data,
            "metadata": metadata or {},
            "error": None,
        }

    def failure(self, error):

        return {
            "success": False,
            "data": None,
            "metadata": {},
            "error": str(error),
        }