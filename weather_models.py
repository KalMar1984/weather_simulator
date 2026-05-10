#izveidojam bāzes klasi, kas satur informāciju par laika apstākļiem konkrētā pilsētā un konkrētās dienās 
class WeatherData:

    def __init__(self, city, days, values): #city - pilsēta, days - dienas, values - laika apstākļu vērtības Kur _init_ ir speciāla metode - izveido objektu konstruktors, kas tiek izsaukts, kad tiek izveidots objekts no šīs klases. Tas inicializē objektu ar norādītajiem parametriem: city, days un values. self = atsaucas uz konkrēto objektu, kas tiek izveidots, un ļauj piekļūt tā atribūtiem un metodēm. Tātad, kad tiek izveidots objekts no klases WeatherData, šī metode tiks izsaukta, un tā iestatīs objekta city, days un values atribūtus ar norādītajām vērtībām.
        self.city = city
        self.days = days
        self.values = values
        
        #izveidojam metodi, kas apskata laika apstākļu vārtības un aprēķina to vidējo vērtību. Šī metode tiek saukta calculate_average, un tā izmanto sum() funkciju, lai saskaitītu visas vērtības self.values sarakstā, un dalot ar len(self.values), lai iegūtu vidējo vērtību.
    def calculate_average(self):
        return sum(self.values) / len(self.values)