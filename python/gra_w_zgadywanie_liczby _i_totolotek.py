#!/usr/bin/env python

import random

def zgadywanie():
    print("Zgadnij liczbe z zakresu od 0 - 100")
    liczba = random.randint(0,100)
    proby = 6
    odpowiedz = ""
    try:
        while liczba != odpowiedz:
            odpowiedz = int(input("Twoja odpowiedz:"))
            if odpowiedz == liczba:
                print("Udalo Ci sie zgadnac za {} razem! Szukana liczba to: {}.\n".format((str(8 - proby)),(liczba)))
            elif proby ==0:
                print("\nNiestety nie udalo sie. Szukana liczba to {}.".format(liczba))
                break
            else:
                if odpowiedz < liczba:
                    print("Za mało, zostało Ci {} prób.\n".format(proby))
                    proby -= 1
                elif liczba < odpowiedz:
                    print("Za duzo, zostalo Ci {} prob.\n".format(proby))
    except:
        print("Błąd. Upewnij sie, ze podales liczbe.")

def totolotek():
    kule_uzytkownika = []
    print("Wybierz 6 kul z zakresu 1-49:")
    try:
        for x in range(1,7):
            kula = int(input())
            if kula in kule_uzytkownika:
                print("Podales juz ten numer!")
                return 0
            kule_uzytkownika.append(kula)
        wylosowane = []
        while len(wylosowane) < 6:
            liczba = random.randint(1,50)
            if liczba in wylosowane:
                continue
            else:
                wylosowane.append(liczba)
        print(wylosowane)
        print(kule_uzytkownika)
        i = 0
        for x in wylosowane:
            for y in kule_uzytkownika:
                if x == y:
                    i += 1
        print("Udalo Ci sie trafic {} z 6 kul.".format(i))
    except:
        print("Błąd. Upewnij sie, ze podales liczbe.")

