import mysql.connector
from mysql.connector import cursor


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="9043148891",
        database="expense_db"
    )
print("connected successfully")

def insert_expense(date,time,category,amount):
    db=get_db_connection()
    cursor=db.cursor()

    sql = "insert into expenses (date,time,category,amount) values (%s, %s, %s, %s)"
    values = (date, time, category, amount)

    cursor.execute(sql, values)
    db.commit()

    cursor.close()
    db.close()
def view_expense():
    conn=get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT date,time,category,expense FROM expenses")
    data=cursor.fetchall()

    cursor.close()
    conn.close()

    return data