from elasticsearch.client import MlClient
from datetime import datetime


def forecast_job(ctx):
    forecast_result = ctx["analy_es_object"].ping() and MlClient.forecast(
        ctx["analy_es_object"],
        job_id=ctx["ml_job_id"],
        params={
            "duration": "1d",
            "expires_in": "3d"
        })

    if forecast_result and forecast_result["acknowledged"]:
        ctx["forecast_job_id"] = forecast_result["forecast_id"]
        ctx["forecast_job_time"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    else:
        ctx = forecast_job(ctx)

    return ctx
