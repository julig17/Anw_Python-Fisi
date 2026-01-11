m_liste = ["Hi", "Hallo", [1,244,2]]
print(m_liste)
print (m_liste[::1])

for zeile in m_liste:
    print("Element:", zeile)
    for spalte in zeile:
        print("  Unterelement:", spalte)


wort = "Hallo"
for buchstabe in wort:
    print("Buchstabe:", buchstabe)

