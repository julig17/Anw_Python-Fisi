quadratzahlen = []
for i in range(1,10):
    quadratzahlen.append(i**2)
print(quadratzahlen)

#das gleiche als List-Comprehension
print([i**2 for i in range(1,10)])

#doppelte
print([i+i for i in range(1,10)])

#zwei for schleifen
print([(x,y) for x in range(1,10) for y in range(1,10)])

#nur Tupel bilden, wenn Summe == 7
print([(x,y) for x in range(1,10) for y in range(1,10) if x+y==7])

#fahrenheit
celsius = [31.8, 32.8, 37.2]
fahrenheit = [(float(9)/5 * grad + 32) for grad in celsius]
print(fahrenheit)