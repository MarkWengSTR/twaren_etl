import db


def interfaces_tracfic_datagrid_query():
    with open("sqls\\interfaces_traffic_data.sql", "r") as sql_file:
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
