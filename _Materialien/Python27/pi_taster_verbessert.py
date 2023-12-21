import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setwarnings(False)
gp.setup(18, gp.IN)

zeitAktuell = time.time()
zeitEnde = zeitAktuell + 5
zeitKontaktAlt = 0              # Allererster Wert

while zeitAktuell < zeitEnde:
    if gp.input(18) == True:
        # Neuer Wert
        zeitKontaktNeu = time.time()

        # Falls Zeitabstand gross genug ist
        if zeitKontaktNeu - zeitKontaktAlt > 0.5:
            print time.time()

            # Fuer naechste Pruefung
            zeitKontaktAlt = zeitKontaktNeu
    zeitAktuell = time.time()
