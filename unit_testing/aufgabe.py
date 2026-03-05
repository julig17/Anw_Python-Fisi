
def maximum_von_zwei_zahlen(zahl1, zahl2):
    if not isinstance(zahl1, int) or not isinstance(zahl2, int):
        raise TypeError("Alle Werte müssen vom Datentyp int sein")
    return max(zahl1, zahl2)


def versandkosten(gewicht):
    if gewicht < 0:
        raise ValueError("Gewicht darf nicht negativ sein")

    if gewicht < 1:
        return 2.99
    elif gewicht < 5:
        return 4.99
    else:
        return 7.99


