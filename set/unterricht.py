#anlegen einer leeren Set
leeres_set = set()
print("Leeres Set:", type(leeres_set))

#anlegen eines Sets mit Werten
zahlen_set = {1, 2, 3, 4, 5}    
print("Zahlen Set:", zahlen_set)

#gleiche Werte werden im Set nur einmal gespeichert
duplikate_set = {1, 2, 2, 3, 4, 4, 5}
print("Set mit Duplikaten (werden entfernt):", duplikate_set)

#set mit unterschiedlichen Datentypen
gemischtes_set = {1, "Hallo", 3.14, True}
print("Gemischtes Set:", gemischtes_set)

#Kein Indexzugriff bei Sets möglich
try:
    print(gemischtes_set[0])
except TypeError as e:
    print("Fehler beim Zugriff per Index auf ein Set:", e)


#set mit mutierbaren Elementen (Listen) ist nicht erlaubt
try:
    ungueltiges_set = {1, 2, [3, 4]}
except TypeError as e:
    print("Fehler beim Erstellen eines Sets mit Listen:", e)


#immutable Set
immutable_set = frozenset([1, 2, 3, 4, 5])
print("Immutable Set (frozenset):", immutable_set)
print("Typ des immutable Sets:", type(immutable_set))
try:
    immutable_set.add(6)
except AttributeError as e:
    print("Fehler beim Hinzufügen zu einem frozenset:", e)

#Set aus anderen Datentypen erstellen
string_set = set("Hallo Welt")
print("Set aus String:", string_set)
liste_set = set([1, 2, 3, 4, 5])
print("Set aus Liste:", liste_set)
print("Set aus Tupel:", set((1, 2, 3, 4, 5)))
print("Set aus Bereich (range):", set(range(1, 6)))
dict_set = set({'a': 1, 'b': 2, 'c': 3})
print("Set aus Dictionary (nur Schlüssel):", dict_set)


#Kein Indexzugriff bei Sets möglich
zahlen_set = {1, 2, 3, 4, 5}
try:
    print(zahlen_set[0])
except TypeError as e:
    print("Fehler beim Zugriff per Index auf ein Set:", e)
#Zugriff auf Set-Elemente durch Iteration
print("Iterieren über ein Set:")    
for element in zahlen_set:
    print(element)  
#Überprüfen auf Mitgliedschaft
print("Ist 3 im zahlen_set?", 3 in zahlen_set)
#set mit len()
print("Länge des zahlen_set:", len(zahlen_set)) 

