import logging
from psycopg2 import DatabaseError

from connect import create_connection


def create_table(conn, sql_path):
    with open(sql_path, 'r') as sql:
        sql_expression = sql.read()

    c = conn.cursor()
    try:
        c.execute(sql_expression)
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()


if __name__ == '__main__':
    try:
        with create_connection() as conn:
            if conn is not None:
                create_table(conn, "create_tables.sql")
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)
