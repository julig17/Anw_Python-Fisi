"""Erstelle aus allen Zeichen(Groß, KLeinbuchstaben, Zahlen, Sonderzeichen)
ein 8 stelliges Passwort"""

import random
def generiere_passwort(laenge):
    zeichen = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    passwort_liste = random.choices(zeichen, k=laenge) 
    print(passwort_liste)
    return "".join(passwort_liste)

print("Das ist dein neues Passwort: ", generiere_passwort(8))