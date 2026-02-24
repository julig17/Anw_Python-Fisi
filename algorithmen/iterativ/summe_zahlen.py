# Aufsummieren von Zahlen – iterative Lösung als Funktion

def summe(zahl):
    summe = 0
    for i in range(1, zahl + 1):
        summe += i
    return summe

print(summe(100))