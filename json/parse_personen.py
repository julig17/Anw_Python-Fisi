#Modul json muss eingebunden werden
import json

personen_liste = []

try:        
    with open("./json/personen.json", "r", encoding="UTF-8") as personendatei:
# json-Datei komplett in die Liste personen Liste einlesen
        personen_liste = json.load(personendatei)
except FileNotFoundError as e:
    print("Datei nicht gefunden", e)
except Exception as e:
    print(f"Sonstiger Dateizugriffsfehler: {e}")

print("So sieht der geparste JSON String aus")
print(personen_liste)
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
            print(f"{eigenschaft} : {wert}")
    print("-" * 10)

