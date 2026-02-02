try:
    with open("./files/zahlen.dat", "wb") as file:
        file.write((103).to_bytes(4))
        file.write((557).to_bytes(4))
except Exception as e:
    print("Dateifehler sind aufgetreten", e)