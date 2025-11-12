# finance/summary.py

from .income import get_total_income
from .expense import get_total_expense

def show_summary():
    total_income = get_total_income()
    total_expense = get_total_expense()
    savings = total_income - total_expense

    print("\n------ Finance Summary ------")
    print("Total Income :", total_income)
    print("Total Expense:", total_expense)
    print("Savings      :", savings)
    print("-----------------------------\n")
