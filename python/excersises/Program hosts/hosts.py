#!/usr/bin/env python

with open("hosts.txt") as text_file:

    for line in text_file.readlines():
        name = line.split('.')[0].title()
        surname = line.split(".")[1].split("@")[0].title()
        email = line.split()[0]
        print("Name: {}. Surname: {}. E-mail: {}".format(name, surname, email))

    text_file.seek(0)
