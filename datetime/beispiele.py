from datetime import datetime, date, time

# Aktuelles Datum und Uhrzeit
jetzt = datetime.now()
print("Aktuelles Datum und Uhrzeit:", jetzt)

# Aktuelles Datum
heute = date.today()
print("Aktuelles Datum:", heute)

#gestiges Datum
datum = date(2024, 6, 15)
differenz = heute - datum
print("Differenz zwischen heute und dem Datum:", differenz)   

#Wochentag des heutigen Datums
wochentag = heute.weekday() 
print("Wochentag des heutigen Datums (0=Montag, 6=Sonntag):", wochentag)

#iso-Format des heutigen Datums
iso_format = heute.isoformat()  
print("Heutiges Datum im ISO-Format:", iso_format)

#datum in einem benutzerdefinierten Format
benutzerdefiniert = heute.strftime("%d.%m.%Y")
print("Heutiges Datum in benutzerdefiniertem Format:", benutzerdefiniert)

#uhrzeit im benutzerdefinierten Format
uhrzeit = jetzt.strftime("%H:%M:%S")
print("Aktuelle Uhrzeit in benutzerdefiniertem Format:", uhrzeit)

#zeitstempel in iso-Format
zeitstempel = jetzt.isoformat()
print("Aktueller Zeitstempel im ISO-Format:", zeitstempel)
