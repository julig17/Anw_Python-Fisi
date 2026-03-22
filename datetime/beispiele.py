from datetime import datetime, date, time

heute = date.today()
print(heute.isoformat())

gestern = date(2026, 3, 9)
print(gestern)

differenz = heute - gestern
print(differenz)


zeitstempel = datetime.now()
print(zeitstempel)

heute_deutsch = heute.strftime("%d.%m.%Y") #10.03.2026

print(heute_deutsch)

wochen_zahl = gestern.weekday()
liste_tag = ["Montag", "Dienstag"]  

tag = liste_tag[wochen_zahl]
dict_tag = {0 : "Montag", 1 : "Dienstag"}
tag = dict_tag[wochen_zahl]


