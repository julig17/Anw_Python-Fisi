"""eine Liste von Zeichenketten enthält die Spaltenüberschrift und dann Datenzeilen
zwischen den Spaltenüberschriften und den einzelnen Werten ist das 
Trennzeichen ,
in jeder Datenzeile ist ein New Line \n  als Trenner der Daten
die Liste von Zeichenketten wird mit writelines in die Datei
geschrieben"""

zeilen = ["Artikelnummer,Artikelname,Preis,Kategorie,Anzahl\n", 
          "1001,Tastatur,29.99,Hardware,15\n",
          "1002,Maus,19.99,Hardware,30\n",
          "1003,Monitor 24 Zoll,179.90,Hardware,8\n",
          "1004,USB-Stick 64GB,12.50,Speicher,50\n",
          "1005,USB-Stick 32GB,8.50,Speicher,50"]
datei_name = "./csv/basis/data/artikel2.csv"
try:
    with open(datei_name, "w", encoding="UTF-8") as artikel_datei:
        artikel_datei.writelines(zeilen)
except Exception as ex:
    print("sonstiges Dateizugriffsfehler", ex)
