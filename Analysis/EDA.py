import pandas as pd
import numpy as np
import json

# df = pd.read_json("../Data/api_response2025-04-17.json")  the json file is not flat


with open("../Data/api_response2025-04-17.json", "r") as f:
    data = json.load(f)

all_hours = []
for day in data["forecast"]["forecastday"]:
    for hour in day["hour"]:
        # Optionally, add the date for easier filtering later
        hour["date"] = day["date"]
        all_hours.append(hour)


dfx = pd.DataFrame(all_hours)

# Convert date and time to datetime, convert obj to type
dfx["datetime"] = pd.to_datetime(dfx["time"])
dfx = dfx.set_index("datetime").sort_index()
dfx["will_it_rain"] = dfx["will_it_rain"].astype(bool)
dfx["is_day"] = dfx["is_day"].astype(bool)
dfx["wind_dir"] = dfx["wind_dir"].astype(str)

# Drop redundant columns
dfx = dfx.drop(
    columns=[
        "date",
        "time",
        "gust_mph",
        "vis_miles",
        "will_it_snow",
        "dewpoint_f",
        "heatindex_f",
        "windchill_f",
        "feelslike_f",
        "snow_cm",
        "precip_in",
        "pressure_in",
        "wind_mph",
        "temp_f",
        "time_epoch",
    ]
)

# Display the DataFrame
print(dfx.head())

# * EDA
