liste = ["Hallo", "Welt", 123, "Python"]
try:
    for index in range(len(liste)+1):
        print(liste[index])
except IndexError:
    print("Bla")

#Attribute Error
#liste.keys()
#liste.apend()


#IndexError 
#alter = int(input("Wie alt bist du??? "))
alter = 2
altersgruppen = ["Kind", "Jugendlich", "Erwachsen"]

print(altersgruppen[alter])

if alter > 18:
    print("Du bisst minderjährig")
else:
    print("Du bist volljährig")

#KexError
try:
    dict = {"Name": "Apfel", "Farbe": "Rot"}
    print(dict["Preis"])
except KeyError:
    print("Dieser Schlüssel existiert nicht")
except:
    print("Irendwas anderes ist schief gelaufen")
 
# Richtig
try:
    dict = {"Name": "Apfel", "Farbe": "Rot"}
    print(dict["Name"])
except KeyError:
    print("Dieser Schlüssel existiert nicht")
except:
    print("Irendwas anderes ist schief gelaufen")

#ValueError
#print(int("Hallo"))

#TypeError
#print("2" + 3)
#kein TypeError
print("2" * 3)

print(dateiname)

#print(x)
# NameError: name 'x' is not defined

#"5" + 3
#TypeError: can only concatenate str (not "int") to str

#int("abc")
#ValueError: invalid literal for int() with base 10: 'abc'

#liste = [1, 2, 3]
#print(liste[5])
#IndexError: list index out of range

#data = {"name": "Max"}
#print(data["alter"])
#KeyError: 'alter'

#10 / 0
#ZeroDivisionError: division by zero

#open("nicht_da.txt", "r")
#FileNotFoundError: [Errno 2] No such file or directory: 'nicht_da.txt' 