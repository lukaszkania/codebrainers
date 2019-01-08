#!/usr/bin/env python

from sys import argv

# Opening the file, that was inputed with the script.
try:
    file_name = str(argv[1])
except IndexError:
    print("To few arguments.")
except NameError:
    print("Be sure You inputed the correct name of file and the file exist")


with open(file_name) as text_file:
    lines = len(text_file.readlines()) # Calculating number of lines.
    text_file.seek(0)
    words = len(text_file.read().replace("\n","").split()) # Calculating number of words.
    text_file.seek(0)
    chars = len(text_file.read().replace("\n","").replace(".","").replace(",","").replace(" ","")) # Calculating number of characters.
    text_file.seek(0)
    # Counting the average length of the word.
    avg_words = round(chars / words)
    # Counting number of sentence.
    sentence = 0 # Iterator whitch will count number of ".".
    for line in text_file.read(): 
        if "." in line:
            sentence += 1
    # Counting the average length of the sentence.
    avg_sent = round(words / sentence)
    
    print(""" Number of lines: {}. \n Number of words: {}. \n Number of characters: {}.\n Rounded average length of the words: {}. \n Rounded average length of the sentences: {}.\n""".format(lines, words, chars,avg_words,avg_sent))


