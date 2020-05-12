from tkinter import *


def ToRGB(rgb):
    return "#%02x%02x%02x" % rgb 

#create main window
main = Tk()
main.title("")
main.configure(bg = 'white')
main.minsize(400,600)
main.geometry('400x600+200+200')
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

#create navigationBar
NavigationBar = Frame(main, bg = ToRGB((249,249,249)), relief = 'raised',width = userImg.width()*2)
NavigationBar.pack(fill = Y,side=LEFT)

#Create Menu in NavigationBar
userBtn = Button(NavigationBar, image= userImgDef, relief = FLAT, bg = ToRGB((249,249,249)))
userBtn.pack(ipady = 15, ipadx = 20)
# userBtn.place(y=0)
userBtn.bind("<Enter>", enterUserBtn)
userBtn.bind("<Leave>", leaveUserBtn)

chatBtn = Button(NavigationBar, image= chatImgDef, relief = FLAT, bg = ToRGB((249,249,249)))
chatBtn.pack(ipady = 15, ipadx = 20)
chatBtn.bind("<Enter>", enterChatBtn)
chatBtn.bind("<Leave>", leaveChatBtn)

mainFrame = Frame(main, bg ="black", relief = 'raised', width = main.winfo_screenmmwidth())
mainFrame.pack(fill = Y, side=LEFT)
print(main.winfo_width(),main.winfo_reqwidth(),main.winfo_vrootwidth(),main.winfo_screenmmwidth())
main.mainloop()
