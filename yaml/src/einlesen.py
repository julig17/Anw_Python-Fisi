import yaml

datei_name = "./yaml/data/data.yaml"
try:
    with open(datei_name, 'r') as datei:
        data = yaml.safe_load(datei)
except FileNotFoundError as ex:
    print("Datei Error", ex)
except yaml.YAMLError as ex:
    print("Yaml Error", ex)
finally:
    print(data)