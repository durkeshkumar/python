# payroll/salary.py
from .employee import Employee
from .tax import compute_tax

# exported alias names (used by payslip)
def calc_gross(employee: Employee) -> float:
    """Gross salary = base + allowances"""
    return employee.base_salary + employee.total_allowances()

def calc_net(employee: Employee) -> float:
    """
    Net salary = gross - tax - other deductions
    where tax is computed based on gross
    """
    gross = calc_gross(employee)
    tax = compute_tax(gross)
    other_deductions = employee.total_deductions()
    net = gross - tax - other_deductions
    return round(net, 2)

def breakdown(employee: Employee):
    gross = calc_gross(employee)
    tax = compute_tax(gross)
    return {
        "gross": round(gross, 2),
        "tax": round(tax, 2),
        "deductions": round(employee.total_deductions(), 2),
        "net": calc_net(employee)
    }
