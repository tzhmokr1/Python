import sys, morsen

# Beispieltext codieren
def schreibeCode(text, code):
    ausgabe = ""
    for zeichen in text:
        try:
            ausgabe += code[zeichen] + " "
        except KeyError:
            ausgabe += " "
    print ausgabe

# Lesefunktion aufrufen
code = morsen.leseCode()

# Schreibfunktion aufrufen
schreibeCode("Hallo Welt", code)

