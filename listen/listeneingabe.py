eingabe_liste = []
while True:
    eingabe = input("Gib ein Listeelement ein, zum Beenden gib ein X ein: ")
    if (eingabe == "X"):
        break
    eingabe_liste.append(eingabe)

print(eingabe_liste)

loesch_element = input("Gib ein Löschelement ein: ")

liste_ohne = []

if loesch_element in eingabe_liste:
    for ele in eingabe_liste:
        if ele != loesch_element:
            liste_ohne.append(ele)
    print(liste_ohne)
else: 
    print("Löschungselement kommt nicht vor")

