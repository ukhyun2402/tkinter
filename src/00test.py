import tkinter as tk
from tkinter import ttk 

style = ttk.Style()
style.theme_use('alt')
style.configure('TButton', background = 'red', foreground = 'white', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
style.map('TButton', background=[('active','red')])

root = tk.Tk()
button = ttk.Button(root,text='Quit', style="TButton")
button.place(relx=0.3,rely=0.4)  
root.mainloop()   