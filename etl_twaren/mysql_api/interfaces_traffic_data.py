import mysql_api.db as db
import os

QUERY_TRAFFIC_DATA_SQL = os.path.join(
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

    with open(QUERY_TRAFFIC_DATA_SQL, "r") as sql_file:
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


def update_traffic_out_bound(db_ctx):
    sql = """
        UPDATE Interfaces
        SET Interfaces_traffic_out_high = {0}, Interfaces_traffic_out_low = {1}
        WHERE Interfaces_id = {2}
        """.format(
        db_ctx["inms_traffic_out"]["upper_bound"],
        db_ctx["inms_traffic_out"]["lower_bound"],
        db_ctx["inms_traffic_out"]["id"]
    )

    try:
        db_props = db.dbconn_prepare(DB_PROPS)

        db_props["db_cursor"].execute(sql)
        db_props["db_conn"].commit()
    except Exception:
        print("Error: unable to insert data")

    return db_ctx


def update_traffic_in_bound(db_ctx):
    sql = """
        UPDATE Interfaces
        SET Interfaces_traffic_in_high = {0}, Interfaces_traffic_in_low = {1}
        WHERE Interfaces_id = {2}
        """.format(
        db_ctx["inms_traffic_in"]["upper_bound"],
        db_ctx["inms_traffic_in"]["lower_bound"],
        db_ctx["inms_traffic_in"]["id"]
    )

    try:
        db_props = db.dbconn_prepare(DB_PROPS)

        db_props["db_cursor"].execute(sql)
        db_props["db_conn"].commit()
    except Exception:
        print("Error: unable to insert data")

    return db_ctx
