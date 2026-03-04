"""Programmiere den Python- Opearator  in rekursiv nach.

liste  = [2,6,3,9]
2 in liste  # true
8 in liste  # false
"""

liste  = ["Ja", "Nein", "Doch"]
print("Ja" in liste)  # true
print(8 in liste)  # false



def pruefe_in(liste, wert):
    #Abbruchfall
    if len(liste) == 0:
        return False
    if liste[0] == wert:
        return True
    #Rekursion
    return pruefe_in(liste[1:], wert)

print(pruefe_in(liste, "Ja"))
print(pruefe_in(liste, 8))


