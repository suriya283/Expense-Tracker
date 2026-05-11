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

def insert_expense(date,time,category,expense):
    db=get_db_connection()
    cursor=db.cursor()

    sql = "insert into expenses (date,time,category,expense) values (%s, %s, %s, %s)"
    values = (date, time, category, expense)

    cursor.execute(sql, values)
    db.commit()

    cursor.close()
    db.close()
def view_expense():
    conn=get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id,date,time,category,expense FROM expenses")
    data=cursor.fetchall()

    cursor.close()
    conn.close()

    return data
def update_expense(date,time,category,expense,id):
    db=get_db_connection()
    cursor=db.cursor()
    query="update expenses set date=%s,time=%s,category=%s,expense=%s where id=%s"
    values=date,time,category,expense,id
    cursor.execute(query,values)
    db.commit()
    cursor.close()
    db.close()
def delete_expense(id):
    db=get_db_connection()
    cursor=db.cursor()
    query="DELETE FROM expenses WHERE id=%s"
    cursor.execute(query,(id,))
    db.commit()
    cursor.close()
    db.close()