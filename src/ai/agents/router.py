class TaskRouter:
    """
    Routes natural-language business questions
    to the appropriate specialist agents.
    """

    def route(self, task: str):

        task = task.lower().strip()

        selected_agents = []

        # --------------------------------------------------
        # Forecast
        # --------------------------------------------------

        forecast_keywords = [
            "forecast",
            "forecasting",
            "predict",
            "prediction",
            "predicted",
            "future demand",
            "future sales",
            "prophet",
            "arima",
            "sarima",
        ]

        if any(word in task for word in forecast_keywords):
            selected_agents.append("forecast")

        # --------------------------------------------------
        # Analytics
        # --------------------------------------------------

        analytics_keywords = [
            # General analytics
            "analysis",
            "analytics",
            "analyze",
            "insight",
            "insights",
            "trend",
            "trends",
            "historical",
            "seasonality",
            "kpi",
            "performance",
            "business intelligence",

            # Sales
            "sales summary",
            "sales trend",
            "sales trends",
            "sales distribution",
            "sales by",
            "total sales",
            "average sales",
            "sales volume",

            # Monthly / temporal analysis
            "monthly sales",
            "sales by month",
            "sales by weekday",
            "weekday sales",
            "weekday",
            "monthly trend",
            "monthly trends",

            # Stores
            "top stores",
            "best stores",
            "top performing stores",
            "top-performing stores",
            "best performing stores",
            "best-performing stores",
            "stores performing best",
            "stores are performing best",
            "stores performed best",
            "stores are performing",
            "best performing",
            "best-performing",
            "store performance",
            "store performance analysis",

            # Products
            "top products",
            "best products",
            "best selling products",
            "best-selling products",
            "top selling products",
            "top-selling products",
            "product performance",
            "product analysis",

            # Categories
            "category performance",
            "category analysis",
            "categories",
            "department performance",
            "department analysis",
            "departments",

            # Pricing
            "price analysis",
            "pricing analysis",
            "price summary",
            "pricing summary",
            "average price",
            "minimum price",
            "maximum price",
            "price distribution",

            # General business questions
            "business performance",
            "business insights",
            "business analysis",
            "retail insights",
            "retail analysis",
            "important insights",
            "key insights",
        ]

        if any(word in task for word in analytics_keywords):
            selected_agents.append("analytics")

        # --------------------------------------------------
        # Inventory
        # --------------------------------------------------

        inventory_keywords = [
            "inventory",
            "stock",
            "reorder",
            "replenishment",
            "safety stock",
            "fast moving",
            "fast-moving",
            "slow moving",
            "slow-moving",
            "selling the fastest",
            "selling fastest",
            "selling slowly",
            "slowest selling",
            "inventory health",
            "inventory risk",
            "stock risk",
            "stockout",
            "stock out",
            "overstock",
        ]

        if any(word in task for word in inventory_keywords):
            selected_agents.append("inventory")

        # --------------------------------------------------
        # SQL
        # --------------------------------------------------

        sql_keywords = [
            "sql",
            "sql query",
            "database query",
            "write a query",
            "show me the query",
            "query for",
            "select statement",
            "join query",
        ]

        if any(word in task for word in sql_keywords):
            return ["sql"]

        # --------------------------------------------------
        # General business report
        # --------------------------------------------------

        report_keywords = [
            "executive report",
            "executive summary",
            "business report",
            "business overview",
            "business summary",
            "overall business",
            "overall performance",
        ]

        if any(word in task for word in report_keywords):

            selected_agents.extend([
                "forecast",
                "analytics",
                "inventory",
            ])

        # --------------------------------------------------
        # Remove duplicates while preserving order
        # --------------------------------------------------

        return list(dict.fromkeys(selected_agents))