while True:
    eingabe = input("Gib etwas ein, zum Abbruch gib ein exit: ")
    if (eingabe == "exit" or eingabe == "Exit"):
        print("Beendet")
        break
    print("Eingabe war", eingabe)

print("Hier wird nach break weitergemacht")

