# import logging

import es_api.object as ob
import es_api.machine_learning.forecast as fc

# logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    ctx = {
        "sql_data": None,
        "analy_es_object": None,
        "ml_job_id": None,
        "forecast_job_id": None,
        "forecast_job_time": None
    }

    ctx["ml_job_id"] = "inms-real-time-current-in-15m"

    ob.prepare_all(ctx) and \
        fc.forecast_job(ctx) and\
        print(ctx)
