'''
   1. First get the connection object
   2. Get Cursor object to execute sql query
   3. Create SQL Query
   4. Use execute() or executeMany to execute sql query
   5. If operation success commit otherwise rollback
   6. close the cursor
   7. close the connection

'''
import mysql.connector
con = None
cursor = None
try:
    con = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "Root#123",
        database = "pdbcdb",
    )
    if con is not None:
        cursor = con.cursor()
        sql = "insert into employee(name,salary,department) values('Atul',90000,'HR')"
        cursor.execute(sql)
        if cursor.rowcount > 0:
            print("Record inserted successfully")
        con.commit() # Commit transaction
except Exception as err:
    if con.is_connected() and con is not None:
        con.rollback()
    print("Oops something went wrong")
finally:
   if cursor is not None:
       cursor.close()
   if con is not None:
       con.close()
