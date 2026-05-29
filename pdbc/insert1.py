import mysql.connector
con = None
cursor = None
try:
    con = mysql.connector.connect(host='localhost',user="root",passwd="Root#123",database="pdbcdb")
    if con is not None:
        cursor = con.cursor()
        nm = input("Enter employee name : ")
        salary = float(input("Enter employee salary : "))
        department = input("Enter department name : ")
        # Parameterized SQL Query
        sql = "insert into employee(name,salary,department) values(%s,%s,%s)"
        cursor.execute(sql,(nm,salary,department))
        print("Record inserted successfully")
        con.commit()

except Exception as err:
    if con is not None and con.is_connected():
        con.rollback()
    print(err)
    print("Oops ! something went wrong")
finally:
    if cursor is not None:
        cursor.close()
    if con is not None:
        con.close() # destroy connection object