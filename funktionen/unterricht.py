'''Im Unterricht behandelter Stoff'''

'''Funktion berechnen Quadrat einer Zahl
und liefert das Quadrat zurück'''
def quadrat_berechnen(zahl):
    return zahl * zahl 

'''Aufruf der Funktion und Ausgabe des Ergebnisses
in Variable quadrat_zahl wird der Rückgabewert gespeichert'''
quadrat_zahl = quadrat_berechnen(5)
print(quadrat_zahl)  

#mehrere Parameter mit Komma trennen
def cpu_last_berechnen(last1, last2):
    return (last1 + last2) / 2

ergebnis = cpu_last_berechnen(40, 60)
print(ergebnis)

#achten auf die Reihenfolge der Parameter
def subtrahiere_zahlen(minuend, subtrahend):
    return minuend - subtrahend
zahl1 = 50
zahl2 = 20
ergebnis = subtrahiere_zahlen(zahl1, zahl2)
ergebnis_falsch = subtrahiere_zahlen(zahl2, zahl1)  
print(ergebnis)
print(ergebnis_falsch)


#schlüsselwort-Parameter
def gruss(name, anrede="Hallo"):
    print(f"{anrede}, {name}!")

# Aufruf mit Positionsargumenten
gruss("Welt") # Ausgabe: Hallo, Welt!

# Aufruf mit Schlüsselwortargumenten (Reihenfolge egal)
gruss(name="Python", anrede="Servus") # Ausgabe: Servus, Python!
gruss(anrede="Servus", name="Python") # Ausgabe: Servus, Python!

# Aufruf mit Keyword-Only Argument
# Keyword-Only-Argumente: Mit einem Sternchen (*) werden Argumente markiert, 
# die nur als Schlüsselwort übergeben werden dürfen
def print_user(user_id, *, verbose=False):
    if verbose:
        print(f"Verbose: User-ID ist {user_id}")
    else:
        print(f"User-ID: {user_id}")

print_user(123, verbose=True) # Funktioniert
print_user(456) # Funktioniert auch
try:
    print_user(123, True) # Fehler: True ist kein Schlüsselwort 
except TypeError as e:
    print("Fehler beim Aufruf von print_user:", e)

'''Rückgabe von Werten aus einer Funktion'''
def subtrahiere(zahl1, zahl2):
    differenz = zahl1 - zahl2
    if differenz < 0:
        differenz = 0
    return differenz
ergebnis = subtrahiere(10, 20)
print(ergebnis)  # Ausgabe: 0
ergebnis = subtrahiere(30, 15)
print(ergebnis)  # Ausgabe: 15

'''Rückgabe mehrerer Werte aus einer Funktion'''

def multipliziere_und_dividiere(zahl1, zahl2):
    return zahl1 * zahl2, zahl1 / zahl2

# Aufruf der Funktion und Speicherung der Ergebnisse
ergebnis_multiplikation, ergebnis_division = multipliziere_und_dividiere(10, 5)
print("Multiplikation:", ergebnis_multiplikation)
print("Division:", ergebnis_division)


def fkt(x, y, z):
    print("\tWerte bei Funktionsbeginn ",x, y, z)
    x = x * 2
    y = y + 100
    z = z / 5
    print("\tWerte bei Funktionsende ",x, y, z)
    return x, y, z

a = 10
b = 20
c = 30
print("Werte vor Funktionsaufruf ",a, b, c)
# Rückgabewerte einzeln
a, b, c = fkt(a, b, c)
print("Werte nach Funktionsaufruf",a, b, c)
print("Werte vor Funktionsaufruf ",a, b, c)
# Rückgabewerte als Tupel
rueckgabe_tupel = fkt(a, b, c)
print("Werte nach Funktionsaufruf", rueckgabe_tupel)

#Beispiel für Prozedur
def drucke_begruessung(name):
    print(f"Willkommen, {name}!")

drucke_begruessung("Anna")
drucke_begruessung("Ben")
rückgabe = drucke_begruessung("Clara")  # Rückgabewert ist None
print(rückgabe)