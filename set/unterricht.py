dict = {"one" : 1, "two" : 2}
leere_set = {1,2,3,5,3,4,5}
#print(dict)
print(leere_set)

try:
    gemischte_set = { 1, "Hallo", 3.14, [1,2]}
except TypeError:
    print("TypeError wegen falscher Datentypen")
except Exception as fehler:
    print("Fehler", fehler)

#print("Gemischte Set", gemischte_set)

zahlen_set = {1,2,3,4,5}
zahlen_set.add(7)
print(zahlen_set)

zahlen_frozen = frozenset([1,2,3,4,5])
#zahlen_frozen.add(8)


#print(dict["one"])
#print(zahlen_set[0])

for element in zahlen_set:
    print(element)

print(5 in zahlen_set)
print(20 in zahlen_set)
print(20 not in zahlen_set)
print(5 not in zahlen_set)
print(len(zahlen_set))

auto_set ={"BMW", "Opel"}
