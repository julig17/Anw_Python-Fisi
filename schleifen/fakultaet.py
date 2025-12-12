import math

fakultaet = int(input("Gib eine Zahl ein: "))
zaehler = 1
ergebnis = 1
while (zaehler <= fakultaet):
    ergebnis = ergebnis * zaehler
    zaehler += 1

print(f"{fakultaet}! ist : {ergebnis}")

print(f"Unser Ergebnis: {ergebnis} == Math.Functions: {math.factorial(fakultaet)}")