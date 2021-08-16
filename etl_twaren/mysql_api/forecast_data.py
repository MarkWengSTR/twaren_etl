import os
import mysql_api.db as db

DB_PROPS = {
    "db_props": {
        "host": os.getenv("FORECAST_DB_HOST"),
        "user": os.getenv("FORECAST_DB_USER"),
        "password": os.getenv("FORECAST_DB_PASSWORD"),
        "name": "forecast_inms"
    },
    "db_conn": None,
    "db_cursor": None
}


def query_forecast_job_id(db_ctx):
    """
    find forecast job id by metric
    """
    metric = db_ctx["forecast"]["metric"]

    sql = """SELECT job_id
        FROM forecast_data
        WHERE metric = '{0}'
        ORDER BY create_time DESC
        LIMIT 1""".format(metric)

    try:
        db_props = db.dbconn_prepare(DB_PROPS)

        db_props["db_cursor"].execute(sql)

        db_ctx["forecast"]["job_id"] = db_props["db_cursor"].fetchall()[0]["job_id"]

        db_ctx["db_query"] = True
    except Exception:
        db_ctx["db_query"] = False
        print("Error: unable to fetch data")

    return db_ctx


def insert_forecast_record(db_ctx):
    sql = """INSERT INTO `forecast_data` (`metric`, `job_id`, `create_time`) VALUES
        ('{0}', '{1}', '{2}')""".format(
        db_ctx["forecast"]["metric"],
        db_ctx["forecast"]["job_id"],
        db.reformat_time_str(db_ctx["forecast"]["job_time"], "%Y-%m-%d %H:%M:%S")
    )

    try:
        db_props = db.dbconn_prepare(DB_PROPS)

        db_props["db_cursor"].execute(sql)
        db_props["db_conn"].commit()
    except Exception:
        print("Error: unable to insert data")

    return db_ctx


###
# test
###

# import db
# import os

# if __name__ == "__main__":
#     ctx = {
#         "props": {
#             "host": os.getenv("FORECAST_DB_HOST"),
#             "user": os.getenv("FORECAST_DB_USER"),
#             "password": os.getenv("FORECAST_DB_PASSWORD"),
#             "name": "forecast_inms"
#         },
#         "db_conn": None,
#         "db_cursor": None,
#         "metric": "CurrentInRate",
#         "forecast_job_id": "testabs123",
#         "forecast_job_time": "2021-08-11"
#     }

#     db.dbconn_prepare(ctx) and \
#         insert_forecast_record(ctx) and \
#         print(ctx)
