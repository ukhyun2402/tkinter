from tkinter import *
from tkinter import ttk

def ToRGB(rgb):
    return "#%02x%02x%02x" % rgb 

#create main window
main = Tk()
# 타이틀 없앰
main.title("")
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

#Create Menu in NavigationBar
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

mainFrame = Frame(main, bg ="black", relief = 'raised', width = main.winfo_screenmmwidth())
mainFrame.pack(fill = Y, side=LEFT)
print(main.winfo_width(),main.winfo_reqwidth(),main.winfo_vrootwidth(),main.winfo_screenmmwidth())
main.mainloop()
