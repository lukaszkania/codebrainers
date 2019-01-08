
def pierwsze(n):
    """Returns true if n is prime
    >>>pierwsze(-1)
    False
    >>>pierwsze(0)
    False
    >>>pierwsze(3)
    True
    >>>pierwsze(4)
    False
    >>>pierwsze(5)
    True
    """
    if n < 2:
        return False

    for liczba in range(2, n):
        if n%liczba == 0:
            return False
    return True

def primes(n):
    prim = []
    for i in range(n):
        if pierwsze(i):
            prim.append(i)
    return prim

if __name__ == "__main__":
    import doctest
    doctest.testmod()

pierwsze(8)