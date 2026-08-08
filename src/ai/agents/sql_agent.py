from src.ai.agents.base_agent import BaseAgent
from src.ai.tools.sql_tool import SQLTool
from src.ai.knowledge.schema_cache import SchemaCache
import re

class SQLAgent(BaseAgent):

    def __init__(self):

        super().__init__()

        self.tool = SQLTool()
        self.schema_cache = SchemaCache()

    def system_prompt(self):

        return """
You are a senior SQL engineer specializing in retail analytics databases.

Your responsibilities include:

- writing SQL queries
- explaining SQL queries
- selecting appropriate tables
- performing joins
- aggregating sales data
- querying forecasting tables
- querying inventory-related data

Assume the database is a MySQL retail data warehouse organized as a star schema.

Typical tables include:

- sales_fact
- price_fact
- calendar_dim
- item_dim
- store_dim
- forecast_predictions
- forecast_experiments

Only answer SQL and database questions.

Do not explain forecasting.

Do not perform business analytics.

Do not recommend inventory policies.
"""

    def _build_prompt(self, question: str) -> str:
        """
        Builds the prompt for SQL generation using the cached schema.
        """

        schema = self.schema_cache.get_schema_text()

        return f"""
    You are given the following MySQL database schema.

    {schema}

    User Question:
    {question}

    Instructions:

    1. Generate ONLY valid MySQL SQL.
    2. Do NOT explain your answer.
    3. Do NOT use markdown.
    4. Return ONLY the SQL query.
    """

    def _generate_sql(self, question: str):

        prompt = self._build_prompt(question)

        sql = self.llm.generate(
            system_prompt=self.system_prompt(),
            user_prompt=prompt,
        )

        return self._clean_sql(sql)

    def _execute_sql(self, sql: str):
        """
        Executes the generated SQL using the SQL Tool.
        """

        return self.tool.execute(sql)

    def _explain_results(self, question, result):

        prompt = f"""
    User Question:

    {question}

    Generated SQL:

    {result['metadata']['query']}

    Returned Data:

    {result['data'].to_string(index=False)}

    Explain the results in business language.

    If appropriate, mention insights and trends.
    """

        return self.llm.generate(

            system_prompt="""
    You are a senior retail business analyst.

    Explain SQL query results clearly.

    Do not generate SQL.

    Only explain the returned data.
    """,

            user_prompt=prompt

        )


    def _clean_sql(self, sql: str) -> str:
        """
        Cleans LLM-generated SQL by removing markdown fences,
        extra whitespace, and trailing explanations.
        """

        sql = sql.strip()

        sql = re.sub(r"^```sql", "", sql, flags=re.IGNORECASE)
        sql = re.sub(r"^```", "", sql)
        sql = re.sub(r"```$", "", sql)

        sql = sql.strip()

        return sql

    def _explain_results(self, question: str, result: dict) -> str:
        """
        Explains SQL results in business language.
        """

        dataframe = result["data"]

        prompt = f"""
    User Question:
    {question}

    SQL Query:
    {result["metadata"]["query"]}

    Returned Data:
    {dataframe.to_markdown(index=False)}

    Explain the results in clear business language.

    Highlight any useful observations.

    Do not generate SQL.
    """

        return self.llm.generate(
            system_prompt="""
    You are a senior retail business analyst.

    Explain SQL results to business users.

    Be concise.

    Focus on insights, not SQL syntax.
    """,
            user_prompt=prompt,
        )

    def run(self, question):

        sql = self._generate_sql(question)

        # If the user explicitly asks for the SQL/query,
        # return the generated SQL without executing it.
        query_only_keywords = [
            "show me the sql",
            "show the sql",
            "give me the sql",
            "give me the query",
            "show me the query",
            "show the query",
            "write the sql",
            "write a sql",
            "generate sql",
            "generate the sql",
            "sql query",
        ]

        question_lower = question.lower()

        if any(keyword in question_lower for keyword in query_only_keywords):

            return {
                "success": True,
                "question": question,
                "sql": sql,
                "result": None,
                "explanation": None,
            }

        # Otherwise execute the SQL normally.
        result = self._execute_sql(sql)

        if not result["success"]:
            return result

        explanation = self._explain_results(
            question,
            result,
        )

        return {
            "success": True,
            "question": question,
            "sql": sql,
            "result": result,
            "explanation": explanation,
        }