# import logging

import es_api.object as ob
import es_api.machine_learning.forecast as fc

# logging.basicConfig(level=logging.DEBUG)

ML_JOB_METRIC_MAPPING = {
    "inms-real-time-current-in-15m": "CurrentInRate"
}

if __name__ == "__main__":
    for ml_job_id in ML_JOB_METRIC_MAPPING.keys():
        ctx = {
            "sql_data": None,
            "analy_es_object": None,
            "ml_job_id": ml_job_id,
            "forecast_job_id": None,
            "forecast_job_time": None
        }

        ob.prepare_all(ctx) and \
            fc.forecast_job(ctx) and \
            print(ctx)
