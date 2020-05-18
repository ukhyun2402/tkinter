from tkinter import *


def onMouseWheel(e):
    # print(e.widget)
    if(re.match(r".+frame*[0-9]*$",str(e.widget))):
        e.widget.master.master.yview_scroll(round(-1*(e.delta/120)), "units")
        # print(e.widget.master.master)
    elif(str(e.widget).endswith('canvas')):
        # print(e.widget)
        e.widget.yview_scroll(round(-1*(e.delta/120)), "units")

class uFrame(Frame):
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)            

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)

        canvas = Canvas(self,bg="white", bd=0, highlightthickness=0,yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)

        vscrollbar.config(command=canvas.yview)
        
        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0) 
        
        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior.pack(fill=BOTH)
        interior_id = canvas.create_window(0, 0, window=interior,anchor=NW)

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

        canvas.bind_all("<MouseWheel>",onMouseWheel)


main = Tk()
main.geometry('400x600')
fs = []

LayoutFrame = uFrame(main)
LayoutFrame.pack(fill=BOTH,expand=1,side=TOP)

for i in range(20):
    fs.append(Frame(LayoutFrame.interior,bg='red'))
    fs[-1].pack(fill=X,side=TOP)
    Label(fs[-1],text="Labeel"+str(i)).pack()


main.mainloop()