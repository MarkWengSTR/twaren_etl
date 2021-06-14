import pymysql


def dbconn_prepare(db_ctx):
    db_conn = pymysql.connect(
        cursorclass=pymysql.cursors.DictCursor,
        host="192.168.3.39",
        user="inms",
        password="twaren.net",
        db="NetFlow")

    db_ctx["db_conn"] = db_conn
    db_ctx["db_cursor"] = db_conn.cursor()

    return db_ctx


def query_all(db_ctx):
    try:
        db_ctx["db_cursor"].execute(db_ctx["sql"])
        db_ctx["result"] = db_ctx["db_cursor"].fetchall()
    except Exception:
        print("Error: unable to fetch data")

    return db_ctx
