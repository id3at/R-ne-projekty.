"""
Autor Tomasz Głuc
Program który wyszukuje w zagniezdzonych listach listy,
te obiekty,  które występują tylko raz w liscie.
I zwraca wynik
"""


lista = [[1, 123, 3, 4, 5, "kot", 4, 7, 7], [1, 4, 5], [1, 2, 3, 4, 5], [6, 7, 89, 0, 5, 43]]


def unikat(lista):
    zbior = set([t for i in lista for t in i])
    lista2 = [list(set(t)) for t in lista]
    warlist = []
    for e, z in enumerate(zbior):
        warlist = []
        for x in lista2:
            if z in x:
                warlist.append(z)
        if len(warlist) > 1:
            for k, j in enumerate(lista2):
                if z in j:
                    lista2[k].remove(z)
    lista3 = [t for i in lista2 if len(i) > 0 for t in i]
    return lista3

print(unikat(lista))
