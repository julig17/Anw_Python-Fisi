"""Für diese mathematischen Funktionen werden Unit Tests erstellt, 
um die Korrektheit der Funktionen zu überprüfen."""

"""Diese Funktion addiert alle int Werte einer Liste
zusammen und gibt die Summe der Werte zurück"""
def sum(values):
    if not values:
        return 0

    if not all(isinstance(value, int) for value in values):
        raise TypeError("Alle Werte müssen vom Datentyp int sein")

    result = 0
    for value in values:
        result += value
    return result

"""Diese Funktion subtrhiert wert2 von wert1 und gibt die Differenz zurück"""
def minus(value1, value2):
    if not isinstance(value1, int) or not isinstance(value2, int):
        raise TypeError("Alle Werte müssen vom Datentyp int sein")
    return value1 - value2

"""Diese Funktion multipliziert wert1 mit wert2 und gibt das Produkt zurück"""
def mal(value1, value2):
    if not isinstance(value1, int) or not isinstance(value2, int):
        raise TypeError("Alle Werte müssen vom Datentyp int sein")
    return value1 * value2

"""Diese Funktion dividiert wert1 durch wert2 und gibt den Quotienten zurück"""
def durch(value1, value2):
    if not isinstance(value1, int) or not isinstance(value2, int):
        raise TypeError("Alle Werte müssen vom Datentyp int sein")
    if value2 == 0:
        raise ValueError("Division durch Null ist nicht erlaubt")
    return value1 / value2  

"""Diese Funktion berechnet die Summe zweier int Werte und gibt die Summe zurück"""
def sum_zwei(value1, value2):
    if not isinstance(value1, int) or not isinstance(value2, int):
        raise TypeError("Alle Werte müssen vom Datentyp int sein")
    return value1 + value2
