lan = {"PC1", "PC2", "PC3", "Server1"}
wlan = {"PC3", "PC4", "Laptop1"}
# 1. LAN und WLAN (Schnittmenge)

print("LAN und WLAN:", lan & wlan)

# 2. Nur LAN (Differenz)
print("Nur LAN:", lan - wlan)

# 3. Nur WLAN (Differenz)
print("Nur WLAN:", wlan - lan)

# 4. Alle Geräte (Vereinigung)
print("Alle Geräte:", lan | wlan)

# 5. Teilmenge prüfen
if wlan.issubset(lan):
    print("Alle WLAN-Geräte sind im LAN")
else:
    print("Nicht alle WLAN-Geräte sind im LAN")