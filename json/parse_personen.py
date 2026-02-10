#Modul json muss eingebunden werden
import json

personen_liste = []
dateiname = "./json/personen.json"

try:        
    with open(dateiname, "r", encoding="UTF-8") as personendatei:
# json-Datei komplett in die Liste personen Liste einlesen
        personen_liste = json.load(personendatei)
except FileNotFoundError as e:
    print("Datei nicht gefunden", e)
except Exception as e:
    print(f"Sonstiger Dateizugriffsfehler: {e}")

print("So sieht der geparste JSON String aus")
#print(personen_liste)

print("-" * 10)

#da unsere Daten in einer Liste liegen, können wir durch die liste iterieren 
#und die Personen ausgeben
for person in personen_liste:
    #jetzt geben wir die Person aus, aus dict
    for eigenschaft, wert in person.items():
        if eigenschaft == "kinder":
            print(f"{eigenschaft} :")
            for kind in wert:
                for eigenschaft, wert in kind.items():
                    print(f"\t{eigenschaft} : {wert}")
                print("-" * 10)
        else:
            print(f"Person: {eigenschaft} : {wert}")
    print("-" * 10)

"""
#Zeigt die Verschachtelung des JSON Dokumentes
    person1= personen_liste[0]
    name = person1["name"]
    print(person1["beruf"])
    #kinder = person1["kinder"]
    #kinder1 = kinder[0]
    #name_kind1 = kinder1["name"]
    #print(name_kind1)

"""