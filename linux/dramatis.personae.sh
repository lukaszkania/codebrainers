#!/usr/bin/env bash
# definiujemy plik
text=william.sheakespeare

# definiujemy liste imion
names="Hamlet Macbeth Ophelia Henry"
# robimy petle po kolejnych imionach
for name in $names
# zawartosc petli pod spodem
do
	# wyswietlamy nazwe zmiennej
	echo -n $name ": "
	# sprawdzamy ile razy zmienna wystepuje w pliku
	grep -E -c $name $text 
done


















