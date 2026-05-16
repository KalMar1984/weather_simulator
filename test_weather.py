# test_weather.py

import unittest

from weather_models import (
    TemperatureData,
    HumidityData,
    WindSpeedData
)

from data_loader import DataLoader


# -----------------------------------
# TESTA KLASE
# -----------------------------------

class TestWeatherProgram(unittest.TestCase):


    # -----------------------------------
    # TESTS 1
    # OBJEKTA IZVEIDE
    # -----------------------------------

    def test_object_creation(self):

        temp = TemperatureData(
            "Riga",
            [1, 2, 3],
            [4, 5, 7]
        )

        self.assertEqual(temp.city, "Riga")

        self.assertEqual(temp.days, [1, 2, 3])

        self.assertEqual(temp.values, [4, 5, 7])


    # -----------------------------------
    # TESTS 2
    # CSV NOLASĪŠANA
    # -----------------------------------

    def test_csv_loading(self):

        loader = DataLoader("weather_data.csv")

        data = loader.load_data()

        self.assertTrue(len(data) > 0)


    # -----------------------------------
    # TESTS 3
    # FILTRĒŠANA PĒC PILSĒTAS
    # -----------------------------------

    def test_city_filter(self):

        loader = DataLoader("weather_data.csv")

        data = loader.load_data()

        riga_data = []

        for row in data:

            if row["city"] == "Riga":

                riga_data.append(row)

        self.assertEqual(len(riga_data), 8)


    # -----------------------------------
    # TESTS 4
    # VIDĒJĀS VĒRTĪBAS APRĒĶINS
    # -----------------------------------

    def test_average_calculation(self):

        temp = TemperatureData(
            "Riga",
            [1, 2, 3],
            [4, 5, 7]
        )

        average = temp.calculate_average()

        self.assertEqual(average, 5.333333333333333)


    # -----------------------------------
    # TESTS 5
    # TUKŠS DATU SARAKSTS
    # -----------------------------------

    def test_empty_values(self):

        temp = TemperatureData(
            "Riga",
            [],
            []
        )

        with self.assertRaises(ZeroDivisionError):

            temp.calculate_average()


    # -----------------------------------
    # TESTS 6
    # NEEKSISTĒJOŠA PILSĒTA
    # -----------------------------------

    def test_invalid_city(self):

        loader = DataLoader("weather_data.csv")

        data = loader.load_data()

        fake_city = []

        for row in data:

            if row["city"] == "Paris":

                fake_city.append(row)

        self.assertEqual(len(fake_city), 0)


# -----------------------------------
# TESTU PALAIŠANA
# -----------------------------------

if __name__ == "__main__":

    unittest.main()