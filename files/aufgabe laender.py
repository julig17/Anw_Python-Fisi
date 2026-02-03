
def ausgabe_dict_in_datei(inhalt, dateiname):
    try:
        with open(dateiname, "w", encoding="utf-8") as file:
            for schluessel, wert in inhalt.items():
                file.write(f"{schluessel} : {wert}\n")
    except FileNotFoundError:
        print("Datei nicht gefunden:")
    except:
        print("sonstige Dateifehler")

def eingabe_aus_datei_in_liste(dateiname):
    liste = []
    try: 
        with open(file=dateiname, mode="r", encoding="utf-8") as file:
            liste = file.readlines()
    except FileNotFoundError:
        print("Datei nicht gefunden")
    except Exception as e:
        print("sonstige Dateifehler", e)
    return liste

def baue_laender_haupstaedte(laender):
    hauptstaedte = {}
    for land in laender:
        land = land.strip()
        hauptstadt = input(f"Was ist die Hauptstadt von {land}? ")
        hauptstaedte[land] = hauptstadt
    return hauptstaedte


datei_r = "./files/laender_r.txt"
datei_w = "./files/laender_w.txt"

laender = eingabe_aus_datei_in_liste(datei_r)
hauptstaedte = baue_laender_haupstaedte(laender=laender)
ausgabe_dict_in_datei(hauptstaedte, datei_w)