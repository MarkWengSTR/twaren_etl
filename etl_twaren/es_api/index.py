def already_exist(index_ctx):
    return index_ctx["es_object"].indices.exists(
        index=index_ctx["index_properties"]["name"])


def create(index_ctx):
    es = index_ctx["es_object"]

    result = es.indices.create(
        index=index_ctx["index_properties"]["name"], body=index_ctx["index_properties"]["body"])
    print(result)

    return index_ctx


def create_process(ctx):
    index_ctx = {
        "es_object": ctx["analy_es_object"],
        "index_properties": ctx["index_properties"]
    }

    if already_exist(index_ctx):
        ctx["is_created_new_index"] = False
    else:
        create(index_ctx)
        ctx["is_created_new_index"] = True

    return ctx
