preis = 900

if (preis > 1000.00):  
    preis = preis * (1 - 0.05)
#print("Preis:" , preis)


#Verzweigung
preis = 900.00

if (preis > 1000.00):  
    pass
else :
    preis = preis * (1 - 0.03)

#print("Preis:" , preis)


#Verchachtelte Verzweigung
zahl = 15
if (zahl % 2 == 0):
    print("Zahl ist Gerade")
else :
    print("Zahl ist ungerade")
    if(zahl %3 == 0):
        print("Zahl ist durch 3 teilbar")
    else: 
        print(" und ????")

if (zahl % 2 == 0):
    print("Zahl ist Gerade")
elif (zahl %3 == 0):
    print("Zahl ist ungerade")
    print("Zahl ist durch 3 teilbar")
else: 
    if(zahl % 5 == 0):
        print("Zahl ist ungerade")
        print(" und durch 5 teilbar")
    else:
        print(" und ????")
        print("Zahl ist ungerade")




monat = int(input("Geben einen Monat aus:"))
text = ""
match monat:
    case 1:
        text = "Januar"
    case 2:
        text = "Februar"
    case 3:
        text = "März"
    case 4:
        text = "April"
    case 5:
        text = "Mai"
    case 6:
        text = "Juni"
    case 7:
        text = "Juli"
    case 8:
        text = "August"
    case 9:
        text = "September"
    case 10:
        text = "Oktober"
    case 11:
        text = "November"
    case 12:
        text = "Dezember"
    case _: 
        text = "Undefiniert"

print(text)

name = "Hallo"
if name :
    print(name)

name = ""
if name :
    print(name)

