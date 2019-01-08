#!usr/bin/env python

def my_range(stop):
    i = 0
    lista = []
    while i < stop:
        lista.append(i)
        i += 1
    return lista


def my_range2(stop, start = 0,  krok = 1):
    i = 0
    lista = []
    while i < stop:
        lista.append(i)
        i += krok
    return lista


def my_range3(*arg):

    if len(arg) > 3 or len(arg) < 0:
        print("Too many arguments passed to te function my_range3. {} was given, 3 is max.".format(len(arg)))
        return 0

    elif len(arg) < 0:
        print("You should give at least one argument to the function my_range3")
    
    elif len(arg) == 1:
        i = 0
        stop = arg[0]
        lista = []
        while i < stop:
            lista.append(i)
            i += 1
        return lista
    
    elif len(arg) == 2:
        start = arg[0]
        stop = arg[1]
        lista = []
        while start < stop:
            lista.append(start)
            start += 1
        return lista

    else:
        start = arg[0]
        stop = arg[1]
        krok = arg[2]
        lista = []

        while start < stop:
            lista.append(start)
            start += krok
        return lista


def proper_range(*args, **kwargs):

    if len(args) < 0 or len(args) > 3:
        print("Podano złą ilość argumentów.")
        return 0
    
    elif len(args) == 1:
        return my_range(args[0])

    elif len(args) == 2:
        return my_range2(args[1], args[0])

    elif len(args) == 3:
        return my_range2(args[1], args[0], args[2])

    else:
        return my_range2(**kwargs)
    

import pierwsze
print(pierwsze.pierwsze(7))
