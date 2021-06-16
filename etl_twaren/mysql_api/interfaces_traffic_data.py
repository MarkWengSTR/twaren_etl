import mysql_api.db as db
import os

SQL_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "sqls\\interfaces_traffic_data.sql"
)


def interfaces_tracfic_datagrid_query():
    with open(SQL_FILE, "r") as sql_file:
        db_ctx = {
            "db_conn": None,
            "db_cursor": None,
            "sql": "",
            "result": {}
        }
        db_ctx["sql"] = sql_file.read()

        db.dbconn_prepare(db_ctx) and \
            db.query_all(db_ctx)

    return db_ctx


print(interfaces_tracfic_datagrid_query())
