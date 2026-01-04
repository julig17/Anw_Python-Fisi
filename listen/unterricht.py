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

#negativer Index von hinten zählen
print(mix_liste[-2])


liste_teil1 = ["Erster", "Teil"]
liste_teil2 = ["der", "Liste"]
liste_gesamt = liste_teil1 + liste_teil2
print(liste_gesamt)

# Vervielfachen von Listen
multi_liste = ["Python"]
print(multi_liste)
print(2*multi_liste)

#Prüfen auf Elemente in der Liste
zeichenketten = ["Das", "ist", "in", "der", "Liste"]
print("Das" in zeichenketten)
print("das" in zeichenketten)
print("das" not in zeichenketten)

print(zeichenketten)
#Löschen eines Elementes über Index
del zeichenketten[0]
print(zeichenketten)
#Löschen von:bis Elemente über Index
del zeichenketten[1:3]
print(zeichenketten)

#Hinzufügen von Elementen
zeichenketten += ["jetzt", "das?"]
print(zeichenketten)

#Länge der Liste
zahlen_liste = [1, 2, 3, 4, 5, 6]
print("Anzahl der Elemente: ", len(zahlen_liste))

#Typische Iteration über alle Elemente
for i in range(len(zahlen_liste)):
    print("Index", i, "Zahl", zahlen_liste[i])

#Iterationen
meine_liste = ["Apfel", "Banane", "Kirsche"]
for frucht in meine_liste:
    print(frucht)

# Oder mit Slicing [::-1]
# [::-1] erstellt eine umgekehrte Kopie
for frucht in meine_liste[::-1]: 
    print(frucht)

meine_liste = ["Apfel", "Banane", "Kirsche"]
for i in range(len(meine_liste)):
    print(f"Element an Index {i}: {meine_liste[i]}")

meine_liste = ["Apfel", "Banane", "Kirsche"]
i = 0
while i < len(meine_liste):
  print(meine_liste[i])
  i = i + 1


mehrdimensionale_liste = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Äußere Schleife: Iteriert durch jede Zeile
for zeile in mehrdimensionale_liste:
    ausgabe = ""
    # Innere Schleife: Iteriert durch jedes Element in der aktuellen Zeile
    for element in zeile:
        ausgabe += str(element) + " " 
    print(ausgabe) 

meine_liste = ["Apfel", "Banane", "Kirsche"]
print(meine_liste)

#Element ans Ende der Liste anhängen:
meine_liste.append("Erdbeere")
print(meine_liste)

#Wie oft ein Element in der Liste enthalten ist:
print(meine_liste.count("Erdbeere"))

#Index des ersten Vorkommens eines Elements in der Liste:
print(meine_liste.index("Erdbeere"))

#Listenelemente ans Ende der Liste anhängen:
mein_liste_2 = ["Gurke", "Paprika"]
meine_liste.extend(mein_liste_2)
print(meine_liste)

meine_liste = ["Apfel", "Banane", "Kirsche"]
print(meine_liste)

#neues Element an einer bestimmten Stelle einfügen:
meine_liste.insert(1, "Orange")
print(meine_liste)

#Element an einer bestimmten Stelle entfernen:
meine_liste.pop(1)
print(meine_liste)
meine_liste.pop()
print(meine_liste)

#entfernt das erste Element aus der Liste, das identisch ist:
meine_liste.remove("Banane")
print(meine_liste)

#dreht die Reihenfolge der Elemente um:
meine_liste = ["Apfel", "Banane", "Kirsche"]
meine_liste.reverse()
print(meine_liste)

meine_liste = ["Apfel", "Banane", "Kirsche"]

#Sortiert die Elemente der Liste aufsteigend:
meine_liste.sort()
print(meine_liste)

meine_liste = ["Apfel", "Banane", "Kirsche"]
#Sortiert die Elemente der Liste absteigend:
meine_liste.sort(reverse=True)
print(meine_liste)
#Löscht alle Elemente der Liste:
meine_liste.clear()
print(meine_liste)







