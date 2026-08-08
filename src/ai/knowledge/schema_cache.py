import json
from pathlib import Path

from src.ai.tools.sql_tool import SQLTool


class SchemaCache:
    """
    Persistent cache for the database schema.
    Loads from disk when available.
    Discovers and saves the schema when needed.
    """

    CACHE_FILE = (
        Path(__file__).parent
        / "cache"
        / "schema.json"
    )

    def __init__(self):
        self.tool = SQLTool()
        self._schema = None

    def load(self):
        """
        Returns the schema.
        Priority:
        1. Memory
        2. Disk
        3. MySQL Discovery
        """

        # ---------- Memory ----------
        if self._schema is not None:
            return self._schema

        # ---------- Disk ----------
        if self.CACHE_FILE.exists():

            with open(self.CACHE_FILE, "r") as f:

                data = json.load(f)

                if data:
                    self._schema = data
                    return self._schema

        # ---------- Discover ----------
        return self.refresh()

    def refresh(self):
        """
        Forces schema discovery and writes it to disk.
        """

        result = self.tool.get_database_schema()

        if not result["success"]:
            raise RuntimeError(result["error"])

        self._schema = result["data"]

        self.CACHE_FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(self.CACHE_FILE, "w") as f:
            json.dump(
                self._schema,
                f,
                indent=4
            )

        return self._schema

    def clear(self):
        """
        Clears both memory and disk cache.
        """

        self._schema = None

        if self.CACHE_FILE.exists():
            self.CACHE_FILE.unlink()

    def get_schema_text(self):
        """
        Returns the schema as formatted text suitable for LLM prompts.
        """

        schema = self.load()

        lines = []

        for table, columns in schema.items():

            lines.append(f"\nTable: {table}")

            for column in columns:
                lines.append(
                    f"  - {column['column']} ({column['type']})"
                )

        return "\n".join(lines)