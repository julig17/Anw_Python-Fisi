dateiname = "./files/gedichte.txt"
try:
    datei_objekt = open(file=dateiname, mode="r", encoding="UTF-8")
    for zeile in datei_objekt:
        #mache sonst a mit der Zeile, verarbeiten
        #print(zeile.strip())
        pass
    datei_objekt.close()
except FileNotFoundError:
    print("Datei nicht gefunden")
except Exception as ex:
    print("Ein anderer Fehler ist aufgetretn", ex)


try:
    datei_objekt = open(file=dateiname, mode="r", encoding="UTF-8")
    zeile = datei_objekt.readline()
    #print(zeile)
    while zeile != "":
        #print(zeile)
        zeile = datei_objekt.readline()
    datei_objekt.close()
except FileNotFoundError:
    print("Datei nicht gefunden")
except Exception as ex:
    print("Ein anderer Fehler ist aufgetretn", ex)

ohne_whitespaces = []
try:
    datei_objekt = open(file=dateiname, mode="r", encoding="UTF-8")
    liste  = datei_objekt.readlines()
    for element in liste:
        if element != "\n":
         ohne_whitespaces.append(element.strip())
    print(ohne_whitespaces)
    datei_objekt.close()
except FileNotFoundError:
    print("Datei nicht gefunden")
except Exception as ex:
    print("Ein anderer Fehler ist aufgetretn", ex)

try:
    datei_objekt = open(file=dateiname, mode="r", encoding="UTF-8")
    inhalt = datei_objekt.read()
    print(inhalt)
    datei_objekt.close()
except FileNotFoundError:
    print("Datei nicht gefunden")
except Exception as ex:
    print("Ein anderer Fehler ist aufgetretn", ex)


