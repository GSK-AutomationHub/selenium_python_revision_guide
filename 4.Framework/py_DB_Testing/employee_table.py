import sqlite3
from employee_info import Employee

connect = sqlite3.connect(':memory:')
cur = connect.cursor()

def create_employee_table():
    cur.execute('''
        CREATE TABLE EMPLOYEE(
        first_name TEXT,
        last_name TEXT,
        pay INTEGER    
        )''')
    connect.commit()

def insert_employee_record(emp):
    with connect:
        cur.execute("INSERT INTO EMPLOYEE VALUES (:first_name, :last_name, :pay)",
                    {'first_name':emp.first_name,'last_name':emp.last_name,'pay':emp.pay})


def get_employee_record(emp):
    with connect:
        cur.execute("SELECT * FROM EMPLOYEE WHERE first_name = :first_name" ,
                    {'first_name':emp.first_name})
        return cur.fetchone()

def get_all_employee_record():
    with connect:
        cur.execute("SELECT * FROM EMPLOYEE")
        return cur.fetchall()

def update_employee_record(emp,pay_value):
    with connect:
        cur.execute("UPDATE EMPLOYEE SET pay =:pay WHERE first_name = :first_name" ,
                    {'pay':pay_value, 'first_name':emp.first_name})

def delete_employee_record(emp):
    with connect:
        cur.execute("DELETE FROM EMPLOYEE WHERE first_name = :first_name" ,
                    {'first_name':emp.first_name})

def delete_all_employee_record():
    with connect:
        cur.execute("DELETE FROM EMPLOYEE")

def setup_db_records():
    create_employee_table()
    for employee_object in Employee.create_employee_objects():
        insert_employee_record(employee_object)
    print(get_all_employee_record())
    return get_all_employee_record()

def update_db_record(emp,pay_value=0):
    # Update employee record
    update_employee_record(emp,pay_value)
    # Get employee record
    print(get_employee_record(emp))

def delete_db_record(emp):
    # Delete employee record
    delete_employee_record(emp)
    # Print employee record
    print(get_employee_record(emp))



