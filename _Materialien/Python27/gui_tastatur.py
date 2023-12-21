import Tkinter

def ende():
    main.destroy()

def kev(e):
    lbanz["text"] = "Zeichen:" + e.char \
       + ", Beschreibung: " + e.keysym \
       + ", Codezahl: " + str(e.keycode)

main = Tkinter.Tk()

# Key-Events
e = Tkinter.Entry(main)
e.bind("<p>",kev)
e.bind("<+>",kev)
e.bind("<%>",kev)
e.bind("<,>",kev)
e.pack()

# Hilfe-Label
lbhlp = Tkinter.Label(main,
        text = "Taste: p oder + oder % oder ,",
        width=40)
lbhlp.pack()

# Anzeigelabel
lbanz = Tkinter.Label(main)
lbanz.pack()

# Ende-Button
bende = Tkinter.Button(main, text = "Ende",
                       command = ende)
bende.pack()

main.mainloop()


