import mysql_api.db as db
import os

SQL_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "sqls/interfaces_traffic_data.sql"
)


def query_netflow(db_ctx):
    try:
        db_ctx["db_cursor"].execute(db_ctx["sql"])
        db_ctx["result"] = db.reformat_time_field(
            db_ctx["db_cursor"].fetchall(),
            "CheckTime"
        )
    except Exception:
        print("Error: unable to fetch data")

    return db_ctx


def interfaces_tracfic_datagrid_query():
    with open(SQL_FILE, "r") as sql_file:
        db_ctx = {
            "props": {
                "host": os.getenv("TWAREN_DB_HOST"),
                "user": os.getenv("TWAREN_DB_USER"),
                "password": os.getenv("TWAREN_DB_POSSWORD"),
                "name": "NetFlow"
            },
            "db_conn": None,
            "db_cursor": None,
            "sql": sql_file.read(),
            "result": {}
        }

        db.dbconn_prepare(db_ctx) and \
            query_netflow(db_ctx)

    return db_ctx


print(interfaces_tracfic_datagrid_query())
