#!usr/bin/env python

import sys

char = 0
lines = 0
words = 0

try:
    f = open(sys.argv[1])
    for line in f:
        lines += 1
        char += len(line)
        words += len(line.split())
    
    print(lines, words, char, sys.argv[1])

except IndexError:
    print("Too few arguments.")

except FileNotFoundError:
    print("Wrong filename.")