from src.database.db_manager import DatabaseManager


class AnalyticsService:
    """
    Provides business analytics operations for the AI platform.
    """

    def __init__(self):
        pass

    def _run_query(self, query: str, values=None):
        """
        Executes a SQL query and returns a DataFrame.
        """

        print("\n========== ANALYTICS QUERY ==========")
        print(query)

        db = DatabaseManager()

        try:
            db.execute(query, values)

            print("QUERY EXECUTED")

            df = db.fetch_dataframe()

            print("ROWS RETURNED:", len(df))

            return df

        finally:
            db.close()

    def get_sales_summary(self):
        """
        Returns high-level sales KPIs
        from the precomputed analytics summary table.
        """

        query = """
        SELECT
            total_records,
            total_sales,
            average_sales,
            minimum_sales,
            maximum_sales
        FROM analytics_sales_summary
        WHERE id = 1;
        """

        return self._run_query(query)

    def get_top_stores(self):
        """
        Returns the highest-performing stores
        using precomputed analytics data.
        """

        query = """
        SELECT
            store_id,
            total_sales
        FROM analytics_store_performance
        ORDER BY total_sales DESC;
        """

        return self._run_query(query)

    def get_top_products(self):
        """
        Returns the highest-selling products
        using precomputed analytics data.
        """

        query = """
        SELECT
            item_id,
            total_sales
        FROM analytics_product_performance
        ORDER BY total_sales DESC
        LIMIT 10;
        """

        return self._run_query(query)

    def get_monthly_sales(self):

        query = """
        SELECT
            year,
            month,
            total_sales
        FROM analytics_monthly_sales
        ORDER BY year, month;
        """

        return self._run_query(query)
    

    def get_weekday_sales(self):
        """
        Returns weekday sales performance
        using precomputed analytics data.
        """

        query = """
        SELECT
            weekday,
            total_sales
        FROM analytics_weekday_sales
        ORDER BY FIELD(
            weekday,
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        );
        """

        return self._run_query(query)

    def get_store_performance(self):
        """
        Returns store performance metrics.
        """

        query = """
        SELECT
            store_id,
            total_sales,
            average_sales,
            peak_sales
        FROM analytics_store_performance
        ORDER BY total_sales DESC;
        """

        return self._run_query(query)

    def get_price_summary(self):
        """
        Returns precomputed price statistics.
        """

        query = """
        SELECT
            average_price,
            minimum_price,
            maximum_price
        FROM analytics_price_summary
        WHERE id = 1;
        """

        return self._run_query(query)

    def get_sales_distribution(self):
        """
        Returns precomputed sales distribution statistics.
        """

        query = """
        SELECT
            total_transactions,
            average_sales,
            sales_stddev,
            minimum_sales,
            maximum_sales
        FROM analytics_sales_distribution
        WHERE id = 1;
        """

        return self._run_query(query)
    def get_category_performance(self):

        query = """
        SELECT
            cat_id,
            total_sales
        FROM analytics_category_performance
        ORDER BY total_sales DESC;
        """

        return self._run_query(query)

    def get_department_performance(self):

        query = """
        SELECT
            dept_id,
            total_sales
        FROM analytics_department_performance
        ORDER BY total_sales DESC;
        """

        return self._run_query(query)