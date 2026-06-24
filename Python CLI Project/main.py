import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9995297607",
    database="hostel_db"
)
if connection.is_connected():
    print("Connected Successfully")
