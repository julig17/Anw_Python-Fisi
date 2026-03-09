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
beispiel_datei = os.path.join(test_verzeichnis, "beispiel.py")
print("Erstellen eines neuen Verzeichnisses namens 'testverzeichnis'")
try:
    os.mkdir(test_verzeichnis)
    print("Verzeichnis 'testverzeichnis' erstellt")
except FileExistsError:
    print("Verzeichnis 'testverzeichnis' existiert bereits")

os.chdir(test_verzeichnis)
with open(beispiel_datei, "w", encoding="utf-8") as f:
    f.write("print('So kann man Code einschleusen....')")

print(os.getcwd())
print(os.path.isfile(beispiel_datei))
print(os.path.isdir(test_verzeichnis))

#Ausführen von harmlosen Code aus einer Datei
#achtung kann schadhafter Code enthalten sein
os.system(f"python {beispiel_datei}")