#Fakultät ist : 5! = 5 · 4 · 3 · 2 · 1


def fakultaet(n):
    if n == 1:
        return 1
    else:
        return n * fakultaet(n - 1)
    

print(fakultaet(0))