from src.config.loader import ConfigLoader


class Settings:

    database = ConfigLoader.load(
        "database.yaml"
    )

    paths = ConfigLoader.load(
        "paths.yaml"
    )

    etl = ConfigLoader.load(
        "etl.yaml"
    )