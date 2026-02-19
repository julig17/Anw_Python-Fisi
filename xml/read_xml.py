import xml.etree.ElementTree as ElementTree

DATEINAME = "./xml/data.xml"
TYPEN = {
    "int" : int,
    "str" : str
    }

"""
Funktion liest aus schluessel- oder wert-Tags das Attribut typ aus
 und konvertiert den  Text in den durch typ angegebenen Datentyp.
"""
def lese_element(element):
    #Attribut typ wird ausgelesen 
    typ = element.get("typ", "str")
    try:
        #Wert in richtigen Datentp wird zurückgegeben z.B int("15")
        return TYPEN[typ](element.text)
    except KeyError:
        return element.text

""" Haupfunktion bekommt den Dateinamen übergeben, gibt den Datendict mit
Daten aus dem XML Dokument zurück"""
def lade_dict(dateiname): 
    d = {}
    #XML Daten werden zu einem Baum aufbearbeitet
    baum = ElementTree.parse(dateiname) 
    #hole Wurzelelement
    tag_dict = baum.getroot()
    #laufe durch Kindelemente
    for eintrag in tag_dict:
        tag_schluessel = eintrag.find("schluessel")
        tag_wert = eintrag.find("wert")
        schluessel = lese_element(tag_schluessel)
        wert = lese_element(tag_wert) 
        d[schluessel] = wert 
    return d

daten_im_dict = lade_dict(DATEINAME)
print(daten_im_dict)