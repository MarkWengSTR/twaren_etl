import es_api.object as ob
import es_properties.machine_learning as es_ml_prop

import mysql_api.forecast_data as fc_sql
import es_api.machine_learning.forecast as fc_es

if __name__ == "__main__":
    for ml_job_id, metric in es_ml_prop.ML_JOB_METRIC_MAPPING.items():
        ctx = {
            "analy_es_object": None,
            "ml_job_id": ml_job_id,
            "forecast": {
                "metric": metric,
                "job_id": "",
                "device_searcher": ".*2671UD80004.*",
                "result": None
            }
        }

        ob.prepare_all(ctx) and \
            fc_sql.query_forecast_job_id(ctx) and \
            fc_es.search_forecast_data(ctx) and \
            print(ctx)
