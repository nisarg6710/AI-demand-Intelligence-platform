from src.utils.config_loader import ConfigLoader

database = ConfigLoader.load(
    "database.yaml"
)

paths = ConfigLoader.load(
    "paths.yaml"
)

etl = ConfigLoader.load(
    "etl.yaml"
)

print(database)
print(paths)
print(etl)