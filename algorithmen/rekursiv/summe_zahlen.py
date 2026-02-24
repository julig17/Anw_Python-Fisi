def summe(zahl):
	if zahl > 0:
		return zahl + summe(zahl-1)
	else:
		return 0
# Aufruf der Funktion summe mit dem Wert 100
print(summe(100))
