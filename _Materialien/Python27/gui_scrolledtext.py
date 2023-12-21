import Tkinter, ScrolledText

def ende():
    main.destroy()

# Anzeigefunktion
def xshow():
    d = open("gui_text.txt")
    z = d.readline()
    while z:
        t.insert("end",z)
        z = d.readline()
    d.close()
    
main = Tkinter.Tk()

# mehrzeiliges Eingabefeld
t = ScrolledText.ScrolledText(main,
            width=40, height=3)
t.pack()

# Inhalt der Datei anzeigen
bshow = Tkinter.Button(main, text = "Anzeigen",
                       command = xshow)
bshow.pack()

bende = Tkinter.Button(main, text = "Ende",
                       command = ende)
bende.pack()

main.mainloop()


