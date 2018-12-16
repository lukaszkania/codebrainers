#!/usr/bin/env python

import random

# Function which the user have to quess the number from  0 - 100.

def zgadywanie():
    print("Zgadnij liczbe z zakresu od 0 - 100")
    liczba = random.randint(0,100) # Drawing the number from the range 0 - 100.
    proby = 6 # Number of avaliable attemps.
    odpowiedz = "" # Variable used to assign answer of the user.
    try:
        while liczba != odpowiedz: # Looping utnill the user quess the number or the number of attemps will be used.
            odpowiedz = int(input("Twoja odpowiedz:")) # Takeing the asner from the user.
            if odpowiedz == liczba:
                print("Udalo Ci sie zgadnac za {} razem! Szukana liczba to: {}.\n".format((str(7 - proby)),(liczba))) # Checking the answer is correct.
                break
            elif proby == 0: # Checking that he number of attemps is still greater than 0.
                print("\nNiestety nie udalo sie. Szukana liczba to {}.".format(liczba))
                break
            else: # Prompting the user the answer is greater or smaller than his input.
                if odpowiedz < liczba:
                    print("Za mało, zostało Ci {} prób.\n".format(proby))
                    proby -= 1
                elif liczba < odpowiedz:
                    print("Za duzo, zostalo Ci {} prob.\n".format(proby))
                    proby -= 1
    except ValueError: # If the user input not number.
        print("Błąd. Upewnij sie, ze podales liczbe.")

# Function which imitates the popular Lotto game.

def totolotek():
    kule_uzytkownika = [] # List where the users types will be stored.
    print("Wybierz 6 kul z zakresu 1-49:")
    try:
        for x in range(1,7): # Asking user to give the number of the ball.
            kula = int(input())
            if kula in kule_uzytkownika: # Checking if the inputed number already was used.
                print("Podales juz ten numer!")
                return 0
            kule_uzytkownika.append(kula)
        wylosowane = [] # List which will contain the random balls.
        while len(wylosowane) < 6: # Checking whether there is six random balls.
            liczba = random.randint(1,50)
            if liczba in wylosowane: # If the licbzba is already in the list we draw again.
                continue
            else:
                wylosowane.append(liczba) # In the other case we append the ball to the list.
        print(wylosowane)
        print(kule_uzytkownika)
        i = 0
        for x in wylosowane: # Compare the result.
            for y in kule_uzytkownika:
                if x == y:
                    i += 1
        print("Udalo Ci sie trafic {} z 6 kul.".format(i)) # Printing the result.
    except ValueError: # If the user input not number.
        print("Błąd. Upewnij sie, ze podales liczbe.")

