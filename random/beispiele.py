import random as r


#random(): zufällige Gleitpunktzahlen (float) zwischen 0.0 und 1.0

print(r.random())

# Generiere 5 zufällige Gleitpunktzahlen zwischen 0.0 und 1.0
for anzahl in range(1,6):
    print(r.random())


#randint(min, max): zufällige ganze Zahlen (int) in einem frei wählbaren Intervall
for anzahl in range(1,6):
    print(r.randint(1,100))

#sample(liste ,k=n): zufällige Elemente aus einem seq. Datentyp auswählen (ohne Wiederholung), n = Anzahl der Elemente

liste = ["Sonnenschein", "Schnee", "Regen", "Bewölkt", "Windig"]
print(r.sample(liste, k = 3))

#.choice(liste ) :zufälliges Element aus einem seq. Datentyp auswählen 
zeichnekette = "Bald ist Wochenende"
print(r.choice(zeichnekette))


#shuffle(liste): Elemente einer Liste in eine zufällige Reihenfolge bringen
r.shuffle(liste)
print(liste)
