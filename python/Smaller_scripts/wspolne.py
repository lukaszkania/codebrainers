#!/usr/bin/env python
import time
import math

first_list = [x**2 for x in range(1,1000)]
second_list = [x**3 for x in range(1,1000)]

common = [] # List where the result will be stored.

start = time.time() # Begining of the loop.

# FIRST WAY OF FINDING COMMON RESULTS BY LOOP.
for element in first_list: # Loop itering through the whole list. 
    if element in second_list: # Condition statment checking if the element from one list is in the other list.
        common.append(element)
    else:
        continue
end_of_action = time.time() # End of the loop.
final = end_of_action - start # Time of action of the first way of finding common results.

print("Pierwszy wariant z petla, czas wykonania: {} \n".format(final)) # Printing the time of action.

final_time_first_way = final # Assign the time of action to the variable to make comparison to the second way.

# SECOND WAY OF FINDING COMMON RESULTS BY ADDING TO SETS.
first_list = set(first_list)
second_list = set(second_list)
start = time.time() # Beginig of the adding two sets.
result = first_list & second_list
end_of_action = time.time() # End of the adding two sets.
final = end_of_action - start # Time of action of the second way of finding common results.

print("Drugi wariant ze zbiorami, czas wykonania: {} \n".format(final))

final_zbiorem = final # Assign the time of action to the variable to make comparison to the first way.

# Results of the time of action.
print("Roznica miedzy pierwszym sposobem, a drugim: {} \n".format(final_time_first_way - final_zbiorem)) # Diffrence between two ways of finding common results.

# Printing the length of lists and final results.
print("Dlugosc listy pierwszej to {}, a listy drugiej to {} \n".format(len(first_list), len(second_list))) # Length of lists.
print("Wspolne elementy dwoch tablic: \n", common, "\n") # FINAL RESULTS - COMMON NUMBERS.

# Loop printing the results and the numbers that was squared and raised to the third power.
print("Wyniki i liczby, które zostały podniesione do kwadratu i podniesione do trzeciej potęgi: \n")
for element in common:
    result_tuple = (element, int(math.ceil(element ** (1/2))), int(math.ceil(element ** (1/3))))
    print(result_tuple)
