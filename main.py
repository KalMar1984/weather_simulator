# -----------------------------------
# IMPORTS
# -----------------------------------

import requests # Importējam requests bibliotēku, lai veiktu HTTP pieprasījumus uz API

from weather_models import ( #importējam klases no weather_models.py, kas ir atbildīgas par dažādiem laika apstākļu datiem, piemēram, temperatūras, mitruma un vēja ātruma datiem. Šīs klases satur metodes, kas ļauj aprēķināt vidējo vērtību un parādīt datu tipu.
    TemperatureData,
    HumidityData,
    WindSpeedData
)

from visualizer import WeatherVisualizer #importējam klasi WeatherVisualizer no visualizer.py, kas ir atbildīga par datu vizualizāciju, piemēram, grafiku zīmēšanu. Šī klase satur metodi show_graph, kas ļauj izveidot un parādīt grafiku, izmantojot matplotlib bibliotēku.


# -----------------------------------
# DATU AVOTA IZVĒLE
# -----------------------------------

from data_loader import DataLoader #izveidojam klasi DataLoader no data_loader.py, kas ir atbildīga par datu ielādi no CSV faila.
from api_client import get_city_forecast_from_meteo


def is_api_city(city):
    """Return True for cities that should be fetched from the Open-Meteo API."""
    return city.strip().lower() in ("rīga", "riga", "liepāja", "liepaja", "daugavpils")


def load_local_city_data(city, data_type):
    """Load city data from the local CSV file and return days and values."""
    loader = DataLoader("weather_data.csv")
    rows = loader.load_data()
    days = []
    values = []
    normalized_city = city.strip().lower()

    for row in rows:
        if row["city"].strip().lower() == normalized_city:
            days.append(int(row["day"]))
            values.append(int(row[data_type]))

    return days, values


def load_city_data(city, data_type):
    """Select the source for city data: API for some cities, CSV for the rest."""
    if is_api_city(city):
        return get_city_forecast_from_meteo(city, data_type)
    return load_local_city_data(city, data_type)


# -----------------------------------
# LIETOTĀJA IZVĒLE
# -----------------------------------

city = input("Choose city (Rīga / Liepāja / Daugavpils / Oslo / Rome): ") 

data_type = input(
    "Choose data type (temperature / humidity / wind_speed): " 
)

# -----------------------------------
# DATU IEGUVE
# -----------------------------------

days, values = load_city_data(city, data_type)

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


# -----------------------------------
# VALSTS DATU IEGUVE (restcountries.com)
# -----------------------------------

def show_latvia_info():
    """Iegūst datus par Latviju no restcountries.com API un tos izdrukā."""
    try:
        # Veicam GET pieprasījumu uz restcountries.com API, lai iegūtu datus par Latviju
        response = requests.get("https://restcountries.com/v3.1/name/latvia")
        # Pārbaudām, vai HTTP pieprasījums bija veiksmīgs (statusa kods 200)
        response.raise_for_status() 
        
        # API atgriež sarakstu, tāpēc mēs paņemam pirmo elementu ar indeksu [0]
        data = response.json()[0]
        
        # Izvelkam nepieciešamos datus no saņemtā JSON objekta
        name = data.get("name", {}).get("common", "Nezināms")
        capital = data.get("capital", ["Nezināms"])[0]
        region = data.get("region", "Nezināms")
        population = data.get("population", "Nezināms")
        
        # Izdrukājam iegūto informāciju konsolē
        print("\n--- Informācija par Latviju ---")
        print(f"Valsts nosaukums: {name}")
        print(f"Galvaspilsēta: {capital}")
        print(f"Reģions: {region}")
        print(f"Iedzīvotāju skaits: {population}")
        print("-------------------------------\n")
        
    except requests.exceptions.RequestException as e:
        # Ja notiek kļūda savienojumā vai pieprasījumā, tiek izvadīts šis paziņojums
        print(f"\nKļūda iegūstot valsts datus: {e}\n")

# Izsaucam funkciju, lai parādītu iegūtos datus par Latviju
show_latvia_info()