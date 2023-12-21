import Tkinter

def ende():
    main.destroy()

# Untersuchung des Passwortes
def pwtest():
    eingabe = e.get()
    if eingabe == "Bingo":
        lb["text"] = "Zugang erlaubt"
    else:
        lb["text"] = "Zugang verweigert"

main = Tkinter.Tk()

# Eingabefeld mit Zeichen * als Darstellung
e = Tkinter.Entry(main, show = "*")
e.pack()

# Test der Eingabe
btest = Tkinter.Button(main, text = "Login",
                       command = pwtest)
btest.pack()

# Anzeige des Ergebnisses
lb = Tkinter.Label(main, text = "Zugang")
lb.pack()

bende = Tkinter.Button(main, text = "Ende",
                       command = ende)
bende.pack()

main.mainloop()


