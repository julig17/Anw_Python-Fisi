#Quadratzahlen
liste = [2,4,5,9]
quadratzahlen = []
"""
for zahl in liste:
    quadratzahlen.append(zahl**2)

print(quadratzahlen)
"""
quadratzahlen = [(zahl**2) for zahl in liste]
print(quadratzahlen)
doppelte = [(zahl*2) for zahl in liste ]
#print(type(doppelte))

#Bilde von zwei Zahlen aus dem Bereich 1...10 (incl) das karthesische Produkt
#(1,1), (1,2,) (1,3) ....

for x in range(1,11):
    for y in range(1,11):
        #print(x,y)
        pass

karthsisch_produkt = [(x, y) for x in range(1,11) for y in range(1,11)] 
#print(karthsisch_produkt)

alle_möglichen_siebener_summen = [(x, y) for x in range(1,11) for y in range(1,11) if x+y == 7]
print(alle_möglichen_siebener_summen)