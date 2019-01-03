#!/usr/bin/env python


imiona_string = "Iga julia Aleksandra Zofia oliwia Kinga Krzysztof antoni Jan Piotr kacper Jakub"
foreign_names_string = "Alex George Jeanette Michael"

# 0 - utwórz listy z podanych ciągów znaków
name_list = imiona_string.split(" ")
foreign_names_list = foreign_names_string.split(" ")

# 1 - wyswietl z name_list imiona kobiet 
for name in name_list:
    if name[len(name)-1] == "a":
        print(name,"\n")
    else:
        continue

# 2 - usuń z listy imiona Piotr i Zofia
for name in name_list:
    if name in ["Piotr", "Zofia"]:
        name_list.remove(name)

# 3 - utworz liste imion zaczynajacych sie na J 
J_list = []
for name in name_list:
    if name.title()[0] == "J":
        J_list.append(name)

# 4 - posortuj alfabetycznie polaczona liste imion
all_names = name_list + foreign_names_list

i = 0
while i < len(all_names):
    all_names[i] = all_names[i].title()
    i += 1 

all_names.sort()

# 5 - posortuj poloczona liste wg dlugosci imion
all_names.sort(key = len)

# 6 - odwroc kolejnosc posortowanej listy 
all_names.reverse()

## zwróc uwagę na wielkość liter