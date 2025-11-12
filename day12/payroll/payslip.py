# payroll/payslip.py
from .employee import Employee
from .salary import breakdown as salary_breakdown   # alias import
from .helpers import fmt_currency, save_text, now_str
from typing import Dict

def generate_payslip(employee: Employee, month: str, year: int, save: bool = False) -> str:
    """
    Returns a formatted payslip string for the employee.
    If save=True, saves a .txt in payslips/<emp_id>_<month>_<year>.txt
    """
    bd: Dict[str, float] = salary_breakdown(employee)
    lines = []
    lines.append("=== Company XYZ Pvt Ltd ===")
    lines.append(f"Payslip for: {employee.name} (ID: {employee.emp_id})")
    lines.append(f"Period: {month} {year}")
    lines.append(f"Generated: {now_str()}")
    lines.append("-" * 30)
    lines.append(f"Base Salary : {fmt_currency(employee.base_salary)}")
    lines.append("Allowances:")
    if employee.allowances:
        for k, v in employee.allowances.items():
            lines.append(f"  {k:12} : {fmt_currency(v)}")
    else:
        lines.append("  (none)")
    lines.append(f"Gross Salary: {fmt_currency(bd['gross'])}")
    lines.append("-" * 30)
    lines.append("Deductions:")
    if employee.deductions:
        for k, v in employee.deductions.items():
            lines.append(f"  {k:12} : {fmt_currency(v)}")
    else:
        lines.append("  (none)")
    lines.append(f"Tax         : {fmt_currency(bd['tax'])}")
    lines.append(f"Total Deduct: {fmt_currency(bd['deductions'])}")
    lines.append("-" * 30)
    lines.append(f"Net Pay     : {fmt_currency(bd['net'])}")
    lines.append("-" * 30)

    text = "\n".join(lines)

    if save:
        filename = f"payslips/{employee.emp_id}_{month}_{year}.txt"
        save_text(filename, text)

    return text

def run_cli():
    # simple CLI to create an employee and generate payslip
    print("Payroll CLI — generate one payslip")
    emp_id = input("Employee ID: ").strip() or "E001"
    name = input("Name: ").strip() or "John Doe"
    base_salary = float(input("Base salary (numbers only): ").strip() or "30000")

    # allowances: quick interactive add
    allowances = {}
    while True:
        a = input("Add allowance (name amount) or press Enter to stop: ").strip()
        if not a:
            break
        try:
            nm, amt = a.split(None, 1)
            allowances[nm] = float(amt)
        except Exception:
            print("Bad input. Example: HRA 2000")

    deductions = {}
    while True:
        d = input("Add deduction (name amount) or press Enter to stop: ").strip()
        if not d:
            break
        try:
            nm, amt = d.split(None, 1)
            deductions[nm] = float(amt)
        except Exception:
            print("Bad input. Example: PF 1500")

    month = input("Month name (e.g. March): ").strip() or "March"
    year = int(input("Year (e.g. 2025): ").strip() or "2025")
    save_opt = input("Save to file? (y/N): ").strip().lower() == "y"

    emp = Employee(emp_id=emp_id, name=name, base_salary=base_salary,
                   allowances=allowances, deductions=deductions)

    payslip = generate_payslip(emp, month, year, save=save_opt)
    print("\n" + payslip)

if __name__ == "__main__":
    run_cli()
