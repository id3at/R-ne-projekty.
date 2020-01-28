"""
Autor: Tomasz Głuc
System logowania, na bazie obiektów słownika.
Z bazą danych logsys.txt.

"""

import ast
import getpass

nazwa = {input("Podaj login: "): getpass.getpass("Podaj hasło: ")}

with open("logsys.txt", "r") as t:
    p = t.readlines()

has = []
for t in p:
    c = ast.literal_eval(t)
    if nazwa == c:
        has.append(c)

if len(has) == 1:
    print("Prawidłowe logowanie")
else:
    print("Nieprawidlowe logowanie. Złe hasło lub login")
