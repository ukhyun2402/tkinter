import tkinter as tk
import time
import threading

root = tk.Tk()
root.geometry('300x400')

def print_numbers(end): #  no capitals for functions in python
    for i in range(end):
        print(i)
        time.sleep(1)

def print_hello():
    print('Hello')

def background(func, args):
    th = threading.Thread(target=func, args=args)
    th.start()

b1 = tk.Button(root,text='copy',command = lambda : background(print_numbers, (50,))) #args must be a tuple even if it is only one
b1.pack()  #  I would advice grid instead for Tk

b2 = tk.Button(root,text='display',command = print_hello)
b2.pack()

root.mainloop()