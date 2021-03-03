import mysql.connector


def conectar():
    bd_conn = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='app_consola',
        port=3306
    )

    cursor = bd_conn.cursor(buffered=True)

    return [bd_conn, cursor]
