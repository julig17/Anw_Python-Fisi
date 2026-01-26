menge1 = {1, 2, 3, 4, 5}
menge2 = {4, 5}
print(f"1 in Menge {menge1=}: {1 in menge1}")
print(f"1 nicht in Menge {menge1=}: {1 not in menge1}")
print(f"{menge2=} Teilmenge von {menge1=}: {menge2 <= menge1}")
print(f"{menge2=} Teilmenge von {menge1=}: {menge2.issubset(menge1)}")
print(f"{menge1=} Obermenge von {menge2=}: {menge1 >= menge2}")
print(f"Vereinigungsmenge von {menge1=} und {menge2=} ist {menge1 | menge2}")
print(f"Schnittmenge von {menge1=} und {menge2=} ist {menge1 & menge2}")
print(f"Differenzmenge von {menge1=} und {menge2=} ist {menge1 - menge2}")