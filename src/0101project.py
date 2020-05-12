from tkinter import *


def ToRGB(rgb):
    return "#%02x%02x%02x" % rgb 

#create main window
main = Tk()
main.title("")
main.configure(bg = 'white')
main.geometry('400x600+200+200')
main.iconbitmap(default = r"./img/favicon.ico")

userImg = PhotoImage(file = r"./img/userDef.png").subsample(13)
userImg = PhotoImage(file = r"./img/user.png").subsample(13)

#create navigationBar
NavigationBar = Frame(main, bg = ToRGB((246,246,246)), relief = 'raised',width = userImg.width()+6)
NavigationBar.pack(fill = Y,side=LEFT)

#Create Menu in NavigationBar
userBtn = Button(NavigationBar, image= userImg, relief = FLAT)
userBtn.place(x=0, y=0)

main.mainloop()
