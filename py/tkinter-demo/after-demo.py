from tkinter import *
import time as t


class App:
    def __init__(self, root):
        self.frame = Frame(root)
        self.frame.pack()
        self.start_time = None
        self.secs = 0
        self.count = 0
        self.var = StringVar()
        self.var.set(f'{self.secs}秒{self.count}次')
        self.textlabel = Label(self.frame, textvariable = self.var)
        self.click = Button(self.frame, text = 'click me!', command = self.count_click)
        self.textlabel.pack()
        self.click.pack()

    def count_click(self):
        if self.start_time is None:
            self.start_time = t.time()
        self.count = self.count + 1
        self.var.set(f'{self.secs}秒{self.count}次')
        self.count += 1
    
    def update_time(self):
        if self.start_time is not None:
            self.secs = int(t.time() - self.start_time)
            self.var.set(f'{self.secs}秒{self.count}次')
        self.frame.after(1000,self.update_time)

root = Tk()
root.geometry('150x150')
app = App(root)
app.update_time()
root.mainloop()
