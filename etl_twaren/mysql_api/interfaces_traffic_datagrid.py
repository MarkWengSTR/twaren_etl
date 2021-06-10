import utils


def interfaces_tracfic_datagrid_query():
    db_ctx = {
        "db_conn": None,
        "db_cursor": None,
        "sql": "",
        "resutl": {}
    }

    with open("sqls\\interfaces_traffic_oatagrid.sql", "r") as sql_file:
        db_ctx["sql"] = sql_file.read()

        utils.dbconn_prepare(db_ctx) and \
            utils.query_all(db_ctx)

    return db_ctx


print(interfaces_tracfic_datagrid_query())

# if (AlarmType == "Green" || AlarmType == "Red" || AlarmType == "Gray")
# {
#     switch (AlarmType)
#     {
#         case "Green":
#             strConditionSQL = " WHERE ShowColor = 'Green' ";
#             break;

#         case "Red":
#             strConditionSQL = " WHERE ShowColor = 'Red' ";
#             break;

#         case "Gray":
#             strConditionSQL = " WHERE ShowColor = 'Gray' ";
#             break;
#     }

#     strSQL = "SELECT A.Interfaces_id, A.Interfaces_description, A.Interfaces_device, A.CheckTime, A.Msg, B.ifDescr, A.CurrentPortStatus, A.ShowColor " +
#              " FROM " +
#              "(SELECT List.* " +
#              "  FROM " +
#              "(SELECT III_Port.Interfaces_id, Interfaces_III.Interfaces_description, Interfaces_III.Interfaces_device, Interfaces_III.Interfaces_ifIndex, DATE_FORMAT(III_Port.CheckTime, '%Y-%m-%d %H:%i:%s') AS CheckTime, Interfaces_III.Interfaces_alarm, '' as Msg, " +
#              "   CASE WHEN (III_Port.CurrentPort = 1) THEN 'UP'  " +
#              "        WHEN (Interfaces_III.Interfaces_alarm = 1) THEN 'Down' " +
#              "        WHEN (Interfaces_III.Interfaces_alarm = 0) THEN 'Ignore' " +
#              "   END CurrentPortStatus, " +
#              "   CASE WHEN (III_Port.CurrentPort = 1) THEN 'Green'  " +
#              "        WHEN (Interfaces_III.Interfaces_alarm = 1) THEN 'Red' " +
#              "        WHEN (Interfaces_III.Interfaces_alarm = 0) THEN 'Gray' " +
#              "   END ShowColor " +
#              "FROM III_Port, Interfaces_III " +
#              "WHERE Interfaces_III.Interfaces_id = III_Port.Interfaces_id) as List " + strConditionSQL +
#              "ORDER BY List.Interfaces_id, List.Interfaces_description) as A " +
#              "LEFT JOIN (SELECT ifDescr, ifIndex FROM Devices_Interfaces WHERE Devices_id=26) as B " +
#               "ON A.Interfaces_ifIndex = B.ifIndex";
# }
# else if (AlarmType == "Total" || AlarmType == null)
# {
#     strSQL = "SELECT A.Interfaces_id, A.Interfaces_description, A.Interfaces_device, A.CheckTime, A.Msg, B.ifDescr, A.CurrentPortStatus, A.ShowColor " +
#              " FROM " +
#              "(SELECT III_Port.Interfaces_id, Interfaces_III.Interfaces_description, Interfaces_III.Interfaces_device, Interfaces_III.Interfaces_ifIndex, DATE_FORMAT(III_Port.CheckTime, '%Y-%m-%d %H:%i:%s') AS CheckTime, Interfaces_III.Interfaces_alarm, '' as Msg, " +
#              "   CASE WHEN (III_Port.CurrentPort = 1) THEN 'UP'  " +
#              "        WHEN (Interfaces_III.Interfaces_alarm = 1) THEN 'Down' " +
#              "        WHEN (Interfaces_III.Interfaces_alarm = 0) THEN 'Ignore' " +
#              "   END CurrentPortStatus, " +
#              "   CASE WHEN (III_Port.CurrentPort = 1) THEN 'Green'  " +
#              "        WHEN (Interfaces_III.Interfaces_alarm = 1) THEN 'Red' " +
#              "        WHEN (Interfaces_III.Interfaces_alarm = 0) THEN 'Gray' " +
#              "   END ShowColor " +
#              "FROM III_Port, Interfaces_III " +
#              "WHERE Interfaces_III.Interfaces_id = III_Port.Interfaces_id " +
#              "ORDER BY Interfaces_id, Interfaces_description) as A " +
#              "LEFT JOIN (SELECT ifDescr, ifIndex FROM Devices_Interfaces WHERE Devices_id=26) as B " +
#               "ON A.Interfaces_ifIndex = B.ifIndex";
# }
