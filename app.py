from unittest import result

from flask import Flask, render_template, request, redirect, url_for
from DB import *
from Utilities import *
app=Flask(__name__)
app.secret_key="secret123"
@app.route('/')
def login():
    return render_template('index.html')
@app.route('/signup',methods=["GET","POST"])
def sign_up():
    if request.method == "POST":
        signup_data()
        return render_template("index.html",result="Successfully Registered")
    return render_template("index.html")
@app.route('/signin',methods=['GET',"POST"])
def sign_in():
    if request.method == "POST":
        result=signin_data()
        if result:
            return render_template("home.html",result="You are Signed In")
        else:
            return render_template("index.html",error="Incorrect Username or Password")
    return render_template("index.html")
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method=='POST':
        add_expenses()
        return redirect(url_for("add"))
    return render_template('add_expense.html')

@app.route('/view',methods =['GET','POST'])
def view():
    expenses=[]
    if request.method=='POST':
        user_input=request.form.get('View expense')
        if user_input == "View All":
            expenses=view_expenses('1')
        elif user_input == "View Date":
            user_input=request.form.get("date")
            expenses=view_expense(date=user_input)
        elif user_input == "View Time":
            user_input=request.form.get("time")
            expenses=view_expense(time=user_input)
        elif user_input == "View Date and Time":
            date=request.form.get("date")
            time=request.form.get("time")
            expenses=view_expense(date=date,time=time)
        elif user_input== "View Date and Category":
            date=request.form.get("date")
            category=request.form.get("category")
            expenses=view_expense(date=date,category=category)
        return render_template('view_expense.html', expenses=expenses)
    return render_template('view_expense.html',expenses=[])
@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    if request.method == 'POST':
        add_expenses(id)
    return render_template('update_expense.html',id=id)
@app.route('/delete/<int:id>')
def delete(id):
    delete_expense(id)
    return redirect('/view')
if __name__=='__main__':
    app.run(debug=True)