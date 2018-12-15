#!/usr/bin/env bash

read -p "Wpisz nazwe pliku ktory chcesz zbadac:" text # Getting input from the user to describe name of the file the program should analize.

# Countig some general info.
echo "Ilosc linii w pliku: $(wc -l $text) w tekscie $text" # Print the newline counts.
echo
echo "Ilosc wyrazow w pliku $(wc -w $text) w tekscie $text" # Print the word counts.
echo
echo "Ilosc liter w pliku $(wc -m $text) w tekscie $text" # Print the characters counts.
echo 

# Countig how many times given char occurs.
read -p "Podaj litere, ktorej czestotliwosc wystepowania chcesz policzyc:" char 
echo
echo "Litera $char wystepuje w pliku $text $(fgrep -o $char $text | wc -l) ilosc razy."
echo
a=$(fgrep -o $char $text | wc -l)
b=$(wc -m $text)
echo "Stanowi to $a/$b  wszystkich znakow. "
echo

# Countig how many times given word occurs.
read -p "Wpisz imie, ktore chcesz policzyc, ile razy wystepuje:" word # Getting input from the user to describe the word we want to analize.
echo
echo "Wyraz $word wystepuje w pliku $text $(grep -E -c $word $text) razy."
echo