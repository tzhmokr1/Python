import Tkinter

# Erzeugt neues Fenster mit Ende-Button
def fenster():
    global status, neu
    if status != "main":
        return
    status = "neu"
    neu = Tkinter.Toplevel(main)
    Tkinter.Button(neu, text="Ende Neu",
        command=endeneu).pack()

# Ende neues Fenster
def endeneu():
    global status
    neu.destroy()
    status = "main"

# Ende Hauptfenster
def ende():
    if status == "main":
        main.destroy()

# Hauptfenster
main = Tkinter.Tk()
status = "main"
Tkinter.Button(main, text="Neu", command=fenster).pack()
Tkinter.Button(main, text="Ende", command=ende).pack()
main.mainloop()
