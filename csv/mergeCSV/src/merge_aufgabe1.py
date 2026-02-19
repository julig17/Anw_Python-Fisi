"""
Dieses Skript enthält Code aus dem Projekt 'ServerMergeBeispiel'

Originalquelle: https://github.com/YourRapiddeath/ServerMergeBeispiel/tree/master
Autor: YourRapiddeath
Änderungen: Variablennamen geändert, Funktionsablauf leicht angepasst 
"""
import csv

#das sind die gültigen Spielerrollen  (role)
VALID_ROLES = {"warrior", "mage", "healer", "archer", "tank", "assassin"}

DATA_NAME_SERVER_A = "./csv/mergeCSV/data/serverA.csv"
DATA_NAME_SERVER_B = "./csv/mergeCSV/data/serverB.csv"

DATA_NAME_SERVER_A_CLEAN = "./csv/mergeCSV/data/merged/serverA_clean.csv"
DATA_NAME_SERVER_B_CLEAN = "./csv/mergeCSV/data/merged/serverB_clean.csv"
DATA_NAME_MERGED = "./csv/mergeCSV/data/merged/merged_clean.csv"


"""
Diese Funktion liest eine csv Datei ein, speichert die spielenamen und spielerrollen
in einem Dictionory, wenn die Daten ok sind. Die fehlerhaften Datensätze sind nicht 
enthaltem, stattdessen werden diese in einer Log Datei geführt mit Angabe der Zeile und 
Fehlerfall. 
"""
def read_csv(path):
    roles = {}
    errors = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        #das machen wir so damit wir die Zeilennummer des evtl. fehlerhaften 
        #Datensatzes haben
        for line_no, row in enumerate(reader, start=2): # ACHTUNG: Header ist Zeile 1
            #bereingen des Spielernamen und Spielerrolle
            player = (row.get("playername") or "").strip().lower()
            role = (row.get("role") or "").strip().lower()
            #Bedingung Spielername ist leere Zeichenkette - also in Fehlerliste
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
    #Rückgabe zweier Werte intern als Tupel, werden dann entpackt
    return roles, errors


#einlesen der serverA Datei und bereinigt in einem Dictionary speichern
#die Fehler sind in errors_a in Liste gespeichert
#Rückgabe als entpackter tupel
roles_a, errors_a = read_csv(DATA_NAME_SERVER_A)
roles_b, errors_b = read_csv(DATA_NAME_SERVER_B)

