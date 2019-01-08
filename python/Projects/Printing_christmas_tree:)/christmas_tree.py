#!/usr/bin/env python

# Zadania

## Program "choinka"

# Z uwagi na otaczającą świąteczną atmosferę, proszę napisać program, który narysuje na ekranie choinkę:


def choinka(branches):
    stars = 1
    for i in range(0,branches):
        print(' ' * branches + '*' * stars)
        stars += 2
        branches -= 1
    
def choinka2():
    for i in range(50):
        for j in range(-50,50):
            if i > abs(j):
                print("*",end="")
            else:
                print(" ",end="")
        print()

choinka(50)
choinka2()
