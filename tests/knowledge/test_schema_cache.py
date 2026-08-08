from src.ai.knowledge.schema_cache import SchemaCache


def main():

    cache = SchemaCache()

    schema = cache.load()

    print("=" * 80)
    print("DATABASE TABLES")
    print("=" * 80)

    for table in schema:
        print(table)


if __name__ == "__main__":
    main()