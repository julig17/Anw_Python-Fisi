"""binärmodus lesen"""
#mit with open benötgt man kein close()
try:
    with open("./files/zahlen.dat", "rb") as bindata:
        byte_daten = bindata.read()
except Exception as e:
    print("sonstige Dateifehler beim Lesen:", e)

# --- Bytes in Zahlen zurückwandeln ---
byte_data1 = byte_daten[:4] # erste 4 Bytes = zahl1
byte_data2 = byte_daten[4:] # nächste 4 Bytes = zahl2
print("byte_data1:", byte_data1, byte_data1.hex())
print("byte_data2:", byte_data2, byte_data2.hex())
# from_bytes(bytes, byteorder)
zahl1 = int.from_bytes(byte_data1)
zahl2 = int.from_bytes(byte_data2)
print("Zahl 1:", zahl1)
print("Zahl 2:", zahl2)


