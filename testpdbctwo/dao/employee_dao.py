from mysql.connector import Error
from config.db import pool
class EmployeeDAO:

    @staticmethod
    def save(emp):
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = "insert into employee(name,salary,department) values(%s,%s,%s)"
                    cursor.execute(sql,(emp.name,emp.salary,emp.department))
                    conn.commit()
                    return True
        except  Error as e:
            print(e)
            if conn and conn.is_connected():
                conn.rollback()
            return False

    @staticmethod
    def fetch_all():
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = "select * from employee"
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    for row in rows:
                      id,name,salary,department = row
                      print(f"{id} : {name} : {salary} : {department}")
        except Error as e:
            print(e)

    @staticmethod
    def update(emp):
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = "update employee set name = %s, salary = %s, department = %s where id = %s"
                    cursor.execute(sql,(emp.name,emp.salary,emp.department,emp.id))
                    conn.commit()
                    return cursor.rowcount > 0

        except Error as e:
            if conn and conn.is_connected():
                conn.rollback()
            print(e)
            return False

    @staticmethod
    def delete(id):
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = "delete from employee where id = %s"
                    cursor.execute(sql,(id,))
                    print(cursor.rowcount)
                    conn.commit()
                    return cursor.rowcount > 0
        except Error as e:
            if conn and conn.is_connected():
                conn.rollback()
            print(e)
            return False

    @staticmethod
    def find_by_id(id):
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = "select * from employee where id = %s"
                    cursor.execute(sql,(id,))
                    row  = cursor.fetchone()
                    print(row)

        except Error as e:
            print(e)