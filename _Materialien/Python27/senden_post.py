import urllib

# Eingabedaten
pnn = raw_input("Bitte den Nachnamen eingeben: ")
pvn = raw_input("Bitte den Vornamen eingeben: ")

# Dictionary mit Sendedaten, Codierung
dc = {"nn":pnn, "vn":pvn}
data = urllib.urlencode(dc)

# sendet Daten
u = urllib.urlopen \
   ("http://localhost/Python27/senden_post.php", data)

# Empfang der Antwort und Ausgabe
li = u.readlines()
u.close()
ausgabe = ""
for element in li:
    ausgabe += element
print ausgabe
