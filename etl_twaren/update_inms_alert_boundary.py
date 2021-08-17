from datetime import datetime

import es_api.object as ob
import es_properties.machine_learning as es_ml_prop

import mysql_api.forecast_data as fc_local_sql
import mysql_api.interfaces_traffic_data as inms_netflow_sql
import es_api.machine_learning.forecast as fc_es

TRAFFIC_ID_DEVICE_KEYWORD_MAPPING = {
    "194": "20_TWAREN-TP-ASR9006-01 to CHI-9006I 10GE",
    "198": "TP_TWGate_Peering",
    "211": "18_TWAREN-TP-ASR9006-01 to CHI-9006I 10GE",
    "502": "TP-PL8960-01_DPI-Int-to-ASR",
    "557": "17_TWAREN-TP-ASR9006-01 to CHI-9006I 1GE"
}


def update_inms_netflow_data(ctx):
    if ctx["forecast"]["metric"] == "CurrentInRate":
        extract_data_to_inms_traf_in(ctx) and \
            inms_netflow_sql.update_traffic_in_bound(ctx)
    else:
        extract_data_to_inms_traf_out(ctx) and \
            inms_netflow_sql.update_traffic_out_bound(ctx)

    return ctx


def extract_data_to_inms_traf_in(ctx):
    data = ctx["forecast"]["result"]["hits"]["hits"][0]["_source"]

    ctx["inms_traffic_in"]["upper_bound"] = data["forecast_upper"]
    ctx["inms_traffic_in"]["lower_bound"] = data["forecast_lower"]

    return ctx


def extract_data_to_inms_traf_out(ctx):
    data = ctx["forecast"]["result"]["hits"]["hits"][0]["_source"]

    ctx["inms_traffic_out"]["upper_bound"] = data["forecast_upper"]
    ctx["inms_traffic_out"]["lower_bound"] = data["forecast_lower"]

    return ctx


if __name__ == "__main__":
    for ml_job_id, metric in es_ml_prop.ML_JOB_METRIC_MAPPING.items():
        for traffic_id, device_keyword in TRAFFIC_ID_DEVICE_KEYWORD_MAPPING.items():
            device_searcher = ".*" + device_keyword + ".*"

            ctx = {
                "job_query_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "analy_es_object": None,
                "ml_job_id": ml_job_id,
                "forecast": {
                    "metric": metric,
                    "job_id": "",
                    "device_searcher": device_searcher,
                    "result": None
                },
                "inms_traffic_in": {
                    "id": traffic_id,
                    "upper_bound": "",
                    "lower_bound": ""
                },
                "inms_traffic_out": {
                    "id": traffic_id,
                    "upper_bound": "",
                    "lower_bound": ""
                }
            }

            ob.prepare_all(ctx) and \
                fc_local_sql.query_forecast_job_id(ctx) and \
                fc_es.search_forecast_data(ctx) and \
                extract_data_to_inms_traf_in(ctx) and \
                update_inms_netflow_data(ctx) and \
                print(ctx)
