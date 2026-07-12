import json
import os

from datetime import datetime


class MetadataWriter:

    @staticmethod
    def save(
        metadata,
    ):

        metadata_dir = "artifacts/metadata"

        os.makedirs(
            metadata_dir,
            exist_ok=True,
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        path = os.path.join(
            metadata_dir,
            f"metadata_{timestamp}.json",
        )

        with open(
            path,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                metadata,
                file,
                indent=4,
            )

        return path