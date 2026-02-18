import csv
daten = []
datei_name = "./csv/modul/data/artikel.csv"
try:
    with open(datei_name, "r", encoding="UTF-8") as artikel_datei:
        # reader-Objekt zum "CSV-Lesen" der CSV-Datei erstellen
        csv_reader = csv.DictReader(artikel_datei)
        zeilen_liste = list(csv_reader)
except FileNotFoundError:
    print("Datei nicht gefunden")
except Exception as e:
    print("sonstiges Dateizugriffsfehler", e)


for zeile in zeilen_liste:
    for spalte, wert in zeile.items():
        print(f"{spalte:15}: {wert}")
    print("-" * 40)