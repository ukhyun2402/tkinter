import tkinter as tk
from tkinter import *

def ToRGB(rgb):
    return "#%02x%02x%02x" % rgb 

# 스크롤 달린 Frame Class
class uFrame(Frame):
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)            

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self,bg="black", bd=0, highlightthickness=0,yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

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

# 메인은 0x0으로 띄움.
main = tk.Tk()

# main -> Toplevel 생성
top = tk.Toplevel(main, bg = 'white')

# top의 title bar 삭제
# top.overrideredirect(1)

# main의 이름 생성
main.title("Hello")
# main 속성 설정
main.attributes("-alpha",0.0)

# top 크기 설정
top.geometry('400x600')

# Frame 생성
title_bar = Frame(top, bg = 'white',relief = 'raised', bd = 0 , borderwidth = 0, highlightthickness = 0)
# NavigationBar = Frame(top, bg = ToRGB((238,238,238)), relief = 'raised')
NavigationBar = Frame(top, bg = ToRGB((230,230,230)), relief = 'raised')

# MagicNavBar = Frame(NavigationBar, bg = ToRGB((238,238,238)), relief = 'raised', width = 100)
# MagicNavBar = Frame(NavigationBar, bg = 'green', relief = 'raised', width = 50)

# 이미지 불러오기 및 사이즈 조정
closeImg = PhotoImage(file = r"./img/close.png").subsample(40)
# maximizeImg = PhotoImage(file = r"./img/max.png").subsample(40)
minimizeImg = PhotoImage(file = r"./img/min.png").subsample(40)


# 타이틀바 버튼 생성 및 함수 컨넥션
closeBtn = Button(title_bar, image = closeImg, relief = FLAT, command = main.destroy, bg='white').pack(side = RIGHT)
minimizeBtn =  Button(title_bar, image = minimizeImg,command = top.withdraw, relief = FLAT, bg='white').pack(side=  RIGHT)

# NavigationBar 버튼 생성
userImg = PhotoImage(file = r"./img/userG.png").subsample(15)
# chatImg = PhotoImage(file = r"./img/chatDef.png").subsample(20)
userBtn = Button(NavigationBar, image = userImg, relief = FLAT).pack(side = TOP)
# chatBtn = Button(NavigationBar, image = chatImg).pack(side = TOP)

# MagicNavBar -> NavBar에서도 Window move Event를 사용할 수 있도록 하는 작은 프레임
# NavigationBar -> 유저목록, 채팅방 목록
NavigationBar.pack(fill = Y, side = LEFT, pady = 100, expand = 1)
NavigationBar.place(x=0, y=0, width = 100)
# MagicNavBar.place(x=0, y=0, relwidth = 1, height = 50)
# # MagicNavBar Z-index 설정
# # relheigt = Navbar에 비해서 얼마만큼의 크기인지
title_bar.pack(ipady = 5, fill = "x")
NavigationBar.pack(fill = Y, side = LEFT)
# title_bar.place(relwidth = 1)

#
def onRootIconify(event): top.withdraw()
main.bind("<Unmap>", onRootIconify)
def onRootDeiconify(event): top.deiconify()
main.bind("<Map>", onRootDeiconify)

# window move event
def get_pos(event):
    xwin = top.winfo_x()
    ywin = top.winfo_y()
    startx = event.x_root
    starty = event.y_root

    ywin = ywin - starty
    xwin = xwin - startx


    def move_window(event):
        top.geometry("400x600" + '+{0}+{1}'.format(event.x_root + xwin, event.y_root + ywin))
    startx = event.x_root
    starty = event.y_root

    title_bar.bind('<B1-Motion>', move_window)
title_bar.bind('<Button-1>', get_pos)

window = tk.Frame(master = top)
window.mainloop()