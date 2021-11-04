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
    slowo_do_zaszyfrowania = input("Podaj slowo_do_zaszyfrowania ").lower()
    index_slowa = [znaki_alfabetu.index(t)
                   for t in slowo_do_zaszyfrowania if t != ' ']
    slowo_zaszyfrowane = [znaki_alfabetu_przesuniete[t] for t in index_slowa]
    print("".join(slowo_zaszyfrowane).title())


def odszyfrowanie():
    slowo_do_odszyfrowania = input("Podaj slowo do odszyfrowania").lower()
    index_slowa_do_odszyfrowania = [znaki_alfabetu_przesuniete.index(
        t) for t in slowo_do_odszyfrowania if t != ' ']
    slowo_odszyfrowane = [znaki_alfabetu[t]
                          for t in index_slowa_do_odszyfrowania]
    print("".join(slowo_odszyfrowane).title())


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
