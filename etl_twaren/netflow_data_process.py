import logging

import es_api.object as ob
import es_api.index as idx
import es_api.bulk as es_bulk
import es_properties.index as es_idx_prop

import mysql_api.interfaces_traffic_data as sql_traffic_data

logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    ctx = {
        "sql_data": None,
        "analy_es_object": None,
        "is_created_new_index": None,
        "index_properties": es_idx_prop.twaren_netflow,
        "search_result": sql_traffic_data.interfaces_tracfic_datagrid_query()["result"],
        "mlad_properties": None,
        "mlad_result": None
    }

    ob.prepare_all(ctx) and \
        idx.create_process(ctx) and \
        es_bulk.bulk_from_mysql(ctx)
