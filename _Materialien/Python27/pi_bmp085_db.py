import os, sys, sqlite3

# Falls vorhanden, nicht neu erzeugen
if os.path.exists("bmp085.db"):
    print "Datei bereits vorhanden"
    sys.exit(0)

# Verbindung, Cursor
connection = sqlite3.connect("bmp085.db")
cursor = connection.cursor()

# Tabelle erzeugen, Ende
sql = "CREATE TABLE werte(zeit FLOAT, " \
      "temperatur FLOAT, druck FLOAT, hoehe FLOAT)"
cursor.execute(sql)
connection.close()
