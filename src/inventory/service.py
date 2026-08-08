from src.database.db_manager import DatabaseManager


class InventoryService:
    """
    Provides inventory intelligence based on historical
    demand and recent sales velocity.
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


    def get_inventory_summary(self):
        """
        Returns high-level inventory demand indicators.

        Since the warehouse does not currently contain
        physical inventory quantities, this method uses
        recent sales velocity as a proxy for inventory demand.
        """

        query = """
        SELECT
            COUNT(DISTINCT item_id) AS active_products,
            COUNT(DISTINCT store_id) AS active_stores,
            SUM(s.sales) AS sales_last_28_days,
            AVG(s.sales) AS average_daily_item_sales,
            MAX(s.sales) AS peak_daily_item_sales
        FROM sales_fact s
        JOIN calendar_dim c
            ON s.d = c.d

        WHERE c.date >= (
            SELECT MAX(c2.date)
            FROM sales_fact s2
            JOIN calendar_dim c2
                ON s2.d = c2.d
        ) - INTERVAL 28 DAY
        """

        return self._run_query(query)


    def get_fast_moving_products(self):
        """
        Returns products with the highest recent demand velocity.
        """

        query = """
        SELECT
            s.item_id,
            SUM(s.sales) AS total_sales,
            AVG(s.sales) AS average_daily_sales
        FROM sales_fact s
        JOIN calendar_dim c
            ON s.d = c.d

        WHERE c.date >= (
            SELECT MAX(c2.date)
            FROM sales_fact s2
            JOIN calendar_dim c2
                ON s2.d = c2.d
        ) - INTERVAL 28 DAY
        GROUP BY s.item_id
        HAVING total_sales > 0
        ORDER BY average_daily_sales DESC
        LIMIT 20;
        """

        return self._run_query(query)


    def get_slow_moving_products(self):
        """
        Returns products with the lowest positive recent demand.
        """

        query = """
        SELECT
            s.item_id,
            SUM(s.sales) AS total_sales,
            AVG(s.sales) AS average_daily_sales
        FROM sales_fact s
        JOIN calendar_dim c
            ON s.d = c.d

        WHERE c.date >= (
            SELECT MAX(c2.date)
            FROM sales_fact s2
            JOIN calendar_dim c2
                ON s2.d = c2.d
        ) - INTERVAL 28 DAY
        GROUP BY s.item_id
        HAVING total_sales > 0
        ORDER BY average_daily_sales ASC
        LIMIT 20;
        """

        return self._run_query(query)



    def get_store_inventory(self):
        """
        Returns recent demand velocity by store.

        This helps identify stores that require greater
        inventory support based on demand.
        """

        query = """
        SELECT
            s.store_id,
            SUM(s.sales) AS total_sales,
            AVG(s.sales) AS average_daily_sales,
            MAX(s.sales) AS peak_daily_sales
        FROM sales_fact s
        JOIN calendar_dim c
            ON s.d = c.d

        WHERE c.date >= (
            SELECT MAX(c2.date)
            FROM sales_fact s2
            JOIN calendar_dim c2
                ON s2.d = c2.d
        ) - INTERVAL 28 DAY
        GROUP BY s.store_id
        ORDER BY total_sales DESC;
        """

        return self._run_query(query)


    def get_reorder_candidates(self):
        """
        Identifies products that should receive higher
        replenishment priority based on recent demand velocity.

        Note:
        This is demand-based prioritization, not a true
        stockout calculation because current inventory
        quantities are not available in the warehouse.
        """

        query = """
        SELECT
            s.item_id,
            SUM(s.sales) AS total_sales,
            AVG(s.sales) AS average_daily_sales,
            MAX(s.sales) AS peak_daily_sales
        FROM sales_fact s
        JOIN calendar_dim c
            ON s.d = c.d

        WHERE c.date >= (
            SELECT MAX(c2.date)
            FROM sales_fact s2
            JOIN calendar_dim c2
                ON s2.d = c2.d
        ) - INTERVAL 28 DAY
        GROUP BY s.item_id
        HAVING total_sales > 0
        ORDER BY average_daily_sales DESC
        LIMIT 20;
        """

        return self._run_query(query)


    def get_inventory_health(self):
        """
        Provides a high-level classification of products
        based on recent demand velocity.
        """

        query = """
        SELECT
            COUNT(*) AS total_active_products,

            SUM(
                CASE
                    WHEN average_daily_sales >= 10
                    THEN 1
                    ELSE 0
                END
            ) AS high_velocity_products,

            SUM(
                CASE
                    WHEN average_daily_sales >= 3
                     AND average_daily_sales < 10
                    THEN 1
                    ELSE 0
                END
            ) AS medium_velocity_products,

            SUM(
                CASE
                    WHEN average_daily_sales > 0
                     AND average_daily_sales < 3
                    THEN 1
                    ELSE 0
                END
            ) AS low_velocity_products

        FROM (
            SELECT
                s.item_id,
                AVG(s.sales) AS average_daily_sales

            FROM sales_fact s

            JOIN calendar_dim c
                ON s.d = c.d

            WHERE c.date >= (
                SELECT MAX(c2.date)
                FROM sales_fact s2
                JOIN calendar_dim c2
                    ON s2.d = c2.d
            ) - INTERVAL 28 DAY

            GROUP BY s.item_id

            HAVING SUM(s.sales) > 0
        ) AS product_velocity;
        """

        return self._run_query(query)