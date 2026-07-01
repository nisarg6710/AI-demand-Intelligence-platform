from dataclasses import dataclass, field
from typing import Callable

@dataclass
class ETLConfig:

    extractor: Callable
    transformer: Callable

    source_path: str
    target_table: str

    # Validation BEFORE transformation
    input_required_columns: list = field(default_factory=list)

    # Validation AFTER transformation
    output_required_columns: list = field(default_factory=list)

    output_null_check_columns: list = field(default_factory=list)

    chunksize: int | None = None