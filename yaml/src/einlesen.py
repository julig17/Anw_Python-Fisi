import yaml

"""
Funktion safe_load entfernt ausführbaren eingeschleusten Code
im Gegensatz zu load()
"""
datei_name = "./yaml/data/data.yaml"
try:
    with open(datei_name, 'r') as datei:
        data = yaml.safe_load(datei)
except FileNotFoundError as ex:
    print("Datei Error", ex)
#fängt Yaml spezifische Fehler ab, die beim PArsen auftreten können
except yaml.YAMLError as ex:
    print("Yaml Error", ex)
finally:
    print(data['multi_line_string'])
    print(type(data['float_scalar']))
    for key, value in data.items():
        print(f"{key} : {value}")
