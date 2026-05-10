# main.py

import csv

from weather_models import (
    TemperatureData,
    HumidityData,
    WindSpeedData
)

from visualizer import WeatherVisualizer


# -----------------------------------
# CSV DATU NOLASĪŠANA
# -----------------------------------

data = []

with open("weather_data.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        data.append(row)


# -----------------------------------
# LIETOTĀJA IZVĒLE
# -----------------------------------

city = input("Choose city (Riga / Oslo / Rome): ")

data_type = input(
    "Choose data type (temperature / humidity / wind_speed): "
)


# -----------------------------------
# DATU FILTRĒŠANA
# -----------------------------------

days = []
values = []

for row in data:

    if row["city"] == city:

        days.append(int(row["day"]))

        values.append(int(row[data_type]))


# -----------------------------------
# OBJEKTU IZVEIDE
# -----------------------------------

if data_type == "temperature":

    weather_object = TemperatureData(
        city,
        days,
        values
    )

elif data_type == "humidity":

    weather_object = HumidityData(
        city,
        days,
        values
    )

else:

    weather_object = WindSpeedData(
        city,
        days,
        values
    )


# -----------------------------------
# POLIMORFISMS
# -----------------------------------

weather_object.show_data_type()


# -----------------------------------
# VIDĒJĀ VĒRTĪBA
# -----------------------------------

average = weather_object.calculate_average()

print(f"Average value: {average}")


# -----------------------------------
# GRAFIKA IZVEIDE
# -----------------------------------

graph = WeatherVisualizer(
    days,
    values,
    f"{city} {data_type}",
    data_type
)

graph.show_graph()