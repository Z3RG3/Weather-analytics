import os
import json
import time
import argparse
import weatherapi
from weatherapi.rest import ApiException
from pprint import pprint
from datetime import datetime, timedelta
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Configuration ---
# It's better to load the API key from an environment variable or a config file
# For environment variable: Set WEATHERAPI_KEY='your_key' in your environment
# For demonstration, we'll try environment variable first, then fallback to hardcoded (not recommended for production)
API_KEY = os.getenv('WEATHERAPI_KEY', '13b1b024b2794e31a07102925253003') # Replace fallback with None or raise error in production

def configure_api(api_key: str) -> weatherapi.Configuration:
    """Configures the WeatherAPI client."""
    if not api_key:
        raise ValueError("API key not found. Set the WEATHERAPI_KEY environment variable.")
    configuration = weatherapi.Configuration()
    configuration.api_key['key'] = api_key
    return configuration

def fetch_forecast(api_instance: weatherapi.APIsApi, query: str, days: int, dt: str | None = None) -> dict | None:
    """Fetches forecast data from the WeatherAPI."""
    try:
        logging.info(f"Fetching forecast for '{query}', days: {days}, start_date: {dt if dt else 'today'}")
        # Forecast API call - pass dt only if specified
        if dt:
             api_response = api_instance.forecast_weather(query, days, dt=dt)
        else:
             # If dt is not specified, the API defaults to the current day + forecast days
             # Adjust 'days' if needed based on API behavior for non-historical requests
             api_response = api_instance.forecast_weather(query, days)

        logging.info(f"Successfully fetched forecast data for '{query}'.")
        return api_response
    except ApiException as e:
        logging.error(f"API Exception when calling forecast_weather for '{query}': {e}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred during API call for '{query}': {e}")
        return None

def save_forecast(data: dict, filename: str) -> bool:
    """Saves the forecast data to a JSON file."""
    try:
        # Use the directory of the script as the base path
        script_dir = os.path.dirname(__file__)
        filepath = os.path.join(script_dir, filename)

        # Ensure the directory exists (though likely '.' or script dir, good practice)
        os.makedirs(os.path.dirname(filepath) or '.', exist_ok=True)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        logging.info(f"Forecast data saved to '{filepath}'")
        return True
    except IOError as e:
        logging.error(f"Failed to write forecast data to '{filename}': {e}")
        return False
    except Exception as e:
        logging.error(f"An unexpected error occurred during saving to '{filename}': {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Fetch weather forecast data using WeatherAPI.")
    parser.add_argument('-q', '--query', type=str, default='Budapest',
                        help="Location query (e.g., city name, postcode, lat/lon). Default: Budapest")
    parser.add_argument('-d', '--days', type=int, default=4, choices=range(1, 15), # Check API limits
                        help="Number of forecast days (1-14). Default: 4")
    parser.add_argument('--date', type=str, default=None,
                        help="Start date for the forecast in YYYY-MM-DD format. Default: Current day.")
    parser.add_argument('-o', '--output', type=str, default=None,
                        help="Output filename. Default: forecast_{query}_{start_date}.json")
    parser.add_argument('--force', action='store_true',
                        help="Force fetch even if a recent file exists.") # Simple force flag

    args = parser.parse_args()

    # Determine the start date for filename generation (even if API uses current day)
    start_date_str = args.date if args.date else datetime.now().strftime('%Y-%m-%d')

    # Determine output filename
    if args.output:
        filename = args.output
    else:
        # Sanitize query for filename (replace spaces, etc.)
        safe_query = "".join(c if c.isalnum() else "_" for c in args.query)
        filename = f"forecast_{safe_query}_{start_date_str}.json"

    # Check if file exists and if force flag is not set
    script_dir = os.path.dirname(__file__)
    filepath = os.path.join(script_dir, filename)

    # --- Simple check: Only fetch if file doesn't exist or --force is used ---
    # More robust check could involve checking file modification time
    if not args.force and os.path.exists(filepath):
        logging.info(f"Forecast file '{filepath}' already exists. Use --force to overwrite.")
        # Optionally load and return existing data here if needed downstream
        # with open(filepath, 'r', encoding='utf-8') as f:
        #     existing_data = json.load(f)
        # pprint(existing_data) # Example: print existing if not fetching
        return # Exit script

    # --- Proceed with fetching ---
    configuration = configure_api(API_KEY)
    api_client = weatherapi.ApiClient(configuration)
    api_instance = weatherapi.APIsApi(api_client)

    forecast_data = fetch_forecast(api_instance, args.query, args.days, args.date)

    if forecast_data:
        # Use pprint for structured output *if* desired after fetching
        # pprint(forecast_data)
        save_forecast(forecast_data, filename)
    else:
        logging.warning("No forecast data was fetched or saved.")

if __name__ == "__main__":
    main()