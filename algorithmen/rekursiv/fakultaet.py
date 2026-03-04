#Fakultät ist : 5! = 5 · 4 · 3 · 2 · 1

def fakultaet(zahl):
    if zahl == 1:
        return 1
    else:
        return zahl * fakultaet(zahl-1)


print(fakultaet(3))