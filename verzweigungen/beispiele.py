#Verschachtelte Verzweigung
zahl = 10
if(zahl %2 == 0):
    print("Gerade")
else:
    print("Ungerade")
    if(zahl % 3 == 0):
        print(" und durch drei teilbar")
    else:
        print(" und ?")

#oder der elegantere Weg
if(zahl %2 == 0):
    print("Gerade")
elif(zahl % 3 == 0):
    print("Ungerade \n und durch drei teilbar")
else:
    print("Ungerade \n und ?")

match zahl:
    case 1|2|3|4|5:
        print("Wochentag")
    case 6|7:
        print("Wochenende!")
    case _:
        print("Kein Wochentag")

#alle Nullwerte oder leeren Objekte sind False
if(not(0 or 0.0 or "" or [] or False or None)):
    print("Alles False")