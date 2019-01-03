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
    

