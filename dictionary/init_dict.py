#Anlegen eines deutsch englisch Wörterbuchs über input in while Schleife
woerterbuch = {}
while True:
    deutsch = input("Geben Sie ein deutsches Wort ein (oder 'ende' zum Beenden): ")
    if deutsch.lower() == 'ende':
        break
    englisch = input("Geben Sie die englische Übersetzung ein: ")
    woerterbuch[deutsch] = englisch 
for wort in woerterbuch:
    print(f"{wort} -> {woerterbuch[wort]}")
