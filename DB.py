import mysql.connector
from mysql.connector import cursor
from flask import session
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
    cursor.execute("select * from users where username=%s",(username,))
    datas=cursor.fetchone()
    if datas:
        return "True"
    query="insert into users (username,name,password) values (%s,%s,%s)"
    values=username,name,password
    cursor.execute(query,values)
    connection.commit()
    cursor.close()
    connection.close()
def check_db(user):
    connection=get_db_connection()
    cursor=connection.cursor(dictionary=True)
    cursor.execute("select id,password from users where username=%s",(user,))
    datas=cursor.fetchone()
    id=datas.get("id")
    session["id"]=id
    cursor.close()
    connection.close()
    return datas
def insert_expense(date,time,category,expense):
    db=get_db_connection()
    cursor=db.cursor()
    id=session.get("id")
    sql = "insert into expenses (user_id, date, time, category, expense) values (%s, %s, %s, %s, %s)"
    values = (id, date, time, category, expense)
    cursor.execute(sql, values)
    db.commit()
    cursor.close()
    db.close()

def view_expense(view=None,date=None,time=None,category=None):
    conn=get_db_connection()
    cursor = conn.cursor(dictionary=True)
    id=session.get("id")
    if view:
        cursor.execute("SELECT * FROM expenses where user_id=%s",(id,))
    elif date and category:
        cursor.execute("select * from expenses where date=%s and category=%s and user_id=%s",(date,category,id))
    elif date and time:
        cursor.execute("select * from expenses where date=%s and time=%s and user_id=%s",(date,time, id))
    elif date:
        cursor.execute("SELECT * FROM expenses where date=%s and user_id=%s",(date,id))
    elif time:
        cursor.execute("SELECT * FROM expenses where time=%s and user_id=%s",(time,id))
    else:
        return None
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def update_expense(date,time,category,expense,id):
    db=get_db_connection()
    cursor=db.cursor()
    user_id=session.get("id")
    query="update expenses set date=%s,time=%s,category=%s,expense=%s where id=%s and user_id=%s"
    values=date,time,category,expense,id,user_id
    cursor.execute(query,values)
    db.commit()
    cursor.close()
    db.close()

def delete_expense(id):
    db=get_db_connection()
    cursor=db.cursor()
    user_id = session.get("id")
    query="DELETE FROM expenses WHERE id=%s and user_id=%s"
    cursor.execute(query,(id,user_id))
    db.commit()
    cursor.close()
    db.close()