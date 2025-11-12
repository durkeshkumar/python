# payroll/tax.py
"""
Simple progressive tax example:
- 0% for up to 25000
- 5% for next 25000
- 10% for next 50000
- 15% above that

This is illustrative — replace with your real rules.
"""

def compute_tax(income: float) -> float:
    tax = 0.0
    remain = income

    brackets = [
        (25000, 0.00),
        (25000, 0.05),
        (50000, 0.10),
        (float("inf"), 0.15),
    ]

    for limit, rate in brackets:
        take = min(remain, limit)
        tax += take * rate
        remain -= take
        if remain <= 0:
            break

    return round(tax, 2)
