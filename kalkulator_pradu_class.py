import datetime


class KalkulatorKosztowUslug():

    def __init__(self, cena_uslugi=0.74, data_od=(2022, 4, 12), data_do=(2022, 5, 8), 
                 licznik_od=5788, licznik_do=5992.2, jednostka='kwh'):
        
        
        """Funkcja inicjalizująca :D

        Args:
            cena_uslugi (float, optional): Cena usługi.. Defaults to 0.74.
            data_od (tuple, optional): Data od ktorej liczymy czas pobierania. Defaults to (2022, 4, 12).
            data_do (tuple, optional): Data do ktorej liczymy czas pobierania. Defaults to (2022, 5, 8).
            licznik_od (int, optional): Odczyt licznika z daty od ktorej zaczynamy liczyc. Defaults to 5788.
            licznik_do (float, optional): Odczyt licznika z daty do ktorej zaczynamy liczyc. Defaults to 5992.2.
        """
        
        self.cena_uslugi = cena_uslugi
        self.data_od = data_od
        self.data_do = data_do
        self.licznik_od = licznik_od
        self.licznik_do = licznik_do
        self.jednostka = jednostka
    
    def __str__(self):
        return f"Helolo. To ja, kalkulator energi"

    def czas_uzytkowania(self):
        czas = datetime.datetime(*self.data_do) - datetime.datetime(*self.data_od)
        return czas.days

    def zuzycie(self):
        return self.licznik_do - self.licznik_od

    def koszt(self):
        return self.cena_uslugi * self.zuzycie()
    
    def inforamcje(self):
        print(f'''Przez {self.czas_uzytkowania()} dni zuzyto {self.zuzycie():.1f} {self.jednostka}.
Koszt wynosi {self.koszt():.2f}zł przy cenie {self.cena_uslugi} gr.
Średnia zuzycia przez jeden dzień wynosi {self.zuzycie() / self.czas_uzytkowania():.2f}{self.jednostka}
Koszt jednego dnia jest równy: {self.zuzycie() / self.czas_uzytkowania() * self.cena_uslugi:.2f}zł przy średniej {self.zuzycie() /self.czas_uzytkowania():.2f}{self.jednostka}\n''')


wstepne = KalkulatorKosztowUslug()
wstepne.inforamcje()
