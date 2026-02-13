datei_name = "./csv/basis/data/artikel.csv"

try:
    with open(datei_name, mode='r', encoding='utf-8') as artikel_datei:
        datei_inhalt = artikel_datei.read()
except FileNotFoundError as ex:
    print(f"Fehler beim Lesen der Datei: {ex}")
except Exception as e:
    print(f"Sonstiger Dateizugriffsfehler: {e}")


zeilen_liste = datei_inhalt.splitlines()
spalten_namen = zeilen_liste[0].split(",")
print(spalten_namen)

daten_zeilen = []
for zeile in zeilen_liste[1:]:
    daten_zeilen.append(zeile.split(","))

for zeile in daten_zeilen:
    for i in range(len(spalten_namen)):
        spaltenname = spalten_namen[i]
        wert = zeile[i]
        print(f"{spaltenname} : {wert}")
    print("-" *20)




