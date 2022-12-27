import psycopg2
from config import Settings

settings = Settings()


def get_db_connection():
    connection = psycopg2.connect(user=settings.POSTGRES_USER,
                                  password=settings.POSTGRES_PASSWORD,
                                  host=settings.POSTGRES_SERVER,
                                  port=settings.POSTGRES_PORT,
                                  database=settings.POSTGRES_DB
    )
    cursor = connection.cursor()
    return connection, cursor
