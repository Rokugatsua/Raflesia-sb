import tkinter as tk
from tkinter import messagebox

from app.script import jnote
from app.deskUI import menubar
from app.script import model

js = jnote.jset()
tfont = ('Fixedsys','12','bold')
cfont = ('Arial','12','bold')

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
            AddAccount,
            Category
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

        self.nval, self.pval = tk.StringVar(), tk.IntVar()
        self.cval = tk.StringVar()

        ctgframe = tk.Frame(self.form)
        ctgframe.pack(fill='x', pady=3)
        ctglabel = tk.Label(ctgframe, text="Category", anchor='e', padx=15)
        ctglabel.pack(side='left', fill='x')
        ctgnames = list(self.account.value.keys())
        self.ctgbox = tk.Spinbox(ctgframe, values=ctgnames, width=38)
        self.ctgbox.pack(side='right')

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
        self.cval.set(self.ctgbox.get())
        if self.nval.get() and self.pval.get() and self.cval.get():
            self.account.add_account(
                str(self.nval.get()).lower(),
                self.pval.get(),
                str(self.cval.get()).lower()
                )
            self.account.commit()
            messagebox.showinfo('info',
                f"Succes add {self.nval.get()} on {self.cval.get()}"
                )
        else:
            messagebox.showinfo("info", "please fill all form")

    def refresh(self):
        self.nval.set('')
        self.pval.set(0)
        self.master.update()

class Category(tk.Frame):
    def __init__(self, parent, master):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.maseter = master
        self.account = model.Account()
        self.title()
        self.content()

    def title(self):
        headframe = tk.Frame(self, bg='steel blue')
        headframe.pack(side='top', fill='x')
        title = tk.Label(headframe, text="Category", anchor='w')
        title.config(font=('fixedsys',12,'bold'))
        title.pack(side='left', padx=15, ipadx=5, ipady=10)

    def content(self):
        self.contentframe = tk.Frame(self)
        self.contentframe.pack(fill='both')

        listtag = tk.Label(self.contentframe, text="List Category")
        listtag.pack(fill='x', padx=20, pady=3)

        listframe = tk.Frame(self.contentframe, width=100)
        listframe.pack()

        for ckey in self.account.value.keys():
            clis = tk.Frame(listframe,  borderwidth=1, relief='solid')
            clis.pack()

            clname = tk.Label(clis, text=str(ckey).capitalize(), anchor='w')
            clname.config(width=40)
            clname.pack(side='left', fill='x', expand=True)
            
            self.btn_del(clis, ckey)
            self.btn_edit(clis, ckey)


        addtag = tk.Label(self.contentframe, text="Add New Category")
        addtag.pack()

        addframe = tk.Frame(self.contentframe)
        addframe.pack()

        self.cval = tk.StringVar()
        ctglabel = tk.Label(addframe, text="Category Name", anchor="e")
        ctglabel.pack()
        ctgvalue = tk.Entry(addframe, textvariable=self.cval)
        ctgvalue.pack()
        submit = tk.Button(addframe, text="submit", relief='solid', command=self.addvalue)
        submit.pack()


    def btn_edit(self, frame, value):
        button = tk.Button(
            frame, text='edit', relief='flat',
            command=lambda : self.editvalue(value)
        )
        button.pack(side='right')

    def btn_del(self, frame, value):
        delButton = tk.Button(
            frame, text='delete', relief='flat',
            command=lambda : self.delvalue(value)
        )
        delButton.pack(side="right")

    def delvalue(self, value):
        print(value)

    def editvalue(self, value):
        print(value)

    def addvalue(self):
        if self.cval.get():
            self.account.add_category(str(self.cval.get()).lower())
            messagebox.showinfo("info", f"succes add {self.cval.get()}")
        else:
            messagebox.showinfo("info", "please fill category name")



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

    