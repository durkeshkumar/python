# payroll/__init__.py
"""Employee payroll package exports."""

from .payslip import generate_payslip, run_cli

__all__ = ["generate_payslip", "run_cli"]
