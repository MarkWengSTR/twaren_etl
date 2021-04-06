from elasticsearch import Elasticsearch
import es_properties.object as es_ob_prop


def prepare(object_ctx):
    es_properties = object_ctx["es_properties"]

    if "user" in es_properties:
        object_ctx["es_object"] = Elasticsearch(
            es_properties["end_point"], http_auth=(
                es_properties["user"], es_properties["password"])
        )
    else:
        object_ctx["es_object"] = Elasticsearch(es_properties["end_point"])

    return object_ctx


def data_es_prepare(ctx):
    object_ctx = {
        "es_object": None,
        "es_properties": es_ob_prop.data_es
    }

    ctx["data_es_object"] = prepare(object_ctx)["es_object"]

    return ctx


def ml_es_prepare(ctx):
    object_ctx = {
        "es_object": None,
        "es_properties": es_ob_prop.ml_es
    }

    ctx["analy_es_object"] = prepare(object_ctx)["es_object"]

    return ctx


def prepare_all(ctx):
    data_es_prepare(ctx) and \
        ml_es_prepare(ctx)

    return ctx
