from pathlib import Path

import yaml


class ConfigLoader:

    @staticmethod
    def load(config_name):

        config_path = Path("configs") / config_name

        with open(config_path, "r") as file:

            return yaml.safe_load(file)