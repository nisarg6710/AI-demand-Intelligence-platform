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

        db = DatabaseManager()

        try:
            db.execute(query, values)
            return db.fetch_dataframe()
        finally:
            db.close()

    def get_sales_summary(self):
        """
        Returns high-level sales KPIs.
        """

        query = """
        SELECT
            COUNT(*) AS total_records,
            SUM(sales) AS total_sales,
            AVG(sales) AS average_sales,
            MIN(sales) AS minimum_sales,
            MAX(sales) AS maximum_sales
        FROM sales_fact;
        """

        df = self._run_query(query)
        return df

    def get_top_stores(self):
        """
        Returns total sales for each store.
        """

        query = """
        SELECT
            store_id,
            SUM(sales) AS total_sales
        FROM sales_fact
        GROUP BY store_id
        ORDER BY total_sales DESC;
        """

        return self._run_query(query)

    def get_top_products(self):
        """
        Returns the highest selling products.
        """

        query = """
        SELECT
            item_id,
            SUM(sales) AS total_sales
        FROM sales_fact
        GROUP BY item_id
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

        query = """
        SELECT
            weekday,
            SUM(sales) AS total_sales
        FROM sales_enriched
        GROUP BY weekday
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
        Returns price statistics.
        """

        query = """
        SELECT
            AVG(sell_price) AS average_price,
            MIN(sell_price) AS minimum_price,
            MAX(sell_price) AS maximum_price
        FROM price_fact;
        """

        return self._run_query(query)

    def get_sales_distribution(self):
        """
        Returns sales distribution statistics.
        """

        query = """
        SELECT
            COUNT(*) AS total_transactions,
            AVG(sales) AS average_sales,
            STDDEV(sales) AS sales_stddev,
            MIN(sales) AS minimum_sales,
            MAX(sales) AS maximum_sales
        FROM sales_fact;
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