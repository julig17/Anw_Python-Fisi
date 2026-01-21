#Schreibe eine Funktion, die eine Liste von Zahlen als 
#Parameter erhält und die größte und kleinste Zahl
#als Tupel(größte, kleinste) zurückgibt.  

def groesste_kleinste_zahl(zahlen_liste):
    groesste = max(zahlen_liste)
    kleinste = min(zahlen_liste)
    return (groesste, kleinste) 

#Beispielaufruf
zahlen = [34, 12, 5, 67, 23, 89, 1]
ergebnis = groesste_kleinste_zahl(zahlen)   
print("Größte Zahl:", ergebnis[0])
print("Kleinste Zahl:", ergebnis[1])

#Alternativ mit Entpacken des Tupels
groesste, kleinste = groesste_kleinste_zahl(zahlen) 
print("Größte Zahl:", groesste)
print("Kleinste Zahl:", kleinste)
