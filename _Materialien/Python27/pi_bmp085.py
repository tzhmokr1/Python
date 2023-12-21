import Adafruit_BMP085

# Sensor im Standardmodus initialisieren
bmp = Adafruit_BMP085.BMP085(0x77)
 
# Werte ausgeben
print "Lufttemperatur:", bmp.readTemperature(), "Grad Celsius"
print "Luftdruck:", bmp.readPressure()/100.0, "hPa"
print "Hoehe:", bmp.read.Altitude(), "m"
