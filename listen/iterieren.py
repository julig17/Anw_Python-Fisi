zeichenketten = ["Das", "ist", "eine", "Liste", "mit", "Zeichenketten"]
#print(len(zeichenketten))

for index in range(len(zeichenketten)): 
    #print("Index", index, "Zeichenkette", zeichenketten[index])
    pass

eingabe = int(input("Gib einen Index ein: "))
if eingabe > len(zeichenketten):
    print("Eingabe zu groß")

else:
    i = 0
    while i <= len(zeichenketten):
        print("Index", i, "Zeichenkette", zeichenketten[i])
        i += 1