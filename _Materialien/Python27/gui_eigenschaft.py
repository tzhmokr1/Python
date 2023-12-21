import Tkinter

# Funktion zu drei Buttons
def ende():
    main.destroy()

# Hauptfenster
main = Tkinter.Tk()

# Button Ende 1
b1 = Tkinter.Button(main, text = "Ende", command = ende)

# Button Ende 2
b2 = Tkinter.Button(main)
b2["text"] = "Auch Ende"
b2["command"] = ende

# Button Ende 3
b3 = Tkinter.Button(main)
b3.configure(text = "Ebenfalls Ende", command = ende)

# Buttons 1 bis 3 anzeigen
b1.pack()
b2.pack()
b3.pack()

# Buttons Ende 4 und 5
b4 = Tkinter.Button(main,text="4",command=ende).pack()
Tkinter.Button(main,text="5",command=ende).pack()

# Endlosschleife
main.mainloop()


