import Tkinter

def ende():
    main.destroy()

def anzeigen():
    lb["text"] = "Auswahl: " + farbe.get()

main = Tkinter.Tk()

# Widget-Variable
farbe = Tkinter.StringVar()
farbe.set("rot")

# Gruppe von Radio-Buttons
rb1 = Tkinter.Radiobutton(main, text="rot",
         variable=farbe, value="rot", command=anzeigen)
rb1.pack()
rb2 = Tkinter.Radiobutton(main, text="gelb",
         variable=farbe, value="gelb", command=anzeigen)
rb2.pack()
rb3 = Tkinter.Radiobutton(main, text="blau",
         variable=farbe, value="blau", command=anzeigen)
rb3.pack()

# Anzeigelabel
lb = Tkinter.Label(main, text = "Auswahl:")
lb.pack()

bende = Tkinter.Button(main, text = "Ende",
                       command = ende)
bende.pack()

main.mainloop()


