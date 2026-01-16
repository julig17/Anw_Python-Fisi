obst_tupel = ("Apfel", "Banane", "Kirsche", "Dattel", "Apfel")           
#print(obst_tupel) 

obst_liste = ["Apfel", "Banane", "Kirsche", "Dattel"]   
#print(obst_liste)

#print(type(obst_tupel))
#print(type(obst_liste)) 

# gemischte Datentypen im Tupel
gemischt_tupel = ("Hallo", 42, 3.14, True)
#print(gemischt_tupel)

#Kurzschreibweise für Tupel 
kurz_tupel = 1, 2, 3, "Vier"
#print(type(kurz_tupel))
eins, zwei, drei, vier = kurz_tupel
#print(vier)



namen = ("Julia", "Greif")
vorname, nachname = namen
#print(nachname)

#mehrdimensionale Tupel
mehrdim_tupel = (("A", "B"), (1, 2), (True, False))


#Index / Slicen
#print(kurz_tupel[::-1])

#Unveränderlichkeit von Tupeln
#kurz_tupel = 1, 2, 3, "Vier"
#kurz_tupel[0] = 10
kurz_tupel = 2,5,"Neu"
#print(kurz_tupel)
kurz_tupel += (7,8)
#print(kurz_tupel)


kurze_antwort = (42, "Die Antwort", 3.14, False)
#print(id(kurze_antwort))

kurze_antwort += (True,)
#print(id(kurze_antwort))
#print(kurze_antwort)

kurze_antwort = (42, "Die Antwort", 3.14, False)
#print(id(kurze_antwort), kurze_antwort)
kurze_antwort += (True,)
#print(id(kurze_antwort) , kurze_antwort)

#del kurze_antwort[1]

#VErvielfachen von Tupel
t1 = (2,4,6)
t2 = (1,3,5)
t_neu = t1 * 2
#print(t_neu)
#Achtung ! Tupel mit einem Element ebenfalls mit Komma definieren
t3  = (2,)
t4 = (3)
print(t3 * t4)

#Hier funktionier die Multiplikation, da auf beide Tupel mit Index zugegriffen wird
t1 = (1,2,3)
t2 = (6,7,8)
print(t1[2]*t2[0])


#gibt wieder Fehler, da Slicing ein Tupel zurückgibt
try:
    print(t1[0:2]*t2[0:2])
except TypeError as e:
    print("Fehler:", e)

t1 = (1,2,3)
t2 = (6,7,8)
print(t1[0:2]*t2[0])

#Workaround für Tupelmanipulationen
t1 = (2, 6, 9)
t2 = (1, 4, 6)

t_gesamt = t1 + t2
sortiert = sorted(t_gesamt) # ACHTUNG LISTE
t_sortiert = tuple(sortiert) # Sortierte Liste in Tupel umwandeln
print("Sortierte Ausgabe:", t_sortiert)

print(len(t_sortiert))

for index in range(len(t_sortiert)):
    print(f"Element an Index {index}: {t_sortiert[index]}") 

for element in t_sortiert:
    print("Element:", element)

