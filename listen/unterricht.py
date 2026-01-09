zahlen_liste = [1,2,5,15]
print(zahlen_liste)

zahlen_liste_2 = [5,5,8,8]
print(zahlen_liste_2)

gemischte_liste = ["Hallo", 5, 5.5, "Welt"]
print(gemischte_liste)

gemischte_liste_2 = ["Hallo", 5, 5.5, "Welt", [1,2,5]]
print(gemischte_liste_2)
print(gemischte_liste_2[-1])

dictionary = {"name" : "Greif"}
liste = [1,2, dictionary]
print(liste)


mehrdimensionale_array = [[1,2,3], [4,5,6]]
print(mehrdimensionale_array)
print(mehrdimensionale_array[0][1])

print(mehrdimensionale_array[1][2])

slice_liste = [2,4,6,7,8,9]
#vom anfang bis incl. 3.Element
print(slice_liste[::-1])

slice_liste[1] = 5
print(slice_liste)


zahlen_liste = [1,2,5,15]
print(zahlen_liste)

zahlen_liste_2 = [5,5,8,8]
print(zahlen_liste_2)

print(zahlen_liste_2*3)

zahlen_liste = [1,2,5,15]
print(zahlen_liste)

zeichenketten = ["Das", "ist", "in", "der", "Liste"]

wort = "ist"
if wort in zeichenketten:
    print(wort)
del zeichenketten[0:2]
print(zeichenketten)
if wort in zeichenketten:
    print(wort)

zeichenketten += ["noch", "das"]
print(zeichenketten)





