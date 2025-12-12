# einmal eins mit kopfgesteuerter Schleife
faktor = 9
zaehler = 0
while (zaehler <= 10):
    print(f"{zaehler} * {faktor} = {zaehler*faktor}")
    zaehler += 1

# einmal eins mit zählergesteuerter Schleife
for i in range(0,11):
    print(f"{i} * {faktor} = {i*faktor}")


# einmal eins mit fussgesteuerter Schleife
zaehler = 0
while True:
    print(f"{zaehler} * {faktor} = {zaehler*faktor}")
    zaehler += 1
    if not (zaehler <= 10):
        break
