import tkinter as tk
from inspect import *
import re
import os.path
from PIL import Image, ImageTk, ImageDraw
import numpy as np
import random as rd
# userDB
import pymysql.connections
# chatDB
import pymongo
#---------------------------------------
# Load user List
db = pymysql.connect(
    host='localhost',
    user='ukhyun',
    passwd='dnr68425',
    db='Messenger'
)
cursor = db.cursor()
cursor.execute('SELECT * FROM MEMBER')
memberInfo = cursor.fetchall()
cursor.close()

#---------------------------------------
def ToRGB(rgb):
    return "#%02x%02x%02x" % rgb
#---------------------------------------

class uMongo():
    def __init__(self):
        self.myclient = pymongo

class mainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwagrs):
        tk.Frame.__init__(self, parent, *args, **kwagrs)
        self.parent = self
        self.config(bg="white")

        self.nav = navigationBar(self)
        self.upper = upperFrame(self)
        
        self._frame = None
        self.switchFrame(staffList)

    def switchFrame(self, frameClass):
        newFrame = frameClass(self)
        if self._frame is not None:
            self._frame.destroy()
        #Save the Current Frame
        self._frame = newFrame

class navigationBar(tk.Frame):
    def __init__(self, parent, *args, **kwagrs):
        tk.Frame.__init__(self, parent, *args, **kwagrs)
        self.parent = parent

        self.config(bg=ToRGB((249, 249, 249)), relief='flat')
        self.pack(fill='y', side='left')

        self.staffBtnImage = tk.PhotoImage(file=r'./img/user.png') # 1
        self.staffBtnImageG = tk.PhotoImage(file=r'./img/userG.png') # 2
        self.chatBtnImage = tk.PhotoImage(file=r'./img/chat.png') # 3
        self.chatBtnImageG = tk.PhotoImage(file=r'./img/chatG.png') # 4

        self.staffBtn = tk.Button(self, bg=ToRGB(
            (249, 249, 249)), relief='flat', bd=0, image=self.staffBtnImage,text="STAFF")
        self.staffBtn.pack(ipady=15, ipadx=20)

        self.chatBtn = tk.Button(self, bg=ToRGB(
            (249, 249, 249)), relief='flat', bd=0, image=self.chatBtnImageG, text="CHAT")
        self.chatBtn.pack(ipady=15, ipadx=20)

        #event
        def _hoverStaff(e):
            e.widget['image'] = self.staffBtnImage
        def _hoverChat(e):
            e.widget['image'] = self.chatBtnImage
        def _leaveStaff(e):
            if isinstance(parent._frame,staffList): return
            else: e.widget['image'] = self.staffBtnImageG
        def _leaveChat(e):
            if isinstance(parent._frame,chatList): return
            else: e.widget['image'] = self.chatBtnImageG

        self.staffBtn.bind("<Enter>",_hoverStaff)
        self.chatBtn.bind("<Enter>",_hoverChat)
        self.staffBtn.bind("<Leave>",_leaveStaff)
        self.chatBtn.bind("<Leave>",_leaveChat)

        def _changeFrame(e):
            print(e.widget['text'])
            if e.widget['text'] == 'STAFF':
                if isinstance(parent._frame,staffList):
                    print("S CHECK")
                    return
                else:
                    print("S ELSE")
                    parent.switchFrame(staffList)
                    self.chatBtn['image'] = self.chatBtnImageG

            elif e.widget['text'] == "CHAT":
                if isinstance(parent._frame,chatList):
                    print("C CHECK")
                    return
                else:
                    print("C ELSE")
                    parent.switchFrame(chatList)
                    self.staffBtn['image'] = self.staffBtnImageG
        
        for child in self.winfo_children():
            child.bind("<Button-1>",_changeFrame)


class upperFrame(tk.Frame):
    def __init__(self, parent, *args, **kwagrs):
        tk.Frame.__init__(self, parent, *args, **kwagrs)
        self.parent = parent
        self.config(bg='white')
        self.pack(side='top', fill='x')

        self.mainLabel = tk.Label(self, text="STAFF", font=(
            "맑은 고딕", 17, 'bold'), bg='white')
        self.mainLabel.pack(side='left', anchor='s', padx=10, pady=10)


class List(tk.Frame):
    def __init__(self, parent, *args, **kwagrs):
        tk.Frame.__init__(self, parent, *args, **kwagrs)
        # List Frmae set backgroundcolor
        self.config(bg='white')
        # List Frame pack
        self.pack(fill='both', expand=True,side='left')

        # create instance of Scrollbar and set way
        self.vScrollBar = tk.Scrollbar(self, orient=tk.VERTICAL,bg='red')
        self.vScrollBar.pack(fill='y', side='right')

        # create canvas
        self.canvas = tk.Canvas(
            self, bg='white', bd=0, highlightthickness=0, yscrollcommand=self.vScrollBar.set)
        self.canvas.pack(fill='both', side='left', expand=True)

        self.vScrollBar.config(command=self.canvas.yview)

        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        self.interior = tk.Frame(self.canvas)

        self.interiorId = self.canvas.create_window(
            (0, 0), window=self.interior, anchor='nw')

        def _configure_interior(e):
            size = (self.interior.winfo_reqwidth(),
                    self.interior.winfo_reqheight())
            self.canvas.config(scrollregion="0 0 %s %s" % size)

            if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
                self.canvas.config(width=self.interior.winfo_reqwidth())
        # interior Frame이 수정됐을때 발생되는 Event
        self.interior.bind("<Configure>", _configure_interior)

        def _configure_canvas(e):
            if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
                self.canvas.itemconfigure(
                    self.interiorId, width=self.canvas.winfo_width())
        # canvas Frame이 수정됐을때 발생되는 Event
        self.canvas.bind("<Configure>", _configure_canvas)

        def _wheel(e):
            sum = 0
            for i in self.interior.children.values():
                sum += i.winfo_height()
            if self.canvas.winfo_height() > sum:
                # self.vScrollBar.pack_forget()
                return
            else:
                self.canvas.yview_scroll(round(-1*(e.delta/120)), 'units')
        self.canvas.bind_all("<MouseWheel>", _wheel)
            
        def _startChat(e):
            window = chat(root)

        self.canvas.bind_all("<Double-1>", _startChat)

class staffList(List):
    def __init__(self, parent, *args, **kwargs):
        List.__init__(self, parent, *args, **kwargs)

        self.users = []
        self.imgs = []
        for i in range(len(memberInfo)):
            self.defaultImg = tk.PhotoImage(file=r'./img/default.png')
            self.users.append(tk.Frame(self.interior, bd=0, bg='white'))
            self.users[-1].pack(side='top', fill='x')

            self.path = r'./img/'+memberInfo[i][6]

            if(os.path.isfile(self.path)):
                img = Image.open(self.path).convert("RGB")
                npImage = np.array(img)
                h, w = img.size
                # Create same size alpha layer with circle
                alpha = Image.new('L', img.size, 0)
                draw = ImageDraw.Draw(alpha)
                draw.pieslice([0, 0, h, w], 0, 360, fill=255)
                # Convert alpha Image to numpy array
                npAlpha = np.array(alpha)
                # Add alpha layer to RGB
                npImage = np.dstack((npImage, npAlpha))
                # Save with alpha
                self.imgs.append(ImageTk.PhotoImage(Image.fromarray(
                    npImage).resize((45, 45), Image.ANTIALIAS)))

                tk.Label(self.users[-1], image=self.imgs[-1], bd=0,
                         bg='white').pack(side='left', padx=10, pady=10)

            else:
                tk.Label(self.users[-1], image=self.defaultImg, bd=0,
                         bg='white').pack(side='left', padx=10, pady=10)

            tk.Label(self.users[-1], text=memberInfo[i][1],
                     bg='white').pack(side='left', padx=5)

            #enroll Event
            def _hover(e):
                #master
                e.widget.config(bg=ToRGB((239,239,239)))
                #slave
                for i in e.widget.children.values():
                    i.config(bg=ToRGB((239,239,239)))

            self.users[-1].bind("<Enter>",_hover)

            def _leave(e):
                #master
                e.widget.config(bg='white')
                #slave
                for i in e.widget.children.values():
                    i.config(bg='white')

            self.users[-1].bind("<Leave>",_leave)

            def _click(e):
                #master
                e.widget.config(bg=ToRGB((215,215,215)))
                #slave
                for i in e.widget.children.values():
                    i.config(bg=ToRGB((215,215,215)))

            self.users[-1].bind("<Button-1>",_click)

class chatList(List):
    def __init__(self, parent, *args, **kwargs):
        List.__init__(self, parent, *args, **kwargs)

        self.users = []
        self.imgs = []
        for i in range(len(memberInfo)):
            self.defaultImg = tk.PhotoImage(file=r'./img/default.png')
            self.users.append(tk.Frame(self.interior, bd=0, bg='white'))
            self.users[-1].pack(side='top', fill='x')

            self.path = r'./img/'+memberInfo[i][6]

            if(os.path.isfile(self.path)):
                img = Image.open(self.path).convert("RGB")
                npImage = np.array(img)
                h, w = img.size
                # Create same size alpha layer with circle
                alpha = Image.new('L', img.size, 0)
                draw = ImageDraw.Draw(alpha)
                draw.pieslice([0, 0, h, w], 0, 360, fill=255)
                # Convert alpha Image to numpy array
                npAlpha = np.array(alpha)
                # Add alpha layer to RGB
                npImage = np.dstack((npImage, npAlpha))
                # Save with alpha
                self.imgs.append(ImageTk.PhotoImage(Image.fromarray(
                    npImage).resize((45, 45), Image.ANTIALIAS)))

                tk.Label(self.users[-1], image=self.imgs[-1], bd=0,
                         bg='white').pack(side='left', padx=10, pady=10)

            else:
                tk.Label(self.users[-1], image=self.defaultImg, bd=0,
                         bg='white').pack(side='left', padx=10, pady=10)

            tk.Label(self.users[-1], text=memberInfo[i][1],
                     bg='white').pack(side='left', padx=5)

            #enroll Event
            def _hover(e):
                #master
                e.widget.config(bg=ToRGB((239,239,239)))
                #slave
                for i in e.widget.children.values():
                    i.config(bg=ToRGB((239,239,239)))

            self.users[-1].bind("<Enter>",_hover)

            def _leave(e):
                #master
                e.widget.config(bg='white')
                #slave
                for i in e.widget.children.values():
                    i.config(bg='white')

            self.users[-1].bind("<Leave>",_leave)

            def _click(e):
                #master
                e.widget.config(bg=ToRGB((215,215,215)))
                #slave
                for i in e.widget.children.values():
                    i.config(bg=ToRGB((215,215,215)))

            self.users[-1].bind("<Button-1>",_click)

class chat(tk.Toplevel):
    def __init__(self,parent,*args,**kw):
        tk.Toplevel.__init__(self,parent,*args,**kw)
        self.parent = parent
        self.title("TEMP")
        self.geometry("400x500+%s+%s"%(str(int(int(self.winfo_screenwidth())/2)+rd.randrange(1,200)),str(int(int(self.winfo_screenmmheight() )/2)+rd.randrange(1,200))))
        self.config(bg='white')

        self.top = tk.Frame(self,bg='red',height = 100)
        self.top.pack(side='top',fill='x')

        self.chatFrame = List(self,bg='blue')
        self.chatFrame.pack(side='top',fill='both',expand = True)

        self.inputFrame = tk.Entry(self,bg='black',bd=2)
        self.inputFrame.pack(side='top',fill='both')

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Messenger - GoodAuction")
    root.minsize(400, 500)
    root.geometry('400x600+200+200')
    root.iconbitmap(default=r"./img/favicon.ico")
    app = mainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
