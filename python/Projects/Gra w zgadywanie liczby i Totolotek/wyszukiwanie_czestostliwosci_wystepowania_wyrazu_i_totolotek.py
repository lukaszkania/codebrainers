#!/usr/bin/env python

import glob
import random

# Zadanie 1 - wyszukiwanie w pliku.

def wyszukiwanie_slow(lista): 
    imie = 0 # Iterator dzięki któremu przejdziemy przez wszystkie imiona listy.
    while imie < len(lista): # Pętla przechodząca przez wszystkie wyrazy zawarte w liście.
        with open("/home/dev/Desktop/codebrainers/python/william.sheakespeare","r",) as file1:
            i = 0 # Licznik określający częstotliwość występowania wyrazu w pliku file1.
            for linia in file1: # Pętla przechodząca przez każdą linie pliku.
                lista_z_wyrazami = linia.split() # Zapisanie linii w postaci pojedynczych wyrazów zawartych w liście.
                for wyraz in lista_z_wyrazami: # Pętla przechodząca przez wyżej opisaną listę.
                    if lista[imie].lower() in wyraz.lower(): # Porównanie wyrazów i ew. liczenie.
                        i += 1
            print("\"{}\" występuje w pliku {} ilosc razy.".format((lista[imie]),(i)))
            imie += 1 # Przejście na kolejny wyraz, który ma zostać wylosowany.

# Zadanie 1a – wyszukiwanie w kilku plikach.

def wyszukiwanie_w_kilku_plikach(lista):
    lista_plikow = glob.glob("/home/dev/Desktop/codebrainers/python/sonety/*.txt") # Zawarcie wszystkich nazw plików w określonej lokacji w liście.
    
    for nazwa_pliku in lista_plikow: # Analogicznie jak w funkcji wyszukiwanie_slow.
        imie = 0
        while imie < len(lista):
            with open(nazwa_pliku,"r") as plik:
                i = 0
                for linia in plik:
                    lista_z_wyrazami = linia.split()
                    for wyraz in lista_z_wyrazami:
                        if lista[imie].lower() in wyraz.lower():
                            i += 1
                print("\"{}\" występuje w pliku o nazwie {}, {} ilosc razy.".format((lista[imie]),(nazwa_pliku[45:]),(i)))
                imie += 1

        print("\n")

# Zadanie 2 - totolotek.

def totolo():
    typy_uzytkownika = set()
    typy_wylosowane = set()

    try:
        while len(typy_uzytkownika) < 6:
            x = int(input("Podaj swój typ: "))
            if x not in range(1,50):
                print("Liczba poza zakresem!")
                continue
            else:
                typy_uzytkownika.add(x)

        while len(typy_wylosowane) < 6:
            typy_wylosowane.add(random.randint(1,50))

        i = list()

        for x in typy_uzytkownika:
            if x in typy_wylosowane:
                i.append(x)
        print("Twoje typy: ",typy_uzytkownika)
        print("Wylosowane kule: ",typy_wylosowane)
        print("Udało Ci się trafić {} z 6. Te kule to {}.".format(len(i),i))

    except ValueError:
        print("Upewnij się, że podajesz liczby!")

# Zadanie 2a – powtarzające się liczby.

def unikalny_lotek():
    typy_uzytkownika = set()
    typy_wylosowane = set()

    while len(typy_uzytkownika) < 6:
        try:
            x = int(input("Podaj swój typ: "))
        except ValueError as err:
            print("Podaj liczbę całkowitą, skąd błąd {}.".format(err))
            continue
        if x in typy_uzytkownika:
            print("Podałeś już tą liczbe!")
        elif x not in range(1,50):
            print("Liczba poza zakresem!")
        else:
            typy_uzytkownika.add(x)

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