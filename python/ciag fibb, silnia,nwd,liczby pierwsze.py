#!/usr/bin/env python

# Silnia

def silnia(n):
    if n == 0 or n == 1:
        result = 1
        return 1
    else:
        result = n * silnia(n-1)
        return n * silnia(n-1)
    print("Silnia z {} wynosi: {}".format((n),(result)))
    
# Ciąg Fibbonaciego.

def ciag_fibbonaciego(n):
    if n == 0:
        result = 0
        return 0
    elif n == 1:
        result = 1
        return 1
    else:
        result = ciag_fibbonaciego(n-2) + ciag_fibbonaciego(n-1)
        return ciag_fibbonaciego(n-2) + ciag_fibbonaciego(n-1)
    print("Ciag Fibbonaciego dla {} wyrazu wynosi: {}".format((n),(result)))

# Największy wspólny dzielnik.

def nwd(x,y):
    while x%y != 0:
        x,y = y,x%y
    print("Największy wspolny dzielnik liczb wynosi {}.".format(y))
    return y

# Wyszukiwanie liczb pierwszych z podanego zakresu n.

def pierwsze(n):
    if n < 3:
        return "Brak liczb pierwszych w podanym zakresie."
    liczby = [x for x in range(3,n+1)] # Tablica przechowywujaca liczby ktore nalezy zbadac.
    liczby_pierwsze = [] # Tablica przechowywujaca liczby pierwsze.
    for i in liczby: # Sprawdzanie wszystkich liczb z podanego zakresu.
        tab_z_dzielnikami = [] # Tablica przechowywujaca dzielniki.
        for x in range(3,i+1): # Pętla w której liczby z tablicy dzielimy po kolei przez kolejne liczby od 3 do niej samej.
            if i%x == 0:
                tab_z_dzielnikami.append(x)
            else:
                continue
        if len(tab_z_dzielnikami) == 1: # Jesli liczba miala dokladnie 2 dzielniki to jest pierwsza.
            liczby_pierwsze.append(tab_z_dzielnikami[0])
            tab_z_dzielnikami = []  # Przypisujemy pusta tablice w celu nastepnego sprawdzenia anstepnej liczby.
    return "Liczby pierwsze z zakresu 2 - {} to: {}.".format((n),(liczby_pierwsze))



