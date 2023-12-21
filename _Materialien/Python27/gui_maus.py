import Tkinter

def ende():
    main.destroy()

def mlinks(e):
    lbanz["text"] = "Linke Maus-Taste"

def mrechts(e):
    lbanz["text"] = "Rechte Maus-Taste"

def mstrglinks(e):
    lbanz["text"] = "Strg-Taste und linke Maus-Taste"

def maltlinks(e):
    lbanz["text"] = "Alt-Taste und linke Maus-Taste"

def mshiftlinks(e):
    lbanz["text"] = "Shift-Taste und linke Maus-Taste"

def mlinkslos(e):
    lbanz["text"] = "Linke Maus-Taste losgelassen"

def mbetreten(e):
    lbanz["text"] = "Button betreten"

def mverlassen(e):
    lbanz["text"] = "Button verlassen"

def mbewegt(e):
    lbanz["text"] = \
    "Koordinaten: x=" + str(e.x) + ", y=" + str(e.y)

main = Tkinter.Tk()

# Label mit Events
im = Tkinter.PhotoImage(file="figur.gif")
lbm = Tkinter.Label(main, image=im)
lbm.bind("<Button 1>", mlinks)
lbm.bind("<Button 3>", mrechts)
lbm.bind("<Control-Button 1>", mstrglinks)
lbm.bind("<Alt-Button 1>", maltlinks)
lbm.bind("<Shift-Button 1>", mshiftlinks)
lbm.bind("<ButtonRelease 1>", mlinkslos)
lbm.bind("<Motion>", mbewegt)
lbm.pack()

# Anzeigelabel
lbanz = Tkinter.Label(main, width=35)
lbanz.pack()

# Ende-Button, mit Events
bende = Tkinter.Button(main, text = "Ende",
                       command = ende)
bende.bind("<Enter>", mbetreten)
bende.bind("<Leave>", mverlassen)
bende.pack()

main.mainloop()


