import Tkinter

# Erzeugt neues Fenster mit Ende-Button
def fenster():
    global neu
    neu = Tkinter.Toplevel(main)
    Tkinter.Button(neu, text="Ende Neu",
        command=endeneu).pack()

# Ende neues Fenster
def endeneu():
    neu.destroy()

# Ende Hauptfenster
def ende():
    main.destroy()

# Hauptfenster
main = Tkinter.Tk()
Tkinter.Button(main, text="Neu", command=fenster).pack()
Tkinter.Button(main, text="Ende", command=ende).pack()
main.mainloop()
