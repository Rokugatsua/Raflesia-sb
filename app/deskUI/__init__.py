import tkinter as tk
from app.script import jnote

js = jnote.jset()

def run():
    root = tk.Tk()
    app = Application(root)
    app.mainloop()

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self)
        self.master = master
        self.initUI()

    def initUI(self):
        self.master.title(js.get('title'))
        self.master.geometry(js.get('geometry'))