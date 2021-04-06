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
