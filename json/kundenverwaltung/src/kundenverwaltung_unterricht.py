import json

DATEINAMEN = "./json/kundenverwaltung/data/kunden.json"

# 1. Funktion alle Kunden auflisten

"""
Das ist eine Hilfsfunktion zum Öffnen und Lesen der Daten
aus dem JSON Kundendokument
Diese Funktion liefert das JSON als Python Datenstruktur zurück
"""
def lade_kunden():
    try:
        with open(DATEINAMEN, "r", encoding="UTF-8") as datei:
            return json.load(datei)
    except Exception as ex:
        print(f"Dehler beim Lesen der Json Datei {ex}")



"""
Das ist eine Hilfsfunktion zum Öffnen und SChreiben der Daten
aus einerm Python Objekt in die JSON Datei
"""
def speichere_kunde(kunden):
    try:
        with open(DATEINAMEN, "w", encoding="UTF-8") as datei:
            json.dump(kunden, datei, indent=4)
    except Exception as ex:
        print(f"Dehler beim Schreiben der Json Datei {ex}")



"""
Diese Funktion listet alle Kunden aus einer Liste auf
und gibt diese aus
"""
def list_kunden():
    kunden_liste = lade_kunden()

    """
    for kunde in kunden_liste:
        print(f"{kunde["name"]} | {kunde["email"]} | {kunde["geburtsjahr"]}")
        print("-" * 40)
    """
    for index, kunde in enumerate(kunden_liste, start = 1):
        print(f"{index} | {kunde["name"]} | {kunde["email"]} | {kunde["geburtsjahr"]}")
        print("-" * 40)
    

"""
Diese Funktion legt einen neuen Kunden an und speichert 
diesen in der JSON Datei ab
"""
def create_kunde(name, email, geburtsjahr):
    kunden_liste = lade_kunden()
    kunde = {"name" : name, 
             "email" : email,
             "geburtsjahr" : geburtsjahr}
    kunden_liste.append(kunde)
    speichere_kunde(kunden_liste)

"""
Findet aus der Kundenliste den Kunden mit entsprechendem Namen
und gibt den Kunden zurück
"""
def finde_kunde_name(name):
    kunden_liste = lade_kunden()
    for kunde in kunden_liste:
        if kunde["name"].lower() == name.lower():
            return kunde


"""Testen der API"""
list_kunden()
create_kunde("Juila GReif", "max@example.de", "2000")
create_kunde("Juila Müller", "max@example.de", "2020")
list_kunden()
name = input("Gib des Namen des Kunden ein:")
kunde = finde_kunde_name(name)
print(kunde)


