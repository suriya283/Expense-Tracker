from flask import Flask, render_template, request, redirect
from DB import get_db_connection, insert_expense

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

cursor=get_db_connection()
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method=='POST':
        date = request.form['date']
        time = request.form['time']
        category = request.form['category']
        expense = int(request.form['expense'])
        insert_expense(date,time,category,expense)

        return "stored successfully"
    return render_template('add_expense.html')

@app.route('/view')
def view():
    return render_template('view_expense.html')
if __name__=='__main__':
    app.run(debug=True)