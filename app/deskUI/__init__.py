import tkinter as tk

from app.script import jnote
from app.deskUI import menubar
from app.script import model

js = jnote.jset()

def run():
    root = tk.Tk()
    app = Application(root)
    app.mainloop()

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self)
        self.master = master
        self._frame = None
        self.pack(fill='both', expand=True, side='top' )
        self.initUI()
        self.menubar()
        self.wrapper()
        self.footer()

    def initUI(self):
        self.master.title(js.get('title'))
        self.master.geometry(js.get('geometry'))
        self.master.resizable(width=True, height=True)

    def menubar(self):
        menu = menubar.Menu(self, self.master).menu
        self.master.config(menu=menu)

    def wrapper(self):
        self.wrapframe = tk.Frame(self, bg='black')
        self.wrapframe.pack(fill='both', expand=True, side='top')

        Frame = (
            Account,
            Transaction
        )
        self.container = {}
        for F in Frame:
            name = F.__name__
            self.container[name] = F

        self.switch_frame('Account')

    def footer(self):
        self.footframe = tk.Frame(self)
        self.footframe.pack(fill='x', side='bottom')

        footnote = tk.Label(self.footframe, text="By Rokugatsua")
        footnote.pack(side='left', padx=10)

    def switch_frame(self, frame):
        new_page = self.container[frame](self.wrapframe, self.master)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_page
        print(self._frame)
        self._frame.pack(fill='both', expand=True)
        self.refresh()

    def refresh(self):
        self.master.update()

class Account(tk.Frame):
    def __init__(self, parent, master):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.master = master
        self.title()
        self.content()

    def title(self):
        headframe = tk.Frame(self)
        headframe.pack(side='top', fill='x')
        title = tk.Label(headframe, text="Account list", anchor='w')
        title.pack(side='left', padx=15, ipadx=5, ipady=10)

    def content(self):
        contentFrame = tk.Frame(self)
        contentFrame.pack()



class Transaction(tk.Frame):
    def __init__(self, parent, master):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.master = master
        self.content()

    def content(self):
        label = tk.Label(self, text="Transaction list")
        label.pack()
        print('arss')

    