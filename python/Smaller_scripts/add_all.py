def add_all(*args):
    return sum(args)

print(add_all(1,2,3,4,5))

def add_all2(*args):
    wynik = 0
    for liczba in args:
        wynik += liczba
    return wynik
