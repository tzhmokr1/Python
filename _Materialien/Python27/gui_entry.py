import Tkinter

def ende():
    main.destroy()

# Funktion zum Quadrieren und Ausgeben
def quad():
    eingabe = e.get()
    try:
        zahl = float(eingabe)
        lb["text"] = "Ergebnis:" + str(zahl * zahl)
    except:
        lb["text"] = "Bitte Zahl eingeben"

main = Tkinter.Tk()

# einzeiliges Eingabefeld
e = Tkinter.Entry(main)
e.pack()

# Button zur Verarbeitung und Ausgabe
bquad = Tkinter.Button(main,
           text = "Quadrieren", command = quad)
bquad.pack()

# Ausgabe-Label
lb = Tkinter.Label(main, text = "Ergebnis:")
lb.pack()

bende = Tkinter.Button(main, text = "Ende",
                       command = ende)
bende.pack()

main.mainloop()


