from pystray import MenuItem as item, Menu as menu, Icon as icon
import pystray
from PIL import Image,ImageDraw
import tkinter as tk

# window = tk.Tk()
# window.title("Welcome")

# def quit_window(icon, item):
#     icon.stop()
#     window.destroy()

# def show_window(icon, item):
#     icon.stop()
#     window.after(0,window.deiconify)

# def withdraw_window():  
#     window.withdraw()
#     image = Image.open("image.ico")
#     menu = (item('Show', show_window),item('Quit', quit_window))
#     icon = pystray.Icon("name", image, "title", menu)
#     icon.run()

# window.protocol('WM_DELETE_WINDOW', withdraw_window)
# window.mainloop()

# class Program:
#     def __init__(self):
#         self.window = tk.Tk()
#         self.window.title("Welcome")
#         self.window.protocol('WM_DELETE_WINDOW', self.withdraw_window)
#         self.window.mainloop()

#     def quit_window(self):
#         self.icon.stop()
#         self.window.destroy()

#     def show_window(self):
#         self.icon.stop()
#         self.window.after(0, self.window.deiconify)

#     def withdraw_window(self):
#         self.window.withdraw()
#         image = Image.open("image.ico")
#         menu = (item('Show', lambda: self.show_window()),item('Quit', lambda: self.quit_window()))
#         self.icon = pystray.Icon("name", image, "title", menu)
#         self.icon.run()

# run=Program()

state = False

def on_clicked(icon, item):
    global state
    state = not item.checked

def setup(icon):
    icon.visible = True

image = Image.open("image.ico")
icon("Hello World",image,menu = menu(
    item(
        'Checkable',
        on_clicked,
        checked = lambda item: state))).run()


# https://pystray.readthedocs.io/en/latest/usage.html