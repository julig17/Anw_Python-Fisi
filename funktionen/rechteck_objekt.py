class Rechteck:
    def __init__(self, laenge, breite):
        self.laenge = laenge
        self.breite = breite

    def flaeche(self):
        return self.laenge * self.breite

    def umfang(self):
        return 2 * (self.laenge + self.breite)

# Beispiel für die Verwendung der Rechteck-Klasse
r1 = Rechteck(5, 3)

print("Länge:", r1.laenge)
print("Breite:", r1.breite)
print("Fläche:", r1.flaeche())
print("Umfang:", r1.umfang())

r2 = Rechteck(7, 5)

print("Länge:", r2.laenge)
print("Breite:", r2.breite)
print("Fläche:", r2.flaeche())
print("Umfang:", r2.umfang())

