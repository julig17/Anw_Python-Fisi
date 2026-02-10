import json

DATEINAME = "./json/kundenverwaltung/data/kunden.json"

# -------------------------
# Hilfsfunktionen
# -------------------------
def lade_kunden():
    try:
        with open(DATEINAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as ex:
        print(f"Fehler bei dem Lesen der Datei: {ex}")


def speichere_kunden(kunden):
    try:
        with open(DATEINAME, "w", encoding="utf-8") as f:
            json.dump(kunden, f, indent=4)
    except Exception as ex:
        print(f"Fehler bei dem Lesen der Datei: {ex}")


# -------------------------
# API-Funktionen
# -------------------------
def create_kunde():
    name = input("Name: ").strip()
    email = input("E-Mail: ").strip()
    geburtsjahr = input("Geburtsjahr: ").strip()

    kunden = lade_kunden()

    kunde = {
        "name": name,
        "email": email,
        "geburtsjahr": geburtsjahr
    }

    kunden.append(kunde)
    speichere_kunden(kunden)

    print("Kunde wurde angelegt.")


def list_kunden():
    kunden = lade_kunden()

    if not kunden:
        print("Keine Kunden vorhanden.")
    else:
        print("\nKundenliste:")
        print("-" * 15)
        #enumerate liefert Zähler und Wert gleichzeitig
        for i, kunde in enumerate(kunden, start=1):
            print(f"{i}. {kunde['name']} | {kunde['email']} | {kunde['geburtsjahr']}")
            print("-" * 40)


def find_kunde_by_name():
    name = input("Name suchen: ").strip()
    kunden = lade_kunden()

    for kunde in kunden:
        if kunde["name"].lower() == name.lower():
            print("Kunde gefunden:")
            print(kunde)
            break


def delete_kunde():
    name = input("Name des zu löschenden Kunden: ").strip()
    kunden = lade_kunden()

    neue_kunden = []
    for kunde in kunden:
        if kunde["name"].lower() != name.lower():
            neue_kunden.append(kunde)

    if len(neue_kunden) == len(kunden):
        print("Kunde nicht gefunden.")
    else:
        speichere_kunden(neue_kunden)
        print("Kunde wurde gelöscht.")


def update_kunde():
    name = input("Name des Kunden: ").strip()
    kunden = lade_kunden()

    for kunde in kunden:
        if kunde["name"].lower() == name.lower():
            print("Neue Daten eingeben (leer lassen = unverändert)")

            neuer_name = input(f"Name [{kunde['name']}]: ").strip()
            neue_email = input(f"E-Mail [{kunde['email']}]: ").strip()
            neues_geburtsjahr = input(f"Geburtsjahr [{kunde['geburtsjahr']}]: ").strip()

            if neuer_name:
                kunde["name"] = neuer_name
            if neue_email:
                kunde["email"] = neue_email
            if neues_geburtsjahr:
                kunde["geburtsjahr"] = neues_geburtsjahr

            speichere_kunden(kunden)
            print("Kunde wurde aktualisiert.")
            return

    print("Kunde nicht gefunden.")

# -------------------------
# Test
# -------------------------
list_kunden()
create_kunde()
find_kunde_by_name()
delete_kunde()
update_kunde()
list_kunden()