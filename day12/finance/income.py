
incomes = []

def add_income(amount, source):
    incomes.append({"amount": amount, "source": source})
    print(f"Income added: ₹{amount} from {source}")

def get_total_income():
    total = 0
    for income in incomes:
        total += income["amount"]
    return total
