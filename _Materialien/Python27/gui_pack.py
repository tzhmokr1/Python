import Tkinter

def ende():
    main.destroy()

main = Tkinter.Tk()

# Frame 1 mit Button 1a und 1b
fr1 = Tkinter.Frame(main, width=200,
         height=100, relief="sunken", bd=1)
fr1.pack(side="left")
b1a = Tkinter.Button(fr1, text="Button 1a")
b1a.pack(padx=5, pady=5)
b1b = Tkinter.Button(fr1, text="Button 1b")
b1b.pack(padx=5, pady=5)

# Frame 2 mit Button 2a und 2b
fr2 = Tkinter.Frame(main, width=200,
         height=100, relief="sunken", bd=1)
fr2.pack(side="right")
b2a = Tkinter.Button(fr2, text="Button 2a")
b2a.pack(ipadx=25, ipady=25)
b2b = Tkinter.Button(fr2, text="Button 2b")
b2b.pack(fill="x")

# Frame 3
fr3 = Tkinter.Frame(main, width=200,
         height=100, relief="sunken", bd=1)
fr3.pack(side="bottom", expand=1, fill="both")

bende = Tkinter.Button(main, text = "Ende",
                       command = ende)
bende.pack()

main.mainloop()


