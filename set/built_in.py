autos = {"BMW", "Mercedes", "VW", "Audi"}
print(f"Autos: {autos}")
autos.add("Porsche")   
print(f"Autos nach Hinzufügen von Porsche: {autos}")
autos.remove("VW")  
print(f"Autos nach Entfernen von VW: {autos}")
try:
    autos.remove("Ferrari")
except KeyError as e:
    print("Fehler beim Entfernen von Ferrari (nicht vorhanden):", e)
autos.discard("Ferrari")  
print(f"Autos nach Discard von Ferrari (nicht vorhanden): {autos}") 
autos.pop()  
print(f"Autos nach Pop (entfernt ein beliebiges Element): {autos}") 
autos.update(["Opel", "Ford"])  
print(f"Autos nach Update mit Opel und Ford: {autos}")