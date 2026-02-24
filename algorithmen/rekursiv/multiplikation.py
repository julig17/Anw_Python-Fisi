#Multiplikation ganzer zahl x und y ist x maliges Addieren der Zahl y 
#rekursiv

def multiplikation(x,y):
    if x == 0:
        return 0
    else:
        return y + multiplikation(x-1, y)

print(multiplikation(3,5))