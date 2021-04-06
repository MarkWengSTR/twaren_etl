import logging
import time

import es_api.object as ob
import es_api.index as idx
import es_api.machine_learning.anomaly_detection as mlad
import es_api.search as es_search
import es_api.bulk as es_bulk
import es_properties.index as es_idx_prop
import es_properties.machine_learning as es_ml_prop
import es_properties.search as es_search_prop

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    while True:
        ctx = {
            "data_es_object": None,
            "analy_es_object": None,
            "is_created_new_index": None,
            "index_properties": es_idx_prop.twaren_device,
            "mlad_properties": es_ml_prop.anomaly_detect_twaren_device,
            "search_properties": es_search_prop.twaren_asr_device,
            "search_result": None,
            "mlad_result": None
        }

        ob.prepare_all(ctx) and \
            idx.create_process(ctx) and \
            es_search.scan(ctx) and \
            es_bulk.bulk_from_scan(ctx) and \
            time.sleep(300)

    # ob.prepare_all(ctx) and \
    #     mlad.process(ctx)
