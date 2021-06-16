import pymysql
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()


def dbconn_prepare(db_ctx):
    db_conn = pymysql.connect(
        cursorclass=pymysql.cursors.DictCursor,
        host=os.getenv("TWAREN_DB_HOST"),
        user=os.getenv("TWAREN_DB_USER"),
        password=os.getenv("TWAREN_DB_POSSWORD"),
        db="NetFlow")

    db_ctx["db_conn"] = db_conn
    db_ctx["db_cursor"] = db_conn.cursor()

    return db_ctx


def reformat_time(records):
    for record in records:
        record["CheckTime"] = datetime.strptime(
            record["CheckTime"], '%Y-%m-%d %H:%M:%S')

    return records


def query_all(db_ctx):
    try:
        db_ctx["db_cursor"].execute(db_ctx["sql"])
        db_ctx["result"] = reformat_time(
            db_ctx["db_cursor"].fetchall()
        )
    except Exception:
        print("Error: unable to fetch data")

    return db_ctx
