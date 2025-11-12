# payroll/employee.py
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Employee:
    emp_id: str
    name: str
    base_salary: float
    allowances: Dict[str, float] = field(default_factory=dict)
    deductions: Dict[str, float] = field(default_factory=dict)

    def total_allowances(self) -> float:
        return sum(self.allowances.values())

    def total_deductions(self) -> float:
        return sum(self.deductions.values())
