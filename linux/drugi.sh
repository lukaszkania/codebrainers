#!/usr/bin/env bash
mkdir -p 2018.12.15.cwiczenia
cd 2018.12.15.cwiczenia

echo "To jest nasz skrypt"

# Przekierownaie do pliku przez > gdy nadpisujemy lub >> gdy dodajemy do konca pliku.
echo 'A to zostanie zapisane w pliku stdout.txt o godzinie ' $(date) >> stdout.txt

echo "Sprawdz czy rzeczywiscie plik stdout.txt zawiera nasz napis"

date

more stdout.txt