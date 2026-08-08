from src.ai.tools.base_tool import BaseTool
from src.inventory.service import InventoryService


class InventoryTool(BaseTool):

    def __init__(self):
        self.service = InventoryService()

    @property
    def name(self):
        return "inventory_tool"

    @property
    def description(self):
        return (
            "Provides inventory intelligence based on recent "
            "sales demand and product velocity."
        )

    def execute(self, *args, **kwargs):
        """
        Required by BaseTool.

        InventoryTool exposes explicit inventory analysis
        methods instead of a generic execute operation.
        """

        return self.failure(
            "Use one of the InventoryTool methods."
        )

    def get_inventory_summary(self):

        try:

            df = self.service.get_inventory_summary()

            return self.success(
                data=df,
                metadata={
                    "rows": len(df),
                    "columns": list(df.columns)
                }
            )

        except Exception as e:

            return self.failure(e)

    def get_fast_moving_products(self):

        try:

            df = self.service.get_fast_moving_products()

            return self.success(
                data=df,
                metadata={
                    "rows": len(df),
                    "columns": list(df.columns)
                }
            )

        except Exception as e:

            return self.failure(e)

    def get_slow_moving_products(self):

        try:

            df = self.service.get_slow_moving_products()

            return self.success(
                data=df,
                metadata={
                    "rows": len(df),
                    "columns": list(df.columns)
                }
            )

        except Exception as e:

            return self.failure(e)

    def get_store_inventory(self):

        try:

            df = self.service.get_store_inventory()

            return self.success(
                data=df,
                metadata={
                    "rows": len(df),
                    "columns": list(df.columns)
                }
            )

        except Exception as e:

            return self.failure(e)

    def get_reorder_candidates(self):

        try:

            df = self.service.get_reorder_candidates()

            return self.success(
                data=df,
                metadata={
                    "rows": len(df),
                    "columns": list(df.columns)
                }
            )

        except Exception as e:

            return self.failure(e)

    def get_inventory_health(self):

        try:

            df = self.service.get_inventory_health()

            return self.success(
                data=df,
                metadata={
                    "rows": len(df),
                    "columns": list(df.columns)
                }
            )

        except Exception as e:

            return self.failure(e)