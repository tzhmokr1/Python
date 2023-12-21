import Tkinter

# Funktion zu Button Ende
def ende():
    main.destroy()

# Hauptfenster
main = Tkinter.Tk()

# Button Ende
b = Tkinter.Button(main, text = "Ende", command = ende)
b.pack()

# Endlosschleife
main.mainloop()
