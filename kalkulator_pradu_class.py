import datetime


class KalkulatorPradu():

    def __init__(self, cena_kwh=0.74, data_od=(2022, 4, 12), data_do=(2022, 5, 7), licznik_od=5788, licznik_do=5981.2,):
        """Funkcja inicjalizująca :D

        Args:
            cena_kwh (float, optional): Cena kilowatogodziny.. Defaults to 0.74.
            data_od (tuple, optional): Data od ktorej liczymy czas pobierania. Defaults to (2022, 4, 12).
            data_do (tuple, optional): Data do ktorej liczymy czas pobierania. Defaults to (2022, 5, 7).
            licznik_od (int, optional): Odczyt licznika z daty od ktorej zaczynamy liczyc. Defaults to 5788.
            licznik_do (float, optional): Odczyt licznika z daty do ktorej zaczynamy liczyc. Defaults to 5981.2.
        """
        
        self.cena_kwh = cena_kwh
        self.data_od = data_od
        self.data_do = data_do
        self.licznik_od = licznik_od
        self.licznik_do = licznik_do

    def czas_uzytkowania(self):
        czas = datetime.datetime(*self.data_do) - datetime.datetime(*self.data_od)
        return czas.days

    def zuzycie_kwh(self):
        return self.licznik_do - self.licznik_od

    def koszt_kwh(self):
        return self.cena_kwh * self.zuzycie_kwh()
    
    def inforamcje(self):
        print(f'''Przez {self.czas_uzytkowania()} dni zuzyto {self.zuzycie_kwh():.1f} kwh.
Koszt wynosi {self.koszt_kwh():.2f}zł przy cenie {self.cena_kwh} gr.
Średnia zuzycia przez jeden dzień wynosi {self.zuzycie_kwh() / self.czas_uzytkowania():.2f}kwh
Koszt jednego dnia jest równy: {self.zuzycie_kwh() / self.czas_uzytkowania() * self.cena_kwh:.2f}zł przy średniej {self.zuzycie_kwh() /self.czas_uzytkowania():.2f}kwh\n''')


wstepne = KalkulatorPradu()
wstepne.inforamcje()
