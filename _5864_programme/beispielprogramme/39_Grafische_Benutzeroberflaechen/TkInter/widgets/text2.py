#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        
        self.text = tkinter.Text(master)
        self.text.pack()
        
        self.text.bind("<KeyRelease>", self.textChanged)
    
    def textChanged(self, event):
        print("Text:", self.text.get("1.0", "end"))
        
root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
