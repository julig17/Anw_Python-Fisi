# Einfaches Tic-Tac-Toe für Anfänger

# Spielfeld als Liste
spielfeld = [" "] * 9

spieler = "X"
zuege = 0

print("Tic-Tac-Toe")

 # Spielfeld anzeigen
print()
print(spielfeld[0], "|", spielfeld[1], "|", spielfeld[2])
print("--+---+--")
print(spielfeld[3], "|", spielfeld[4], "|", spielfeld[5])
print("--+---+--")
print(spielfeld[6], "|", spielfeld[7], "|", spielfeld[8])
print()

while True:
   
    #Eingabe die Position entspricht dem Spielfeld-Listen Index, deshalb -1
    position = int(input(f"Spieler {spieler}, Gib Position 1-9 ein: ")) - 1

    if position < 0 or position > 8:
        print("Ungültige Position!")
        continue

    if spielfeld[position] != " ":
        print("Feld schon belegt!")
        continue

    #auf dem Spielfeld den Zug setzten
    spielfeld[position] = spieler
    #spielzug erhoehen, war gueltig
    zuege += 1

     # Spielfeld anzeigen
    print()
    print(spielfeld[0], "|", spielfeld[1], "|", spielfeld[2])
    print("--+---+--")
    print(spielfeld[3], "|", spielfeld[4], "|", spielfeld[5])
    print("--+---+--")
    print(spielfeld[6], "|", spielfeld[7], "|", spielfeld[8])
    print()

    # Gewinn prüfen
    if (
        (spielfeld[0] == spielfeld[1] == spielfeld[2] == spieler) or
        (spielfeld[3] == spielfeld[4] == spielfeld[5] == spieler) or
        (spielfeld[6] == spielfeld[7] == spielfeld[8] == spieler) or
        (spielfeld[0] == spielfeld[3] == spielfeld[6] == spieler) or
        (spielfeld[1] == spielfeld[4] == spielfeld[7] == spieler) or
        (spielfeld[2] == spielfeld[5] == spielfeld[8] == spieler) or
        (spielfeld[0] == spielfeld[4] == spielfeld[8] == spieler) or
        (spielfeld[2] == spielfeld[4] == spielfeld[6] == spieler)
    ):
        print("Spieler", spieler, "hat gewonnen!")
        break

    if zuege == 9:
        print("Unentschieden")
        break

    #spieler wechseln
    if spieler == "X":
        spieler = "O"
    else:
        spieler = "X"

