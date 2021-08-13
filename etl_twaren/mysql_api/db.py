import pymysql
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()


def dbconn_prepare(db_ctx):
    db_conn = pymysql.connect(
        cursorclass=pymysql.cursors.DictCursor,
        host=db_ctx["db_props"]["host"],
        user=db_ctx["db_props"]["user"],
        password=db_ctx["db_props"]["password"],
        db=db_ctx["db_props"]["name"])

    db_ctx["db_conn"] = db_conn
    db_ctx["db_cursor"] = db_conn.cursor()

    return db_ctx


def reformat_time_str(time_str, ori_format):
    return datetime.strptime(time_str, ori_format)


def reformat_all_time_field(records, time_field, ori_format):
    for record in records:
        record[time_field] = reformat_time_str(record[time_field], ori_format)

    return records

# def reformat_all_time_field(records, time_field, ori_format):
#     for record in records:
#         record[time_field] = datetime.strptime(
#             record[time_field], '%Y-%m-%d %H:%M:%S')

#     return records
