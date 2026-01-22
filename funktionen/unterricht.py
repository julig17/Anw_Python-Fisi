'''Im Unterricht behandelter Stoff'''

def quadrat_berechnen(zahl):
    return zahl * zahl 

'''Aufruf der Funktion und Ausgabe des Ergebnisses
in Variable quadrat_zahl wird der Rückgabewert gespeichert'''
quadrat_zahl = quadrat_berechnen(5)
print(quadrat_zahl)  

quadrat = quadrat_berechnen(5)
quadrat2 = quadrat_berechnen(10)
quadrat3 = quadrat_berechnen(15)   


def cpu_last_berechnen(last1, last2):
    return (last1 + last2) / 2

ergebnis = cpu_last_berechnen(40, 60)
print(ergebnis)

def subtrahiere_zahlen(minuend, subtrahend):
    return minuend - subtrahend

zahl1 = 50
zahl2 = 20
ergebnis = subtrahiere_zahlen(zahl1, zahl2)
ergebnis_falsch = subtrahiere_zahlen(zahl2, zahl1)  
print(ergebnis)
print(ergebnis_falsch)

#Bei Standardwerten für Parameter muss die Reihenfolge eingehalten werden
#Bei Schlüsselwortparametern kann die Reihenfolge geändert werden
def gruss(name, anrede="Hallo"):
    print(anrede, name)

gruss("Peter")
gruss("Anna", "Guten Tag")
gruss("Tschüß", "Michael")
gruss(anrede="Willkommen", name="Maria")
gruss(name="Maria", anrede="Willkommen")


def print_user(user_id, *, ausgabe=False):
    if ausgabe:
        print("User ID:", user_id)
    else:
        print("Kein Ausgabeparameter gesetzt.")
    return user_id



rueckgabe = print_user(101)
print(rueckgabe)
print_user(202, ausgabe=True)
#print_user(303, False)



def quadrat_berechnen(zahl):
    return zahl * zahl 

'''Aufruf der Funktion und Ausgabe des Ergebnisses
in Variable quadrat_zahl wird der Rückgabewert gespeichert'''
quadrat_zahl = quadrat_berechnen(5)
print(quadrat_zahl)  

def quadrat_und_umfang_berechnen(breite, laenge):
    quadrat = breite * laenge
    umfang = 2 * (breite + laenge)
    return quadrat, umfang

breite = 5
laenge = 10
quadrat, umfang = quadrat_und_umfang_berechnen(breite, laenge)
print("Quadrat:", quadrat)
print("Umfang:", umfang)