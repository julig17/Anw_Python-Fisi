import yaml

datei_name = "./yaml/data/config.yaml"

try:
    with open(datei_name, "r", encoding="utf-8") as datei:
        config = yaml.safe_load(datei)
except (FileNotFoundError, yaml.YAMLError, Exception) as ex:
    print("Dateifehler", ex)

# Serverdaten
"""print("Server:")
print("Hostname:", config["server"]["hostname"])
print("IP:", config["server"]["ip"])
print("Umgebung:", config["server"]["environment"])
print("-" * 10)"""

print("Services")
"""
for service in config["services"]:
        print(f"{service["name"]}, {service["port"]}")
        if(service["enabled"]):
             print(f"Starte Service  {service["name"]} auf {service["port"]} ")
"""
print("-" * 10)
print("Benutzer")

def lege_benutzer_an(benutzer):
    #legt die BEnutzer in DB an
    #....
    print(f"Der Benutzer wurde angelegt mit Name {benutzer["name"]} und Rolle {benutzer["role"]} ")

for benutzer in config["users"]:
    lege_benutzer_an(benutzer)
    