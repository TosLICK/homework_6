import psycopg2
from contextlib import contextmanager


@contextmanager
def create_connection():
    try:
        """ create a database connection to database """
        conn = psycopg2.connect(host="localhost", database="university", user="postgres", password="123456")
        yield conn
    except psycopg2.OperationalError as err:
        conn.rollback()
        raise RuntimeError(f"Failed to create database connection {err}")
    finally:
        conn.close()
    