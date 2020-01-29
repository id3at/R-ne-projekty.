"""
Autor: Tomasz Głuc
System rejestracji i logowania uzytkownika.
Tworzy baze danych logsys.txt uzytkowników.
Zapisując dane w formie {'login': 'haslo'}
"""

import getpass
import ast
statusr = ""
def status():
    """
    Menu stary nowy uzytkownik.
    """
    statusr = input('Jestes zarejestrowanym użytkownikiem? t/n? Wcisnij q by zakończyć')
    if statusr == "t":
        login()
    elif statusr == "n":
        rejestr()
    elif statusr == "q":
        print("Do widzenia. Zapraszamy ponownie")

def rejestr():
    """
    Rejestracja uzytkownikow
    """
    logis = []
    while True:
        logis = []
        loginon = input('Podaj unikatowy login: ')
        with open("logsys.txt", "r") as t:
            p = t.readlines()
        for t in p:
            if t != "\n":
                c = ast.literal_eval(t)
                for f in c.keys():
                    if loginon == f:
                        logis.append(f)
                        print("Taki login istnieje")
        if len(logis) == 0:
            break
    haslo = getpass.getpass('Podaj swoje hasło: ')
    user = {loginon: haslo}
    with open("logsys.txt", "a") as t:
        t.write(f'\n{str(user)}')
    print("Rejestracja powiodła sie")

def login():
    """
    Logowanie uzytkowników
    """
    while True:
        nazwa = {input("Podaj login: "): getpass.getpass("Podaj hasło: ")}
        with open("logsys.txt", "r") as t:
            p = t.readlines()
        has = []
        for t in p:
            if t != "\n":
                c = ast.literal_eval(t)
                if nazwa == c:
                    has.append(c)
        if len(has) == 1:
            print("Prawidłowe logowanie")
            break
        else:
            print("Nieprawidlowe logowanie. Złe hasło lub login")
status()
