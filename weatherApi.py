from __future__ import print_function
import os
import json
import time
import weatherapi
from weatherapi.rest import ApiException
from pprint import pprint
from datetime import datetime, timedelta

# Configure API key authorization: ApiKeyAuth
configuration = weatherapi.Configuration()
configuration.api_key['key'] = '13b1b024b2794e31a07102925253003' #
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = weatherapi.APIsApi(weatherapi.ApiClient(configuration))
q = 'Budapest' # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more.
tomorrow = str(datetime.now() + timedelta(1)) #
dt = tomorrow[:10] # date | Date on or after 1st Jan, 2015 in YYYY-MM-DD format
days = 4 #
if not os.path.exists(f"api_response{dt}.json"): #
    try:
        # Forecast API
        api_response = api_instance.forecast_weather(q, days) #
        with open(f"api_response{dt}.json",'w', encoding='utf-8') as f: #
            json.dump(api_response,f, ensure_ascii=False, indent=4) #

        pprint(api_response) #
    except ApiException as e: #
        print("Exception when calling APIsApi->forecast_weather: %s\n" % e) #