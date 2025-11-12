
expenses = []

def add_expense(amount, category):
    expenses.append({"amount": amount, "category": category})
    print(f"Expense added: ₹{amount} for {category}")

def get_total_expense():
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total
