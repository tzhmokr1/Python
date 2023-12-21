import os, sys, sqlite3

# Falls DB nicht vorhanden, Ende
if not os.path.exists("bmp085.db"):
    print "Datei nicht vorhanden"
    sys.exit(0)

# Verbindung, Cursor
connection = sqlite3.connect("bmp085.db")
cursor = connection.cursor()

# SQL-Abfrage
sql = "SELECT * FROM werte order by zeit desc"
cursor.execute(sql)
for dsatz in cursor:
    print dsatz[0], dsatz[1], dsatz[2], dsatz[3]

# Verbindung beenden
connection.close()
