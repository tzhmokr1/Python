import Adafruit_BMP085, os, sys, sqlite3, time

# Falls DB nicht vorhanden, Ende
if not os.path.exists("bmp085.db"):
    print "Datei nicht vorhanden"
    sys.exit(0)

# Sensor im Standardmodus initialisieren
bmp = Adafruit_BMP085.BMP085(0x77)
 
# Verbindung, Cursor
connection = sqlite3.connect("bmp085.db")
cursor = connection.cursor()

# Zeiten setzen
zeitAktuell = time.time()
zeitEnde = zeitAktuell + 5

# Ende erreicht?
while zeitAktuell < zeitEnde:
    # Werte ermitteln
    zeit  = time.time()
    temp  = bmp.readTemperature()
    druck = bmp.readPressure()
    hoehe = bmp.readAltitude()

    # Datensatz erzeugen
    sql = "INSERT INTO werte VALUES(" + str(zeit) + ", " \
        + str(temp) + ", " + str(druck) + ", " \
        + str(hoehe) + ")"
    cursor.execute(sql)
    connection.commit()

    # Warten
    time.sleep(0.3)

    # Zeit fuer Schleife ermitteln
    zeitAktuell = time.time() 

# Verbindung beenden
connection.close()
