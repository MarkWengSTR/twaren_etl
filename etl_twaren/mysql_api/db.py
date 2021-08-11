import pymysql
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()


def dbconn_prepare(db_ctx):
    db_conn = pymysql.connect(
        cursorclass=pymysql.cursors.DictCursor,
        host=db_ctx["props"]["host"],
        user=db_ctx["props"]["user"],
        password=db_ctx["props"]["password"],
        db=db_ctx["props"]["name"])

    db_ctx["db_conn"] = db_conn
    db_ctx["db_cursor"] = db_conn.cursor()

    return db_ctx


def reformat_time_field(records, time_field):
    for record in records:
        record[time_field] = datetime.strptime(
            record[time_field], '%Y-%m-%d %H:%M:%S')

    return records
