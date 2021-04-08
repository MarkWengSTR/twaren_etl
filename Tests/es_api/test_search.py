from unittest import TestCase
from etl_twaren.es_api.search import time_range_from_now_props_list, replace_range_prop


class TestSearch(TestCase):
    def test_time_range_from_now_props_list(self):
        self.assertEqual(
            time_range_from_now_props_list("d", 3),
            [
                {"gte": "now/d", "lt": "now+1d/d"},
                {"gte": "now-1d/d", "lt": "now-0d/d"},
                {"gte": "now-2d/d", "lt": "now-1d/d"},
                {"gte": "now-3d/d", "lt": "now-2d/d"},
                {"gte": "now-4d/d", "lt": "now-3d/d"},
            ]
        )

        self.assertEqual(
            time_range_from_now_props_list("m", 2),
            [
                {"gte": "now/m", "lt": "now+1m/m"},
                {"gte": "now-1m/m", "lt": "now-0m/m"},
                {"gte": "now-2m/m", "lt": "now-1m/m"},
                {"gte": "now-3m/m", "lt": "now-2m/m"}
            ]
        )

    def test_replace_range_prop(self):
        search_properties = {
            "body": {
                "query": {
                    "bool": {
                        "filter": [{
                            "range": {
                                "@timestamp": {
                                    "gte": "now-15m/m",
                                    "lt": "now/m"
                                }
                            }
                        }]
                    }
                }
            }
        }

        self.assertEqual(
            replace_range_prop(
                search_properties, {"gte": "now/d", "lt": "now+1d/d"}
            ),
            {
                "body": {
                    "query": {
                        "bool": {
                            "filter": [{
                                "range": {
                                    "@timestamp": {
                                        "gte": "now/d",
                                        "lt": "now+1d/d"
                                    }
                                }
                            }]
                        }
                    }
                }
            }
        )
