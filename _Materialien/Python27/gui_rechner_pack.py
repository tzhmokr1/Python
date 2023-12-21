import Tkinter

def ende():
    main.destroy()

# Kehrwert
def kw():
    if not lb["text"]:
        return
    z = float(lb["text"])
    z = 1/z
    lb["text"] = str(z)

# Quadrat
def qu():
    if not lb["text"]:
        return
    z = float(lb["text"])
    z = z*z
    lb["text"] = str(z)

# Anzeige leeren
def cl():
    lb["text"] = ""

# Ziffern 0 bis 9
def anz(ziffer):
    lb["text"] += str(ziffer)
    
# Punkt, falls noch nicht vorhanden
def anzp():
    if lb["text"].find(".") == -1:
        lb["text"] += "."
    
main = Tkinter.Tk()

# Frame A mit Anzeige-Label
fra = Tkinter.Frame(main)
fra.pack(expand=1, fill="x")
lb = Tkinter.Label(fra, bg="#FFFFFF", bd=5,
                   relief="sunken", anchor="e")
lb.pack(expand=1, fill="x", pady=10)

# Frame B mit Kehrwert, Quadrat und Leeren
frb = Tkinter.Frame(main)
frb.pack()
Tkinter.Button(frb, text="1/x", width=7,
    command=kw).pack(side="left")
Tkinter.Button(frb, text="x hoch 2", width=7,
    command=qu).pack(side="left")
Tkinter.Button(frb, text="CL", width=7,
    command=cl).pack(side="left")

# Frame C mit Ziffern 7, 8, 9
frc = Tkinter.Frame(main)
frc.pack()
Tkinter.Button(frc, text="7", width=7,
    command=lambda:anz(7)).pack(side="left")
Tkinter.Button(frc, text="8", width=7,
    command=lambda:anz(8)).pack(side="left")
Tkinter.Button(frc, text="9", width=7,
    command=lambda:anz(9)).pack(side="left")

# Frame D mit Ziffern 4, 5, 6
frd = Tkinter.Frame(main)
frd.pack()
Tkinter.Button(frd, text="4", width=7,
    command=lambda:anz(4)).pack(side="left")
Tkinter.Button(frd, text="5", width=7,
    command=lambda:anz(5)).pack(side="left")
Tkinter.Button(frd, text="6", width=7,
    command=lambda:anz(6)).pack(side="left")

# Frame E mit Ziffern 1, 2, 3
fre = Tkinter.Frame(main)
fre.pack()
Tkinter.Button(fre, text="1", width=7,
    command=lambda:anz(1)).pack(side="left")
Tkinter.Button(fre, text="2", width=7,
    command=lambda:anz(2)).pack(side="left")
Tkinter.Button(fre, text="3", width=7,
    command=lambda:anz(3)).pack(side="left")

# Frame F mit Dezimalpunkt, Ziffer 0 und Ende
frf = Tkinter.Frame(main)
frf.pack()
Tkinter.Button(frf, text=".", width=7,
    command=anzp).pack(side="left")
Tkinter.Button(frf, text="0", width=7,
    command=lambda:anz(0)).pack(side="left")
Tkinter.Button(frf, text="Ende", width=7,
    command=ende).pack(side="left")

main.mainloop()

