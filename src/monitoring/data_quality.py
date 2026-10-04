from dataclasses import dataclass
from typing import Any

import pandas as pd


@dataclass
class DataQualityReport:
    row_count: int
    duplicate_count: int
    missing_values: dict[str, int]
    negative_values: dict[str, int]
    null_columns: list[str]
    passed: bool


class DataQualityMonitor:
    """
    Lightweight data-quality monitoring utility.

    Designed for sampled or aggregated datasets so that monitoring
    does not require repeatedly scanning the full sales warehouse.
    """

    def __init__(
        self,
        required_columns: list[str] | None = None,
        non_negative_columns: list[str] | None = None,
    ):
        self.required_columns = required_columns or []
        self.non_negative_columns = non_negative_columns or []

    def validate_schema(self, df: pd.DataFrame) -> dict[str, Any]:
        missing_columns = [
            column
            for column in self.required_columns
            if column not in df.columns
        ]

        return {
            "valid": len(missing_columns) == 0,
            "missing_columns": missing_columns,
        }

    def generate_report(self, df: pd.DataFrame) -> DataQualityReport:
        schema_result = self.validate_schema(df)

        missing_values = df.isnull().sum()
        missing_values = {
            column: int(count)
            for column, count in missing_values.items()
            if count > 0
        }

        duplicate_count = int(df.duplicated().sum())

        negative_values = {}

        for column in self.non_negative_columns:
            if column not in df.columns:
                continue

            negative_count = int((df[column] < 0).sum())

            if negative_count > 0:
                negative_values[column] = negative_count

        null_columns = list(missing_values.keys())

        passed = (
            schema_result["valid"]
            and duplicate_count == 0
            and len(negative_values) == 0
        )

        return DataQualityReport(
            row_count=len(df),
            duplicate_count=duplicate_count,
            missing_values=missing_values,
            negative_values=negative_values,
            null_columns=null_columns,
            passed=passed,
        )