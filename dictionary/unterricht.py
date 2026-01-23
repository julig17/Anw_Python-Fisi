#anlegen eines leeren Dictionaries
leeres_dict = {}
#anlegen eines Dictionaries mit Werten
noten_dict = {"Mathematik": 1, "Deutsch": 2, "Englisch": 3}
print(noten_dict)
#dictionary mit verschiedenen Datentypen
personen_dict = {"Name": "Max", "Alter": 21, "Student": True, "Noten": [1, 2, 3]}
print(personen_dict)

#SChlüssel nur aus immutablen Datentypen
valid_dict = {42: "Antwort", (1, 2): "Tupel als Schlüssel"}
print(valid_dict)
# invalid_dict = {[1, 2]: "Liste als Schlüssel"}  #Fehler

#SChlüssel müssen eindeutig sein
noten_dict = {"Mathematik": 1, "Deutsch": 2, "Englisch": 3, "Mathematik": 4}
print(noten_dict)  #Mathematik hat den Wert 4

#Zugriff über Indexes nicht möglich
try:
    print(noten_dict[0])  #Fehler
except KeyError as e:
    print("Fehler:", e)

#Zugriff auf SChlüssel, wenn es den Schlüssel nicht gibt, 
# gibt es einen Fehler
try:
    print(noten_dict["Biologie"])  #Fehler  
except KeyError as e:
    print("Fehler:", e)

#Zugriff auf Werte über Schlüssel
mathe_note = noten_dict["Mathematik"]
print("Mathe Note:", mathe_note)


#Iterieren über Dictionary, zunächst über Schlüssel
for fach in noten_dict:
    note = noten_dict[fach]
    print(fach, ":", note)

