meine_liste = ["Apfel", "Banane", "Kirsche"]
print(meine_liste)
gemuese_liste = ["Karotte", "Brokkoli", "Spinat"]
meine_liste.append(gemuese_liste)
print(meine_liste)
print(len(meine_liste))

meine_liste_2 = ["Apfel", "Banane", "Kirsche"]
print(meine_liste_2)
gemuese_liste = ["Karotte", "Brokkoli", "Spinat"]
meine_liste_2.extend(gemuese_liste)
print(meine_liste_2)
print(len(meine_liste_2))
print(meine_liste_2.count("Apfel"))
meine_liste_2.append("Apfel")
print(meine_liste_2.count("Birne")) 

meine_liste_3 = ["Apfel", "Banane", "Kirsche"]
meine_liste_3.insert(1, ["Birne", "Pfirsich"])
print(meine_liste_3)



meine_liste_4 = ["Apfel", "Banane", "Kirsche"]
ele = meine_liste_4.pop()
print(ele)



meine_liste_5 = ["Apfel", "Banane", "Kirsche"] 
gemuese_liste_1 = ["Karotte", "Brokkoli"]
for index in range(len(gemuese_liste_1)):
    meine_liste_5.insert(index + 5, gemuese_liste_1[index])
print(meine_liste_5)


meine_liste_6 = ["Apfel", "Banane", "Kirsche", "Birne", "Pfirsich", "Kirsche"]
meine_liste_6.remove("Kirsche")
print(meine_liste_6)    

meine_liste_7 = ["Apfel","Banane", "Kirsche", "Birne", "Pfirsich", "Kirsche"]
meine_liste_7.sort()        
print(meine_liste_7)

#Hier ein Fehler zum Demonstrieren, da Listen mit unterschiedlichen Datentypen 
#nicht sortiert werden können
#meine_liste_7 = ["Apfel", 2, 5 , ["Banane", "Kirsche", "Birne"], "Pfirsich", "Kirsche"]
#meine_liste_7.sort()        
