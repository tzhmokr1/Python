import Tkinter

def ende():
    main.destroy()

# bewegt nach ganz links
def movetoleft():
    lb.place(relx=0, rely=0, anchor="nw")

# bewegt nach ganz rechts
def movetoright():
    lb.place(relx=1, rely=0, anchor="ne")

main = Tkinter.Tk()

# Bewegtes Label
lb = Tkinter.Label(main, text="Test",
                   relief="sunken", bd=1)
lb.place(relx=0, rely=0, anchor="nw")

# bewegt nach ganz links
bleft = Tkinter.Button(main, text="ganz links",
                       command=movetoleft)
bleft.place(relx=0, rely=1, anchor="sw")

# bewegt nach ganz rechts
bright = Tkinter.Button(main, text="ganz rechts",
                        command=movetoright)
bright.place(relx=1, rely=1, anchor="se")

bende = Tkinter.Button(main, text="Ende",
                       command=ende)
bende.place(relx=0.5, rely=1, anchor="s")

main.mainloop()

