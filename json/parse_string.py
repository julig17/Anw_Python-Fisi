#.loads() JSON-Zeichenfolge (JSON-String) im Python-Code  in ein Dictionary (assoziatives Array) umwandeln

import json

json_string =  '{"name":"John", "age":30, "city":"New York"}'

# parse :
python_object = json.loads(json_string)
print(type(python_object))

# the result is a Python dictionary:
alter = python_object["age"]
print(type(alter))
print(python_object["age"])



json_string = '[1, 2, 3, "four", "five"]'
python_object = json.loads(json_string)
print(python_object)
print(type(python_object))
print(python_object[::-1])