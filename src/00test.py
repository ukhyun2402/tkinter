from tkinter import *
from tkinter import ttk 

main = Tk()
main.geometry('400x400')

#main


a = Canvas(main,bg="black")
a.configure(scrollregion = a.bbox("all"))
sb = Scrollbar(a,orient=VERTICAL,command =a.yview)
sb.pack(side=RIGHT,fill=Y)
#Top bar
b = Frame(a,bg="green")

a.pack(fill=BOTH,side=LEFT,expand = YES)
b.pack(fill=X,side=TOP,ipady = 15)
a.update()

bLabel = Label(b,text="User",bg="red").pack(side=LEFT,anchor = S)
cLabel = Label(b,text="HELLO",bg="blue").pack(side=RIGHT,ipadx = 10,anchor = S)
cLabel = Label(b,text="HELLO",bg="white").pack(side=RIGHT, ipadx = 10,anchor = S)

for i in range(10):
    Frame(a,height=50,bd = 5,bg="yellow",highlightbackground="red", highlightcolor="red", highlightthickness=1).pack(side=TOP,fill=X)


main.mainloop()   