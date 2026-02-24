#Schreibe eine Funktion, die die Vielfachen von 3 berechnet, rekursiv.

ZAHL = 3

def mult(n):
    if n == 1:
        return ZAHL
    else:
        return mult(n -1) + ZAHL
    
print(mult(9))
