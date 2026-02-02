autos = {"BMW", "Mercedes", "VW", "Audi"}
auto_copy = autos.copy()
frozen = frozenset(auto_copy)
autos.add("Opel")


frozen2 = frozenset(["Tulpen", "Narzissen"])
auto = set(frozen2.copy())
print(type(auto))
print(type(frozen2))
auto.add("Opel")

                     