import yaml

datei_name = "./yaml/data/config.yaml"

try:
    with open(datei_name, "r", encoding="utf-8") as datei:
        config = yaml.safe_load(datei)
except (FileNotFoundError, yaml.YAMLError, Exception) as ex:
    print("Dateifehler", ex)

# Serverdaten
print("Server:")
print("Hostname:", config["server"]["hostname"])
print("IP:", config["server"]["ip"])
print("Umgebung:", config["server"]["environment"])
print("-" * 10)

# Services
print("Services:")
for service in config["services"]:
    if service["enabled"]:
        print(f"Starte Service: {service['name']} auf Port {service['port']}")
    else:
        print(f"Service deaktiviert: {service['name']}")

print("-" * 10)

# Benutzer
print("Benutzer:")
for user in config["users"]:
    print(f"Benutzer anlegen: {user['name']} ({user['role']})")
