"""Füge zwei vorher festgelegte Tupel zu einer zusammen und gib diese aus:

Beispiel: (2,6,9) zusammengefügt mit (1,4,6) ergibt (2,6,9,1,4,6)
Gib vom Tupel das 2 bis 4 Element aus.
Was passiert wenn du versuchst ein Element mit einem Index auszugeben, das über die Anzahl der Elemente im Tupel hinausgeht?
Prüfe mit Operator in / not in ob Elemente im Tupel drin sind, oder nicht
Lösche das letzte Element aus dem Tupel."""

tupel_1 = (2,6,9)
tupel_2 = (1,4,6)  
tupel_3 = tupel_1 + tupel_2
print(tupel_3)
print(tupel_3[1:4])
try:
    print(tupel_3[10]) # IndexError: Hier gibt es keinen Index 10
except IndexError as e:
    print("Fehler:", e)
print(2 in tupel_3)
print(10 not in tupel_3)
try:    
    del tupel_3[-1]  # TypeError: 'tuple' object doesn't support item deletion
except TypeError as e:
    print("Fehler:", e)



#Element aus Tupel löschen
#t1.pop()
#del t1[-1]
#nicht möglich, da Tupel als unveränderbar definiert ist!

#aber Tupel kann ohne letztes Element dargestellt werden, 
# indem das Element ausgeschnitten wird und ein neues Tupel erstellt wird
#Aber Achtung, in dem neuen Tupel ist das letzte Element nicht mehr enthalten
#im alten Tupel bleibt es aber erhalten
t1 = (1,2,3,4,5)
t1_new = t1[:-1]
print(t1_new)
print(t1)
 