import logging

import es_api.object as ob
import es_api.index as idx
import es_api.search as es_search
import es_api.bulk as es_bulk
import es_properties.index as es_idx_prop
import es_properties.search as es_search_prop

logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    ctx = {
        "data_es_object": None,
        "analy_es_object": None,
        "is_created_new_index": None,
        "index_properties": es_idx_prop.twaren_device,
        "search_properties": None,
        "search_result": None,
        "override_index_name": "twaren_asr_device"
    }
    ctx = ob.prepare_all(ctx) and \
        idx.create_process(ctx)

    for day_range in es_search.time_range_from_now_props_list("d", 3):
        search_properties = es_search.replace_range_prop(
            es_search_prop.twaren_asr_device, day_range)

        ctx["search_properties"] = search_properties

        es_search.scan(ctx) and \
            es_bulk.bulk_from_scan(ctx)
