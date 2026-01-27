def erhoehe_zahl(zahl):
    """Erhöht die übergebene Zahl um 1 und gibt sie zurück."""
    return zahl + 1


meine_zahl = 10
print("Vor dem Funktionsaufruf:", meine_zahl)   
zahl = erhoehe_zahl(meine_zahl)
print("Nach dem Funktionsaufruf:", zahl)
print("Originalwert bleibt unverändert:", meine_zahl)  


def erhoehe_liste(zahlen_liste):
    """Fügt der übergebenen Liste eine Zahl hinzu."""
    zahlen_liste.append(99)
    return zahlen_liste 

meine_liste = [1, 2, 3]
print("Vor dem Funktionsaufruf:", meine_liste)
erweiterte_liste = erhoehe_liste(meine_liste[:])
print("Nach dem Funktionsaufruf:", erweiterte_liste)    
print("Originalwert wurde verändert:", meine_liste)
