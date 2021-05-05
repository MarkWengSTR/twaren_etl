import logging

import es_api.object as ob
import es_api.machine_learning.anomaly_detection as mlad
import es_properties.index as es_idx_prop
import es_properties.machine_learning as es_ml_prop

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    ctx = {
        "data_es_object": None,
        "analy_es_object": None,
        "is_created_new_index": None,
        "index_properties": es_idx_prop.twaren_device,
        "mlad_properties": es_ml_prop.anomaly_detect_twaren_device,
        "search_result": None,
        "mlad_result": None
    }

    ob.prepare_all(ctx) and \
        mlad.get_resutl_process(ctx)
