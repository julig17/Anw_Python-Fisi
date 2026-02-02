#einfachen Text in eine Textdatei schreiben
try: 
    gedichte_schreiber = open("./files/gedichte.txt", "w", encoding="utf-8")
except FileNotFoundError:
    print("Datei nicht gefunden:")
except:
    print("sonstige Dateifehler")

gedicht = "Ene mene Miste\n" \
"Was rappelt in der Kiste\n\n" \
"\tEne mene meg\n" \
"\tUnd du bist weg!\n\n\n"
gedichte_schreiber.write(gedicht)
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