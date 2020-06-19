import tkinter as tk


class Menu:
    def __init__(self, parent, master):
        self.menu = tk.Menu(master)
        self.master = master
        self.parent = parent
        self.filemenu()
        self.transaction()
        self.account()


    def filemenu(self):
        filemenu = tk.Menu(self.menu, tearoff=0)
        filemenu.add_command(label="new", command=None)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)

        self.menu.add_cascade(label="file", menu=filemenu)

    def transaction(self):
        transmenu = tk.Menu(self.menu, tearoff=0)
        transmenu.add_command(
            label="new",
            command=lambda : self.parent.switch_frame("Transaction"))
        self.menu.add_cascade(label="transaction", menu=transmenu)

    def account(self):
        accountmenu = tk.Menu(self.menu, tearoff=0)
        accountmenu.add_command(
            label="View Details",
            command=lambda : self.parent.switch_frame('Account'))
        
        addmenu = tk.Menu(accountmenu, tearoff=0)
        addmenu.add_command(label="account", command=lambda : self.parent.switch_frame('AddAccount'))
        addmenu.add_command(label="category", command=lambda : self.parent.switch_frame('AddCategory'))
        accountmenu.add_cascade(label="add", menu=addmenu)
        self.menu.add_cascade(label="account", menu=accountmenu)
        
