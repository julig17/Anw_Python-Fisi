for zeile in range(1,4):        # äußere Schleife
    print (f"Zeile {zeile}:")
    for spalte in range(1,6): #innere SChleife
        if(spalte == 4) :
            print("  Abbruch der inneren Schleife")
            break
        print(f"  Spalte {spalte}")

    print("Weiter mit nächster Zeile\n")