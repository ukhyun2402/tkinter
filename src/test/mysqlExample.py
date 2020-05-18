import mysql.connector
from inspect import *
from tkinter import *
from PIL import ImageTk,Image

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'ukhyun',
    passwd = 'dnr68425',
    database = 'Messenger'
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM MEMBER")
a = mycursor.fetchall()
mycursor.close()

# a is below
# [(1, 'ukhyun', '1234', '하욱현', '01024021051', 'hyun4911@gmail.com', 'ukhyun.png'),
# (2, 'ukhyun1', '1234', '하욱현1', '01024021051', 'hyun4911@gmail.com', 'ukhyun1.png'), 
# (3, 'ukhyun2', '1234', 'Jail', '01024021051', 'hyun4911@gmail.com', 'jail.png'), 
# (4, 'ukhyun', '1234', 'welcome', '01024021051', 'hyun4911@gmail.com', 'welcome.png'), 
# (5, 'ukhyun3', '1234', 'hello', '01024021051', 'hyun4911@gmail.com', 'hello.png')]

main = Tk()
main.configure(bg = 'white')
main.geometry('400x600+200+200')

f = Frame(main)
f.pack(fill=BOTH, side=TOP, expand=1)

Fs = []
Img = []

for i in range(len(a)):
    Fs.append(Frame(f,bg="black"))
    Fs[-1].pack(fill = X)
    
    path = "./img/"+a[i][6]

    if(os.path.isfile(path)):
        Img.append(ImageTk.PhotoImage(Image.open(path).resize((35,35))))
        Label(Fs[-1],image = Img[-1],bd=5).pack(side=LEFT,padx=10,pady=8)

main.mainloop()