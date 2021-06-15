use NetFlow;

SELECT Interfaces.Interfaces_id, Interfaces.Interfaces_device, Interfaces.Interfaces_description,
       DATE_FORMAT(Interfaces_Traffic.CheckTime, '%Y-%m-%d %H:%i:%s')  AS CheckTime,
       Interfaces_Traffic.CurrentInRate, Interfaces_Traffic.CurrentOutRate
FROM Interfaces
LEFT JOIN (Interfaces_Traffic, Interfaces_Status)
ON (Interfaces_Traffic.Interfaces_id = Interfaces.Interfaces_id  AND Interfaces_Status.Interfaces_id = Interfaces.Interfaces_id)
WHERE Interfaces_Type NOT IN ('International','IP Research')

/* SELECT count(Interfaces.Interfaces_id) AS count_id FROM Interfaces */
/* SELECT Interfaces.Interfaces_id, Interfaces.Interfaces_device, Interfaces.Interfaces_description, Interfaces.Interfaces_alarm, */
/*        Interfaces.Interfaces_traffic_in_high, Interfaces.Interfaces_traffic_in_low, */
/*        Interfaces.Interfaces_traffic_out_high,Interfaces.Interfaces_traffic_out_low, */
/*        DATE_FORMAT(Interfaces_Traffic.CheckTime, '%Y-%m-%d %H:%i:%s')  AS CheckTime, */
/*        Interfaces_Traffic.CurrentInRate, Interfaces_Traffic.CurrentOutRate, */
/*        Interfaces_Status.Traffic_inStatus, Interfaces_Status.Traffic_outStatus */
