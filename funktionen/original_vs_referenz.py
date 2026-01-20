#Unveränderliche Datentypen
'''Argumente werden per Call by Value(Wertübergabe) übergeben'''
'''für zahl neue Speicheradresse reserviert '''
def erhoehe(zahl):
    zahl = zahl + 1
    print("In Funktion:", zahl)

zahl = 10
erhoehe(zahl)
print("Außerhalb:", zahl)

#Veränderliche Datentypen
'''Argumente werden per Call by Reference(Referenzübergabe) übergeben'''
def server_hinzufuegen(serverliste):
    serverliste.append("srv03")
    print("In Funktion:", serverliste)  

server = ["srv01", "srv02"]
server_hinzufuegen(server)
print("Außerhalb:", server)

#Achtung kann Konfiguration verändern
def ports_hinzufuegen(ports):
    ports.append(8080)

firewall_ports = [22, 80, 443]
ports_hinzufuegen(firewall_ports)
print("Firewall Ports:", firewall_ports)

#Lösung: Kopie der Liste übergeben
def ports_hinzufuegen_kopie(ports):
    ports.append(8080)  
    print("In Funktion:", ports)
firewall_ports = [22, 80, 443]
ports_hinzufuegen_kopie(firewall_ports.copy())  
print("Firewall Ports:", firewall_ports)

