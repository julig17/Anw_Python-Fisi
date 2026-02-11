import csv
datei_name = "./csv/modul/data/artikel_w.csv"
# Artikel Daten
zeilen = [["1001","Tastatur","29.99","Hardware","15"],
          ["1002","Maus","19.99","Hardware","30"]]
# CSV-Datei zum Schreiben öffnen und CSV-Writer-Objekt erstellen
try:
    with open(datei_name, "w", encoding="UTF-8", newline="") as datei:
        csv_writer = csv.writer(datei)
        # Spaltenköpfe schreiben
        csv_writer.writerow(['Artikelnummer', 'Artikelname', 'Preis', 'Kategorie', 'Anzahl'])
        # Datenzeilen schreiben
        csv_writer.writerows(zeilen)
except Exception as e:
    print(f"Zugriffsfehler auf die CSV-Datei: {e}")
