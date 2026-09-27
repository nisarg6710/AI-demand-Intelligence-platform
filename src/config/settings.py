import os

from dotenv import load_dotenv

from src.config.loader import ConfigLoader

load_dotenv()

class Settings:

    paths = ConfigLoader.load("paths.yaml")

    etl = ConfigLoader.load("etl.yaml")

    database = {
        "host": os.getenv("DB_HOST"),
        "port": int(os.getenv("DB_PORT", "3306")),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_NAME"),
    }

    llm = {
        "provider": os.getenv("LLM_PROVIDER", "gemini"),
        "model": os.getenv(
            "LLM_MODEL",
            "models/gemini-3.1-flash-lite"
        ),
        "api_key": os.getenv("GEMINI_API_KEY"),
    }