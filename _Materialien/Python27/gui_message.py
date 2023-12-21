import Tkinter, tkMessageBox

def ende():
    main.destroy()

def msginfo():
    tkMessageBox.showinfo \
       ("Info","Eine Info-Box")

def msgwarning():
    tkMessageBox.showwarning \
       ("Warnung","Eine Warnungs-Box")

def msgerror():
    tkMessageBox.showerror \
       ("Fehler","Eine Fehler-Box")

def msgyesno():
    antwort = tkMessageBox.askyesno \
       ("Ja/Nein", "Eine Ja/Nein-Box")
    if antwort == 1:
        lbanz["text"] = "Ja"
    else:
        lbanz["text"] = "Nein"

def msgokcancel():
    antwort = tkMessageBox.askokcancel \
       ("Ok/Abbrechen", "Eine Ok/Abbrechen-Box")
    if antwort == 1:
        lbanz["text"] = "Ok"
    else:
        lbanz["text"] = "Abbrechen"

def msgretrycancel():
    antwort = tkMessageBox.askretrycancel \
       ("Wiederholen/Abbrechen",
        "Eine Wiederholen/Abbrechen-Box")
    if antwort == 1:
        lbanz["text"] = "Wiederholen"
    else:
        lbanz["text"] = "Abbrechen"

def msgfrage():
    # hier einmal in allgemeiner Technik, ohne Komfort
    msgbox = tkMessageBox.Message(main,
        type=tkMessageBox.ABORTRETRYIGNORE,
        icon=tkMessageBox.QUESTION,
        title="Beenden/Wiederholen/Ignorieren",
        message="Beenden, Wiederholen oder Ignorieren")
    
    antwort = msgbox.show()

    if antwort == "abort":
        lbanz["text"] = "Beenden"
    elif antwort == "retry":
        lbanz["text"] = "Wiederholen"
    else:
        lbanz["text"] = "Ignorieren"

main = Tkinter.Tk()

# Button: Message Info
binfo = Tkinter.Button(main,
   text = "Info", command=msginfo)
binfo.pack()

# Button: Message Box Warning
bwarning = Tkinter.Button(main,
   text = "Warnung", command=msgwarning)
bwarning.pack()

# Button: Message Box Error
berror = Tkinter.Button(main,
   text = "Fehler", command=msgerror)
berror.pack()

# Button: Message Box Ja/Nein
byesno = Tkinter.Button(main,
   text = "Ja/Nein", command=msgyesno)
byesno.pack()

# Button: Message Box OK/Cancel
bokcancel = Tkinter.Button(main,
   text = "Ok/Abbrechen", command=msgokcancel)
bokcancel.pack()

# Button: Message Box Retry/Cancel
bretrycancel = Tkinter.Button(main,
   text = "Wiederholen/Abbrechen",
   command=msgretrycancel)
bretrycancel.pack()

# Button: Message Box Frage
bfrage = Tkinter.Button(main,
   text = "Allgemeine Frage", command=msgfrage)
bfrage.pack()

# Ende-Button
bende = Tkinter.Button(main,
   text = "Ende", command=ende)
bende.pack()

# Anzeige-Label
lbanz = Tkinter.Label(main)
lbanz.pack()

main.mainloop()
