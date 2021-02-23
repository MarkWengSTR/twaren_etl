import elasticsearch.helpers
import functools
import datetime

SYSLOG_TIME_FIELDS = [
    "@timestamp", "received_at", "syslog_timestamp"
]


def date_string_to_epoch(date: str) -> float:
    return datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ').timestamp()


def pre_date_list(days=0) -> list:
    return list(
        map(
            lambda day: str(datetime.date.today() - datetime.timedelta(day)),
            list(range(days+1))
        )
    )


# print(pre_date_interval_list(3)) # 2021-02-17 use 3 ;=> ['2021-02-17', '2021-02-16', '2021-02-15', '2021-02-14']"


def dates_to_syslog_indexs_list(dates_list):
    return map(
        lambda date_string:
        "logstash-syslog-" + str(date_string).replace("-", "."),
        dates_list
    )


def format_hours_list_in_day(date) -> list:
    """
    "2020-02-03" -> ["2020-02-03T00:00:00", "2020-02-03T01:00:00", ... "2020-02-03T23:00:00", "2020-02-03T23:59:59"]
    """
    date_interval_list = list(
        functools.reduce(
            lambda collec, hour:
            collec + [
                (
                    datetime.datetime.strptime(
                        str(date), "%Y-%m-%d") + datetime.timedelta(hours=hour)
                ).strftime("%Y-%m-%dT%H:%M:%S")
            ],
            list(range(24)),
            []
        )
    )

    date_interval_list.append(date + "T23:59:59")

    return date_interval_list


def hours_range_prop_list_in_day(date_interval_list) -> list:
    """
    ["2020-02-03T00:00:00", "2020-02-03T01:00:00", ... "2020-02-03T23:00:00", "2020-02-03T23:59:59"]
     -> [
            {"gte": "2020-02-03T00:00:00", "lt": "2020-02-03T01:00:00"},
            {"gte": "2020-02-03T01:00:00", "lt": "2020-02-03T02:00:00"},
            .....
            {"gte": "2020-02-03T23:00:00", "lt": "2020-02-03T23:59:59"},
        ]
    """
    return list(map(
        lambda hour_begin, hour_end:
        {
            "gte": hour_begin,
            "lt": hour_end
        },
        date_interval_list[:-1], date_interval_list[1:]))


def hour_range_prop_per_day_lists(dates_list):
    return list(
        functools.reduce(
            lambda collec, date:
            collec + [
                hours_range_prop_list_in_day(
                    format_hours_list_in_day(date))
            ],
            dates_list,
            []
        )
    )


def time_range_from_now_props_list(time_unit="d", nums=0):
    """
    [
        {"gte": "now/d", "lt": "now+1d/d"}, time_unit="d", -> nums=0
        {"gte": "now-1d/d", "lt": "now-0d/d"}, time_unit="d", -> nums=1
        {"gte": "now-2d/d", "lt": "now-1d/d"}, time_unit="d", -> nums=2
        {"gte": "now-3d/d", "lt": "now-2d/d"},
        {"gte": "now-4d/d", "lt": "now-3d/d"},
        ...
    ]
    """
    init_range = {
        "gte": "now/{0}".format(time_unit),
        "lt": "now+1{0}/{0}".format(time_unit)
    }

    return list(
        functools.reduce(
            lambda collec, num: collec +
            [{
                "gte": "now-{0}{1}/{1}".format(num+1, time_unit),
                "lt": "now-{0}{1}/{1}".format(num, time_unit)
            }],
            list(range(nums+1)),
            [init_range]
        ))


def replace_range_prop(search_properties, day_prop):
    """
    search_properties =
        "body": {
            "query": {
                "bool": {
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
    """
    search_properties["body"]["query"]["bool"]["filter"][0]["range"]["@timestamp"] = day_prop

    print(search_properties)
    return search_properties


def scan(ctx):
    es = ctx["data_es_object"]
    search_properties = ctx["search_properties"]

    ctx["search_result"] = list(
        elasticsearch.helpers.scan(
            es, index=search_properties["index"], preserve_order=True, query=search_properties["body"]))

    return ctx


def execute(ctx):
    es = ctx["data_es_object"]
    search_properties = ctx["search_properties"]

    ctx["search_result"] = es.search(
        index=search_properties["index"], body=search_properties["body"])

    return ctx
