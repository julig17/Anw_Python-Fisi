f_zahl_1 = float(input("Gib eine Kommazahl ein: "))
f_zahl_2 = float(input("Gib noch eine Kommazahl ein: "))
f_zahl_3 = float(input("Gib noch eine Kommazahl ein: "))

minimum = f_zahl_1
if f_zahl_2 < minimum:
    minimum = f_zahl_2
if f_zahl_3 < minimum:
    minimum = f_zahl_3

maximum = f_zahl_1
if f_zahl_2 > maximum:
    maximum = f_zahl_2
if f_zahl_3 > maximum:
    maximum = f_zahl_3

print(f"MINIMUM: {minimum}, MAXIMUM: {maximum}")