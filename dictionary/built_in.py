#Eingebeute Funktionen 
woerterbuch = {
    'Apfel': 'apple',
    'Banane': 'banana',
    'Kirsche': 'cherry',
    "Birne": "pear"
}
print(woerterbuch)
# Zugriff auf ein Element
print(woerterbuch.get('Apfel')) 
# oder mit []
print(woerterbuch['Apfel'])
print(woerterbuch.get('Orange'))
try:  
  print(woerterbuch['Orange'])
except: 
  print("Zugriff auf nicht vorhandenen Schlüssel")

#Hinzufügen eines neuen Elements
woerterbuch['Orange'] = 'orange'
print(woerterbuch)
#oder updaten
woerterbuch.update({'Traube': 'grape'})
woerterbuch = woerterbuch | {'Erdbeere': 'strawberry'}
print(woerterbuch)

#WErt ändern
woerterbuch['Banane'] = 'yellow banana'
print(woerterbuch)
#oder mit update
woerterbuch.update({'Kirsche': 'red cherry'})
print(woerterbuch)
"""!!!Falls der Key nicht vorhanden, wird der Key mit Schlüssel dem Dict. hinzugefügt"""
woerterbuch["Blaubeere"] = "blueberry"
print(woerterbuch)

#Löschen eines Elements
del woerterbuch['Birne']
print(woerterbuch)
#oder mit pop
wert = woerterbuch.pop('Kirsche')
print(woerterbuch)
print('Entfernter Wert:', wert)

#Liefert alle Schlüssel
schluessel = woerterbuch.keys()
print('Schlüssel:', schluessel)
for schluessel in woerterbuch.keys():
  print(schluessel)

#Liefert alle Werte
werte = woerterbuch.values()
print('Werte:', werte)
for wert in woerterbuch.values():
  print(wert)

#Liefert alle Schlüssel-Wert-Paare
paare = woerterbuch.items()
print('Paare:', paare)
for schluessel, wert in woerterbuch.items():
  print(schluessel, '->', wert)

 