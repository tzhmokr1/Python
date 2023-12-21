import sys

# Zugriffsversuch
try:
    d = open("lesen.txt")
except:
    print "Dateizugriff nicht erfolgreich"
    sys.exit(0)

# Lesen, Ausgabe und Summierung aller Zeilen
summe = 0
zeile = d.readline()
while zeile:
    summe += float(zeile)
    print zeile[0:len(zeile)-1]
    zeile = d.readline()

# Ausgabe der Summe
print "Summe:", summe

# Schliessen der Datei
d.close()

