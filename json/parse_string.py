#.loads() JSON-Zeichenfolge (JSON-String) im Python-Code  in ein Dictionary (assoziatives Array) umwandeln

import json

json_string =  '{ "name":"John", "age":30, "city":"New York"}'

# parse :
python_pbject = json.loads(json_string)

# the result is a Python dictionary:
print(python_pbject["age"])

json_string = '[1, 2, 3, "four", "five"]'
python_pbject = json.loads(json_string)
print(python_pbject)
