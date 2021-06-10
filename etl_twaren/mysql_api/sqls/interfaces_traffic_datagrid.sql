use NetFlow;

SELECT MAX(CASE WHEN SummaryTable.ShowColor='Green' THEN CAST(AlarmCount AS CHAR) ELSE '0' END) AS GreenCount,
MAX(CASE WHEN SummaryTable.ShowColor='Red' THEN CAST(AlarmCount AS CHAR)  ELSE '0' END) AS RedCount,
MAX(CASE WHEN SummaryTable.ShowColor='Gray' THEN CAST(AlarmCount AS CHAR)  ELSE '0' END) AS GrayCount,
MAX(CASE WHEN SummaryTable.ShowColor is NULL THEN CAST(AlarmCount AS CHAR)  ELSE '0' END) AS MonitorTotalCount
FROM
(SELECT Total.ShowColor, COUNT(*)as AlarmCount
FROM
(SELECT List.*,
CASE WHEN (List.Traffic_inStatus = 0 AND List.Traffic_outStatus = 0 AND List.Interfaces_alarm = 1) THEN 'Green'
 WHEN (List.Traffic_inStatus = 1 AND List.Traffic_outStatus = 0 AND List.Interfaces_alarm = 1) THEN 'Red'
 WHEN (List.Traffic_inStatus = 0 AND List.Traffic_outStatus = 1 AND List.Interfaces_alarm = 1) THEN 'Red'
 WHEN (List.Traffic_inStatus = 1 AND List.Traffic_outStatus = 1 AND List.Interfaces_alarm = 1) THEN 'Red'
 WHEN (List.Traffic_inStatus = 1 AND List.Traffic_outStatus = 0 AND List.Interfaces_alarm = 0) THEN 'Gray'
 WHEN (List.Traffic_inStatus = 0 AND List.Traffic_outStatus = 1 AND List.Interfaces_alarm = 0) THEN 'Gray'
 WHEN (List.Traffic_inStatus = 0 AND List.Traffic_outStatus = 0 AND List.Interfaces_alarm = 0) THEN 'Gray'
 WHEN (List.Traffic_inStatus = 1 AND List.Traffic_outStatus = 1 AND List.Interfaces_alarm = 0) THEN 'Gray'
 End ShowColor
 FROM
 (SELECT Interfaces.Interfaces_id, Interfaces.Interfaces_device, Interfaces.Interfaces_description, Interfaces.Interfaces_alarm,
  Interfaces.Interfaces_traffic_in_high, Interfaces.Interfaces_traffic_in_low,
  Interfaces.Interfaces_traffic_out_high,Interfaces.Interfaces_traffic_out_low,
  DATE_FORMAT(Interfaces_Traffic.CheckTime, '%Y-%m-%d %H:%i:%s')  AS CheckTime,
  Interfaces_Traffic.CurrentInRate, Interfaces_Traffic.CurrentOutRate,
  Interfaces_Status.Traffic_inStatus, Interfaces_Status.Traffic_outStatus
  FROM Interfaces
  LEFT JOIN (Interfaces_Traffic, Interfaces_Status)
  ON (Interfaces_Traffic.Interfaces_id = Interfaces.Interfaces_id  AND Interfaces_Status.Interfaces_id = Interfaces.Interfaces_id)
  WHERE Interfaces_Type NOT IN ('International','IP Research')
  ) as List) as Total
 GROUP BY (Total.ShowColor) WITH ROLLUP) as SummaryTable
