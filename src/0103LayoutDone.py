from tkinter import *
from tkinter import ttk
from inspect import *

import os.path

from PIL import Image,ImageTk,ImageDraw
import numpy as np

import pymysql

mydb = pymysql.connect(
    host = 'localhost',
    user = 'ukhyun',
    passwd = 'dnr68425',
    database = 'Messenger'
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM MEMBER")

a = mycursor.fetchall()

# 함수목록
def ToRGB(rgb):
    return "#%02x%02x%02x" % rgb 

def hover(e):
    e.widget.configure(bg= ToRGB((230,230,230)),bd=0)
    for i in e.widget.children.values():
        i.configure(bg=ToRGB((230,230,230)))

def leave(e):
    e.widget.configure(bg = "white",bd=0)
    for i in e.widget.children.values():
        i.configure(bg="white")

def click(e):
    e.widget.configure(bg = ToRGB((220,220,220)))
    for i in e.widget.children.values():
        i.configure(bg=ToRGB((220,220,220)))

# class
class uFrame(Frame):
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)            

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)

        canvas = Canvas(self,bg="white", bd=0, highlightthickness=0)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)

        vscrollbar.config(command=canvas.yview)
        
        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
        
        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,anchor=NW)

        canvas.config(xscrollcommand = vscrollbar.set, yscrollcommand = vscrollbar.set, scrollregion = (0, 0, 100, 100))
        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)

        def _on_mousewheel(event):
            canvas.yview_scroll(round(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>",_on_mousewheel)



#create main window
main = Tk()
main.title("Messenger - GoodAuction")
# 메인 윈도우 배경 하얀색으로 지정
main.configure(bg = 'white')
# 윈도우 최소크기 설정
main.minsize(400,600)
# 기본 크기 설정 및 offset
main.geometry('400x600+200+200')


# 메인 윈도우 아이콘 이미지 설정
main.iconbitmap(default = r"./img/favicon.ico")
userImgDef = PhotoImage(file = r"./img/userG.png")
userImg = PhotoImage(file = r"./img/user.png")
chatImgDef = PhotoImage(file = r"./img/chatG.png")
chatImg = PhotoImage(file = r"./img/chat.png")

# hover function
def enterUserBtn(e):
    userBtn['image'] = userImg

def leaveUserBtn(e):
    userBtn['image'] = userImgDef
    
def enterChatBtn(e):
    chatBtn['image'] = chatImg

def leaveChatBtn(e):
    chatBtn['image'] = chatImgDef

def _on_press(e):
    userBtn['relief'] = SUNKEN

def _on_press1(e):
    chatBtn['relief'] = SUNKEN


#create navigationBar
NavigationBar = Frame(main, bg = ToRGB((249,249,249)), relief = FLAT, width = userImg.width()*2)
NavigationBar.pack(fill = Y,side=LEFT)

#Create Item in NavigationBar
userBtn = Button(NavigationBar, image= userImgDef, relief = FLAT, bg = ToRGB((249,249,249)), bd = 0)
userBtn.pack(ipady = 15, ipadx = 20)
userBtn.bind("<Enter>", enterUserBtn)
userBtn.bind("<Leave>", leaveUserBtn)
userBtn.bind("<1>",_on_press)

chatBtn = Button(NavigationBar, image= chatImgDef, relief = FLAT, bg = ToRGB((249,249,249)), bd = 0)
chatBtn.pack(ipady = 15, ipadx = 20)
chatBtn.bind("<Enter>", enterChatBtn)
chatBtn.bind("<Leave>", leaveChatBtn)
chatBtn.bind("<1>",_on_press1)


# Create Main Frame
# mainFrame = Frame(main, bg ="green")
mainFrame = Frame(main)
mainFrame.pack(fill = BOTH, side=TOP, expand = YES)

# Top Frame inner Main Frame
topFrame = Frame(mainFrame, bg = "white",height=50)
topFrame.pack(fill=X,side=TOP,ipady = 8)

bLabel = Label(topFrame,text="STAFF",font=("맑은 고딕",17,"bold"),bg="white").pack(side=LEFT,anchor = S,padx=10,pady=10)
cLabel = Label(topFrame,text="HELLO",bg="white").pack(side=RIGHT,ipadx = 10,anchor = S,pady=5)
cLabel = Label(topFrame,text="HELLO",bg="white").pack(side=RIGHT, ipadx = 10,anchor = S,pady=5)

userFrame = uFrame(mainFrame,bg="red")
userFrame.pack(fill=BOTH,side=TOP,expand = 1,anchor = N)

# User List Frame
frames = []
imgs = []

defaultProfileImg = PhotoImage(file = r'./img/default.png')

for i in range(len(a)):
    frames.append(Frame(userFrame.interior,bd=0,bg="white"))
    frames[-1].pack(fill=BOTH,side=TOP)
    frames[-1].bind("<Enter>",hover)
    frames[-1].bind("<Leave>",leave)
    frames[-1].bind("<1>",click)

    #load user information
    path = "./img/"+a[i][6]

    if(os.path.isfile(path)):
        img=Image.open(path).convert("RGB")
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
        imgs.append(ImageTk.PhotoImage(Image.fromarray(npImage).resize((35,35),Image.ANTIALIAS)))
        
        #image
        Label(frames[-1],image = imgs[-1],bd=0,bg='white').pack(side=LEFT,padx=10,pady=8,anchor=S)
        #name
        Label(frames[-1],text=a[i][1],bg='white').pack(side=LEFT,padx =12)
    else:
        Label(frames[-1],image = defaultProfileImg,bd=0,bg='white').pack(side=LEFT,padx=10,pady=8)
    
main.mainloop()
