
import csv
datei_name = "./csv/modul/data/viele_artikel.csv"
try:
    with open(datei_name, "r", encoding="UTF-8") as artikel_datei:
        csv_reader = csv.DictReader(artikel_datei)
        zeilen_liste = list(csv_reader) 
except FileNotFoundError:
    print("Datei nicht gefunden")
except Exception as e:
    print("sonstiges Dateizugriffsfehler", e)


anzahl_artikel = len(zeilen_liste)
print(f"Anzahl der Artikel: {anzahl_artikel}")

summe_anzahl = 0
kategorien = {}
for zeile in zeilen_liste:
    artikelnummer = zeile['Artikelnummer']
    anzahl = int(zeile['Anzahl'])
    summe_anzahl += anzahl
    kategorie = zeile['Kategorie']
    if kategorie in kategorien:
        kategorien[kategorie] += anzahl
    else:
        kategorien[kategorie] = anzahl
    print(f"Artikelnummer: {artikelnummer}, Anzahl: {anzahl}")
print(f"Summe der Artikelanzahl: {summe_anzahl}")
print("Anzahl der Artikel in den einzelnen Kategorien:")
for kategorie, anzahl in kategorien.items():
    print(f"Kategorie: {kategorie}, Anzahl: {anzahl}")  