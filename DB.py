import mysql.connector
from mysql.connector import cursor
from select import select


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="9043148891",
        database="expense_db"
    )
print("connected successfully")
def store_user(username,name,password):
    connection=get_db_connection()
    cursor=connection.cursor()
    query="insert into users (username,name,password) values (%s,%s,%s)"
    values=username,name,password
    cursor.execute(query,values)
    connection.commit()
    cursor.close()
    connection.close()
def check_db(user):
    connection=get_db_connection()
    cursor=connection.cursor(dictionary=True)
    cursor.execute("select password from users where username=%s",(user,))
    hash_pass=cursor.fetchone()
    cursor.close()
    connection.close()
    return hash_pass
def insert_expense(date,time,category,expense):
    db=get_db_connection()
    cursor=db.cursor()

    sql = "insert into expenses (date,time,category,expense) values (%s, %s, %s, %s)"
    values = (date, time, category, expense)

    cursor.execute(sql, values)
    db.commit()

    cursor.close()
    db.close()

def view_expense(view=None,date=None,time=None,category=None):
    conn=get_db_connection()
    cursor = conn.cursor(dictionary=True)
    if view:
        cursor.execute("SELECT * FROM expenses")
    elif date and not time:
        cursor.execute("SELECT * FROM expenses where date=%s",(date,))
    elif time and not date:
        cursor.execute("SELECT * FROM expenses where time=%s",(time,))
    elif date and time:
        cursor.execute("select * from expenses where date=%s and time=%s",(date,time))
    elif date and category:
        cursor.execute("select * from expenses where date=%s and time=%s",(date,category))
    else:
        return None
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