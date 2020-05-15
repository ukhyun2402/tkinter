from tkinter import *
from tkinter import ttk
root = Tk()
treedata = [('column 1', 'column 2'), ('column 1', 'column 2'), ('column 1',       'column 2'), ('column 1', 'column 2'), ('column 1', 'column 2'), ('column 1',    'column 2'), ('column 1', 'column 2'), ('column 1', 'column 2'), ('column 1', 'column 2'), ('column 1', 'column 2'), ('column 1', 'column 2'), ('column 1', 'column 2'), ('column 1', 'column 2'), ('column 1', 'column 2'), ('column 1', 'column 2'), ('column 1', 'column 222'), ('column 1', 'column 2')]
column_names = ("heading1", "heading2")

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

tree = ttk.Treeview(root, columns = column_names, yscrollcommand =    scrollbar.set)

for x in treedata:
       tree.insert('', 'end', values =x)
for col in column_names: 
       tree.heading(col, text = col)
scrollbar.config(command=tree.yview)
tree.pack()
#tree.see(END)

root.mainloop() 