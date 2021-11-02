import random
wisielec = "wisielec"

wisielecGry = ["_","_","_","_","_","_","_","_",]
indexwisielca = 0

listaSlow = ['dobro', 'markiz', 'słowa', 'zbrodnia', 'radość']

losoweSlowo = random.choice(listaSlow)
zakryteLosSlo = ["_" for t in losoweSlowo]
print(zakryteLosSlo)

while losoweSlowo != "".join(zakryteLosSlo):
    literaUsera = input("Podaj literę: ")
    if literaUsera in losoweSlowo:
        for index,litera in enumerate(losoweSlowo):
           if literaUsera == litera:
                zakryteLosSlo[index] = litera    
        print(zakryteLosSlo)
        if losoweSlowo == "".join(zakryteLosSlo):
            print("Wygrałeś")
    else:
        wisielecGry[indexwisielca] = wisielec[indexwisielca]
        indexwisielca += 1
        print("".join(wisielecGry))
        if wisielec == ''.join(wisielecGry):
            print('Przegrałeś')
            break
