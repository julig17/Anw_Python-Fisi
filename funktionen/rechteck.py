"""Lese von der Konsole die Breite und die Länge eines Rechteckes ein.
Berechne in Funktionen die Fläche und den Umfangs des Rechtecks und gebe es aus."""

def flaeche(breite, laenge):
    return breite * laenge

def umfang(breite, laenge):
    return 2 * (breite + laenge)

breite = float(input("Breite des Rechtecks: "))
laenge = float(input("Länge des Rechtecks: "))

print("Fläche:", flaeche(breite, laenge))
print("Umfang:", umfang(breite, laenge))