import time, random, glob, sqlite3, \
    Tkinter, tkMessageBox

def auswertung():
    if status != "main":
        return

    # Zeit berechnen
    endzeit = time.time()
    differenz = endzeit - startzeit
    
    # Auswertung
    richtig = 0
    for i in range(5):
        try:
            # Falsche Eingabe abfangen
            if int(enliste[i].get()) == ergliste[i]:
                richtig = richtig + 1
        except:
            pass

    # Kein Highscore
    if richtig < 5:
        tkMessageBox.showinfo("Kein Highscore",
            "Leider kein Highscore")
        main.destroy()
        return
    
    ##### Highscore speichern, ausgeben #####

    # Highscore-DB nicht vorhanden, erzeugen
    if not glob.glob("gui_highscore.db"):
        con = sqlite3.connect("gui_highscore.db")
        cursor = con.cursor()
        sql = "CREATE TABLE daten(name TEXT, zeit FLOAT)"
        cursor.execute(sql)
        con.close()

    # Datensatz in DB schreiben
    con = sqlite3.connect("gui_highscore.db")
    cursor = con.cursor()
    sql = "INSERT INTO daten VALUES('" \
        + lbname["text"] + "'," + str(differenz) + ")"
    cursor.execute(sql)
    con.commit()
    con.close()

    # Highscores sortiert laden
    con = sqlite3.connect("gui_highscore.db")
    cursor = con.cursor()
    sql = "SELECT * FROM daten ORDER BY zeit LIMIT 10"
    cursor.execute(sql)

    # Ausgabe Highscore
    ausgabe = ""
    i = 1
    for dsatz in cursor:
        ausgabe += str(i) + ". " + dsatz[0] + " " \
            + str(round(dsatz[1],2)) + " sec.\n"
        i = i+1
    tkMessageBox.showinfo("Highscore", ausgabe)
    con.close()
    main.destroy()

def endeneu():
    global startzeit, status
    lbname["text"] = enname.get()
    startzeit = time.time()
    status = "main"
    neu.destroy()

# Hauptprogramm
main = Tkinter.Tk()

# Titel
lbtitel = Tkinter.Label(main, text="Kopfrechnen")
lbtitel.grid(row=0, column=0, columnspan=6)

# Name
lbname = Tkinter.Label(main, text=" ")
lbname.grid(row=1, column=0, columnspan=6)

# Aufgaben
enliste = []     # Liste der Entries
ergliste = []    # Liste der richtigen Ergebnisse
for i in range(5):
    # Aufgabe mit Ergebnis
    a = random.randint(10,30)
    b = random.randint(10,30)
    ergliste.append(a + b)

    # Aufgabenstellung
    Tkinter.Label(main, text=str(i+1)+"."). \
        grid(row=i+1, column=0)
    Tkinter.Label(main, text=a).grid(row=i+1, column=1)
    Tkinter.Label(main, text="+").grid(row=i+1, column=2)
    Tkinter.Label(main, text=b).grid(row=i+1, column=3)
    Tkinter.Label(main, text="=").grid(row=i+1, column=4)

    # Eingabefeld
    en = Tkinter.Entry(main)
    en.grid(row=i+1, column=5)
    enliste.append(en)

# Ergebnis
b = Tkinter.Button(main, text="Fertig", \
                   command=auswertung)
b.grid(row=7, column=0, columnspan=6)

# Fenster zur Namenseingabe
neu = Tkinter.Toplevel(main)
Tkinter.Label(neu, text="Ihr Name:").pack()
enname = Tkinter.Entry(neu)
enname.pack()
Tkinter.Button(neu, text="Start", command=endeneu).pack()
status="neu"

main.mainloop()
