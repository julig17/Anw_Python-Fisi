eingabe_daten = input("Gebe  kommasepariert Personendaten ein:\n" \
"Beispiel : Vorname, Nachname, Straße, Ort, Telefonnummer:")

assertion_nachricht = "Du hast nicht genügend Daten eingegeben"
assert eingabe_daten.count(",") >= 4, assertion_nachricht

visitenkarte = '''Name: {0} {1} 
Straße: {2} 
Ort: {3} 
Telefon: {4}'''

'''Erste Möglichkeit: benutze nur Funktionen slicing, find()!
noch keine Liste, Schleifen, Verzweigungen......'''
person = eingabe_daten
#suche den vornamen, bis zu ersten ","
vorname_bis = person.find(",")
vorname = person[0:vorname_bis]
vorname = vorname.strip()
#schneide vornamen ab, incl. dem Komma
person = person[vorname_bis + 1 : ]
#suche nach dem nachnamen
nachname_bis = person.find(",")
nachname = person[0 : nachname_bis].strip()
#schneide nachnamen ab
person = person[nachname_bis + 1 : ]
#suche die strasse 
strasse_bis = person.find(",")
strasse = person[0 : strasse_bis].strip()
#schneide strasse ab
person = person[strasse_bis + 1 : ]
#suche ort
ort_bis =  person.find(",")
ort = person[0 : ort_bis].strip()
#schneide ort ab
person = person[ort_bis + 1 : ]
#die telenr im rest
telenr = person[0 : ].strip()

#Ausgabe über die format Methode
print("Die Ausgabe über format:")
print(visitenkarte.format(vorname, nachname, 
                          strasse, ort, telenr))

#oder über eine Tabelle:
print("\nUnd das die Ausgabe über eine Tabelle:")
print(f"{"Name:":10s} {vorname} {nachname}\n\
{"Straße:":10s} {strasse}\n\
{"Ort:":10s} {ort}\n\
{"Telefon:":10s} {telenr} ")


'''Zweite Möglichkeit: benutze Funktion split(",")
Das ist für unseren Zweck zwar sehr einfach, 
aber wir hatten noch keine 
Listen :)'''

assertion_nachricht = "Du hast nicht genügend Daten eingegeben"
ergebnis_liste_mit_eingaben = eingabe_daten.split(",")
print(ergebnis_liste_mit_eingaben)
#damit kann ich auch sicherstelen, dass genug Eingabenwerte da sind
assert len(ergebnis_liste_mit_eingaben) == 5, assertion_nachricht
vorname = ergebnis_liste_mit_eingaben[0]
nachname = ergebnis_liste_mit_eingaben[1]
strasse = ergebnis_liste_mit_eingaben[2]
ort = ergebnis_liste_mit_eingaben[3]
telenr = ergebnis_liste_mit_eingaben[4]

print("\nÜber das split():")
print(visitenkarte.format(vorname, nachname, strasse, ort, telenr))

print("\nÜber den Einzeiler:")
daten = eingabe_daten.split(",")
print(f"{"Name:":10s} {daten[0]} {daten[1]}\n\
{"Straße:":10s} {daten[2].strip()}\n\
{"Ort:":10s} {daten[3].strip()}\n\
{"Telefon:":10s} {daten[4].strip()} ")
