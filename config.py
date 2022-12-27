import os
from pathlib import Path
from pydantic import BaseSettings
from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    PROJECT_NAME: str = "TRADE_BOOK"
    PROJECT_VERSION: str = "1.0.0"

    USE_SQLITE_DB: str = False
    POSTGRES_USER: str = os.environ.get('PSQL_USER')
    POSTGRES_PASSWORD = os.environ.get('PSQL_PASSWORD')
    POSTGRES_SERVER: str = 'localhost'
    POSTGRES_PORT: str = '5432'
    POSTGRES_DB: str = os.environ.get('PSQL_DB')
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
