#!/usr/bin/env python

from random import choice

# HANGMAN GAME

# Function which will open file, inputed by the user and return list of words from that file.
def operation_on_file():
    file_name = input("Input Your file name: ")

    try:
        with open(file_name) as file:
            words_list = file.read().split("\n")
            return words_list
    except FileNotFoundError:
        print("Be sure You inputed the correct file name, and file exist.")

# Function which will draw a word from created list of words and return it.
def drawing_word(words_list):
    if isinstance(words_list, list): # Chechking we operate on the list object.
        word = choice(words_list) # Using the choice function from random module, it returns the random element form list.
        return word
    else:
        print("There was a problem in converting file into a list.") # If we do not work on list object.

# Function whcih will return the list of all finded letters indexes in string word.
def indexes_of_letters(word, letter):
    indexes = [] # List where will be storage indexes of letters which are in word.
    ind = 0 # Iterator of while loop.
    while ind < len(word): # Looping through the whole word.
        if letter == word[ind]: # If the letter is in word, we:
            indexes.append(ind) # Appending it to our list.
        ind += 1
    return indexes

# Function which will ask the user for the letter and controls whole game.
def hangman(word):
    display_of_word = "_ " * len(word) # String representing length of our word.
    display_of_word = display_of_word.split(" ")[:-1] # Splitting the string into list.
    set_of_input_letters = set() # Set which will storage the allready inputed letters.
    tries = 6 # Number of actual tries.
    while True: # Looping until the number of tries will be equal to 0.
        print(" ".join(display_of_word))
        letter = input("\nInput letter: ")
        if letter in set_of_input_letters: # Checking if the letter was already inputed before.
            print("You're allready input this letter. Try another one.\n")
            continue
        elif letter not in word: # If letter is not in the word, we take one of the tries.
            tries -= 1
            print("Tries: {}.".format(tries))
            if tries == 0: # If number of tries is already equal to 0, we finish the script work.
                print("\nYou've lost. Drawed word is '{}'.".format(word))
                break
        else: # If letter is in the word.
            indexes = indexes_of_letters(word, letter) # Calling the function that returns all the position of the inputed letter.
            for index in indexes: # Loop through the word and changeing the correct "_" into inputed letters.
                display_of_word[index] = letter
            if "_" not in display_of_word: # Checking if the word is allready queesed and in that case finishing the script work.
                print("\nYou're a winner! The drawed word is '{}'.".format(word))
                break
        set_of_input_letters.add(letter) # Adding to the set inputed word, so we can prevent from inputing by the user the same letter again.

words_list = operation_on_file()
drawed_word = drawing_word(words_list)
hangman(drawed_word)
