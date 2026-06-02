from mysql.connector import Error
from db_config import pool
def fetch_all_employee():
    try:
        with pool.get_connection() as con:
            with con.cursor() as cursor:
                sql = "select * from employee"
                cursor.execute(sql)
                rows = cursor.fetchall() # [(),()]
                for row in rows:
                    id,name,salary,department = row
                    #print(f"{row[0]} : {row[1]} : {row[2]} : {row[3]}")
                    print(f"{id} : {name} : {salary} : {department}")
                    print("-------------------------------------------")
    except Error as e:
        print(e)
    pass
def insert():
    try:
        with pool.get_connection() as con:
            with con.cursor() as cursor:
                sql = "insert into employee(name,salary,department) values(%s,%s,%s)"
                name = input("Enter employee name: ")
                salary = float(input("Enter employee salary: "))
                department = input("Enter department: ")
                cursor.execute(sql,(name,salary,department))
                con.commit()
                print("employee inserted successfully")
    except Error as e:
        if con and con.is_connected():
            con.rollback()
        print(e)

# def insert():
#     con = None
#     cursor = None
#     try:
#       con = pool.get_connection()
#       cursor = con.cursor()
#       sql = "insert into employee(name,salary,department) values(%s,%s,%s)"
#       name = input("Enter employee name: ")
#       salary = float(input("Enter employee salary: "))
#       department = input("Enter department: ")
#       cursor.execute(sql,(name,salary,department))
#       if cursor.rowcount > 0:
#           print("Employee successfully added!")
#       con.commit()
#     except Error as e:
#         if con and con.is_connected():
#             con.rollback()
#         print(e)
#     finally:
#         if cursor is not None:
#             cursor.close()
#         if con is not None:
#             con.close()

#insert()
fetch_all_employee()