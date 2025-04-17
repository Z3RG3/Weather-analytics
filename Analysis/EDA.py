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

# Convert date and time to datetime
dfx["datetime"] = pd.to_datetime(dfx["date"] + " " + dfx["time"])
dfx = dfx.set_index("datetime").sort_index()

# Drop redundant columns
dfx = dfx.drop(columns=["date", "time"])

# Display the DataFrame
print(dfx.head())
