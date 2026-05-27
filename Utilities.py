from flask import request, flash
from DB import *
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
def signin_data():
    user_name=request.form["username"]
    password=request.form["password"]
    db_pass=check_db(user_name)
    db_pass=db_pass.get("password")
    if check_password_hash(db_pass,password):
        return True
    else:
        return False
def signup_data():
    user_name=request.form["username"]
    name=request.form["name"]
    password=request.form["password"]
    hash_password=generate_password_hash(password)
    store_user(user_name,name,hash_password)
def add_expenses(id=None):
    if not id:
        date = request.form['date']
        time = request.form['time']
        category = request.form['category']
        expense = int(request.form['expense'])
        insert_expense(date, time, category, expense)
        flash("Stored Successfully")
    else:
        date = request.form['date']
        time = request.form['time']
        category = request.form['category']
        expense = int(request.form['expense'])
        update_expense(date, time, category, expense,id)

def view_expenses(view):
        if view == "1":
            return view_expense(view="all")