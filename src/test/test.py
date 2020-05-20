import tkinter as tk
from tkinter import ttk
def set_text_newline(s):
    """start text s on a new line"""
    text1.insert(tk.INSERT, '\n' + s)
root = tk.Tk()
# width=width characters, height=lines of text
text1 = tk.Text(root, width=50, height=12, bg='red',font=("돋움"))
text1.pack()
set_text_newline("line one")
set_text_newline("line two")
set_text_newline("line three")
root.mainloop()