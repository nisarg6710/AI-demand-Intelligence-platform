from src.database.db_manager import DatabaseManager


class AnalyticsBuilder:


    @staticmethod
    def build_monthly_sales():

        db = DatabaseManager()

        query = """
        CREATE TABLE IF NOT EXISTS analytics_monthly_sales AS
        SELECT
            c.year,
            c.month,
            SUM(s.sales) AS total_sales
        FROM sales_fact s
        JOIN calendar_dim c
            ON s.d = c.d
        GROUP BY
            c.year,
            c.month;
        """

        db.execute(query)
        db.commit()
        db.close()


    @staticmethod
    def build_store_performance():

        db = DatabaseManager()

        query = """
        CREATE TABLE IF NOT EXISTS analytics_store_performance AS
        SELECT
            store_id,
            SUM(sales) AS total_sales,
            AVG(sales) AS average_sales,
            MAX(sales) AS peak_sales
        FROM sales_fact
        GROUP BY store_id;
        """

        db.execute(query)
        db.commit()
        db.close()



if __name__ == "__main__":

    print("Building analytics tables...")

    AnalyticsBuilder.build_monthly_sales()

    AnalyticsBuilder.build_store_performance()

    print("Completed")