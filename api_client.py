"""
Example usage of the Open-Meteo client.

Notes:
- Installation commands are commented out so the file can be imported without
  executing shell commands. Put the following in your README or run them in
  a terminal if you need to install dependencies:

  pip install openmeteo-requests requests-cache retry-requests numpy pandas

This module contains an example `main()` that will only run when the file is
executed as a script (not when imported by tests).
"""

import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry


def main():
	# Setup the Open-Meteo API client with cache and retry on error
	cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
	retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
	openmeteo = openmeteo_requests.Client(session=retry_session)

	# Example request parameters (this example requests multiple coordinates)
	url = "https://api.open-meteo.com/v1/forecast"
	params = {
		"latitude": [56.946, 56.5047, 55.8833],
		"longitude": [24.1059, 21.0109, 26.5333],
		"hourly": ["temperature_2m", "relative_humidity_2m", "wind_speed_180m"],
	}

	responses = openmeteo.weather_api(url, params=params)

	# Process locations in the response
	for response in responses:
		print(f"\nCoordinates: {response.Latitude()}°N {response.Longitude()}°E")
		print(f"Elevation: {response.Elevation()} m asl")
		print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

		# Process hourly data. The order of variables needs to match the request.
		hourly = response.Hourly()
		hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
		hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()
		hourly_wind_speed_180m = hourly.Variables(2).ValuesAsNumpy()

		hourly_data = {
			"date": pd.date_range(
				start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
				end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
				freq=pd.Timedelta(seconds=hourly.Interval()),
				inclusive="left",
			)
		}

		hourly_data["temperature_2m"] = hourly_temperature_2m
		hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
		hourly_data["wind_speed_180m"] = hourly_wind_speed_180m

		hourly_dataframe = pd.DataFrame(data=hourly_data)
		print("\nHourly data\n", hourly_dataframe)


if __name__ == "__main__":
	main()