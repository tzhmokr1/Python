import urllib

# Eingabedaten
pnn = raw_input("Bitte den Nachnamen eingeben: ")
pvn = raw_input("Bitte den Vornamen eingeben: ")

# sendet Daten
u = urllib.urlopen \
   ("http://localhost/Python27/senden_get.php?nn="
    + pnn + "&vn=" + pvn)

# Empfang der Antwort und Ausgabe
li = u.readlines()
u.close()
ausgabe = ""
for element in li:
    ausgabe += element
print ausgabe
