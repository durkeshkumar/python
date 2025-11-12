# payroll/helpers.py
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

def fmt_currency(amount: float) -> str:
    # simple INR style (you can change)
    return f"₹{amount:,.2f}"

def save_text(filename: str, text: str) -> None:
    p = Path(filename)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")

def now_str() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def dict_to_lines(d: Dict[str, Any]) -> str:
    return "\n".join(f"{k}: {v}" for k, v in d.items())
