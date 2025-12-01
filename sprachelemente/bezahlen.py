anzahl = 6
preis = 13.5
vorname = "Julia"

print(vorname,"kauft",anzahl,"Artikel zum Einzelpreis von",
       preis,"Euro und bezahlt:",anzahl * preis)

#Mischung von Datentypen int und str, muss beim Zusammensetzen in str
#umgewandelt werden
print(vorname + " kauft " + anzahl + " Artikel zum Einzelpreis von "
       + str(preis) + " Euro und bezahlt: " + str(anzahl * preis))

