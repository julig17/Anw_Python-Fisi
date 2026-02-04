import json

try:        
    with open("./json/konfig.json", "r", encoding="UTF-8") as konfig_datei:
# json-Datei komplett in die Liste personen einlesen
        konfig = json.load(konfig_datei)
except FileNotFoundError as e:
    print("Datei nicht gefunden", e)
except Exception as e:
    print(f"Sonstiger Dateizugriffsfehler: {e}")

print(konfig["hostname"])
print(konfig["ip"])
print(konfig["port"])