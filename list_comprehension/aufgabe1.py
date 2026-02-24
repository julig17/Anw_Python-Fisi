"""
Aufgabe1 : Bilde die Menge aller Paare bis 10 
so dass erste Zahl durch zweite ohne Rest teilbar ist und beide Zahlen nicht 
gleich sind mit Hilfe von 1) For SChleife
2) als List Comprehension und 
"""
zahlen = []
for x in range(1,11):
    for y in range(1,11):
        if( x % y == 0 and x != y):
            zahlen.append((x,y))
print(zahlen)

zahlen_lc = [(x,y) for x in range(1,11) 
             for y in range(1,11) if ( x % y == 0 and x != y)]
print(zahlen_lc)