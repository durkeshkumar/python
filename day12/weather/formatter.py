"""
weather.formatter
Formatting helpers to make CLI output nice.
"""

from datetime import datetime
from typing import Dict

def format_weather_short(data: Dict) -> str:
    city = data.get("city", "Unknown")
    t = data.get("temp_c")
    w = data.get("weather_desc", "")
    return f"{city}: {t}°C — {w}"

def format_weather_verbose(data: Dict) -> str:
    city = data.get("city", "Unknown")
    t = data.get("temp_c")
    feels = data.get("feels_like_c")
    hum = data.get("humidity")
    main = data.get("weather_main", "")
    desc = data.get("weather_desc", "")
    ts = data.get("timestamp")
    time_str = datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S") if ts else "N/A"

    return (
        f"Weather for {city} at {time_str}\n"
        f"  Condition : {main} — {desc}\n"
        f"  Temperature: {t}°C (feels like {feels}°C)\n"
        f"  Humidity   : {hum}%\n"
    )
