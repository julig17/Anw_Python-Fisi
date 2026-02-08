try:
    zahl = int(input("Bitte Zahl eingeben: "))
    ergebnis = 10 / zahl
    print("Das wird nicht ausgeführt, wenn Fehler auftritt")
except ValueError as ex:
    print("Eingabe ist keine Zahl.", ex)
except ZeroDivisionError as ex:
    print("Division durch 0 ist nicht erlaubt.", ex)
except Exception as ex:
    print("Sonstiger fehler.", ex)
else:
    print("Ergebnis:", ergebnis)
finally:
    print("Berechnung beendet.")