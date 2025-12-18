zeichenkette = "Systemintegration"

for buchstabe in zeichenkette:
    if buchstabe.lower() == "l":
        break
    print(buchstabe)
else:
    print("Ich habe diese Zeichenkette nicht gefunden")
print("Fertig")