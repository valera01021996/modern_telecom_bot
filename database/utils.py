import pymysql


def connect_to_database() -> tuple:
    connection = pymysql.connect(
        host="192.168.100.4",
        database="modern",
        user="root",
        password="twix3327348"
    )
    cursor = connection.cursor()
    return connection, cursor
