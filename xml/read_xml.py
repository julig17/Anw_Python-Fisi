import xml.etree.ElementTree as ElementTree

dateiname = "./xml/data.xml"

baum = ElementTree.parse(dateiname) 
#hole Wurzelelement
tag_dict = baum.getroot()

print(tag_dict)

for kind_element in tag_dict:
    print("Kindelemente: ", kind_element)
    schluessel = kind_element.find("schluessel")
    #Inhalt vom Tag   
    tag_inhalt = schluessel.text
    #tag Name
    print(f"Tag: {schluessel.tag} : {tag_inhalt} ")
    #Attribut vom Tag
    print(f"Tag: {schluessel.get("typ")} ")