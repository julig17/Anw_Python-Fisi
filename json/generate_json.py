import json
# Daten vorbereiten (Liste von Dictionaries)
konfiguration = {
  "server": {
    "hostname": "fileserver01",
    "ip": "192.168.1.10",
    "port": 22
  },
  "paths": {
    "log_dir": "/var/log/myapp",
    "backup_dir": "/backup/myapp"
  },
  "logging": {
    "level": "INFO",
    "file": "app.log"
  },
  "features": {
    "debug": False,
    "auto_backup": True
  }
}
# json-Datei schreiben
dateiname = "./json/konfig_neu.json"
try:
    with open(file=dateiname, mode="w", encoding="UTF-8") as konfigdatei:
        json.dump(konfiguration, konfigdatei, indent=4)
except Exception as e:
    print(f"Zugriffsfehler auf die json-Datei: {e}")