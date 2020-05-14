import tkinter as Tk
root = Tk.Tk()
ent = Tk.Entry(root, state='readonly', readonlybackground='white', fg='black')
var = Tk.StringVar()
var.set('Some text')
ent.config(textvariable=var, relief='flat')
ent.pack()
root.mainloop()