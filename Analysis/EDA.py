import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import json
from ydata_profiling import ProfileReport

# simd json for huge 5Gb< files
# Pandoc   a universal document converter

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

# Data Cleaning: it was pretty immaculate because its a weatherAPi which have to provide good quality data,
# I know its now typical in reallife scenarios, but enough for this little proj.
# DataWrangler was used to deal with missing data, set up variable types (especially Date)
# we're mostly working with numerical (continuous, discrete) and two categorical (datetime = 'yyyymmdd hh'; condition)

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

# Checking the whole the DataFrame
dfx.head()
dfx.info()
dfx.describe()  # <–– byfar the best built-in func

# * EDA
# TODO - These are the top EDA libs:  pandas-profiling, SweetViz, lux and HiPlot
# In my opinion they are pretty powerful, for me they work perfectly as a starting-point to decide where to go next,
#  but of course that's what EDA is for!
# resources: https://www.kaggle.com/code/ekami66/detailed-exploratory-data-analysis-with-python/comments ; https://shopify.engineering/conducting-exploratory-data-analysis ;
# https://www.kaggle.com/code/kashnitsky/topic-1-exploratory-data-analysis-with-pandas ; http://www.feat.engineering/index.html

dfx_num = dfx.select_dtypes(include=["float64", "int64"])
dfx_num.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8)

sns.distplot(dfx["humidity"], color="g", bins=100, hist_kws={"alpha": 0.4})

for i in range(0, len(dfx_num.columns), 5):
    sns.pairplot(data=dfx_num, x_vars=dfx_num.columns[i : i + 5], y_vars=["humidity"])

# *pandas-profiling     ; these ones maybe an other time SweetViz, lux and HiPlot
profile = ProfileReport(dfx, title="Biking profile")
profile.to_notebook_iframe()

# Time series
profile_ts = ProfileReport(dfx, tsmode=True)
profile_ts.to_notebook_iframe()
profile_ts.to_file("biking_timeseriesEDA.html")

# Plot temperature over time
dfx["temp_c"].plot(figsize=(15, 5), title="Temperature Over Time")
plt.show()


# Forecasting (Example with Prophet)
from prophet import Prophet

# Prepare data for Prophet (requires 'ds' and 'y' columns)
prophet_df = dfx["temp_c"].reset_index()
prophet_df.columns = ["ds", "y"]

# Fit model
model = Prophet(daily_seasonality=True)
model.fit(prophet_df)

# Forecast next 24 hours
future = model.make_future_dataframe(periods=24, freq="H")
forecast = model.predict(future)
model.plot(forecast)
plt.show()
