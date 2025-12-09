jahr = int(input("Gib ein Jahr ein: "))
schaltjahr = False
if (jahr % 4 == 0):
    schaltjahr = True
    if((jahr % 100 == 0) and (jahr % 400 != 0)):
        schaltjahr = False

print(f"Schaltjahr:  {"ja" if schaltjahr else "Nein"}")