#anlegen eines leeren Dictionaries
leeres_dict = {}
#print(type(leeres_dict))

#anlegen eines Dictionaries mit Werten
noten_dict = {"Mathematik": 1, "Deutsch": 2, "Englisch": 3, "Mathematik":4}
#print(noten_dict)




valides_dict = {42 : "Antwort", (1,2) : {"zweites Dict" : "Inneres Dict"}, 3.14 : "Pi"}
#print(valides_dict)


#Dict mit unterschiedlichen Datentypen
personen_dict = {"Name": "Max Mustermann",
                   1: 21,
                   "Student": True,
                   "Noten": [1, 2, 3]}
print(personen_dict)
print(personen_dict["Student"])
for key in personen_dict:
    print(key,":", personen_dict[key])






