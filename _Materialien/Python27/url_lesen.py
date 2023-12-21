import sys, urllib

# Verbindung zu einem URL
try:
    u = urllib.urlopen \
        ("http://localhost/Python27/url_lesen.htm")
except:
    print "Fehler"
    sys.exit(0)

# Liest alle Zeilen in eine Liste
li = u.readlines()

# Schliesst die Verbindung
u.close()

# Ausgabe der Liste
ausgabe = ""
for element in li:
    ausgabe += element
print ausgabe
