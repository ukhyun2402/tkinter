# -*- coding: utf-8 -*-
import tkinter as tk
import random as rd
import inspect
#---------------------------------------
def ToRGB(rgb):
    return "#%02x%02x%02x" % rgb
#---------------------------------------

class List(tk.Frame):
    def __init__(self, parent, *args, **kwagrs):
        tk.Frame.__init__(self, parent, *args, **kwagrs)
        # List Frmae set backgroundcolor
        self.config(bg='blue')
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

class chat(tk.Toplevel):
    def __init__(self,parent,*args,**kw):
        tk.Toplevel.__init__(self,parent,*args,**kw)
        self.iconbitmap(default=r"./img/favicon.ico")
        self.parent = parent
        self.title("")
        self.geometry("400x500+%s+%s"%(str(int(int(self.winfo_screenwidth())/2)+rd.randrange(1,200)),str(int(int(self.winfo_screenmmheight() )/2)+rd.randrange(1,200))))

        self.top = tk.Frame(self,bg='white',height = 80,bd=0)
        self.top.pack(side='top',fill='x')

        self.label = tk.Label(self.top,text="CHATROOM", font = ("맑은 고딕",16,'bold'),bg='white')
        self.label.pack(side='left',anchor='s',pady = 10,padx = 10)

        self.chatFrame = List(self)
        self.chatFrame.pack(side='top',fill='both',expand = True)
        self.chatFrame.canvas.configure(bg = ToRGB((220,220,220)))
        self.chatFrame.interior.config(bg = ToRGB((220,220,220)))

        self.inputFrame = tk.Frame(self,bg='white')
        self.inputFrame.pack(fill='x',side= 'top')

        self.inputText = tk.Text(self.inputFrame,height = 5,bd = 0,font=("돋움"))
        self.inputText.pack(fill='both',anchor='c',padx = 5, pady = 5)
        
        def a(e):
            print(e.widget.get("1.0",'end-1c'))
            e.widget.delete("1.0",'end')
            e.widget.mark_set(tk.INSERT,"%d.%d"%(1,0))
            return "break"
        def b(e):
            pass
        self.inputText.bind("<Shift-Return>",b)
        self.inputText.bind("<Return>",a)

root = tk.Tk()
root.iconify()
app = chat(root)
root.mainloop()