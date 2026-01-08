"""Füge zwei vorher festgelegte Listen zu einer zusammen und gib diese aus:

Beispiel: [2,6,9] zusammengefügt mit [1,4,6] ergibt [2,6,9,1,4,6]
Gib von deiner Liste das 2 bis 4 Element aus.
Was passiert wenn du versuchst ein Element mit einem Index auszugeben, das über die Anzahl der Elemente in der Liste hinausgeht?
Prüfe mit Operator in / not in ob Elemente in der Liste drin sind, oder nicht
Lösche das letzte Element aus der Liste.
"""
erste_liste = [1, "Hallo", "Plus"]
zweite_liste = ["Operator", 2]
#Zusammenfügen zweier Liste
print(erste_liste + zweite_liste)
#Reinhenfolge ist entscheidend
print(zweite_liste + erste_liste)
zusammengefuegte_liste = erste_liste + zweite_liste
print(zusammengefuegte_liste[1:3])
#IndexError Out of range
#print(zusammengefuegte_liste[10])
#Hallo ist in Liste
print("Hallo" in erste_liste)
#Tschüß ist nicht in der LIste
print("Tschüß"  not in erste_liste)
del erste_liste[-1]
print(erste_liste)