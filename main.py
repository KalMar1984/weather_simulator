import csv

with open("weather_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

from weather_models import WeatherData

temp = WeatherData("Riga", [1,2,3], [4,5,7])

average = temp.calculate_average()

print(average)    