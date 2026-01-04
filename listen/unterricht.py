# erstellen einer Liste, beachte Ausgabe
zahlen_liste = [1,2,3,4,5]

#Liste ausgeben
print(zahlen_liste)

#gleiche Elemente in einer Liste sind möglich
zahlen_liste_2 = [1,1,2,2]
print(zahlen_liste_2)

#eine Liste kann unterschiedliche Datentypen enthalten
mix_liste = ["Hallo", 2, 2.5, "Listen"]
print(mix_liste)

#eine Liste kann wiederum eine Liste enthalten
verschachtelte_liste = [2, 5, "Zeichen", [15, 12, [23, 48]], ["noch eine Liste"]]
print(verschachtelte_liste)

mehrdimensional_array = [[1,2,3], [4,5,6]]
print(mehrdimensional_array)

#1. Element der Misch-Liste ausgeben (index fängt bei 0 an)
print(mix_liste[0])

# 2. bis 4. Element der Misch-Liste ausgeben (index = 1:4) / Slicen
print(mix_liste[1:4])

# ändern der Elemente
mix_liste[0] = "Tschüß"
print(mix_liste)



