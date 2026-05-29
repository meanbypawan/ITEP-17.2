import mysql.connector
def get_connection():
    con = None
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Root#123",
            database="pdbcdb"
        )
    except mysql.connector.Error as error:
        print("Connection Error")

    return con