# Ziffern
ausgabe = ""
for i in range(48,58):
    ausgabe += chr(i)
print ausgabe

# grosse Buchstaben
ausgabe = ""
for i in range(65,91):
    ausgabe += chr(i)
print ausgabe

# kleine Buchstaben
ausgabe = ""
for i in range(97,123):
    ausgabe += chr(i)
print ausgabe

# Codenummern
ausgabe = ""
for z in "Robinson":
    ausgabe += str(ord(z)) + " "
print ausgabe

# Verschoben
ausgabe = ""
for z in "Robinson":
    ausgabe += chr(ord(z)+1)
print ausgabe

