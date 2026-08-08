from src.ai.tools.base_tool import BaseTool
from src.database.db_manager import DatabaseManager


class SQLTool(BaseTool):

    @property
    def name(self):
        return "sql_tool"

    @property
    def description(self):
        return "Executes SQL queries."

    def execute(self, query: str):

        db = None

        try:
            db = DatabaseManager()

            db.execute(query)

            dataframe = db.fetch_dataframe()

            metadata = {
                "query": query,
                "rows": len(dataframe),
                "columns": list(dataframe.columns)
            }

            return self.success(
                data=dataframe,
                metadata=metadata
            )

        except Exception as e:

            return self.failure(e)

        finally:

            if db:
                db.close()
    def get_tables(self):

        db = None

        try:

            db = DatabaseManager()

            db.execute("SHOW TABLES;")

            tables = db.fetchall()

            tables = [table[0] for table in tables]

            return self.success(
                data=tables,
                metadata={
                    "count": len(tables)
                }
            )

        except Exception as e:

            return self.failure(e)

        finally:

            if db:
                db.close()

    def get_schema(self, table_name):

        db = None

        try:

            db = DatabaseManager()

            db.execute(f"DESCRIBE {table_name};")

            df = db.fetch_dataframe()

            return self.success(
                data=df,
                metadata={
                    "table": table_name,
                    "columns": len(df)
                }
            )

        except Exception as e:

            return self.failure(e)

        finally:

            if db:
                db.close()

    def get_database_schema(self):

        tables = self.get_tables()

        if not tables["success"]:
            return tables

        schema = {}

        for table in tables["data"]:

            result = self.get_schema(table)

            if result["success"]:

                df = result["data"]

                schema[table] = [
                    {
                        "column": row["Field"],
                        "type": row["Type"]
                    }
                    for _, row in df.iterrows()
                ]

        return self.success(
            data=schema,
            metadata={
                "tables": len(schema)
            }
        )