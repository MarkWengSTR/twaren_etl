twaren_asr_device = {
    "index": "nms-devices_status-test-2020.07",
    "body": {
        "query": {
            "bool": {
                "must": [
                    {"regexp": {
                        "Devices_name.keyword": {
                            "value": ".*ASR.*"
                        }
                    }}
                ],
                "filter": [
                    {"range": {
                        "@timestamp": {
                            "gte": "now-15m/m",
                            "lt": "now/m"
                        }
                    }}
                ]
            }
        }
    }
}

twaren_asr_syslog = {
    "index": "logstash-syslog-2021.02.19",
    "body": {
        "query": {
            "bool": {
                "must": [
                    {"regexp": {
                        "syslog_hostname.raw": {
                            "value": ".*ASR.*"
                        }
                    }}
                ],
                "filter": [
                    {"range": {
                        "@timestamp": {
                            "gte": "now-15m/m",
                            "lt": "now/m"
                        }
                    }}
                ]
            }
        }
    }
}


forecast_data = {
    "index": ".ml-anomalies-shared",
    "body": {
        "query": {
            "bool": {
                "filter": [
                    {
                        "query_string": {
                            "query": "result_type:model_forecast"
                        }
                    },
                    {
                        "query_string": {
                            "query": "job_id:inms-real-time-current-in-15m"
                        }
                    },
                    {
                        "query_string": {
                            "query": "forecast_id:eMkXPnsBMasMJgE74t0i"
                        }
                    },
                    {"range": {
                        "timestamp": {
                            "gte": "now/m",
                            "lt": "now+15m/m"
                        }
                    }}
                ],
                "must": [
                    {"regexp": {
                        "partition_field_value": ".*2671UD80004.*"
                    }}
                ]
            }
        }
    }
}


def forecast_15m_es_props_setting(ml_job_id, forecast_id, device_searcher):
    forecast_data["body"]["query"]["bool"]["filter"][1]["query_string"]["query"] = "job_id:" + ml_job_id
    forecast_data["body"]["query"]["bool"]["filter"][2]["query_string"]["query"] = "forecast_id:" + forecast_id
    forecast_data["body"]["query"]["bool"]["must"][0]["regexp"]["partition_field_value"] = device_searcher

    return forecast_data

# "body": {
#     "size": 10000,
# }
# "filter": [
#     {"range": {
#         "@timestamp": {
#             "gte": "now-1h/h",
#             "lt": "now/h"
#         }
#     }},
#     {"range": {"CurrentCPU": {"lte": 100}}},
#     {"range": {"CurrentMemory": {"lte": 100}}}
# ]
# "bool": {
#     "must": [
#         {"regexp": {
#             "syslog_hostname.raw": {
#                 "value": ".*ASR.*"
#             }
#         }}
#     ],
#     "filter": [
#         {"range": {
#             "@timestamp": {
#                 "gte": "now-15m/m",
#                 "lt": "now/m"
#             }
#         }}
#     ]
# }
