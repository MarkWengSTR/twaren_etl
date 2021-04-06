twaren_device = {
    "name": "nms-devices_status-test-2020.07",
    "body": {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 1
        },
        "mappings": {
            "properties": {
                "@timestamp": {
                    "type": "date"
                },
                "CPUStatus": {
                    "type": "long"
                },
                "CPUStatus_CheckTime": {
                    "type": "date"
                },
                "Channel1_CurrentTemperature": {
                    "type": "float"
                },
                "Channel2_CurrentTemperature": {
                    "type": "float"
                },
                "Channel3_CurrentTemperature": {
                    "type": "float"
                },
                "Channel4_CurrentTemperature": {
                    "type": "long"
                },
                "CurrentAvgRTT": {
                    "type": "float"
                },
                "CurrentCPU": {
                    "type": "long"
                },
                "CurrentMaxRTT": {
                    "type": "float"
                },
                "CurrentMemory": {
                    "type": "long"
                },
                "CurrentMinRTT": {
                    "type": "float"
                },
                "CurrentPktLossRate": {
                    "type": "long"
                },
                "CurrentStatus": {
                    "type": "long"
                },
                "CurrentStatus_CheckTime": {
                    "type": "date"
                },
                "Devices_id": {
                    "type": "long"
                },
                "Devices_name": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "MemoryStatus": {
                    "type": "long"
                },
                "MemoryStatus_CheckTime": {
                    "type": "date"
                },
                "TemperatureStatus": {
                    "type": "long"
                },
                "TemperatureStatus_CheckTime": {
                    "type": "date"
                },
                "VoltageStatus": {
                    "type": "long"
                },
                "VoltageStatus_CheckTime": {
                    "type": "date"
                },
                "v4PingStatus": {
                    "type": "long"
                },
                "v4PingStatus_CheckTime": {
                    "type": "date"
                },
                "v6PingStatus": {
                    "type": "long"
                }
            }
        }
    }
}
