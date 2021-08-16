# import logging

import es_api.object as ob
import es_properties.machine_learning as es_ml_prop
import es_api.machine_learning.forecast as fc_es

import mysql_api.forecast_data as fc_sql

# logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    for ml_job_id, metric in es_ml_prop.ML_JOB_METRIC_MAPPING.items():
        ctx = {
            "analy_es_object": None,
            "ml_job_id": ml_job_id,
            "forecast": {
                "metric": metric,
                "job_id": None,
                "job_time": None
            }
        }

        ob.prepare_all(ctx) and \
            fc_es.forecast_job(ctx) and \
            fc_sql.insert_forecast_record(ctx) and \
            print(ctx)
