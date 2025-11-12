# finance/main.py

from .income import add_income
from .expense import add_expense
from .summary import show_summary

def main():
    while True:
        print("\n=== Personal Finance Tracker ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter income amount: "))
            source = input("Enter income source: ")
            add_income(amount, source)

        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            add_expense(amount, category)

        elif choice == "3":
            show_summary()

        elif choice == "4":
            print("Thank you! Exiting...")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
