import json

# Python dict to JSON string
python_obj = {'name': 'John', 'age': 30}

json_string = json.dumps(python_obj)
print(json_string)  


#mit Einrückung
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_data = json.dumps(data, indent=2)

print(json_data)