import json

dateiname = "./json/konfig.json"

try :
    with open(dateiname, "r", encoding="UTF-8") as konfig_datei:
        konfiguration = json.load(konfig_datei)
        print(konfiguration)
        print(type(konfiguration))
except FileNotFoundError as e:
    print("Datei nicht gefunfen", e)
except Exception as e:
    print("Sonstiger Fehler", e)

#{'hostname': 'fileserver01', 'ip': '192.168.1.10', 'port': 22}
ip_adresse = konfiguration["ip"]
hostname = konfiguration["hostname"]
print(ip_adresse)
print(hostname)

for schluessel, wert in konfiguration.items():
    print(f"{schluessel} : {wert}")
