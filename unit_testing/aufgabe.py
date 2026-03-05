
def maximum_von_zwei_zahlen(zahl1, zahl2):
    if not isinstance(zahl1, int) or not isinstance(zahl2, int):
        raise TypeError("Alle Werte müssen vom Datentyp int sein")
    return max(zahl1, zahl2)


