import tkinter as tk
from inspect import *

import re

import os.path

from PIL import Image,ImageTk,ImageDraw
import numpy as np

import pymysql.connections
#---------------------------------------

db = pymysql.connect(
    host = 'localhost',
    user = 'ukhyun',
    passwd = 'dnr68425',
    db = 'Messenger'
)

cursor = db.cursor()
cursor.execute('SELECT * FROM MEMBER')
memberInfo = cursor.fetchall()
cursor.close()

#---------------------------------------
def ToRGB(rgb):
    return "#%02x%02x%02x" % rgb 

#---------------------------------------

class mainApplication(tk.Frame):
    def __init__(self,parent,*args,**kwagrs):
        tk.Frame.__init__(self,parent,*args, **kwagrs)
        self.parent = parent
        self.config(bg="white")

        nav = navigationBar(self)
        upper = upperFrame(self)
        staff = staffList(self)

class navigationBar(tk.Frame):
    def __init__(self,parent,*args,**kwagrs):
        tk.Frame.__init__(self,parent,*args, **kwagrs)
        self.parent = parent

        self.config(bg = ToRGB((249,249,249)), relief = 'flat')
        self.pack(fill='y', side='left')

        self.staffBtnImage = tk.PhotoImage(file = r'./img/user.png')
        self.chatBtnImage = tk.PhotoImage(file = r'./img/chat.png')
        self.staffBtnImageG = tk.PhotoImage(file = r'./img/userG.png')
        self.chatBtnImageG = tk.PhotoImage(file = r'./img/chatG.png')

        self.staffBtn = tk.Button(self, bg = ToRGB((249,249,249)),relief = 'flat',bd = 0, image = self.staffBtnImage)
        self.staffBtn.pack(ipady = 15, ipadx = 20)

        self.chatBtn = tk.Button(self, bg = ToRGB((249,249,249)),relief = 'flat', bd = 0, image = self.chatBtnImageG)
        self.chatBtn.pack(ipady = 15, ipadx = 20)

class upperFrame(tk.Frame):
    def __init__(self,parent,*args,**kwagrs):
        tk.Frame.__init__(self,parent,*args, **kwagrs)
        self.parent = parent
        self.config(bg='white')
        self.pack(side='top',fill='x')

        self.mainLabel = tk.Label(self,text="STAFF", font=("맑은 고딕",17,'bold'), bg = 'white')
        self.mainLabel.pack(side='left', anchor = 's', padx = 10, pady = 10)

class List(tk.Frame):
    def __init__(self,parent,*args,**kwagrs):
        tk.Frame.__init__(self,parent,*args, **kwagrs)
        # List Frmae set backgroundcolor
        self.config(bg = 'red')
        # List Frame pack
        self.pack(fill='both', expand = True)

        # create instance of Scrollbar and set way
        self.vScrollBar = tk.Scrollbar(self, orient = tk.VERTICAL)
        self.vScrollBar.pack(fill = 'y', side = 'right')

        # create canvas 
        self.canvas = tk.Canvas(self, bg = 'blue', bd = 0, highlightthickness=0, yscrollcommand = self.vScrollBar.set)
        self.canvas.pack(fill = 'both', side = 'left', expand = True)

        self.vScrollBar.config(command = self.canvas.yview)

        self.interior = tk.Frame(self.canvas,bg="black")
        self.interior.pack(fill='both',anchor='nw')
        
        self.interiorId = self.canvas.create_window((0,0), window = self.interior,anchor = 'nw')

        def _configure_interior(e):
            size = ( self.interior.winfo_reqwidth(), self.interior.winfo_reqheight())
            self.canvas.config(scrollregion = self.interior.bbox('all'))


            if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
                self.canvas.config(width = self.interior.winfo_reqwidth())
        # interior Frame이 수정됐을때 발생되는 Event
        self.interior.bind("<Configure>", _configure_interior)

        def _configure_canvas(e):
            if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
                self.canvas.itemconfigure(self.interiorId, width = self.canvas.winfo_width())
        # canvas Frame이 수정됐을때 발생되는 Event
        self.canvas.bind("<Configure>",_configure_canvas)

        def _wheel(e):
            self.canvas.yview_scroll(round(-1*(e.delta/120)), 'units')
        self.canvas.bind_all("<MouseWheel>",_wheel)

class staffList(List):
    def __init__(self,parent,*args,**kwargs):
        List.__init__(self,parent,*args,**kwargs)

        self.users = []
        self.imgs = []
        for i in range(3):
            self.defaultImg = tk.PhotoImage(file = r'./img/default.png')
            self.users.append(tk.Frame(self.interior,bd = 0, bg= 'red'))
            self.users[-1].pack(side='top')
            
            self.path = r'./img/'+memberInfo[i][6]

            if(os.path.isfile(self.path)):
                img=Image.open(self.path).convert("RGB")
                npImage=np.array(img)
                h,w=img.size
                # Create same size alpha layer with circle
                alpha = Image.new('L', img.size,0)
                draw = ImageDraw.Draw(alpha)
                draw.pieslice([0,0,h,w],0,360,fill=255)
                # Convert alpha Image to numpy array
                npAlpha=np.array(alpha)
                # Add alpha layer to RGB
                npImage=np.dstack((npImage,npAlpha))
                # Save with alpha
                self.imgs.append(ImageTk.PhotoImage(Image.fromarray(npImage).resize((35,35),Image.ANTIALIAS)))
            
                tk.Label(self.users[-1],image = self.imgs[-1], bd = 0,bg = 'white').pack(side='left',padx = 10, pady = 8)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Messenger - GoodAuction")
    root.minsize(400,500)
    root.geometry('400x600+200+200')
    root.iconbitmap(default = r"./img/favicon.ico")

    app =  mainApplication(root).pack(side="top", fill="both", expand = True)
    root.mainloop()