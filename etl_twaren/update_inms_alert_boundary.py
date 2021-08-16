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


def extract_forecast_data_to_inms(ctx):
    data = ctx["forecast"]["result"]["hits"]["hits"][0]["_source"]

    ctx["inms_traffic"]["upper_bound"] = data["forecast_upper"]

    return ctx


if __name__ == "__main__":
    for ml_job_id, metric in es_ml_prop.ML_JOB_METRIC_MAPPING.items():
        for traffic_id, device_keyword in TRAFFIC_ID_DEVICE_KEYWORD_MAPPING.items():
            device_searcher = ".*" + device_keyword + ".*"

            ctx = {
                "analy_es_object": None,
                "ml_job_id": ml_job_id,
                "forecast": {
                    "metric": metric,
                    "job_id": "",
                    "device_searcher": device_searcher,
                    "result": None
                },
                "inms_traffic": {
                    "id": traffic_id,
                    "upper_bound": ""
                }
            }

            ob.prepare_all(ctx) and \
                fc_local_sql.query_forecast_job_id(ctx) and \
                fc_es.search_forecast_data(ctx) and \
                extract_forecast_data_to_inms(ctx) and \
                inms_netflow_sql.update_traffic_bound(ctx) and \
                print(ctx)
