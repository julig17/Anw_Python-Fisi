#einfachen Text in eine Textdatei schreiben
try: 
    gedichte_schreiber = open("./files/poesie.txt", "a", encoding="utf-8")
    gedicht = "Ein zweites Gedicht \n"
    gedichte_schreiber.write(gedicht)
except FileNotFoundError:
    print("Datei nicht gefunden:")
except:
    print("sonstige Dateifehler")
finally:
    gedichte_schreiber.close()



#schreiben in Datei mit with, dabei wird der Inhalt der Datei überschrieben
ueberschrift = "Im Wald\n"
gedicht = "Im Walde stehen Buchen,\n" \
"und Du musst suchen!\n\n\n"
try:
    with open("./files/gedichte.txt", "a", encoding="utf-8") as file:
        file.write(ueberschrift)
        file.write(gedicht)
except FileNotFoundError:
    print("Datei nicht gefunden:")
except:
    print("sonstige Dateifehler")
  