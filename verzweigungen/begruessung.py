name = input("Gib einen Namen ein: ")
geschlecht = input("Gib ein Gechlecht ein m/w/ : ")
uhrzeit = int(input("Gib eine Uhrzeit ein 0-24: "))

uhrzeit_begruessung = "Guten Morgen"
geschlecht_text = " "
if(uhrzeit >= 10 and uhrzeit <= 17):
    uhrzeit_begruessung = "Guten Tag"
elif(uhrzeit >= 18 and uhrzeit <= 24):
    uhrzeit_begruessung = "Guten Abend"
else:
    pass

if(geschlecht == "m"):
    geschlecht_text = "Herr"
elif(geschlecht == "w"):
    geschlecht_text = "Frau"
else:
    pass

print(f"{uhrzeit_begruessung} {geschlecht_text} {name}")

