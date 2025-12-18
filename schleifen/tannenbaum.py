hoehe = int(input("Wie groß soll der Baum sein?"))

print("Frohe Weihnachten")

for i in range(1, hoehe+1):
    sterne = "*" * (2*i -1)
    leerzeichen = " " * (hoehe - i)
    print(leerzeichen+sterne)

print(" " * (hoehe -2) + "||")