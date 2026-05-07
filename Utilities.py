from flask import Flask, request, flash
from DB import get_db_connection, insert_expense, view_expense
def add_expenses():
    date = request.form['date']
    time = request.form['time']
    category = request.form['category']
    expense = int(request.form['expense'])
    insert_expense(date, time, category, expense)
    flash("stored successfully")
def view_expenses(view):
        if view == "1":
            return view_expense()
    #     elif view == "2":
    #         found = False
    #         print_found = False
    #         view_date=input("Enter the date (dd-mm-yyyy): ")
    #         if not validate_date(view_date):
    #             return
    #         for expense in summary:
    #             now_date=expense["date"]
    #             if now_date== view_date:
    #                 print_found=display(expense,print_found)
    #                 found=True
    #         if not found:
    #             print("data not found")
    #         print("_" * 50)
    #     elif view == "3":
    #         found = False
    #         print_found = False
    #         view_time=input("Enter the time in hours (0-23): ").strip()
    #         if not validate_hour(view_time):
    #             return
    #         for expense_record in summary:
    #             time_text=expense_record.get("time")
    #             split_part=time_text.split(":")
    #             hour=split_part[0]
    #             if hour == view_time:
    #                 print_found = display(expense_record, print_found)
    #                 found = True
    #                 found=True
    #         if not found:
    #             print("Data not found")
    #         print("_" * 50)
    #     elif view == "4":
    #         found = False
    #         print_found=False
    #         view_date=input("Enter the date (dd-mm-yyyy): ").strip()
    #         view_time=input("Enter the time (0-23): ").strip()
    #         if not validate_date(view_date):
    #             return
    #         if not validate_hour(view_time):
    #             return
    #         for expense_record in summary:
    #             now_date=expense_record.get("date")
    #             part=expense_record.get("time")
    #             split_part=part.split(":")
    #             hour=split_part[0]
    #             if now_date==view_date and hour == view_time:
    #                 print_found = display(expense_record, print_found)
    #                 found=True
    #         if not found:
    #             print("Expense not found!")
    #         print("_"*50)
    #     elif view == "5":
    #         found=False
    #         print_found = False
    #         view_date = input("Enter the date (dd-mm-yyyy): ").strip()
    #         view_category = input("Enter the category: ").strip()
    #         if not validate_date(view_date):
    #             return
    #         if validate_category(view_category):
    #             return
    #         for expense_record in summary:
    #             if view_date==expense_record.get("date") and view_category==expense_record.get("category"):
    #                 print_found = display(expense_record, print_found)
    #                 found= True
    #         if not found:
    #             print("Expense not found!")
    #         print("_"*50)
    # else:
    #     print(f"{view} is invalid! Please enter an valid option.")