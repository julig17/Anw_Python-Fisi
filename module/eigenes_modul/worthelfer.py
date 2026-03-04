"""
Diese Funktion entfernt alle unnötigen Whitespaces
und konvertiert in Kleinbuchtsteben
"""
def saeubere_text(text):
    return text.strip().lower()

"""Diese Funktion zählt die Wörter im Text"""
def zaehle_woerter(text):
    return len(text.split())

"""Mit dieser Funktion kann man Text ersetzten"""
def ersetze_wort(text, alt, neu):
    return text.replace(alt,neu)

