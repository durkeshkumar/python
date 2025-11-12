"""
weather.api
Responsible for calling external APIs (OpenWeatherMap).
If api_key is None, returns mocked data for testing.
"""

from typing import Dict, Any, Optional
import time
import os

try:
    import requests
except Exception:
    requests = None

# alias-style exported name for use by other modules
def fetch_weather(city: str, api_key: Optional[str] = None) -> Dict[str, Any]:
    """
    Return a dict with simplified weather info for `city`.
    If api_key is None, return mock data.
    """
    if not api_key:
        return _mock_weather(city)

    if requests is None:
        raise RuntimeError("requests library required for real API calls. Install with: pip install requests")

    # OpenWeatherMap current weather endpoint (example)
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    # simplify the response
    return {
        "city": data.get("name"),
        "temp_c": data["main"]["temp"],
        "feels_like_c": data["main"].get("feels_like"),
        "humidity": data["main"].get("humidity"),
        "weather_main": data["weather"][0]["main"],
        "weather_desc": data["weather"][0]["description"],
        "timestamp": int(time.time())
    }

def _mock_weather(city: str) -> Dict[str, Any]:
    # deterministic mock data so you can test quickly
    city_clean = city.strip().title()
    return {
        "city": city_clean,
        "temp_c": 25.0,
        "feels_like_c": 26.0,
        "humidity": 60,
        "weather_main": "Clear",
        "weather_desc": "clear sky",
        "timestamp": int(time.time())
    }
