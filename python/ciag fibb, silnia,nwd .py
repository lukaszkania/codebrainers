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



