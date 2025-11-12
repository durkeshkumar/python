"""
Entry point for the weather CLI.
Run with: python -m weather.cli   (from parent folder)
"""

from . import api as api_mod               # alias import
from .formatter import format_weather_short as fmt_short, format_weather_verbose as fmt_verbose
from .helpers.utils import parse_args, get_api_key_from_env, save_cache, load_cache

def main(argv=None):
    args = parse_args(argv)

    # determine city
    if not args.city:
        # try previous cached city first
        if args.use_cache:
            cached = load_cache()
            if cached and cached.get("city"):
                city = cached["city"]
            else:
                city = input("Enter city: ").strip()
        else:
            city = input("Enter city: ").strip()
    else:
        city = args.city

    # api key: CLI arg -> env var -> None (mock)
    api_key = args.api_key or get_api_key_from_env()

    # fetch weather
    try:
        data = api_mod.fetch_weather(city, api_key=api_key)
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return

    # save cache for convenience
    try:
        save_cache(data)
    except Exception:
        pass

    # print according to verbosity
    if args.verbose:
        print(fmt_verbose(data))
    else:
        print(fmt_short(data))

if __name__ == "__main__":
    main()
