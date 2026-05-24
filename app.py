from flask import Flask, render_template, request, redirect, url_for
from DB import delete_expense
from Utilities import add_expenses, view_expenses, add_expense
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
        add_expenses()
        return redirect(url_for("add"))
    return render_template('add_expense.html')

@app.route('/view',methods =['GET','POST'])
def view():
    expense=[]
    if request.method=='POST':
        user_input=request.form.get('View expense')
        if user_input == "View All":
            expense=view_expenses('1')
    return render_template('view_expense.html', expense=expense)
@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    if request.method == 'POST':
        add_expense(id)
    return render_template('update_expense.html',id=id)
@app.route('/delete/<int:id>')
def delete(id):
    delete_expense(id)
    return redirect('/view')
if __name__=='__main__':
    app.run(debug=True)