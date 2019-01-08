#!/usr/bin/env python

import random

def wczytaj_liczby(starsze_liczby):

    liczby = list()

    try:
        wejsciowe = input("Podaj swój typ: ")
        try:
            liczby.append(int(wejsciowe))
        except:
            try:
                lista_wejsciowych = wejsciowe.split(",")
                for liczba in lista_wejsciowych:
                    liczby.append(int(liczba))
            #print("Podaj liczbę całkowitą, skąd błąd {}.".format(err))
            except:
                print("Podaj liczbę całkowitą lub liczby całkowite oddzielone przecinkiem.")
    except:
        pass
    
    for num in liczby:
        if num not in range(1,50):
            print("Liczba poza zakresem!")
        elif num in starsze_liczby:
            print("Liczba {} została wcześniej podana.".format(num))
        else:
            starsze_liczby.add(num)
    return starsze_liczby


def unikalny_lotek():
    typy_uzytkownika = set()
    typy_wylosowane = set()

    print("Program wylosuje 6 liczb z zakresu 1-49.")
    while len(typy_uzytkownika) < 6:
        typy_uzytkownika = wczytaj_liczby(typy_uzytkownika)

    while len(typy_wylosowane) < 6:
        los = random.randint(1,49)
        if los in typy_wylosowane:
            continue
        else:
            typy_wylosowane.add(los)

        i = list()

        for x in typy_uzytkownika:
            if x in typy_wylosowane:
                i.append(x)

    print("Twoje typy: ",typy_uzytkownika)
    print("Wylosowane kule: ",typy_wylosowane)
    print("Udało Ci się trafić {} z 6. Te kule to {}.".format(len(i),i))

unikalny_lotek()