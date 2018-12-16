#!/usr/bin/env python

import glob

# Function which display the result of counting.

def results(word,file_name,count):
    print("Word {} occurs in the file {} {} times.".format((word),(file_name),(count)))
    return count


# Function which counts from file inputed word that are extacly the same.

def count_from_file_extacly_same(file_name): # Calculating the number of files from inputed directory.
    with open(file_name) as file1:
        word = input("What would You like to count: ")
        i = 0   # Variable whitch counts the amount of words.
        for line in file1: # Looping through all lines of file.
            words_split = line.split() # Splitting the line into list.
            for word2 in words_split: # Looping through made before lists which contain words from line.
                if word in word2: # Counting.
                    i += 1
                else:
                    continue
    results(word,file_name,i) # Displaying the result.

# Function which counts from file, inputed word that are the same.

def count_from_file(file_name):
    with open(file_name) as file1:
        word = input("What would You like to count: ")
        i = 0   # Variable whitch counts the amount of words.
        for line in file1: # Looping through all lines of file.
            words_split = line.split() # Splitting the line into list.
            for word2 in words_split: # Looping through made before lists which contain words from line.
                if word.lower() in word2.lower(): # Counting.
                    i += 1
                else:
                    continue
    results(word,file_name,i)
    return i

# Function which counts from file inputed by the user, words that are the same.

def count_from_inputed_file():
    name_of_file = input("Input name of file You want to analize: ")
    with open(name_of_file) as file1:
        word = input("What word would You like to count: ")
        i = 0 # Variable whitch counts the amount of words.
        for line in file1: # Looping through all lines of file.
            words_split = line.split() # Splitting the line into list.
            for word2 in words_split: # Looping through made before lists which contain words from line.
                if word.lower() in word2.lower(): # Counting.
                    i += 1
                else:
                    continue
    results(word,name_of_file,i)


def count_every_sonet():
    list_of_files = glob.glob("/home/dev/Desktop/codebrainers/python/sonety/*") # Directory of files we want to check.
    word = input("What would You like to count: ")
    for name_of_file in list_of_files:
        with open(name_of_file,"r") as file1:
            i = 0 # Variable whitch itering through all files, so it have to be 0 for every file.
            for line in file1: # Looping through all lines of file.
                words_split = line.split() # Splitting the line into list.
                for word2 in words_split: # Looping through made before lists which contain words from line. 
                    if word.lower() == word2.lower(): # Counting.
                        i += 1
                    else:
                        continue
            print("In file: {} the word {} occurs {} times.\n".format((file1),(word),(i))) # Printing the results for every file.
