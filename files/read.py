"""open öffnet die Datei, und gibt ein file-Objekt zurück
mit dem file-Objekt kann man den Inhalt der Datei auslesen read()"""
"""Immer im try except Block, da bei Dateien Fehler auftreten können"""
try: 
    file = open(file="./files/text.txt", mode="r", encoding="utf-8")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Datei nicht gefunden")
except Exception:
    print(Exception, "Sonstiger Dateifehler")

print("einfache Iteration zum Lesen")
try: 
    file = open(file="./files/text.txt", mode="r", encoding="utf-8")
    for zeile in file:
        print(zeile)
    file.close()
except FileNotFoundError:
    print("Datei nicht gefunden")
except:
    print("sonstige Dateifehler")

"""mit readline()"""
try: 
    with open(file="./files/text.txt", mode="r", encoding="utf-8") as file:
    #lese erste Zeile
        zeile = file.readline()
        while zeile != "":
            print(zeile)
            zeile = file.readline()
except FileNotFoundError:
    print("Datei nicht gefunden")
except:
    print("sonstige Dateifehler")

"""in Liste"""
zeilen = []
try: 
    with open(file="./files/text.txt", mode="r", encoding="utf-8") as file:
        zeilen = file.readlines()
except FileNotFoundError:
    print("Datei nicht gefunden")
except Exception as e:
    print("sonstige Dateifehler", e)
print(zeilen)


