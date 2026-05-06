from flask import Flask, render_template, request, redirect, url_for, flash
from DB import get_db_connection, insert_expense

app=Flask(__name__)
app.secret_key="secret123"
@app.route('/')
def login():
    return render_template('login_page.html')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method=='POST':
        date = request.form['date']
        time = request.form['time']
        category = request.form['category']
        expense = int(request.form['expense'])
        insert_expense(date,time,category,expense)
        flash("stored successfully")
        return redirect(url_for("add"))
    return render_template('add_expense.html')

@app.route('/view')
def view():
    return render_template('view_expense.html')
if __name__=='__main__':
    app.run(debug=True)