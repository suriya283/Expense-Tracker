from flask import Flask, render_template, request, redirect

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods=["get","post"])
def add():
    if request.method=="post":
        date=request.form["Date"]
        time=request.form["time"]
        category=request.form["category"]
        expense=request.form["expense"]
        print(date,time,category,expense)
        return redirect("/")
    return render_template("add_expense.html")
@app.route('/view')
def view():
    return render_template('view_expense.html')
if __name__=='__main__':
    app.run(debug=True)