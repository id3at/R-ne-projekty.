"""
Autor: Tomasz Głuc
System rejestracji uzytkownika.
Tworzy baze danych logsys.txt uzytkowników.
Zapisując dane w formie {'login': 'haslo'}
"""

import getpass
import ast

logis = []
while True:
    logis = []
    login = input('Podaj swój login: ')
    with open("logsys.txt", "r") as t:
        p = t.readlines()
    for t in p:
        if t != "\n":
            c = ast.literal_eval(t)
            for f in c.keys():
                if login == f:
                    logis.append(f)
                    print("Taki login istnieje")
    if len(logis) == 0:
        break

haslo = getpass.getpass('Podaj swoje hasło: ')
user = {login: haslo}
with open("logsys.txt", "a") as t:
    t.write(f'\n{str(user)}')
