# Module
import random, time, glob, sqlite3

######################################################

# Funktion Highscore Anzeigen
def hs_anzeigen():
    # Highscore-DB nicht vorhanden
    if not glob.glob("highscore.db"):
        print("Keine Highscores vorhanden")
        return

    # Highscores laden
    con = sqlite3.connect("highscore.db")
    cursor = con.cursor()
    sql = "SELECT * FROM daten ORDER BY zeit LIMIT 10"
    cursor.execute(sql)

    # Ausgabe Highscore
    print(" P. Name            Zeit")
    i = 1
    for dsatz in cursor:
        print("{0:2d}. {1:10} {2:5.2f} sec".format
              (i, dsatz[0], dsatz[1]))
        i = i+1

    # Verbindung beenden
    con.close()

######################################################

# Funktion Spiel
def spiel():
    # Eingabe des Namens
    name = input("Bitte geben Sie Ihren "
                 "Namen ein (max. 10 Zeichen): ")
    name = name[0:10]

    # Initialisierung Counter und Zeit
    richtig = 0
    startzeit = time.time()

    # 5 Aufgaben
    for aufgabe in range(5):
        # Aufgabe mit Ergebnis
        a = random.randint(10,30)
        b = random.randint(10,30)
        c = a + b

        # Eingabe
        try:
            zahl = int(input("Aufgabe "
                + str(aufgabe+1) + " von 5: "
                + str(a) + " + " + str(b) + " : "))
            if zahl == c:
                print("*** Richtig ***")
                richtig += 1
            else:
                raise
        except:
            print("* Falsch *")

    # Auswertung
    endzeit = time.time()
    differenz = endzeit-startzeit
    print("Ergebnis: {0:d} von 5 in {1:.2f} Sekunden".
          format(richtig, differenz), end = "")
    if richtig == 5:
        print(", Highscore")
    else:
        print(", leider kein Highscore")
        return

    # Highscore-DB nicht vorhanden, erzeugen
    if not glob.glob("highscore.db"):
        con = sqlite3.connect("highscore.db")
        cursor = con.cursor()
        sql = "CREATE TABLE daten(" \
              "name TEXT, " \
              "zeit FLOAT)"
        cursor.execute(sql)
        con.close()

    # Datensatz in DB schreiben
    con = sqlite3.connect("highscore.db")
    cursor = con.cursor()
    sql = "INSERT INTO daten VALUES('" \
          + name + "'," + str(differenz) + ")"
    cursor.execute(sql)
    con.commit()
    con.close()

    # Highscoreliste anzeigen
    hs_anzeigen()

######################################################

# Hauptprogramm

# Initialisierung Zufallsgenerator
random.seed()

# Endlosschleife
while True:
    # Hauptmenu, Auswahl
    try:
        menu = int(input("Bitte eingeben "
            "(0: Ende, 1: Highscores, 2: Spielen): "))
    except:
        print("Falsche Eingabe")
        continue

    # Aufruf einer Funktion oder Ende
    if menu == 0:
        break
    elif menu == 1:
        hs_anzeigen()
    elif menu == 2:
        spiel()
    else:
        print("Falsche Eingabe")
