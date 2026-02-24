def in_liste(liste, wert):
    if len(liste) == 0:          # Base Case
        return False
    if liste[0] == wert:
        return True
    return in_liste(liste[1:], wert)

print(in_liste([5, 8, 2, 9], 2))   
print(in_liste([5, 8, 2, 9], 7))   