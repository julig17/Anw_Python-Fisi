import json

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

print(type(konfiguration))

dateiname = "./json/konfiguration.json"

try:
  with open(dateiname, "w", encoding="UTF-8") as konfig_datei: 
      json.dump(konfiguration, konfig_datei, indent=4)
except Exception as ex:
   print(f"Zugrffsfehler beim Schreiben: {ex}")