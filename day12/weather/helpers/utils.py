"""
Utility helpers for CLI argument parsing, caching, and small helpers.
"""

import argparse
import os
import json
from pathlib import Path
from typing import Tuple, Optional, Dict, Any

CACHE_DIR = Path.home() / ".weather_cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)
CACHE_FILE = CACHE_DIR / "last.json"

def parse_args(argv=None) -> argparse.Namespace:
    p = argparse.ArgumentParser(prog="weather", description="Console Weather Report")
    p.add_argument("city", nargs="?", help="City name (e.g. London)")
    p.add_argument("-k", "--api-key", dest="api_key", help="OpenWeatherMap API key (optional)")
    p.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    p.add_argument("--use-cache", action="store_true", help="Use cached last result if available")
    return p.parse_args(argv)

def save_cache(data: Dict[str, Any]) -> None:
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_cache() -> Optional[Dict[str, Any]]:
    if not CACHE_FILE.exists():
        return None
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

def get_api_key_from_env() -> Optional[str]:
    return os.environ.get("OPENWEATHER_API_KEY")
