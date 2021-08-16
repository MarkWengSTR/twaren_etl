from elasticsearch.client import MlClient
from datetime import datetime

import es_properties.search as es_search_prop
import es_api.search as es_search


def forecast_job(ctx):
    forecast_result = ctx["analy_es_object"].ping() and MlClient.forecast(
        ctx["analy_es_object"],
        job_id=ctx["ml_job_id"],
        params={
            "duration": "1d",
            "expires_in": "3d"
        })

    if forecast_result and forecast_result["acknowledged"]:
        ctx["forecast"]["job_id"] = forecast_result["forecast_id"]
        ctx["forecast"]["job_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        ctx = forecast_job(ctx)

    return ctx


def search_forecast_data(ctx):
    search_ctx = {
        "data_es_object": ctx["analy_es_object"],
        "search_properties": es_search_prop.forecast_15m_es_props_setting(
            ctx["ml_job_id"],
            ctx["forecast"]["job_id"],
            ctx["forecast"]["device_searcher"]
        )
    }

    search_ctx = ctx["analy_es_object"].ping() and es_search.execute(search_ctx)

    if search_ctx and search_ctx["search_result"]:
        ctx["forecast"]["result"] = search_ctx["search_result"]
    else:
        ctx = search_forecast_data(ctx)

    return ctx
