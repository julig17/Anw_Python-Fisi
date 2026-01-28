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