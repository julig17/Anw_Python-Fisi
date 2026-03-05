import random
# Generiere 5 zufällige Gleitpunktzahlen zwischen 0.0 und 1.0
print("5 zufällige Gleitpunktzahlen zwischen 0.0 und 1.0")
for zufallszahl in range(1,6):
    print(zufallszahl, random.random())

# Generiere 5 zufälligen integer zwischen 1 und 100
print("5 zufällige integer zwischen 1 und 100")
for zufallszahl in range(1, 6):
    print(zufallszahl, random.randint(1, 100))

# 2 Elemente aus Liste auswählen (ohne Wiederholung)
print("2 zufällige Elemente aus einer Liste")
print(random.sample(["Tomate", "Birne", "Kiwi", "Erdbeere"], 2))

# ein zufälliges Zeichen aus einer Zeichenkette ausgeben
text = "Python ist toll"
print(random.choice(text))

# 5 zufällige Zeichen aus einer Zeichenkette ausgeben
print(random.choices(text, k=5))

liste = [1, 3, 5, 7, 9]
# ein zufälliges Element aus einer Liste ausgeben
print(random.choice(liste))
# 3 zufällige Elemente aus einer Liste ausgeben
print(random.choices(liste, k=3))
# Elemente einer Liste in eine zufällige Reihenfolge bringen - mischen
liste = [1, 3, 5, 7, 9]
print("vor dem Mischen: ", liste)
# Mischen von list
random.shuffle(liste)
print("nach dem Mischen:", liste)