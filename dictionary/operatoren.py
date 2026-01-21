#Operator zum Zusammenführen von Dictionaries
dict1 = {"a": 1, "b": 2}
print(dict1["a"])
print(len(dict1))
print("b" in dict1)  
print("c" not in dict1)  
dict2 = {"c": 3, "d": 4}
kombiniertes_dict = dict1 | dict2
print(kombiniertes_dict)
del kombiniertes_dict["a"]
print(kombiniertes_dict)


ports = [22, 80, 443]
dienste = ["SSH", "HTTP", "HTTPS"]

port_dienst = dict(zip(ports, dienste))
print(port_dienst)