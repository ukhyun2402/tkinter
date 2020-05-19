import tkinter as tk
from inspect import *


memberInfo = [(1, 'ukhyun', '1234', '하욱현', '01024021051', 'hyun4911@gmail.com', 'ukhyun.png'),
                (2, 'ukhyun1', '1234', '하욱현1', '01024021051', 'hyun4911@gmail.com', 'ukhyun1.png'),
                (3, 'ukhyun2', '1234', 'Jail', '01024021051', 'hyun4911@gmail.com', 'jail.png'),
                (4, 'ukhyun', '1234', 'welcome', '01024021051', 'hyun4911@gmail.com', 'welcome.png'),
                (5, 'ukhyun3', '1234', 'hello', '01024021051', 'hyun4911@gmail.com', 'hello.png'),
                (6, 'ukhyun', '1234', 'welcome', '01024021051', 'hyun4911@gmail.com', 'welcome.png'),
                (7, 'ukhyun3', '1234', 'hello', '01024021051', 'hyun4911@gmail.com', 'hello.png'),
                (8, 'ukhyun', '1234', 'welcome', '01024021051', 'hyun4911@gmail.com', 'welcome.png'),
                (9, 'ukhyun3', '1234', 'hello', '01024021051', 'hyun4911@gmail.com', 'hello.png'),
                (10, 'ukhyun', '1234', 'welcome', '01024021051', 'hyun4911@gmail.com', 'welcome.png'),
                (11, 'ukhyun3', '1234', 'hello', '01024021051', 'hyun4911@gmail.com', 'hello.png'),
                (12, 'ukhyun', '1234', 'welcome', '01024021051', 'hyun4911@gmail.com', 'welcome.png'),
                (13, 'ukhyun3', '1234', 'hello', '01024021051', 'hyun4911@gmail.com', 'hello.png'),
                (14, 'ukhyun', '1234', 'welcome', '01024021051', 'hyun4911@gmail.com', 'welcome.png'),
                (15, 'ukhyun3', '1234', 'hello', '01024021051', 'hyun4911@gmail.com', 'hello.png'),
                (16, 'ukhyun', '1234', 'welcome', '01024021051', 'hyun4911@gmail.com', 'welcome.png'),
                (17, 'ukhyun3', '1234', 'hello', '01024021051', 'hyun4911@gmail.com', 'hello.png'),
                (18, 'ukhyun', '1234', 'welcome', '01024021051', 'hyun4911@gmail.com', 'welcome.png'),
                (19, 'ukhyun3', '1234', 'hello', '01024021051', 'hyun4911@gmail.com', 'hello.png')]

class mainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwagrs):
        tk.Frame.__init__(self, parent, *args, **kwagrs)
        self.parent = parent
        self.config(bg="white")

        staff = staffList(self)


class List(tk.Frame):
    def __init__(self, parent, *args, **kwagrs):
        tk.Frame.__init__(self, parent, *args, **kwagrs)
        self.config(bg='red')
        self.pack(fill='both', expand=True)

        self.vScrollBar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.vScrollBar.pack(fill='y', side='right')

        self.canvas = tk.Canvas(
            self, bg='blue', bd=0, highlightthickness=0, yscrollcommand=self.vScrollBar.set)
        self.canvas.pack(fill='both', side='left', expand=True)

        self.vScrollBar.config(command=self.canvas.yview)

        self.interior = tk.Frame(self.canvas, bg="black")
        self.interior.pack(fill='both')

        self.interiorId = self.canvas.create_window(
            0, 0, window=self.interior, anchor='nw')

        def _configure_interior(e):
            size = (self.interior.winfo_reqwidth(),
                    self.interior.winfo_reqheight())
            self.canvas.config(scrollregion=self.interior.bbox('all'))
            print(self.canvas.yview)

            if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
                self.canvas.config(width=self.interior.winfo_reqwidth())
        self.interior.bind("<Configure>", _configure_interior)

        def _configure_canvas(e):
            if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
                self.canvas.itemconfigure(
                    self.interiorId, width=self.canvas.winfo_width())
        self.canvas.bind("<Configure>", _configure_canvas)

        def _wheel(e):
            self.canvas.yview_scroll(round(-1*(e.delta/120)), 'units')
        self.canvas.bind_all("<MouseWheel>", _wheel)

        for i in getmembers(self.canvas.yview):
            print(i)
        print(self.canvas.yview)


class staffList(List):
    def __init__(self, parent, *args, **kwargs):
        List.__init__(self, parent, *args, **kwargs)

        self.users = []
        self.imgs = []
        for i in range(3):
            self.users.append(tk.Frame(self.interior, bd=0, bg='red'))
            self.users[-1].pack(side='top', fill='x')

            tk.Label(self.users[-1], text="hello").pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Messenger - GoodAuction")
    root.minsize(400, 500)
    root.geometry('400x600+200+200')
    root.iconbitmap(default=r"./img/favicon.ico")

    app = mainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()