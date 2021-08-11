import pymysql
import os
from dotenv import load_dotenv
load_dotenv()


###
# Create database forecast_inms first,
# GRANT ALL PRIVILEGES ON forecast_inms.* TO 'user'@'host';
###


def dbconn_prepare(db_ctx):
    db_conn = pymysql.connect(
        host=os.getenv("FORECAST_DB_HOST"),
        user=os.getenv("FORECAST_DB_USER"),
        password=os.getenv("FORECAST_DB_PASSWORD"),
        database="forecast_inms",
    )

    db_ctx["db_conn"] = db_conn
    db_ctx["db_cursor"] = db_conn.cursor()

    return db_ctx


def create_forecast_table(db_ctx):
    sql = """
        CREATE TABLE IF NOT EXISTS forecast_data(
        id INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        metric VARCHAR(50),
        job_id VARCHAR(50),
        create_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
    """

    db_ctx["table_create_res"] = db_ctx["db_cursor"].execute(sql)

    db_ctx["db_conn"].commit()

    return db_ctx


def create_forecast_test_datas(db_ctx):
    sql = """
        INSERT INTO `forecast_data` (`metric`, `job_id`) VALUES
        ('CurrentInRate', 'testCurrentInRate123'),
        ('CurrentOutRate', 'testCurrentOutRate456')
    """

    db_ctx["datas_create_res"] = db_ctx["db_cursor"].execute(sql)

    db_ctx["db_conn"].commit()

    return db_ctx


if __name__ == "__main__":
    ctx = {
        "db_conn": None,
        "db_cursor": None,
        "table_create_res": None,
        "datas_create_res": None
    }

    dbconn_prepare(ctx) and \
        create_forecast_table(ctx) and \
        create_forecast_test_datas(ctx) and \
        print(ctx)
