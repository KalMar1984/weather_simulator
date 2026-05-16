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

import pandas as pd


def get_city_forecast_from_meteo(city, data_type):
	"""
	Fetch daily forecast data for a known city from Open-Meteo.

	For this project we support Riga via its latitude/longitude coordinates.
	The function returns a list of day indices and the requested values.
	"""
	city_coordinates = {
		"rīga": (56.946, 24.1059),
		"riga": (56.946, 24.1059),
		"liepāja": (56.5047, 21.0109),
		"liepaja": (56.5047, 21.0109),
		"daugavpils": (55.8833, 26.5333),
	}

	variable_map = {
		"temperature": "temperature_2m_max",
		"humidity": "relative_humidity_2m_mean",
		"wind_speed": "windspeed_10m_max",
	}

	key = city.strip().lower()
	if key not in city_coordinates:
		raise ValueError(f"Meteo.com data unavailable for city '{city}'")

	if data_type not in variable_map:
		raise ValueError(f"Unsupported data type '{data_type}'")

	lat, lon = city_coordinates[key]
	url = "https://api.open-meteo.com/v1/forecast"
	params = {
		"latitude": lat,
		"longitude": lon,
		"daily": [variable_map[data_type]],
		"timezone": "Europe/Riga",
	}

	try:
		import openmeteo_requests
		import requests_cache
		from retry_requests import retry
	except ImportError as exc:
		raise ImportError(
			"To fetch data from meteo.com, install the required packages first: "
			"pip install openmeteo-requests requests-cache retry-requests numpy pandas"
		) from exc

	session = requests_cache.CachedSession('.cache', expire_after=3600)
	retry_session = retry(session, retries=5, backoff_factor=0.2)
	client = openmeteo_requests.Client(session=retry_session)

	responses = client.weather_api(url, params=params)
	response = responses[0]
	jwt_daily = response.Daily()
	values = jwt_daily.Variables(0).ValuesAsNumpy().tolist()
	return list(range(1, len(values) + 1)), values


def main():
	try:
		import openmeteo_requests
		import requests_cache
		from retry_requests import retry
	except ImportError as exc:
		raise ImportError(
			"To run the Open-Meteo example, install the required packages first: "
			"pip install openmeteo-requests requests-cache retry-requests numpy pandas"
		) from exc

	# Setup the Open-Meteo API client with cache and retry on error
	cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
	retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
	openmeteo = openmeteo_requests.Client(session=retry_session)

	# Map the requested cities to their latitude/longitude coordinates.
	# Open-Meteo itself uses coordinates, so we keep the city names locally
	# and show them together with the returned forecast data.
	cities = ["Rīga", "Liepāja", "Daugavpils"]
	latitudes = [56.946, 56.5047, 55.8833]
	longitudes = [24.1059, 21.0109, 26.5333]

	url = "https://api.open-meteo.com/v1/forecast"
	params = {
		"latitude": latitudes,
		"longitude": longitudes,
		"hourly": ["temperature_2m", "relative_humidity_2m", "wind_speed_180m"],
	}

	responses = openmeteo.weather_api(url, params=params)

	# Process each returned location together with its city name.
	for city, response in zip(cities, responses):
		print(f"\nCity: {city}")
		print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
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