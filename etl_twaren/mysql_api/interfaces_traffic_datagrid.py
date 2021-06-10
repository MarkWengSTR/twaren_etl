import utils


def interfaces_tracfic_datagrid_query():
    db_ctx = {
        "db_conn": None,
        "db_cursor": None,
        "sql": "",
        "resutl": {}
    }

    with open("sqls\\interfaces_traffic_oatagrid.sql", "r") as sql_file:
        db_ctx["sql"] = sql_file.read()

        utils.dbconn_prepare(db_ctx) and \
            utils.query_all(db_ctx)

    return db_ctx


print(interfaces_tracfic_datagrid_query())
