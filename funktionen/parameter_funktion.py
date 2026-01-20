'''Übergeben von Parametern an Funktionen per Call by Value'''
def person_daten(alter, nachname):
    print("Wert in Funktion:", id(alter), alter)
    print("Wert in Funktion:", id(nachname), nachname)
    alter = 20
    nachname = "Müller"
    print("Wert in Funktion nach Änderung:", id(alter), alter)
    print("Wert in Funktion nach Änderung:", id(nachname), nachname)

#außerhalb der Funktion
mein_alter = 30
mein_nachname = "Schmidt"
print("Wert außerhalb Funktion vor Aufruf:", id(mein_alter), mein_alter)
print("Wert außerhalb Funktion vor Aufruf:", id(mein_nachname), mein_nachname)

person_daten(mein_alter, mein_nachname) 
print("Wert außerhalb Funktion nach Aufruf:", id(mein_alter), mein_alter)
print("Wert außerhalb Funktion nach Aufruf:", id(mein_nachname), mein_nachname)

       