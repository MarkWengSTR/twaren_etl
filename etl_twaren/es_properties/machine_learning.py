ML_JOB_METRIC_MAPPING = {
    "inms-real-time-current-in-15m": "CurrentInRate",
    "inms-real-time-current-out-15m": "CurrentOutRate"
}

anomaly_detect_twaren_device = {
    "job_id": "must assign",
    "job_body": {
        "description": "",
        "groups": [],
        "analysis_config": {
            "bucket_span": "5m",
            "detectors": [
                {
                    "detector_description": "mean(CurrentAvgRTT) partitionfield=\"Devices_name.keyword\"",
                    "function": "mean",
                    "field_name": "CurrentAvgRTT",
                    "partition_field_name": "Devices_name.keyword",
                    "detector_index": 0
                },
                {
                    "detector_description": "mean(CurrentCPU) partitionfield=\"Devices_name.keyword\"",
                    "function": "mean",
                    "field_name": "CurrentCPU",
                    "partition_field_name": "Devices_name.keyword",
                    "detector_index": 1,
                    "custom_rules": [{
                        "actions": ["skip_result", "skip_model_update"],
                        "conditions": [
                            {
                                "applies_to": "actual",
                                "operator": "gt",
                                "value": 100
                            }
                        ]
                    }]
                },
                {
                    "detector_description": "mean(CurrentMemory) partitionfield=\"Devices_name.keyword\"",
                    "function": "mean",
                    "field_name": "CurrentMemory",
                    "partition_field_name": "Devices_name.keyword",
                    "detector_index": 2,
                    "custom_rules": [{
                        "actions": ["skip_result", "skip_model_update"],
                        "conditions": [
                            {
                                "applies_to": "actual",
                                "operator": "gt",
                                "value": 100
                            }
                        ]
                    }]
                }
            ],
            "influencers": [
                "Devices_name.keyword"
            ]
        },
        "data_description": {
            "time_field": "@timestamp"
        },
        "custom_settings": {
            "created_by": "multi-metric-wizard"
        },
        "analysis_limits": {
            "model_memory_limit": "18MB"
        },
        "model_plot_config": {
            "enabled": False,
            "annotations_enabled": False
        },
        "results_index_name": "same as job id"
    },
    "close_job_params": None,
    "datafeed_id": "must assign",
    "datafeed_body": {
        "job_id": "must assign",
        "indices": "must assign",
        "frequency": "1m",
        "query_delay": "5m",
        "scroll_size": 1000,
        "chunking_config": {
            "mode": "auto"
        },
    },
    "datafeed_time": {
        "start": "2021-01-12T00:00:00",
    },
    "datafeed_stop_params": None,
    "get_records_params": {
        "sort": "record_score",
        "desc": True
    },
}
# "delayed_data_check_config": {
#     "enabled": True,
#     "check_window": "5m"
# },
# {
#     "detector_description": "mean(CurrentAvgRTT) partitionfield=\"Devices_name.keyword\"",
#     "function": "mean",
#     "field_name": "CurrentAvgRTT",
#     "partition_field_name": "Devices_name.keyword",
#     "detector_index": 0
# },
# {
#     "detector_description": "mean(CurrentCPU) partitionfield=\"Devices_name.keyword\"",
#     "function": "mean",
#     "field_name": "CurrentCPU",
#     "partition_field_name": "Devices_name.keyword",
#     "detector_index": 1,
#     "custom_rules": [{
#         "actions": ["skip_result", "skip_model_update"],
#         "conditions": [
#             {
#                 "applies_to": "actual",
#                 "operator": "gt",
#                 "value": 100
#             }
#         ]
#     }]
# },
# {
#     "detector_description": "mean(CurrentMemory) partitionfield=\"Devices_name.keyword\"",
#     "function": "mean",
#     "field_name": "CurrentMemory",
#     "partition_field_name": "Devices_name.keyword",
#     "detector_index": 2,
#     "custom_rules": [{
#         "actions": ["skip_result", "skip_model_update"],
#         "conditions": [
#             {
#                 "applies_to": "actual",
#                 "operator": "gt",
#                 "value": 100
#             }
#         ]
#     }]
# }
# {
#     "detector_description": "mean(CurrentAvgRTT)",
#     "function": "mean",
#     "field_name": "CurrentAvgRTT",
#     "by_field_name": "Devices_name.keyword",
#     "detector_index": 0
# },
# {
#     "detector_description": "mean(CurrentCPU)",
#     "function": "mean",
#     "field_name": "CurrentCPU",
#     "by_field_name": "Devices_name.keyword",
#     "detector_index": 1,
#     "custom_rules": [{
#         "actions": ["skip_result", "skip_model_update"],
#         "conditions": [
#             {
#                 "applies_to": "actual",
#                 "operator": "gt",
#                 "value": 100
#             }
#         ]
#     }]
# },
# {
#     "detector_description": "mean(CurrentMemory)",
#     "function": "mean",
#     "field_name": "CurrentMemory",
#     "by_field_name": "Devices_name.keyword",
#     "detector_index": 2,
#     "custom_rules": [{
#         "actions": ["skip_result", "skip_model_update"],
#         "conditions": [
#             {
#                 "applies_to": "actual",
#                 "operator": "gt",
#                 "value": 100
#             }
#         ]
#     }]
# }
# {
#     "detector_description": "mean(CurrentAvgRTT)",
#     "function": "mean",
#     "field_name": "CurrentAvgRTT",
#     "over_field_name": "Devices_name.keyword",
#     "detector_index": 0
# },
# {
#     "detector_description": "mean(CurrentCPU)",
#     "function": "mean",
#     "field_name": "CurrentCPU",
#     "over_field_name": "Devices_name.keyword",
#     "detector_index": 1,
#     "custom_rules": [{
#         "actions": ["skip_result", "skip_model_update"],
#         "conditions": [
#             {
#                 "applies_to": "actual",
#                 "operator": "gt",
#                 "value": 100
#             }
#         ]
#     }]
# },
# {
#     "detector_description": "mean(CurrentMemory)",
#     "function": "mean",
#     "field_name": "CurrentMemory",
#     "over_field_name": "Devices_name.keyword",
#     "detector_index": 2,
#     "custom_rules": [{
#         "actions": ["skip_result", "skip_model_update"],
#         "conditions": [
#             {
#                 "applies_to": "actual",
#                 "operator": "gt",
#                 "value": 100
#             }
#         ]
#     }]
# }
