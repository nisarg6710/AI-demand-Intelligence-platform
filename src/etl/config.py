from dataclasses import dataclass
from typing import Callable

@dataclass
class ETLConfig:

    extractor: Callable
    transformer: Callable

    source_path: str
    target_table: str

    required_columns: list
    null_check_columns: list

    chunksize: int | None = None