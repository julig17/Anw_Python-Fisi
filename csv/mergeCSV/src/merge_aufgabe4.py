"""
Dieses Skript enthält Code aus dem Projekt 'ServerMergeBeispiel'

Originalquelle: https://github.com/YourRapiddeath/ServerMergeBeispiel/tree/master
Autor: YourRapiddeath
Änderungen: Variablennamen geändert, Funktionsablauf leicht angepasst, Kommentare,
Exceptions, Consts 
"""
import csv

#das sind die gültigen Spielerrollen  (role)
VALID_ROLES = {"warrior", "mage", "healer", "archer", "tank", "assassin"}

DATA_NAME_SERVER_A = "./csv/mergeCSV/data/serverA.csv"
DATA_NAME_SERVER_B = "./csv/mergeCSV/data/serverB.csv"

DATA_NAME_SERVER_A_CLEAN = "./csv/mergeCSV/data/merged/serverA_clean.csv"
DATA_NAME_SERVER_B_CLEAN = "./csv/mergeCSV/data/merged/serverB_clean.csv"
DATA_NAME_MERGED = "./csv/mergeCSV/data/merged/merged_clean.csv"

DATA_NAME_ERROR_A = "./csv/mergeCSV/data/log/serverA.txt"
DATA_NAME_ERROR_B = "./csv/mergeCSV/data/log/serverB.txt"
DATA_NAME_CONFLICTS = "./csv/mergeCSV/data/log/conflicts.txt"

COLUMN_NAME = ["playername", "role"]


"""
Diese Funktion liest eine csv Datei ein, speichert die spielenamen und spielerrollen
in einem Dictionory, wenn die Daten ok sind. Die fehlerhaften Datensätze sind nicht 
enthaltem, stattdessen werden diese in einer Log Datei geführt mit Angabe der Zeile und 
Fehlerfall. 
"""
def read_csv(path):
    roles = {}
    errors = []
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            #das machen wir so damit wir die Zeilennummer des evtl. fehlerhaften 
            #Datensatzes haben
            for line_no, row in enumerate(reader, start=2): # ACHTUNG: Header ist Zeile 1
                #bereingen des Spielernamen und Spielerrolle
                player = (row.get("playername") or "").strip().lower()
                role = (row.get("role") or "").strip().lower()
                #Bedingung Spielername ist leere ZEichenkette - also in Fehlerliste
                if player == "":
                    errors.append(f"{path}: Zeile {line_no}: Spielername fehlt")
                    continue
                #Bedingung Spielerrolle ist leere ZEichenkette - also in Fehlerliste
                if role == "":
                    errors.append(f"{path}: Zeile {line_no}: Rolle fehlt für {player}")
                    continue
                #Bedingung Spielerrolle ist nicht gültig - also in Fehlerliste
                if role not in VALID_ROLES:
                    errors.append(f"{path}: Zeile {line_no}: Ungültige Rolle '{role}' für {player}")
                    continue
                #Bedingung Spielername ist bereits im Dictionary, die gespeicherte
                #Rolle wird nicht überschrieben - also in Fehlerliste
                if player in roles and roles[player] != role:
                    errors.append(
                        f"{path}: Zeile {line_no}: Konflikt für {player} "
                        f"(alt: {roles[player]}, neu: {role}), alte Rolle bleibt"
                    )
                    continue
                #Alle Bedingunggen erfüllt, also in Dictionary
                roles[player] = role
    except FileNotFoundError:
        print("Datei nicht gefunden")
    except Exception as e:
        print("sonstiges Dateizugriffsfehler", e)
    #Rückgabe zweier Werte intern als Tupel, werden dann entpackt
    return roles, errors

"""
Diese Funktion merged zwei Dictionaries, indem der Dict a als
Basis genommen wird und um Datensätze aus dict 2 erweitert wird,
falls nicht bereits enthalten
"""
def merge(a, b):
    # der MErge dictionary wird mit den Daten aus Dict a initialisiert
    merged = dict(a)
    conflicts = []
    for player, role_b in b.items():
        #Spieler ist bereits in dem Dict enthalten
        if player in merged:
            #Konflikt, da Spieler in Dict unterschiedliche Roll hat
            if merged[player] != role_b:
                conflicts.append(
                    f"Konflikt: {player} -> serverA={merged[player]} vs serverB={role_b}"
                )
        else:
            #Spieler ist nicht drin, deshalb wird er in den gemergden gespeichrt
            merged[player] = role_b
    return merged, conflicts

"""
Diese Funktion schreibt die Daten aus den Dictionaries in 
eine Datei rein
"""
def write_csv(path, roles):
    try:
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(COLUMN_NAME)
            #die Daten werden nach Spielername sortiert
            for player in sorted(roles):
                writer.writerow([player, roles[player]])
    except FileNotFoundError:
        print("Datei nicht gefunden: ", path)
    except Exception as e:
        print("sonstiges Dateizugriffsfehler", e)
    else:
        print("Geschrieben:", path)

def print_evaluation(roles_a, roles_b, merged):
    #nur in a
    only_a = set(roles_a) - set(roles_b)
    #nur in b
    only_b = set(roles_b) - set(roles_a)
    #sowohl als auch
    both = set(roles_a) & set(roles_b)
    #alle 
    union = set(roles_a) | set(roles_b)
    gesamt = len(roles_a) + len(roles_b)
    #entweder oder
    only_one_server = set(roles_a) ^ set(roles_b)

    print("=== Gesamtübersicht ===")
    print(f"Gesamteinträge (mit Duplikaten): {gesamt}")
    print(f"Gesamteinträge (ohne Duplikate): {len(union)}")
    print(f"Nur auf einem Server vorhanden: {len(only_one_server)}")

    print("\n=== Serververteilung ===")
    print(f"Server A Spieler: {len(roles_a)}")
    print(f"Server B Spieler: {len(roles_b)}")

    print("\n=== Nach Merge ===")
    print(f"Gesamt nach Merge: {len(merged)}")
    print(
        f"Spieler nur auf einem Server: {len(only_one_server)} | "
        f"Nur A: {len(only_a)} | "
        f"Nur B: {len(only_b)} | "
        f"Beide: {len(both)}"
    )

"""
Zeile für Zeile in error_log schreiben
"""
def write_error_log(errors, path):
    try:
        with open(path, "w", encoding="utf-8") as file:
            for row in errors:
                file.write(f"{row}\n")
    except FileNotFoundError as ex:
        print(f"Datei nicht gefunden: {ex}")
    except:
        print("sonstige Dateifehler")

#einlesen der serverA Datei und bereinigt in einem Dictionary speichern
#die Fehler sind in errors_a in Liste gespeichert
#Rückgabe als entpackter tupel
roles_a, errors_a = read_csv(DATA_NAME_SERVER_A)
roles_b, errors_b = read_csv(DATA_NAME_SERVER_B)

#Aufgabe 2, gemergte Dictionaries mit Fehlerliste
merged, conflicts = merge(roles_a, roles_b)

#Aufgabe 3, in Datei schreiben
write_csv(DATA_NAME_SERVER_A_CLEAN, roles_a)
write_csv(DATA_NAME_SERVER_B_CLEAN, roles_b)
write_csv(DATA_NAME_MERGED, merged)

#Aufgabe 4
print_evaluation(roles_a, roles_b, merged)

#Aufgabe5
write_error_log(errors_a, DATA_NAME_ERROR_A)
write_error_log(errors_b, DATA_NAME_ERROR_B)
write_error_log(conflicts, DATA_NAME_CONFLICTS)


