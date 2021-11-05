import string

logo = """                                                                         mm              mm                          
  mm@***@m@                                                   mm@***@m@  @@             @@@                          
m@@*     *@                                                 m@@*     *@                  @@                          
@@*       * m@*@@m    mm@*@@  m@@*@@@ m@*@@m  *@@@m@@@      @@*       **@@@  *@@@@@@@@m  @@@@@@@m    mm@*@@ *@@@m@@@ 
@@         @@   @@   m@*   @@ @@   **@@   @@    @@* **      @@           @@    @@   *@@  @@    @@   m@*   @@  @@* ** 
@!m         m@@@!@   !@****** *@@@@@m m@@@!@    @!          @!m          !@    !@    @@  @@    @!   !@******  @!     
*!@m     m*@!   !@   !@m    m      @@@!   !@    @!          *!@m     m*  !@    !@    !@  @!    @!   !@m    m  @!     
!!!         !!!!:!   !!****** *!   @! !!!!:!    !!          !!!          !!    !@!   !!  !!    !!   !!******  !!     
:!!:     !*!!   :!   :!!      !!   !!!!   :!    !:          :!!:     !*  !!    !@   !!!  !:    !:   :!!       !:     
  : : : :! :!: : !:   : : ::  : :!:  :!: : !: : :::           : : : :! : : :   :!: : :  : :   : : :  : : :: : :::    
                                                                               ::                                    
                                                                             : : ::                                  
"""
opis = """In cryptography, a Caesar cipher, also known as Caesar's cipher, 
the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. 
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number 
of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B,
and so on. The method is named after Julius Caesar, who used it in his private correspondence."""
print(logo, opis, "\n")

decyzja_uzytkownika = input(
    "Jesli chcesz szyfrować to wcisni 's', jeśli odszyfrować wcisni 'o'. Zakonczyć wcisni 'q'")


def szyfrowanie():
    slowa_do_zaszyfrowania = input("Podaj tekst do zaszyfrowania ").lower().split(' ')
    index_slow = []
    for slowo in slowa_do_zaszyfrowania:
        for litera in slowo:
            if litera in symbole or litera in liczby:
                index_slow.append(litera)
            else:
                index_slow.append(znaki_alfabetu.index(litera))
        index_slow.append(' ')
            
    slowa_zaszyfrowane = []

    for index in index_slow:
        if type(index) == type(1):
            slowa_zaszyfrowane.append(znaki_alfabetu_przesuniete[index])
        elif index == ' ':
            slowa_zaszyfrowane.append(str(index))
        elif str(index) in symbole:
            slowa_zaszyfrowane.append(str(index))
        elif str(index) in liczby:
            slowa_zaszyfrowane.append(str(index)) 
        
    print("".join(slowa_zaszyfrowane).title())


def odszyfrowanie():
    slowa_do_odszyfrowania = input("Podaj tekst do odszyfrowania").lower().split(' ')
    index_slow_do_odszyfrowania = []
    for slowo in slowa_do_odszyfrowania:
        for litera in slowo:
            if litera in symbole or litera in liczby:
                index_slow_do_odszyfrowania.append(litera)
            else:
                index_slow_do_odszyfrowania.append(znaki_alfabetu_przesuniete.index(litera))
        index_slow_do_odszyfrowania.append(' ')
    
    slowa_odszyfrowane = []

    for index in index_slow_do_odszyfrowania:
        if type(index) == type(1):
             slowa_odszyfrowane.append(znaki_alfabetu[index])
        elif index == ' ':
            slowa_odszyfrowane.append(str(index))
        elif str(index) in symbole:
            slowa_odszyfrowane.append(str(index))
        elif str(index) in liczby:
            slowa_odszyfrowane.append(str(index))
        
           


    print("".join(slowa_odszyfrowane).title())


while decyzja_uzytkownika not in 'soq':

    decyzja_uzytkownika = input(
        "Szyfrowanie: 's', Deszyfrowanie: 'o'. Koniec: 'q'")


while decyzja_uzytkownika != 'q':

    while True:
        try:
            przesuniecie_alfabetu = int(
                input("Podaj przesunięcie alfabetu: Przesuniecie musi byc liczbą całkowitą:  "))
            break

        except:
            print("Przesuniecie musi byc liczbą całkowitą.")
    liczby = string.digits
    symbole = string.punctuation
    znaki_alfabetu = list(string.ascii_lowercase)
    znaki_alfabetu_przesuniete = znaki_alfabetu[przesuniecie_alfabetu:] + \
        znaki_alfabetu[:przesuniecie_alfabetu]

    if decyzja_uzytkownika == 's':
        szyfrowanie()
    elif decyzja_uzytkownika == 'o':
        odszyfrowanie()

    decyzja_uzytkownika = input(
        "Jesli chcesz szyfrować to wcisni 's', jeśli odszyfrować wcisni 'o'. Zakonczyć wcisni 'q'")

else:
    print("Koniec")
