#!/usr/bin/env python
from collections import Counter

# First slower posibility.

#with open("proust.txt","r") as file_txt:
#    dict_with_word = {} # Dict in which we will be counting words.
#    for line in file_txt: # Itering through each line from file_txt.
#        list_with_words = line.split() # Makeing a list with each word from actual line.
#        for word in list_with_words: # Looping through made before list.
#            if word in dict_with_word: 
#                dict_with_word[word] += 1
#            else:
#                dict_with_word[word] = 1


# Second faster posibility.

#with open("proust.txt","r") as file_txt:
#    dictionary_with_words = {} # Dict in which we will be counting words.
#    long_string = file_txt.read().split() # Splitting the file.txt to the list which contains every word.
#    for word in long_string:  # Looping through the every word that is in file.
#        if word in dictionary_with_words:
#            dictionary_with_words[word] += 1
#        else:
#            dictionary_with_words[word] = 1


# Third posibility with removeing ',.!?' signs from each word that contain it.

with open("proust.txt","r") as file_txt:
    dictionary_with_words = {}
    long_string = file_txt.read().split()
    for word in long_string:
        if word.lower().strip(",.!?") in dictionary_with_words:
            dictionary_with_words[word.lower().strip(",.!?")] += 1
        else:
            dictionary_with_words[word.lower().strip(",.!?")] = 1

# Printing 10 most common words using Counter object.    

#try:
    #how_many = int(input("How many common words would You like to print: "))
#except ValueError:
#    print("Input integer!")
#word_counter = Counter(dictionary_with_words) # Making a object that will be opearte on our dict that we made.

#print("{} most common words from file '{}' are:".format(how_many,file_txt.name))
#for word, count in word_counter.most_common(how_many): # Using the most_common method on our dictionary.
#    print(word,":",count)


#  First posibility. !ORDER DICTIONARY!

#most_common = {}
#for key, value in dictionary_with_words.items():
#    if value not in most_common:
#        most_common[value] = [key]
#    else:
#        most_common[value] += [key]
#print(most_common) 


# Second posibility.

with open("proust.txt","r") as file_txt:
    most_common = {}
    for word in dictionary_with_words:
        f = dictionary_with_words[word.lower().strip(",.!?")]
        if not f in most_common:
            most_common[f] = [word.lower().strip(",.!?")]
        else:
            most_common[f].append(word.lower().strip(",.!?"))
print(sorted(most_common.items()))