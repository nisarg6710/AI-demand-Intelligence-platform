import os
from pathlib import Path

import yaml

class ConfigLoader:


    CONFIG_DIR = Path("configs")

    @staticmethod
    def load(config_name):


        config_path = ConfigLoader.CONFIG_DIR / config_name

        if not config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {config_path}"
            )

        with open(config_path, "r") as file:

            return yaml.safe_load(file)