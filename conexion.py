import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='app_consola',
    port=3306
)

cursor = database.cursor(buffered=True)
