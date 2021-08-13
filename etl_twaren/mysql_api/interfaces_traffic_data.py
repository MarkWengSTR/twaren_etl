import mysql_api.db as db
import os

SQL_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "sqls/interfaces_traffic_data.sql"
)

DB_PROPS = {
    "db_props": {
        "host": os.getenv("TWAREN_DB_HOST"),
        "user": os.getenv("TWAREN_DB_USER"),
        "password": os.getenv("TWAREN_DB_POSSWORD"),
        "name": "NetFlow"
    },
    "db_conn": None,
    "db_cursor": None
}


def query_netflow():
    db_ctx = db.dbconn_prepare(DB_PROPS)

    with open(SQL_FILE, "r") as sql_file:
        try:
            db_ctx["db_cursor"].execute(sql_file.read())
            result = db.reformat_all_time_field(
                db_ctx["db_cursor"].fetchall(),
                "CheckTime",
                "%Y-%m-%d %H:%M:%S"
            )
        except Exception:
            print("Error: unable to fetch data")

    return result


print(query_netflow())
