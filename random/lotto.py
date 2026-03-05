"""Erstelle ein Programm, welches für den Eurojackpot die Gewinnzahlen
generiert. Beim Eurojackpot wählen Sie einfach 5 Zahlen 
aus der Zahlenreihe von 1 bis 50 
und zusätzlich 2 Zahlen aus 12 Eurozahlen """
import random

def generiere_eurozahlen(range_end, anzahl):
    return random.choices(range(1,range_end), k = anzahl)


print("Das sind die 5 Zahlen für das heutige Eurojackpot Spiel")
print(generiere_eurozahlen(51, 5))


print("Das sind die Eurozahlen für das heutige Spiel")
print(generiere_eurozahlen(13, 2))