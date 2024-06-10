from connect import create_connection

path = "query_01.sql"
with create_connection() as conn:
    with conn.cursor() as cur:
        with open(path, "r", encoding="utf-8") as query:
            sql_query = query.read()
            cur.execute(sql_query)
            print(cur.fetchall())
    conn.commit()
