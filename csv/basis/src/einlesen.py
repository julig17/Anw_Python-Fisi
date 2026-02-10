datei_name = "./csv/basis/data/artikel.csv"
try:
# Datei öffnen und gesamten Inhalt lesen
    with open(datei_name "r", encoding="UTF-8") as artikel_datei:
        datei_inhalt = artikel_datei.read()
except FileNotFoundError:
    print("Datei nicht gefunden")
except Exception as e:
    print(f"Sonstiger Dateizugriffsfehler: {e}")
# ---------------------------------------------------
# Aufbereitung der eingelesenen Daten
# ---------------------------------------------------
# Zeilen in Liste umwandeln, Ergebnis ist eine Liste mit Zeile als Listenelement
zeilen_liste = datei_inhalt.splitlines()
# Kopfzeile (erste Zeile) und restliche Daten trennen
#KOpfzeile enthält die Spaltenüberschriften
kopfzeile = zeilen_liste[0].split(",")
#die Artikel slicen aus der zeilen_liste,  als Daten aufspalten, 
#und in daten_zeilen speichern
daten_zeilen = []
for zeile in zeilen_liste[1:]:
    daten_zeilen.append(zeile.split(","))
#Kurzschreibweise als List Comprehension
#daten_zeilen = [zeile.split(",") for zeile in zeilen_liste[1:]]


for zeile in daten_zeilen:              #ueber alle Listenelemente in der Daten Liste iterieren
    for i in range(len(kopfzeile)):     #über die Kopfzeile iterieren
        spaltenname = kopfzeile[i]
        wert = zeile[i]
        print(f"{spaltenname:15}: {wert}")
    print("-" * 40)