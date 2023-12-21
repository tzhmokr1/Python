import Tkinter

def ende():
    main.destroy()

def anzeigen():
    lb["text"] = "Auswahl: " + li.get("active")

main = Tkinter.Tk()

# Listbox mit vier Elementen
li = Tkinter.Listbox(main, height=0)
li.insert("end","Hamburg")
li.insert("end","Stuttgart")
li.insert("end","Berlin")
li.insert("end","Dortmund")
li.pack()

# Auswahl anzeigen lassen
bshow = Tkinter.Button(main, text = "Anzeigen",
                       command = anzeigen)
bshow.pack()

# Anzeigelabel
lb = Tkinter.Label(main, text = "Auswahl:")
lb.pack()

bende = Tkinter.Button(main, text = "Ende",
                       command = ende)
bende.pack()

main.mainloop()


