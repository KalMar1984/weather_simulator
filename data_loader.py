import csv #importe csv moduli


class DataLoader: #klase DataLoader, kas ir atbildīga par datu ielādi no CSV faila. Šī klase satur divas metodes: __init__, kas inicializē objektu ar norādīto faila nosaukumu, un load_data, kas ielādē datus no CSV faila un atgriež tos kā sarakstu.

    def __init__(self, filename): #metode __init__ tiek izsaukts, kad tiek izveidots objekts no klases DataLoader.
        self.filename = filename


    def load_data(self): #metode load_data ir atbildīga par datu ielādi no CSV faila. Šī metode atver norādīto failu, izmantojot csv.DictReader, lai nolasītu datus kā vārdnīcas (dictionary) formātā. Katrs rinda CSV failā tiek pārveidota par vārdnīcu, kur atslēgas ir kolonu nosaukumi un vērtības ir attiecīgās šūnas vērtības. Visi rindiņas tiek saglabātas sarakstā data, kas tiek atgriezts pēc tam, kad visi dati ir nolasīti.

        data = [] #izveido tukšu sarakstu data, kurā tiks saglabāti nolasītie dati no CSV faila.

        with open(self.filename, "r") as file: #atver norādīto failu (self.filename) lasīšanas režīmā ("r") un piešķir to mainīgajam file. Šī konstrukcija nodrošina, ka fails tiks pareizi aizvērts pēc tam, kad darbs ar to ir pabeigts, pat ja rodas kļūdas.

            reader = csv.DictReader(file) #izveido csv.DictReader objektu, kas ļauj nolasīt CSV failu kā vārdnīcas (dictionary) formātā. Katrs rinda CSV failā tiks pārveidota par vārdnīcu, kur atslēgas ir kolonu nosaukumi un vērtības ir attiecīgās šūnas vērtības.

            for row in reader: #iterē cauri katrai rindiņai (row) CSV failā, izmantojot for ciklu. Katrs row ir vārdnīca, kas satur datus no attiecīgās rindiņas CSV failā.

                data.append(row) #pievieno katru rindiņu (row) sarakstam data, izmantojot append metodi. Tādējādi visi dati no CSV faila tiek saglabāti sarakstā data kā vārdnīcas.

        return data #atgriež sarakstu data, kas satur visus nolasītos datus no CSV faila kā vārdnīcas.