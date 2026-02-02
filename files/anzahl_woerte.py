def lese_aus_datei(dateiname):
    try: 
        with open(file=dateiname, mode="r", encoding="utf-8") as file:
            inhalt = file.read()
    except FileNotFoundError:
        print("Datei nicht gefunden")
    except Exception as e:
        print("sonstige Dateifehler", e)
    return inhalt

inhalt = lese_aus_datei("./files/gedichte.txt")
#split() trennt bei Leerzeichen, Tabs, Zeilenumbrüchen und erstellt
#eine Liste
print(len(inhalt.split()))