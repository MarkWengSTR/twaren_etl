import logging

import es_properties.search as es_search_prop
import es_api.bulk as es_bulk
import es_api.search as es_search
import es_api.object as ob

logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    dates_list = es_search.pre_date_list(0)

    for index, hour_ranges_list in zip(
            es_search.dates_to_syslog_indexs_list(dates_list), es_search.hour_range_prop_per_day_lists(dates_list)):

        es_search_prop.twaren_asr_syslog.update({"index": index})

        for hour_range in hour_ranges_list:
            search_properties = es_search.replace_range_prop(
                es_search_prop.twaren_asr_syslog, hour_range)

            ctx = {
                "data_es_object": None,
                "analy_es_object": None,
                "is_created_new_index": None,
                "search_properties": search_properties,
                "search_result": None,
                "override_index_name": "twaren_asr_logs"
            }

            ob.prepare_all(ctx) and \
                es_search.scan(ctx) and \
                es_bulk.bulk_from_scan(ctx)


"""
exam from device_data_migrate:

for day_range in es_search.time_range_from_now_props_list("h", 12):
    search_properties = es_search.replace_range_prop(
        es_search_prop.twaren_asr_syslog, day_range)
    ctx = {
        "data_es_object": None,
        "analy_es_object": None,
        "is_created_new_index": None,
        "search_properties": search_properties,
        "search_result": None,
        "override_index_name": "twaren_asr_logs"
    }

    ob.prepare_all(ctx) and \
        es_search.scan(ctx) and \
        es_bulk.bulk_from_scan(ctx)

"""
