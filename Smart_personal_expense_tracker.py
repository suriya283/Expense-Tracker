from datetime import datetime
import json


file_path= "expenses.json"
def write_data(all_expenses):
    with open(file_path,"w") as file:
        json.dump(all_expenses,file, indent=4)

def read_data():
    try:
        with open(file_path,"r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]
def validate_date(date_text):
    try:
        datetime.strptime(date_text,"%d-%m-%Y")
        return True
    except ValueError:
        print("Invalid date format. use (dd-mm-yyyy)")
        return False
def validate_hour(hour):
    if not hour.isdigit():
        print("Hour must be in number")
        return False
    if int(hour) < 0 or int(hour) > 23:
        print("Hour must be between 0-23")
        return False
    return True
def validate_category(category):
    if category == "":
        print("It not to be empty")
        return True
    if category.isdigit():
        print("It must be string")
        return True
    else:
        return False
def display(record,print_found):
    if not print_found:
        print("_" * 50)
        print(f"{'DATE':<12}{'TIME':<10}{'CATEGORY':<15}{'EXPENSE':>10}")
        print("_" * 50)
    print(f"{record['date']:<12}{record['time']:<10}{record['category']:<15}{'₹'+str(record['expense']):>10}")
    return True
def add_expenses():
    while True:
        today = datetime.today()
        now_date=today.strftime("%d-%m-%Y")
        now_time=today.strftime("%H:%M:%S")
        category=input("Enter an category (Food / Travel / Rent ): ").strip()
        if category.isdigit():
            print(f"it must be string.")
            continue
        if category == "" or category == " ":
            print("Its not allowed empty space")
            continue
        else:
            try:
                expense = int(input("Enter an expenses: "))
                expenses={"date":now_date,"time":now_time,"category":category,"expense":expense}
                all_expenses=read_data()
                all_expenses.append(expenses)
                write_data(all_expenses)
                stop=input("Enter an option(y/n):").lower().strip()
                if stop!="y":
                    break
            except ValueError:
                print(f"invalid! Its not allowed string value!")

def view_expenses():
    print("1.View all expenses")
    print("2.View by date")
    print("3.View by time")
    print("4.View by date and time")
    print("5.View by date and category")
    summary=read_data()
    if not summary:
        print("File not found or empty!")
        return
    view = input("Enter the choice (1 | 2 | 3 | 4 | 5 | 6 | 7 ): ").strip()
    if view.isalpha():
        print(f"{view} is invalid!")
        return
    if view.isdigit():
        if int(view)<=0 or int(view)>7:
            print("Enter the valid option!")
            return
        if view == "1":
            print("_" * 50)
            print(f"{'DATE':<12}{'TIME':<10}{'CATEGORY':<15}{'EXPENSE':>10}")
            print("_" * 50)
            for record in summary:
                print(f"{record['date']:<12}{record['time']:<10}{record['category']:<15}{'₹'+ str(record['expense']):>10}")
            print("_" * 50)
        elif view == "2":
            found = False
            print_found = False
            view_date=input("Enter the date (dd-mm-yyyy): ")
            if not validate_date(view_date):
                return
            for expense in summary:
                now_date=expense["date"]
                if now_date== view_date:
                    print_found=display(expense,print_found)
                    found=True
            if not found:
                print("data not found")
            print("_" * 50)
        elif view == "3":
            found = False
            print_found = False
            view_time=input("Enter the time in hours (0-23): ").strip()
            if not validate_hour(view_time):
                return
            for expense_record in summary:
                time_text=expense_record.get("time")
                split_part=time_text.split(":")
                hour=split_part[0]
                if hour == view_time:
                    print_found = display(expense_record, print_found)
                    found = True
                    found=True
            if not found:
                print("Data not found")
            print("_" * 50)
        elif view == "4":
            found = False
            print_found=False
            view_date=input("Enter the date (dd-mm-yyyy): ").strip()
            view_time=input("Enter the time (0-23): ").strip()
            if not validate_date(view_date):
                return
            if not validate_hour(view_time):
                return
            for expense_record in summary:
                now_date=expense_record.get("date")
                part=expense_record.get("time")
                split_part=part.split(":")
                hour=split_part[0]
                if now_date==view_date and hour == view_time:
                    print_found = display(expense_record, print_found)
                    found=True
            if not found:
                print("Expense not found!")
            print("_"*50)
        elif view == "5":
            found=False
            print_found = False
            view_date = input("Enter the date (dd-mm-yyyy): ").strip()
            view_category = input("Enter the category: ").strip()
            if not validate_date(view_date):
                return
            if validate_category(view_category):
                return
            for expense_record in summary:
                if view_date==expense_record.get("date") and view_category==expense_record.get("category"):
                    print_found = display(expense_record, print_found)
                    found= True
            if not found:
                print("Expense not found!")
            print("_"*50)
    else:
        print(f"{view} is invalid! Please enter an valid option.")
def monthly_summary():
    summary=read_data()
    if not summary:
        print("File not found or empty!")
        return
    month_summary = {}
    for expense_record in summary:
        date=expense_record["date"]
        date=date.split("-")
        month=date[1]
        year=date[2]
        month_name= months[month] + "-" + year
        expense=expense_record["expense"]
        if month_name in month_summary:
            month_summary[month_name]+=expense
        else:
            month_summary[month_name]=expense
    print(f"{'MONTH':<10} {'TOTAL':>10}")
    for key,value in month_summary.items():
        print(f"{key:<10} {'₹'+str(value):>10}")

def category_summary():
    summary = read_data()
    if not summary:
        print("File not found or empty!")
        return
    print("1.For all category.")
    print("2.For specific category.")
    option=input("Enter an option (1 | 2): ").strip()
    if option.isalpha():
        print(f"{option} is invalid! ")
        return
    if option.isdigit():
        if int(option)>2 or int(option)<=0:
            print("Enter valid option")
            return
    if option=="1":
        all_category={}
        for expense_record in summary:
            category=expense_record["category"]
            expense=expense_record["expense"]
            if category in all_category:
                all_category[category] += expense
            else:
                all_category[category] = expense
        print("_"*23)
        print(f"{'CATEGORY':<10} {'TOTAL':>10}")
        print("_" * 23)
        for key,value in all_category.items():
            print(f"{key:<10} {'₹'+str(value):>10}")
        print("_" * 23)
    elif option=="2":
        found = False
        input_category = input("Enter the category: ").strip()
        amt = 0
        if validate_category(input_category):
            return
        for expense_record in summary:
            if expense_record["category"] == input_category:
                amt += expense_record["expense"]
                found = True
        if found:
            print("_" * 23)
            print(f"{'CATEGORY':<10} {'TOTAL':>10}")
            print("_" * 23)
            print(f"{input_category:<10} {'₹'+str(amt):>10}")
            print("_" * 23)
        else:
            print("category not found")
    else:
        print("Invalid option! Please enter an valid option.")
def total_summary():
    summary = read_data()
    if not summary:
        print("File not found or empty!")
        return
    total_expense=0
    for expense_record in summary:
        total_expense+=expense_record["expense"]
    print("_"*25)
    print(f"Total expense= ₹{total_expense}")
    print("_" * 25)
def highest_expenses():
    summary=read_data()
    if not summary:
        print("File not found or empty!")
        return
    highest_expense = max(summary, key=lambda x: x["expense"])
    print("\nHighest expense")
    display(highest_expense, print_found=False)
    print("_" * 50)
def minimum_expenses():
    summary = read_data()
    if not summary:
        print("File not found or empty!")
        return
    minimum_expense = min(summary, key=lambda x: x["expense"])
    print("\nMinimum expense")
    display(minimum_expense, print_found=False)
    print("_" * 50)
def edit_expenses():
    summary = read_data()
    if not summary:
        print("File not found or empty!")
        return
    print("1.For edit date")
    print("2.For edit category")
    print("3.For edit expense")
    choice=input("Enter the choice (1 | 2 | 3 ): ").strip()
    if choice.isalpha():
        print(f"{choice} is invalid")
        return
    if choice.isdigit():
        if int(choice)<=0 or int(choice)>3:
            return
    index = -1
    index_list=[]
    found = False
    date = input("Enter the date (dd-mm-yyyy): ").strip()
    category = input("Enter the category: ").strip()
    if not validate_date(date):
        return
    for expense_record in summary:
        index += 1
        if expense_record["date"] == date and expense_record["category"] == category:
            index_list.append(index)
            found = True
    if choice == "1":
        if found:
            print(f"{len(index_list)} records found!")
            for idx in range(len(index_list)):
                print(f"\nIndex {idx + 1}")
                display(summary[index_list[idx]],print_found=False)
                print("_"*50)
            date_index = input("Enter the index: ").strip()
            if date_index.isalpha():
                print(f"{date_index} is invalid!")
                return
            if date_index.isdigit():
                if int(date_index) > len(index_list) or int(date_index) <=0:
                    print("Enter valid option!")
                    return
            new_date = input("Enter new date (dd-mm-yyyy): ").strip()
            if not validate_date(new_date):
                return
            summary[index_list[int(date_index) - 1]]["date"] = new_date
            write_data(summary)
            print("date updated successfully")
    elif choice == "2":
        if found:
            print(f"{len(index_list)} records found!")
            for idx in range(len(index_list)):
                print(f"\nIndex {idx + 1}")
                display(summary[index_list[idx]], print_found=False)
                print("_" * 50)
            category_index=input("Enter the category: ").strip()
            if category_index.isdigit():
                if int(category_index) > len(index_list) or int(category_index) <= 0:
                    print("Enter valid option!")
                    return
            new_category =input("Enter new category: ").strip()
            if validate_category(new_category):
                return
            summary[index_list[int(category_index)-1]]["category"] = new_category
            write_data(summary)
            print("Category updated successfully")
    elif choice =="3":
        if found:
            print(f"{len(index_list)} records found!")
            for idx in range(len(index_list)):
                print(f"\nIndex {idx + 1}")
                display(summary[index_list[idx]], print_found=False)
                print("_" * 50)
            expense_index = input("Enter expense index: ").strip()
            if expense_index.isalpha():
                print(f"{expense_index} is invalid!")
                return
            if expense_index.isdigit():
                if int(expense_index) > len(index_list) or int(expense_index) <= 0:
                    print("Enter valid option!")
                    return
            try:
                new_expense = int(input("Enter new expense: "))
                summary[index_list[int(expense_index)-1]]["expense"]=new_expense
                write_data(summary)
                print("Expense updated successfully")
            except ValueError:
                print("String is not acceptable!")
        else:
            print("expense not found!")
def delete_expense():
    summary = read_data()
    if not summary:
        print("File not found or empty!")
        return
    index=-1
    index_list=[]
    found=False
    date = input("Enter the date (dd-mm-yyyy): ").strip()
    category=input("Enter the category: ").strip()
    if not validate_date(date):
        print("Invalid date format. use (dd-mm-yyyy)")
        return
    if validate_category(category):
        return
    for expense_record in summary:
        index+=1
        if expense_record["date"]==date and expense_record["category"]==category:
            index_list.append(index)
            found=True
    if found:
        print(f"{len(index_list)} expense found")
        expense_index=1
        for idx in index_list:
            print(f"\nIndex {expense_index}")
            display(summary[idx], print_found=False)
            print("_" * 50)
            expense_index+=1
        delete_index=input("Enter expense index: ").strip()
        if delete_index.isalpha():
            print(f"{delete_index} is invalid!")
            return
        if delete_index.isdigit():
            if int(delete_index)>len(index_list) or int(delete_index)<=0:
                print("Enter valid option!")
                return
        summary.pop(index_list[int(delete_index)-1])
        write_data(summary)
        print("Expense successfully deleted")
    else:
        print("expense not found!")
def main():
    is_running=True
    while is_running:
        print("SMART PERSONAL EXPENSES TRACKER")
        print("1.Add Expenses")
        print("2.View Expenses")
        print("3.Monthly-wise total expense")
        print("4.Category-wise total expense")
        print("5.Total expense")
        print("6.View highest expense")
        print("7.View minimum expense")
        print("8.For edit expense")
        print("9.Delete expense")
        print("10.Exit")
        options=input("Enter an option (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 ): ").strip()
        if options.isdigit():
            if  options == "1":
                add_expenses()
            elif  options == "2":
                view_expenses()
            elif  options == "3":
                monthly_summary()
            elif  options == "4":
                category_summary()
            elif options == "5":
                total_summary()
            elif options == "6":
                highest_expenses()
            elif options == "7":
                minimum_expenses()
            elif options=="8":
                edit_expenses()
            elif options == "9":
                delete_expense()
            elif  options == "10":
                print("You are exited")
                is_running=False
            else:
                print("Please enter the valid option")
        else:
            print(f"{options} is invalid! string is not acceptable.")
if __name__=="__main__":
    months = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr", "05": "May", "06": "June", "07": "July", "08": "Aug",
              "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}
# def sort_expense(summary):
#     for i in range(len(summary)):
#         date1=summary[i]["date"].split("-")
#         for j in range(1,len(summary)):
#             date2 = summary[j]["date"].split("-")
#             if date1[0]>date2[0]:
#                 summary[j],summary[i]=summary[i],summary[j]
#     return summary