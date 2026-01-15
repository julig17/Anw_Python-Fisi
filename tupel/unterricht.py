#Definition
mein_tupel = ("Apfel", "Apfel", "Banane", "Kirsche")
print(mein_tupel)
zahlen_tupel = (1,2,2,5,15)
print(zahlen_tupel)

#Kurzschreibweise = Tupel  einpacken
namen_tupel = "Max", "Moritz", "Lisa"
print(namen_tupel)
print(type(namen_tupel))
#tupel auspacken
vorname, nachname, spitzname = namen_tupel 
print(vorname)
print(nachname)
#gleiche Elemente sind erlaubt
doppel_tupel = ("Apfel", "Apfel", "Banane", "Kirsche")
print(doppel_tupel)
#gemischte Datentypen-Elemente sind erlaubt
gemischtes_tupel = ("Apfel", 5, 5.5, "Kirsche")
print(gemischtes_tupel)
#Tupel können wiederum Tupel enthalten
mehrdimensionales_tupel = ("Apfel", (1,2,3), "Kirsche")
print(mehrdimensionales_tupel)


#Zugriff auf Elemente über Index
#erster Eintrag
print(mein_tupel[0])
#letzter Eintrag
print(mein_tupel[-1])
#Zugriff auf Elemente in mehrdimensionalen Tupeln
print(mehrdimensionales_tupel[1][2])

#Slicing
slice_tupel = (2,4,6,7,8,9) 
#vom anfang bis incl. 3.Element
print(slice_tupel[0:3])  
#rückwärts
print(slice_tupel[::-1])   

#die Elemente des Tupels sind nicht änderbar 
#slice_tupel[1] = 5
#print(slice_tupel)

#Verketten von Tupel mit +
tupel_1 = (1,2,5)
tupel_2 = (5,5,8,8) 
print(tupel_1 + tupel_2)


#Vervielfachen von Tupel mit *
print(tupel_2 * 3)

#Prüfen, ob ein Element in  Tupel  enthalten ist mit in
zeichenkette = ("Das", "ist", "in", "der", "Tupel")
wort = "ist"    
if wort in zeichenkette:
    print(wort)

print("Hallo" not in zeichenkette)

#Elemente können nicht gelöscht werden
#del mein_tupel[1]

#Länge eines Tupels mit len()
print("Anzahl der Elemente:", len(mein_tupel))
#Typische Iteration über alle Elemente
for element in mein_tupel:
    print("Element:", element)

#weitere Möglichkeit über Tupel zu iterieren mit Index
for index in range(len(mein_tupel)):
    print("Element mit Index", index, ":", mein_tupel[index])

mehrdimensionales_tupel = (("Apfel", "Banane"), (1,2,3), ("Kirsche", "Pflaume"))
for kleines_tupel in mehrdimensionales_tupel:
    for element in kleines_tupel:
        print("KLeines Tupel", kleines_tupel,"Element:", element)


tuple = (1,3,7,8,7,5,4,6,8,5)
        
print(tuple.count(5))

#Index des ersten Vorkommens eines Elements im Tupel:
print(tuple.index(8))

zahlen_1 = (16, 37, 31, 10, 27)
zahlen_2 = (45, 76, 53, 28, 37)
gesamt = zahlen_1 + zahlen_2

print("37 kommt", zahlen_1.count(37), "-mal in zahlen_1 vor")
print("37 kommt", zahlen_2.count(37), "-mal in zahlen_2 vor")
print("37 kommt", gesamt.count(37), "-mal in gesamt vor")
# Index des ersten Vorkommens eines Elements im Tupel ermitteln
# index("xy")
print("37 hat in gesamt den Index", gesamt.index(37))



