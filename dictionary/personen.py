"""Dictionary in Dictionary
Ein Dictionary mit den Namen als Key von 5 Personen ist zu erstellen.
Als Schlüssel  ist ein weiteres Dictionary zu erstellen mit Geburtsjahr und Geschlecht
Das Dictionary ist ohne die inneren Schlüssel auf der Konsole auszugeben
Beispiel (Max Mustermann, 1990, männlich)"""
personen = {
    "Max Mustermann": {"Geburtsjahr": 1990, "Geschlecht": "männlich"},
    "Anna Müller": {"Geburtsjahr": 1985, "Geschlecht": "weiblich"},
    "Peter Schmidt": {"Geburtsjahr": 1978, "Geschlecht": "männlich"},
    "Laura Fischer": {"Geburtsjahr": 1995, "Geschlecht": "weiblich"},
    "Tom Weber": {"Geburtsjahr": 2000, "Geschlecht": "männlich"}
}
for name in personen:
    ausgabe = ""
    for werte in personen[name].values():
        ausgabe += str(werte) +", "
    print(name,",",ausgabe)

# Alternative Ausgabe mit Formatierung
print("\nAlternative Ausgabe mit Formatierung:")    
for name, details in personen.items():
    geburtsjahr = details["Geburtsjahr"]
    geschlecht = details["Geschlecht"]
    print(f"{name}, {geburtsjahr}, {geschlecht}")