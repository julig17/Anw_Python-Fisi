#Beispielcode zum Modul os
import os

print("aktuelles Arbeitsverzeichnis anzeigen")
print(os.getcwd())

print("Gibt eine Liste mit allen Dateien und Verzeichnissen zurück:")
print(os.listdir())

print("Wechseln des aktuellen Arbeitsverzeichnisses auf os")
os.chdir("os")
print(os.getcwd())


test_verzeichnis = r"C:\Users\greif\workspace\python\Anw_Python-Fisi\os\testverzeichnis"
beispiel_datei = "beispiel.py"
verzeichnis_und_datei = os.path.join(test_verzeichnis, beispiel_datei)


print("Erstellen eines neuen Verzeichnisses namens 'testverzeichnis'")
try:
    os.mkdir(test_verzeichnis)
except FileExistsError:
    print("Verzeichnis existiert bereits")

os.chdir(test_verzeichnis)
print(os.getcwd())

with open(verzeichnis_und_datei, "w", encoding="utf-8") as f:
    f.write("print('So kann man Code einschleusen....')")

os.system(f"python {verzeichnis_und_datei}")
