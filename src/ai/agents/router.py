class TaskRouter:

    def route(self, task: str):

        task = task.lower()

        selected_agents = []

        ## forecast
        if any(word in task for word in [
            "forecast",
            "predict",
            "prediction",
            "predicted",
            "future demand",
            "forecasting",
            "prophet",
            "arima",
            "sarima",
        ]):
            selected_agents.append("forecast")

        ## analytics
        if any(word in task for word in [
            "trend",
            "analysis",
            "analytics",
            "eda",
            "historical",
            "seasonality",
            "kpi",
            "sales summary",
            "monthly sales",
            "weekday sales",
            "top stores",
            "top products",
            "best stores",
            "stores performed",
            "store performance",
            "sales distribution",
            "category performance",
            "department performance",
        ]):
            selected_agents.append("analytics")

        
        ## inventory
        if any(word in task for word in [
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
        ]):
            selected_agents.append("inventory")


        ## sql
        if any(word in task for word in [
            "sql",
            "sql query",
            "database query",
            "write a query",
            "show me the query",
            "query for",
            "select statement",
            "join query",
        ]):
            return ["sql"]

        ## general business report
        if any(word in task for word in [
            "executive report",
            "executive summary",
            "business report",
            "business overview",
        ]):
            selected_agents.extend([
                "forecast",
                "analytics",
                "inventory", ## we did not add sql here as "executive summary of the business" don't need a sql speceialist
            ])

        return list(dict.fromkeys(selected_agents))