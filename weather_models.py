#izveidojam bāzes klasi, kas satur informāciju par laika apstākļiem konkrētā pilsētā un konkrētās dienās 
class WeatherData:

    def __init__(self, city, days, values): #city - pilsēta, days - dienas, values - laika apstākļu vērtības Kur _init_ ir speciāla metode - izveido objektu konstruktors, kas tiek izsaukts, kad tiek izveidots objekts no šīs klases. Tas inicializē objektu ar norādītajiem parametriem: city, days un values. self = atsaucas uz konkrēto objektu, kas tiek izveidots, un ļauj piekļūt tā atribūtiem un metodēm. Tātad, kad tiek izveidots objekts no klases WeatherData, šī metode tiks izsaukta, un tā iestatīs objekta city, days un values atribūtus ar norādītajām vērtībām.
        self.city = city
        self.days = days
        self.values = values

    #izveidojam metodi, kas apskata laika apstākļu vērtības un aprēķina to vidējo vērtību.
    def calculate_average(self):
        return sum(self.values) / len(self.values)

#izveidojam apakšklasi, kas manto no bāzes klases WeatherData un pievieno jaunu metodi, lai parādītu datu tipu.
#Šī klase tiek saukta TemperatureData, un tā satur metodi show_data_type, kas izvada "Temperature data" uz ekrāna.
class TemperatureData(WeatherData):
    def show_data_type(self):
        print("Temperature data")
temp = TemperatureData("Riga", [1,2,3], [4,5,7])

print(temp.calculate_average()) #izsauc calculate_average metodi no bāzes klases WeatherData, lai aprēķinātu vidējo vērtību no self.values saraksta, kas ir [4,5,7]. Rezultāts būs 5.0, jo (4 + 5 + 7) / 3 = 16 / 3 = 5.0.

class HumidityData(WeatherData): 

    def show_data_type(self):
        print("Humidity data")

class WindSpeedData(WeatherData):

    def show_data_type(self):
        print("Wind speed data")