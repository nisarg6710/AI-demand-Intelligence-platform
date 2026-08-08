from src.ai.knowledge.schema_cache import SchemaCache


def main():

    cache = SchemaCache()

    print(cache.get_schema_text())


if __name__ == "__main__":
    main()