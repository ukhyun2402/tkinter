import tkinter as tk

class mainChatWindow(tk.Frame):
    def __init__(self,parent,*args,**kw):
        tk.Frame.__init__(self,parent,*args,**kw)
        self.parent = self