import Tkinter

def ende():
    main.destroy()

def anzeigen():
    lb["text"] = "Zimmer " + du.get() + " " + mb.get()

main = Tkinter.Tk()

# Anzeigelabel
lb = Tkinter.Label(main, text = "Zimmer ", width=40)
lb.pack()

# Widget-Variablen
du = Tkinter.StringVar()
du.set("ohne Dusche")
mb = Tkinter.StringVar()
mb.set("ohne Minibar")

# Zwei Checkbuttons
cb1 = Tkinter.Checkbutton(main, text="Dusche",
         variable=du, onvalue="mit Dusche",
         offvalue="ohne Dusche", command=anzeigen)
cb1.pack()
cb2 = Tkinter.Checkbutton(main, text="Minibar",
         variable=mb, onvalue="mit Minibar",
         offvalue="ohne Minibar", command=anzeigen)
cb2.pack()

bende = Tkinter.Button(main, text = "Ende",
                       command = ende)
bende.pack()

main.mainloop()


