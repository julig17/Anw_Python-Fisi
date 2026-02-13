import csv
daten = []
datei_name = "./csv/modul/data/artikel.csv"
try:
    with open(datei_name, "r", encoding="UTF-8") as artikel_datei:
        # reader-Objekt zum "CSV-Lesen" der CSV-Datei erstellen
        csv_reader = csv.reader(artikel_datei)
        for row in csv_reader:
            print(row)
        # die Zeile werden als Elemente einer Liste bereitgestellt
        #zeilen_liste = list(csv_reader)
except FileNotFoundError:
    print("Datei nicht gefunden")
except Exception as e:
    print("sonstiges Dateizugriffsfehler", e)
"""
#Daten und Spaltenüberschrift liegen separiert 
#in als Liste vor
kopfzeile = zeilen_liste[0]
datenzeilen = zeilen_liste[1:]


for zeile in datenzeilen:
    for i in range(len(kopfzeile)):
        spaltenname = kopfzeile[i]
        wert = zeile[i]
        print(f"{spaltenname} : {wert}")
    print("-" *20)"""