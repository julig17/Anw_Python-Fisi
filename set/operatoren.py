menge1 = {1, 2, 3, 4, 5}
menge2 = {4, 5}
print(f"{menge2=} Teilmenge von {menge1=}: {menge2 <= menge1}")
print(f"{menge2=} Teilmenge von {menge1=}: {menge2.issubset(menge1)}")

print(f"{menge1=} Obermenge von {menge2=}: {menge1 >= menge2}")
print(f"{menge1=} Obermenge von {menge2=}: {menge1.issuperset(menge2)}")

menge3 = {7, 8}
print(f"Vereinigungsmenge von {menge1=} und {menge3=} ist {menge1 | menge3}")
vereinigungsmenge = menge1 | menge3
print(vereinigungsmenge)
print(f"Vereinigungsmenge von {menge1=} und {menge3=} ist {menge1.union(menge3)}")

print(f"Schnittmenge von {menge1=} und {menge2=} ist {menge1 & menge2}")
print(f"Schnittmenge von {menge1=} und {menge3=} ist {menge1 & menge3}")

print(f"Differenzmenge von {menge1=} und {menge2=} ist {menge1 - menge2}")
print(f"Differenzmenge von {menge2=} und {menge1=} ist {menge2 - menge1}")