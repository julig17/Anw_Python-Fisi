'''Übergeben von Parametern an Funktionen per Call by Value'''
def person_daten(alter, nachname, kinder_alter):
    print("Wert in Funktion:", id(alter), alter)
    print("Wert in Funktion:", id(nachname), nachname)
    print("Wert in Funktion:", id(kinder_alter), kinder_alter)
    alter = 20
    nachname = "Müller"
    kinder_alter.append(7)
    print("Wert in Funktion nach Änderung:", id(alter), alter)
    print("Wert in Funktion nach Änderung:", id(nachname), nachname)
    print("Wert in Funktion nach Änderung:", id(kinder_alter), kinder_alter)

#außerhalb der Funktion
alter = 30
nachname = "Schmidt"
kinder_alter = [2, 5]
print("Wert außerhalb Funktion vor Aufruf:", id(alter), alter)
print("Wert außerhalb Funktion vor Aufruf:", id(nachname), nachname)
print("Wert außerhalb Funktion vor Aufruf:", id(kinder_alter), kinder_alter)


person_daten(alter, nachname, kinder_alter) 
print("Wert außerhalb Funktion nach Aufruf:", id(alter), alter)
print("Wert außerhalb Funktion nach Aufruf:", id(nachname), nachname)
print("Wert außerhalb Funktion nach Aufruf:", id(kinder_alter), kinder_alter)   

       