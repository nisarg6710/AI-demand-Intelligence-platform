from src.ai.tools.base_tool import BaseTool
from src.analytics.service import AnalyticsService


class AnalyticsTool(BaseTool):

    def __init__(self):

        self.service = AnalyticsService()

    @property
    def name(self):
        return "analytics_tool"

    @property
    def description(self):
        return "Provides business analytics from the retail data warehouse."

    def execute(self, *args, **kwargs):
        """
        Required by BaseTool.
        AnalyticsTool exposes explicit methods instead.
        """
        return self.failure(
            "Use one of the AnalyticsTool methods."
        )

    def get_sales_summary(self):

        try:

            # print("=" * 80)
            # print("Inside AnalyticsTool.get_sales_summary()")

            df = self.service.get_sales_summary()

            # print("Returned object:")
            # print(df)
            # print("Type:", type(df))

            # if df is None:
            #     print("df is None!")

            return self.success(
                data=df,
                metadata={
                    "rows": len(df),
                    "columns": list(df.columns)
                }
            )

        except Exception as e:

            # print("Exception:", repr(e))
            return self.failure(e)

    def get_top_stores(self):

        try:

            df = self.service.get_top_stores()

            return self.success(
                data=df,
                metadata={
                    "rows": len(df),
                    "columns": list(df.columns)
                }
            )

        except Exception as e:

            return self.failure(e)

    def get_top_products(self):

        try:

            df = self.service.get_top_products()

            return self.success(
                data=df,
                metadata={
                    "rows": len(df),
                    "columns": list(df.columns)
                }
            )

        except Exception as e:

            return self.failure(e)

    def get_monthly_sales(self):

        try:

            df = self.service.get_monthly_sales()

            return self.success(
                data=df,
                metadata={
                    "rows": len(df),
                    "columns": list(df.columns)
                }
            )

        except Exception as e:

            return self.failure(e)

    def get_weekday_sales(self):

        try:

            df = self.service.get_weekday_sales()

            return self.success(
                data=df,
                metadata={
                    "rows": len(df),
                    "columns": list(df.columns)
                }
            )

        except Exception as e:

            return self.failure(e)

    def get_store_performance(self):

        try:

            df = self.service.get_store_performance()

            return self.success(
                data=df,
                metadata={
                    "rows": len(df),
                    "columns": list(df.columns)
                }
            )

        except Exception as e:

            return self.failure(e)

    def get_price_summary(self):

        try:

            df = self.service.get_price_summary()

            return self.success(
                data=df,
                metadata={
                    "rows": len(df),
                    "columns": list(df.columns)
                }
            )

        except Exception as e:

            return self.failure(e)

    def get_sales_distribution(self):

        try:

            df = self.service.get_sales_distribution()

            return self.success(
                data=df,
                metadata={
                    "rows": len(df),
                    "columns": list(df.columns)
                }
            )

        except Exception as e:

            return self.failure(e)

    def get_category_performance(self):

        try:

            df = self.service.get_category_performance()

            return self.success(
                data=df,
                metadata={
                    "rows": len(df),
                    "columns": list(df.columns)
                }
            )

        except Exception as e:

            return self.failure(e)

    def get_department_performance(self):

        try:

            df = self.service.get_department_performance()

            return self.success(
                data=df,
                metadata={
                    "rows": len(df),
                    "columns": list(df.columns)
                }
            )

        except Exception as e:

            return self.failure(e)