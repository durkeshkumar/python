# day12/weather/__init__.py
"""
Weather package initialization
Provides tools to fetch and display weather data.
"""

from .api import fetch_weather
from .formatter import format_weather_short, format_weather_verbose
