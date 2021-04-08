from elasticsearch import Elasticsearch
import etl_twaren.es_properties.object as es_ob_prop


def prepare_all(ctx):
    ctx["data_es_object"] = Elasticsearch(es_ob_prop.data_es["end_point"])
    ctx["analy_es_object"] = Elasticsearch(
        es_ob_prop.ml_es["end_point"], es_ob_prop.ml_es["user"], es_ob_prop.ml_es["password"]
    )

    return ctx
