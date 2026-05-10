import matplotlib.pyplot as plt #importē bibliotēku matplotlib.pyplot, kas tiek izmantota datu vizualizācijai, piemēram, grafiku zīmēšanai. plt ir saīsinājums, kas ļauj vieglāk piekļūt šīs bibliotēkas funkcijām.


class WeatherVisualizer:

    def __init__(self, days, values, title, ylabel): #metode __init__ ir konstruktors, kas tiek izsaukts, kad tiek izveidots objekts no klases WeatherVisualizer. Šī metode inicializē objektu ar norādītajiem parametriem: days (dienas), values (vērtības), title (grafika nosaukums) un ylabel
        self.days = days #saglabā dienas, kas tiks izmantotas grafika x-asi
        self.values = values #saglabā vērtības, kas tiks izmantotas grafika y-asi
        self.title = title #saglabā grafika nosaukumu, kas tiks parādīts grafika augšdaļā
        self.ylabel = ylabel #saglabā y-asi nosaukumu, kas tiks parādīts grafika vertikālajā asī

    def show_graph(self): #metode show_graph ir atbildīga par grafika zīmēšanu, izmantojot matplotlib bibliotēku. Šī metode izmanto saglabātos dienas, vērtības, nosaukumu un y-asi nosaukumu, lai izveidotu un parādītu grafiku.

        plt.plot(self.days, self.values, marker="o") #izveido līnijas grafiku, kur x-asi pārstāv dienas (self.days) un y-asi pārstāv vērtības (self.values). marker="o" nozīmē, ka katrs datu punkts tiks apzīmēts ar apli.

        plt.title(self.title) #iestata grafika nosaukumu, izmantojot self.title, kas tika saglabāts objektā.

        plt.xlabel("Day") #iestata x-asi nosaukumu kā "Day", kas norāda, ka x-asi pārstāv dienas.

        plt.ylabel(self.ylabel) #iestata y-asi nosaukumu, izmantojot self.ylabel, kas tika saglabāts objektā. Tas norāda, ka y-asi pārstāv konkrētas vērtības, piemēram, temperatūru, mitrumu vai vēja ātrumu.

        plt.grid(True) #parāda režģi grafika fonā, kas palīdz labāk saskatīt datu punktus un to attiecības.

        plt.show() #parāda izveidoto grafiku. Šī funkcija atver jaunu logu ar grafiku, kas tika izveidots, un ļauj lietotājam to apskatīt.