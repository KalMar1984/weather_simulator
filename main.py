# -----------------------------------
# IMPORTS
# -----------------------------------

import csv

from weather_models import ( #importējam klases no weather_models.py, kas ir atbildīgas par dažādiem laika apstākļu datiem, piemēram, temperatūras, mitruma un vēja ātruma datiem. Šīs klases satur metodes, kas ļauj aprēķināt vidējo vērtību un parādīt datu tipu.
    TemperatureData,
    HumidityData,
    WindSpeedData
)

from visualizer import WeatherVisualizer #importējam klasi WeatherVisualizer no visualizer.py, kas ir atbildīga par datu vizualizāciju, piemēram, grafiku zīmēšanu. Šī klase satur metodi show_graph, kas ļauj izveidot un parādīt grafiku, izmantojot matplotlib bibliotēku.


# -----------------------------------
# CSV DATU NOLASĪŠANA
# -----------------------------------

from data_loader import DataLoader #izveidojam klasi DataLoader no data_loader.py, kas ir atbildīga par datu ielādi no CSV faila.


loader = DataLoader("weather_data.csv") #izveidojam objektu no klases DataLoader, kas ir atbildīga par datu ielādi no CSV faila.

data = loader.load_data() #izveidojam sarakstu data, kas satur visus nolasītos datus no CSV faila.

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

days = [] #izveido tukšu sarakstu days, kurā tiks saglabātas dienas, kas atbilst lietotāja izvēlētajai pilsētai un datu tipam.
values = [] #izveido tukšu sarakstu values, kurā tiks saglabātas laika apstākļu vērtības, kas atbilst lietotāja izvēlētajai pilsētai un datu tipam.

for row in data: #iterē cauri katrai rindiņai (row) nolasītajos datos no CSV faila, izmantojot for ciklu. Katrs row ir vārdnīca, kas satur datus no attiecīgās rindiņas CSV failā. Šis cikls tiek izmantots, lai filtrētu datus un saglabātu tikai tos, kas atbilst lietotāja izvēlētajai pilsētai (city) un datu tipam (data_type).

    if row["city"] == city: #pārbauda, vai "city" vērtība rindiņā (row) atbilst lietotāja izvēlētajai pilsētai (city). Ja tā ir vienāda, tad tiek izpildīts iekšējais kods, kas pievieno attiecīgās dienas un vērtības sarakstiem days un values.

        days.append(int(row["day"])) #pievieno "day" vērtību no rindiņas (row) sarakstam days, izmantojot append metodi. Šī vērtība tiek pārveidota par veselu skaitli (int), jo CSV failā tā var būt saglabāta kā teksts.

        values.append(int(row[data_type])) #pievieno "data_type" vērtību no rindiņas (row) sarakstam values, izmantojot append metodi.


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

weather_object.show_data_type() #izsauc show_data_type metodi no konkrētās klases (TemperatureData, HumidityData vai WindSpeedData), kas tika izveidota atkarībā no lietotāja izvēles. Šī metode izvada uz ekrāna datu tipu, piemēram, "Temperature data", "Humidity data" vai "Wind speed data". Polimorfisms ļauj izmantot vienu un to pašu metodi (show_data_type) dažādās klasēs, un katra klase var sniegt savu specifisko implementāciju šai metodei.


# -----------------------------------
# VIDĒJĀ VĒRTĪBA
# -----------------------------------

average = weather_object.calculate_average() #izsauc calculate_average metodi no bāzes klases WeatherData, lai aprēķinātu vidējo vērtību no self.values saraksta, kas tika saglabāts objektā. Šī metode pārbauda, vai self.values saraksts nav tukšs, un, ja tas ir tukšs, izvada kļūdas ziņojumu un atgriež 0. Ja saraksts nav tukšs, tā aprēķina vidējo vērtību, summējot visus elementus sarakstā un dalot ar elementu skaitu, un atgriež šo vidējo vērtību.

print(f"Average value: {average}")


# -----------------------------------
# GRAFIKA IZVEIDE
# -----------------------------------

graph = WeatherVisualizer( #izveido objektu no klases WeatherVisualizer, kas ir atbildīga par datu vizualizāciju, piemēram, grafiku zīmēšanu. Šī klase satur metodi show_graph, kas ļauj izveidot un parādīt grafiku, izmantojot matplotlib bibliotēku. Šajā gadījumā tiek nodoti parametri: city (pilsēta), data_type (datu tips), days (dienas) un values (vērtības), lai izveidotu grafiku ar atbilstošu nosaukumu un y-asi nosaukumu.
    days,
    values,
    f"{city} {data_type}",
    data_type
)

graph.show_graph()