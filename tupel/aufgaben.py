#Gegeben ist folgendes Tupel:

#a) Gib alle Ports einzeln aus (z. B. mit einer Schleife
#b) Versuche, einen weiteren Port (8080) hinzuzufüge
#c) Beschreibe, was passiert und warum

ports = (22, 80, 443)
for port in ports:
    print("Port:", port)
#ports[3] = 8080  # TypeError: 'tuple' object does not support item assignment
#Tupel sind unveränderbar (immutable), daher können keine Elemente hinzugefügt oder geändert


#Erstelle ein Tupel mit folgenden Informationen zu einem Server:
#Hostname, IP-Adresse, Status (True/False)
#Gib die Informationen formatiert aus, z. B.:
#Server: srv01
#IP: 192.168.1.10
#Status: Aktiv
server_info = ("srv01", "192.168.1.10", False)
print("Server:", server_info[0])
print("IP:", server_info[1])
print("Status:", "Aktiv" if server_info[2] else "Inaktiv")

#Gegeben ist folgendes Tupel:
#a) Weise jedem Wert eine eigene Variable zu
#b) Gib jede Variable einzeln aus
server = ("srv02", "192.168.1.20", "Linux")
hostname, ip_address, os_type = server
print("Hostname:", hostname)
print("IP-Adresse:", ip_address)
print("Betriebssystem:", os_type)    


"""Erstelle eine Liste von Tupeln, in der mehrere Server gespeichert werden:
	(Servername, IP-Adresse)
Füge mindestens 3 Server hinzu
Gib alle Server übersichtlich aus
Beispiel: ("srv01", "192.168.1.10")
"""
servers = [("srv01", "192.168.1.10"), ("srv02", "192.168.1.20"), ("srv03", "192.168.1.30")]
for server in servers:
    print("Server:", server[0], "IP-Adresse:", server[1])   


"""Gegeben ist eine Liste von Tupeln:
devices = [
    ("PC01", "online"),
    ("PC02", "offline"),
    ("PC03", "online")
]
Gib alle Geräte aus, die online sind
"""
devices = [("PC01", "online"),
    ("PC02", "offline"),    
    ("PC03", "online")              
]
for device in devices:
    if device[1] == "online":
        print("Gerät:", device[0], "Status:", device[1])