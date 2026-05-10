import csv

with open("weather_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

from weather_models import WeatherData

temp = WeatherData("Riga", [1,2,3], [4,5,7])

average = temp.calculate_average()

print(average)    
#testē - polimorfisms, jo 'show_data_type()' uzvedas dažādi dažādos objektos. Ktra mantojošā klase uz šo modeli reaģē atšķirīgi
from weather_models import *

temp = TemperatureData("Riga", [1,2], [4,5])
humid = HumidityData("Riga", [1,2], [80,82])
wind = WindSpeedData("Riga", [1,2], [12,15])

temp.show_data_type()
humid.show_data_type()
wind.show_data_type()