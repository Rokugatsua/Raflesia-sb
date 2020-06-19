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
        self.wrapframe = tk.Frame(self)
        self.wrapframe.pack(fill='both', expand=True, side='top')

        Frame = (
            Account,
            Transaction,
            AddAccount
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
        self.account = model.Account()
        self.title()
        self.content()

    def title(self):
        headframe = tk.Frame(self)
        headframe.pack(side='top', fill='x')
        title = tk.Label(headframe, text="Account list", anchor='w')
        title.pack(side='left', padx=15, ipadx=5, ipady=10)

        var_total = "{:,}".format(sum([dval for cvalues in self.account.value.values() \
            for dval in cvalues.values()]))

        total = tk.Label(headframe, text="Total : " + var_total, anchor='e', padx=15)
        total.pack(side='right')


    def content(self):
        contentFrame = tk.Frame(self)
        contentFrame.pack(fill='x')

        for key, dvalues in self.account.value.items():
            ctgFrame = tk.Frame(contentFrame, width=400)
            ctgFrame.pack(fill='x')
            ctglabel = tk.Label(ctgFrame, text=str(key).capitalize(), anchor='w', bg='green', padx=10)
            ctglabel.pack(side='top', fill='x', ipadx=25, ipady=2)

            ctgvalue = tk.Frame(ctgFrame)
            ctgvalue.pack(side='bottom', fill='x')

            for dkey, dvalue in dvalues.items():
                detailFrame = tk.Frame(ctgvalue)
                detailFrame.pack(fill='x', expand=True, padx=15, ipady=1)
                dname = tk.Label(detailFrame, text=str(dkey).capitalize(), anchor='w', padx=10)
                dname.pack(side='left', expand=True, ipadx=10, fill='x')
                price = "{:,}".format(dvalue)
                dval = tk.Label(detailFrame, text=price, anchor='e', padx=5)
                dval.pack(side='right',expand=True, ipadx=10, fill='x')

class AddAccount(tk.Frame):
    def __init__(self, parent, master):
        tk.Frame.__init__(self, parent)
        self.master = master
        self.parent = parent
        self.account = model.Account()
        self.title()
        self.content()

    def title(self):
        headframe = tk.Frame(self)
        headframe.pack(side='top', fill='x')
        title = tk.Label(headframe, text="Add Account", anchor='w')
        title.pack(side='left', padx=15, ipadx=5, ipady=10)


    def content(self):
        contentframe = tk.Frame(self)
        contentframe.pack(fill='x')
        self.form = tk.Frame(self)
        self.form.pack()

        self.cval, self.nval, self.pval = tk.StringVar(), tk.StringVar(), tk.IntVar()

        ctgframe = tk.Frame(self.form)
        ctgframe.pack(fill='x', pady=3)
        ctglabel = tk.Label(ctgframe, text="Category", anchor='e', padx=15)
        ctglabel.pack(side='left', fill='x')
        ctgnames = list(self.account.value.keys())
        ctgbox = tk.Spinbox(ctgframe, values=ctgnames, width=38)
        ctgbox.pack(side='right')
        self.cval.set(ctgbox.get())

        nameframe = tk.Frame(self.form)
        nameframe.pack(fill='x', pady=3)
        namelabel = tk.Label(nameframe, text="Account Name", anchor='e', padx=15)
        namelabel.pack(side='left', fill='x')
        nameentry = tk.Entry(nameframe, textvariable=self.nval, width=40)
        nameentry.pack(side='right')

        pricframe = tk.Frame(self.form)
        pricframe.pack(fill='x', pady=3)
        priclabel = tk.Label(pricframe, text="Value", anchor='e', padx=15)
        priclabel.pack(side='left', fill='x')
        pricentry = tk.Entry(pricframe, textvariable=self.pval, width=40)
        pricentry.pack(side='right')

        submit = tk.Button(self.form, relief='solid', text='Submit', command=self.addvalue)
        submit.pack(expand=True, pady=3)

    def addvalue(self):
        if self.nval and self.pval and self.cval:
            self.account.add_account(
                str(self.nval.get()).lower(),
                self.pval.get(),
                str(self.cval.get()).lower()
                )
            self.account.commit()
        else:
            print("please insert all")
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

    