import csv
datei_name = "./csv/modul/data/artikel_w.csv"
# SpaltenListe mit Spaltennamen
spalten_namen = ['Artikelnummer', 'Artikelname', 'Preis', 'Kategorie', 'Anzahl']
# Daten vorbereiten (Liste von Dictionaries)
daten = [{'Artikelnummer': '1001', 'Artikelname': 'Tastatur', 'Preis': '29.99', 'Kategorie': 'Hardware', 'Anzahl': '15'},
        {'Artikelnummer': '1002', 'Artikelname': 'Maus', 'Preis': '19.99', 'Kategorie': 'Hardware', 'Anzahl': '30'}
]
# CSV-Datei schreiben
try:
    with open(datei_name, "w", encoding="UTF-8", newline="") as datei:
        csv_writer = csv.DictWriter(datei, fieldnames=spalten_namen)
        # Spaltenköpfe schreiben
        csv_writer.writeheader()
        # Datenzeilen schreiben
        csv_writer.writerows(daten)
except Exception as e:
    print(f"Zugriffsfehler auf die CSV-Datei: {e}")
