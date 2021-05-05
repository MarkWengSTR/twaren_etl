from elasticsearch import Elasticsearch
import es_properties.object as es_ob_prop


def prepare_all(ctx):
    ctx["data_es_object"] = Elasticsearch(es_ob_prop.data_es["end_point"])
    ctx["analy_es_object"] = Elasticsearch(es_ob_prop.ml_es["end_point"])

    return ctx

    # ctx["analy_es_object"] = Elasticsearch(
    #     es_ob_prop.ml_es["end_point"],
    #     http_auth=(es_ob_prop.ml_es["user"], es_ob_prop.ml_es["password"])
    # )
