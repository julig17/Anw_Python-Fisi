#Multiplikation ganzer zahl x und y ist x maliges Addieren der Zahl y 
#iterativ mit while schleife


def multiplikation(a, b):
    i = 0
    ergebnis = 0
    while i < b:
        i += 1
        ergebnis += a
    return ergebnis

print(multiplikation(3, 5))