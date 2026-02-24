#Multiplikation ganzer zahl x und y ist x maliges Addieren der Zahl y 
#iterativ mit while schleife

def multiplikation(x, y):
    ergebnis = 0
    start = 0
    while x > start:
        ergebnis += y
        start += 1
    return ergebnis

print(multiplikation(0,20))